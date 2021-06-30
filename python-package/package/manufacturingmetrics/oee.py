import logging
import pandas as pd
from .mfgmetrics import ManufacturingMetrics, OEEDetails
from .mfgconfigs import OEEConfiguration, Shift
from .kustohelper import KustoHelper
from .sqlhelper import SQLHelper
import json

def calculateOEE(configJson):
    shifts = []
    for s in configJson["shiftdetails"]:
        shifts.append(Shift(**s))
    oeeConfig = OEEConfiguration(shifts)
    
    print("Fetching data from kusto.")
    kustoHelper = KustoHelper()
    allAssetEvents = kustoHelper.getEventsFromKusto(oeeConfig)

    print("Calculating OEE details.")
    mfgMetrics = ManufacturingMetrics()
    assetAPQCalucations = mfgMetrics.calculateAPQByShiftByAsset(allAssetEvents,oeeConfig)
    print("Saving OEE details to SQL DB.")
    df = SQLHelper().saveToSQL(assetAPQCalucations)
    return df