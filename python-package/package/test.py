import json
from typing import List
import pandas as pd
from manufacturingmetrics.mfgmetrics import ManufacturingMetrics, OEEDetails
from manufacturingmetrics.mfgconfigs import OEEConfiguration, Shift
from manufacturingmetrics.sqlhelper import SQLHelper
from manufacturingmetrics.kustohelper import KustoHelper
from dotenv import load_dotenv
load_dotenv() 

jsondata = json.loads('''
{
    "shiftdetails": [
        {
        "title": "local-test-pst-1",
        "startDateTime": "2021-06-30 13:00:00",
        "endDateTime": "2021-06-30 15:00:00",
        "idealProductionUnitsPerMinute": 1,
        "breakInMinutes": 10
        },
        {
        "title": "local-test-pst-2",
        "startDateTime": "2021-06-30 15:00:00",
        "endDateTime": "2021-06-30 18:00:00",
        "idealProductionUnitsPerMinute": 1,
        "breakInMinutes": 10
        }
    ]
    }
''')
shifts = []
for s in jsondata["shiftdetails"]:
    shifts.append(Shift(**s))
oeeConfig = OEEConfiguration(shifts)

kustoHelper = KustoHelper()
allAssetEvents = kustoHelper.getEventsFromKusto(oeeConfig)

print(allAssetEvents)

mfgMetrics = ManufacturingMetrics()
assetAPQCalucations = mfgMetrics.calculateAPQByShiftByAsset(allAssetEvents,oeeConfig)
print(assetAPQCalucations)
df = SQLHelper().getOEEDataFrame(assetAPQCalucations)
print(f"{df.to_json(orient='records') }")
    
