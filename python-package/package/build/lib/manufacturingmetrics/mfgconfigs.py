from datetime import datetime
from typing import List
import os

class Shift():

    def __init__(self, title, startDateTime, endDateTime, idealProductionUnitsPerMinute, 
                breakInMinutes = 60, startAssetStatus = 0):
        super().__init__()
        self.ShiftTitle = title
        self.ShiftStartTime = datetime.strptime(startDateTime, '%Y-%m-%d %H:%M:%S')
        self.ShiftEndTime = datetime.strptime(endDateTime, '%Y-%m-%d %H:%M:%S')
        self.IdealRunRate = idealProductionUnitsPerMinute
        self.StartAssetStatus = startAssetStatus
        self.BreakInMinutes = breakInMinutes   

class OEEConfiguration():
    
    def __init__(self, shifts: List[Shift]):
        super().__init__()
        self.shifts = shifts
        self.assetIdColumnName = os.getenv("assetIdColumnName")
        self.eventTypeColumnName = os.getenv("eventTypeColumnName")
        self.eventValueColumnName = os.getenv("eventValueColumnName")
        self.eventTimeColumnName = os.getenv("eventTimeColumnName")
        self.assetStatusEventType = os.getenv("assetStatusEventType")
        self.goodProductionEventType = os.getenv("goodProductionEventType")
        self.badProductionEventType = os.getenv("badProductionEventType")
        self.utcOffsetInHours = os.getenv("utcOffsetInHours") 