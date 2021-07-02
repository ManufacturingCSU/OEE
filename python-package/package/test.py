import json
from typing import List
import pandas as pd
from manufacturingmetrics.mfgmetrics import ManufacturingMetrics, OEEDetails
from manufacturingmetrics.mfgconfigs import OEEConfiguration, Shift
from manufacturingmetrics.sqlhelper import SQLHelper
from manufacturingmetrics.kustohelper import KustoHelper
from dotenv import load_dotenv
load_dotenv() 

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

configJson = json.loads('{ "oeeDate": "2021-06-30" }')
calculateOEE(configJson)


    
