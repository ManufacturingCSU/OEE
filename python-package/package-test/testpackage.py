# pip install manufacturingmetrics-0.1.4-py3-none-any.whl
# pip install azure-kusto-data sqlalchemy
# pip install python-dotenv

from manufacturingmetrics import oee
import json
import os
from dotenv import load_dotenv

load_dotenv() 

configJson = json.loads('{ "oeeDate": "2021-06-30" }')

oee.calculateOEE(configJson)