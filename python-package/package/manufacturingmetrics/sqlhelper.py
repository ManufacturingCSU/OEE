import json
from typing import List
import pyodbc
from sqlalchemy import create_engine
import urllib
import pandas as pd
from .mfgmetrics import OEEDetails
import os

class SQLHelper():

    def __init__(self):
        super().__init__()

    def getAPQDataFrame(self,assetAPQ: OEEDetails):
        attrs = vars(assetAPQ.shift) #print('\n'.join("%s: %s" % item for item in attrs.items()))
        df1 = pd.DataFrame({ attrs.values() },columns=attrs.keys())
        attrs = vars(assetAPQ.assetDetails)
        df2 =  pd.DataFrame({ attrs.values() },columns=attrs.keys())
        attrs = vars(assetAPQ.availabilityDetails)
        df3 =  pd.DataFrame({ attrs.values() },columns=attrs.keys())
        attrs = vars(assetAPQ.qualityDetails)
        df4 =  pd.DataFrame({ attrs.values() },columns=attrs.keys())
        return pd.concat([df1,df2,df3,df4,pd.DataFrame({"Performance":[assetAPQ.Performance], "OEE": [assetAPQ.OEE]})], axis=1)

    def saveToSQL(self,assetAPQCalucations: List[OEEDetails]):
        df = pd.DataFrame()
        for a in assetAPQCalucations:
            df = pd.concat([df, self.getAPQDataFrame(a)],axis=0)
        df = df[df.columns.difference(['StartAssetStatus'])]
        
        server = os.getenv("sql_server")
        database = os.getenv("sql_db_name")
        username = os.getenv("sql_username")
        password = os.getenv("sql_password")
        table = os.getenv("sql_table_name")
        connectionString = f"Server={server},1433;Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
        params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};" + connectionString)
        conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
        engine_azure = create_engine(conn_str,echo=False)
        df.to_sql(table,con=engine_azure,if_exists='append', index=False)
        return df
