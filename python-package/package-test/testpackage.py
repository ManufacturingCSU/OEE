# pip install manufacturingmetrics-0.1.3-py3-none-any.whl
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
      "title": "night-package-test",
      "startDateTime": "2021-05-22 18:00:00",
      "endDateTime": "2021-05-22 22:00:00",
      "idealProductionUnitsPerMinute": 1.5,
      "breakInMinutes": 60
    },
    {
      "title": "day-package-test",
      "startDateTime": "2021-05-20 18:00:00",
      "endDateTime": "2021-05-23 21:00:00",
      "idealProductionUnitsPerMinute": 1.5,
      "breakInMinutes": 60
    }
  ]
}
    ''')

oee.calculateOEE(jsondata)