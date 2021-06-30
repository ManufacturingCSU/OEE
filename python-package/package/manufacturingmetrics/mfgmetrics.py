from datetime import datetime
from typing import List
from .mfgconfigs import OEEConfiguration, Shift

class AvailabilityDetails():

    def __init__(self, plannedProductionTime,downTime):
        super().__init__()
        self.PlannedProductionTime = plannedProductionTime
        self.DownTime = downTime
        self.RunTime = self.PlannedProductionTime - self.DownTime
        self.Availability = (self.RunTime / self.PlannedProductionTime)

class QualityDetails():

    def __init__(self, goodUnits,badUnits):
        super().__init__()
        self.GoodUnits = goodUnits
        self.BadUnits = badUnits
        self.TotalUnits = self.GoodUnits + self.BadUnits
        self.Quality = self.GoodUnits / self.TotalUnits

class AssetDetails():

    def __init__(self, id):
        super().__init__()
        self.AssetId = id

class OEEDetails():

    def __init__(self, shift: Shift, assetDetails: AssetDetails, 
                availabilityDetails: AvailabilityDetails, qualityDetails: QualityDetails):
        super().__init__()
        self.shift = shift
        self.assetDetails = assetDetails
        self.availabilityDetails = availabilityDetails
        self.qualityDetails = qualityDetails
        self.Performance = (self.qualityDetails.TotalUnits / (self.availabilityDetails.RunTime /60)) / self.shift.IdealRunRate
        self.OEE = self.availabilityDetails.Availability * self.qualityDetails.Quality * self.Performance

class ManufacturingMetrics():

    def __init__(self):
        super().__init__()

    def calculateAPQByShiftByAsset(self,allAssetEvents, oeeConfig: OEEConfiguration) -> List[OEEDetails]:
        shifts = oeeConfig.shifts
        assetAPQ = []
        for s in shifts:
            shiftEvents = allAssetEvents[(allAssetEvents[oeeConfig.eventTimeColumnName] >= s.ShiftStartTime) & 
                                         (allAssetEvents[oeeConfig.eventTimeColumnName] <= s.ShiftEndTime)] 
            assetIds = shiftEvents[oeeConfig.assetIdColumnName].unique()
            for a in assetIds:
                assetAvailabilitydf = shiftEvents[(shiftEvents[oeeConfig.assetIdColumnName] == a) & 
                                      (shiftEvents[oeeConfig.eventTypeColumnName] == oeeConfig.assetStatusEventType)]
                availabilityDetails = self.calculateAvailabilityByAsset(a,assetAvailabilitydf,s,oeeConfig)
                assetQualitydf = shiftEvents[(shiftEvents[oeeConfig.assetIdColumnName] == a) & 
                                ((shiftEvents[oeeConfig.eventTypeColumnName] == oeeConfig.goodProductionEventType) | 
                                (shiftEvents[oeeConfig.eventTypeColumnName] == oeeConfig.badProductionEventType))]
                qualityDetails = self.calculateQualityByAsset(assetQualitydf, oeeConfig)
                assetAPQ.append(OEEDetails(s,AssetDetails(a),availabilityDetails,qualityDetails))

        return assetAPQ

    def calculateAvailabilityByAsset(self,assetId, assetAvailabilityData, shift: Shift, oeeConfig: OEEConfiguration):
        diffInSecondsColumnName = 'DiffInSeconds'
        productionStartRow = {oeeConfig.assetIdColumnName: assetId, oeeConfig.eventTypeColumnName: 'ShiftStartEvent', 
                                oeeConfig.eventValueColumnName: shift.StartAssetStatus, oeeConfig.eventTimeColumnName: shift.ShiftStartTime}
        productionEndRow = {oeeConfig.assetIdColumnName: assetId, oeeConfig.eventTypeColumnName: 'ShiftEndEvent', 
                                oeeConfig.eventValueColumnName: shift.StartAssetStatus, oeeConfig.eventTimeColumnName: shift.ShiftEndTime}                        
        assetAvailabilityData = assetAvailabilityData.append(productionStartRow, ignore_index=True)
        assetAvailabilityData = assetAvailabilityData.append(productionEndRow, ignore_index=True)

        groupdf = assetAvailabilityData.sort_values(by=oeeConfig.eventTimeColumnName)
        groupdf[diffInSecondsColumnName] = groupdf[oeeConfig.eventTimeColumnName].diff(-1).dt.total_seconds()*-1
        plannedProductionTime = ((shift.ShiftEndTime - shift.ShiftStartTime ).total_seconds()) - (shift.BreakInMinutes * 60)
        downTime = groupdf[groupdf[oeeConfig.eventValueColumnName] >  0][diffInSecondsColumnName].sum()
        #upTime = groupdf[groupdf[oeeConfig.eventValueColumnName] ==  0][diffInSecondsColumnName].sum()
        return AvailabilityDetails(plannedProductionTime, downTime)

    def calculateQualityByAsset(self, assetQualityData, oeeConfig: OEEConfiguration):
        goodUnits = assetQualityData[assetQualityData[oeeConfig.eventTypeColumnName] == oeeConfig.goodProductionEventType][oeeConfig.eventValueColumnName].sum()
        badUnits = assetQualityData[assetQualityData[oeeConfig.eventTypeColumnName] == oeeConfig.badProductionEventType][oeeConfig.eventValueColumnName].sum()
        return QualityDetails(goodUnits, badUnits)
