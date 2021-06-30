# pip install manufacturingmetrics-0.1.0-py3-none-any.whl
# pip install azure-kusto-data sqlalchemy
# pip install python-dotenv

from manufacturingmetrics import oee
import json
import os
from dotenv import load_dotenv

load_dotenv() 

jsondata = json.loads('''
    {
  "shiftdetails": [
    {
      "title": "night-local-test",
      "startDateTime": "2021-05-23 00:00:00",
      "endDateTime": "2021-05-23 04:00:00",
      "idealProductionUnitsPerMinute": 1.5,
      "breakInMinutes": 60
    },
    {
      "title": "day-local-test",
      "startDateTime": "2021-05-21 00:00:00",
      "endDateTime": "2021-05-24 04:00:00",
      "idealProductionUnitsPerMinute": 1.5,
      "breakInMinutes": 60
    }
  ]
}
    ''')

oee.calculateOEE(jsondata)