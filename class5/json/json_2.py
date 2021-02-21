import json

# a Python object (dict):
python_dict = {"name": "Jim & Por", "age": 26, "city": "Bangkok"}

# convert into JSoN:
json_string = json.dumps(python_dict)

# the result is a JSON string:
print(json_string)