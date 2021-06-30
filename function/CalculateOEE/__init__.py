import logging
import azure.functions as func
import pandas as pd
import json
from manufacturingmetrics import oee

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Parsing oee configuration json body.")
    reqBody = req.get_json()
    df = oee.calculateOEE(reqBody)

    return func.HttpResponse(f"{df.to_json(orient='records') }")