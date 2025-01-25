import json
import pandas as pd

#Parse JSON String
json_str ='{"name" : "Alice", "age" : "30"}'
data = json.loads(json_str)

json_str_unload ={"name" : "Alice", "age" : "30"}
print(json_str_unload)

#Convert to JSON string
print(json.dumps(json_str_unload, indent = 2))

with open('output.json','w') as f:
    json.dump(data, f, indent=2)

with open('output.json') as file:
    data = json.load(file)
        
df = pd.read_json('output.json')
print(df)