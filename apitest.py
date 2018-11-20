# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:15:09 2018

@author: OMeng
"""

import housecanary
import json
from pandas.io.json import json_normalize

client = housecanary.ApiClient("test_OYRBLG90GQNYHBVIN6OY", "d1hlVCOrvVQv4A2RDOO4eC9XcWrMIOoQ")


# result is an instance of housecanary.response.Response
#print(json_parsed['msa'])

#%%
#####
import pandas as pd
root = 'U:\\Data Staging\\HouseCanary\\'
dataset = pd.read_csv(root+'Free_Address_HC_API.csv', header=0, converters={'Zipcode': lambda x:str(x)})
dataset.update(dataset[['Address','Zipcode']].astype(str))
#dataset['HCinput'] = dataset['Address']+','+dataset['Zipcode']
subset = dataset[['Address','Zipcode']]
address_tuples = [tuple(x) for x in subset.values]

#%%
result = client.property.value(address_tuples)
json_parsed = json.dumps(result.json())
json_parsed_final = json.loads(json_parsed)
outputdata = json_normalize(json_parsed_final,record_path=[['address_info','address','city','zipcode']],meta=[['property/value','result','value','price_mean']],errors='raise')