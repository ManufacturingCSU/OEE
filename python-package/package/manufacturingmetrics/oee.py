import logging
import pandas as pd
from .mfgmetrics import ManufacturingMetrics, OEEDetails
from .mfgconfigs import OEEConfiguration, Shift
from .kustohelper import KustoHelper
from .sqlhelper import SQLHelper
import json

def calculateOEE(configJson):
    sqlHelper = SQLHelper()
    shifts = sqlHelper.getShiftConfiguration(configJson["oeeDate"])
    oeeConfig = OEEConfiguration(shifts)

    print("Fetching data from kusto.")
    kustoHelper = KustoHelper()
    allAssetEvents = kustoHelper.getEventsFromKusto(oeeConfig)

    print("Calculating OEE details.")
    mfgMetrics = ManufacturingMetrics()
    assetAPQCalucations = mfgMetrics.calculateAPQByShiftByAsset(allAssetEvents,oeeConfig)

    #df = sqlHelper.getOEEDataFrame(assetAPQCalucations)
    #print(f"{df.to_json(orient='records') }")

    print("Saving OEE details to SQL DB.")
    df = sqlHelper.saveToSQL(assetAPQCalucations)
    return df