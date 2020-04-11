import requests
import json
from typing import Union, Dict, List, Any
from pandas import DataFrame, isnull
from datetime import datetime

uri =  ('https://services6.arcgis.com/5jNaHNYe2AnnqRnS/arcgis/rest/services/COVID19_JapanData/FeatureServer/0'
        '/query?where=%E9%80%9A%E3%81%97%3E0&returnIdsOnly=false&returnCountOnly=false&&f='
        'pgeojson&outFields=*&orderByFields=%E9%80%9A%E3%81%97')
encoding = 'utf-8'
res = requests.get(uri)
print(res.json()["features"][0]["properties"])
print(json.dumps(res.json()["features"][0]["properties"], indent=4, ensure_ascii=False))
propertyies_data = []
for prop in res.json()["features"]:
    propertyies_data.append(prop["properties"])

df = DataFrame(propertyies_data)
