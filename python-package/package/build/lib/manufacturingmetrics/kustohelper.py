from typing import List
import pandas as pd
from .mfgmetrics import ManufacturingMetrics, OEEDetails
from .mfgconfigs import OEEConfiguration, Shift
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.helpers import dataframe_from_result_table
import os

class KustoHelper():

    def __init__(self):
        super().__init__()

    def getEventsFromKusto(self,oeeConfig: OEEConfiguration):
        shifts = oeeConfig.shifts
        shifts.sort(key=lambda x:x.ShiftStartTime)
        startDateTime = shifts[0].ShiftStartTime
        shifts.sort(key=lambda x:x.ShiftEndTime, reverse=True)
        endDateTime = shifts[0].ShiftEndTime
        utcOffsetInHours = shifts[0].UtcOffsetInHours
        aadTenantId = os.getenv("kusto_aad_tenant_id")
        cluster = os.getenv("kusto_cluster_url")
        appId = os.getenv("kusto_app_id")
        appSecret = os.getenv("kusto_app_secret")
        db = os.getenv("kusto_db_name")
        tableName = os.getenv("kusto_table_name")
        client = KustoClient(KustoConnectionStringBuilder.with_aad_application_key_authentication
                            (cluster,appId,appSecret,aadTenantId))
        query = f"""{tableName}
            | extend  {oeeConfig.eventTimeColumnName} =  {oeeConfig.eventTimeColumnName} {utcOffsetInHours}
            | where  {oeeConfig.eventTimeColumnName} > datetime({startDateTime}) and {oeeConfig.eventTimeColumnName} < datetime({endDateTime})
            | project {oeeConfig.assetIdColumnName}, {oeeConfig.eventTypeColumnName}, {oeeConfig.eventValueColumnName}, {oeeConfig.eventTimeColumnName} = format_datetime(todatetime({oeeConfig.eventTimeColumnName}),'yyyy-MM-dd HH:mm:ss')
            | order by {oeeConfig.eventTimeColumnName} desc"""
        
        queryResult = client.execute(db, query)    
        df = dataframe_from_result_table(queryResult.primary_results[0])
        df[oeeConfig.eventTimeColumnName] = pd.to_datetime(df[oeeConfig.eventTimeColumnName],format='%Y-%m-%d %H:%M:%S')
        #df[oeeConfig.eventTimeColumnName] =  df[oeeConfig.eventTimeColumnName].dt.tz_localize(None)
        return df