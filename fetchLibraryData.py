# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 15:23:02 2021

@author: camden
"""




# import urllib library
from urllib.request import urlopen
import pandas as pd
from datetime import datetime
import json
import pytz

url = "https://www.library.jhu.edu/wp-json/spacecapacity/v1/space/spc_827896044539871335"
data_file = "library_data.csv"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())

#data_all = pd.read_csv(data_file, encoding = "ISO-8859-1", error_bad_lines=False).loc[: , ['date','name','current_count','capacity','percentage']]

#create DataFrame
tz = pytz.timezone('America/New_York')
df = pd.DataFrame({'date': [datetime.now(tz)],
                    'current_count': [data_json['current_count']],
                    'percentage': [data_json['current_count'] / data_json['capacity']],
                    'capacity': [data_json['capacity']],
                   'name': [data_json['name']]})

df.to_csv('library_data.csv', mode='a', index = False, header=False)

#df.to_csv('./library_data.csv', mode='a', index=False, header=False)
  
# print the json response
#print(data_json)