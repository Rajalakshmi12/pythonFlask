import json
import pandas as pd

# #Parse JSON String
# json_str ='{"name" : "Alice", "age" : "30"}'
# data = json.loads(json_str)

# json_str_unload ={"name" : "Alice", "age" : "30"}
# print(json_str_unload)

# #Convert to JSON string
# print(json.dumps(json_str_unload, indent = 2))

# with open('output.json') as file:
#     data = json.load(file)
        
# df = pd.read_json('output.json')
# print(df)

toSortJson = [{"name":"Alice","age":48},{"name":"Bob","age":69},{"name":"Charlie","age":27},{"name":"David","age":26},{"name":"Emma","age":68},{"name":"Frank","age":90},{"name":"Grace","age":78},{"name":"Henry","age":27},{"name":"Ivy","age":85},{"name":"Jack","age":74},{"name":"Karen","age":43},{"name":"Liam","age":52},{"name":"Mary","age":19},{"name":"Nora","age":36},{"name":"Oscar","age":5},{"name":"Paul","age":11}]
print(type(toSortJson))

newData = sorted(toSortJson, key=lambda x: (x['age'],x['name']))

print(json.dumps(newData))