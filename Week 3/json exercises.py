#JSON to Python

import json 
 
# some JSON: 
x =  '{ "first_name": "Joe", "age": 30, "last_name": "Bloggs"}' 
 
# parse x: 
y = json.loads(x) 
 
# the result is a Python dictionary: 
print(y["age"])

#Python to JSON

import json 
 
# a Python object (dict): 
x = { 
  "first_name": "Joe", 
  "age": 30, 
  "last_name": "Bloggs" 
} 
 
# convert into JSON: 
y = json.dumps(x) 
 
# the result is a JSON string: 
print(y) 

import json

with open('example.json') as file:
    json_doc = json.load(file)

    items_list = json_doc['menu']['items']
    for item in items_list:
        print(item['id'])

president = {
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}

with open('president.json', 'w') as file:
    json.dump(president, file)