import json, requests

def create_json(query, name, api_item):
	slots_dict = {"name":name, "values":[]}
	response = requests.get(query)
	data = json.loads(response.text)

	counter = 0
	for x in data:
		_ = {}
		_["id"] = str(counter)
		_["name"] = {"value":x[api_item]}
		slots_dict["values"].append(_)
		counter += 1
	answer = str(slots_dict).replace("'", "\"")

	return json.loads(answer)

filename = "output.txt" # Set the file name of your JSON output file 
with open(filename,'w') as f:
	# Example of how to use the create_json arguments:
	#print (json.dumps(create_json("https://api.coinmarketcap.com/v1/ticker/?limit=500", "Coins", "id"), indent=1, sort_keys=False), file=f)

	print (json.dumps(create_json("foo","foo","foo"), indent=1, sort_keys=False), file=f)

# This will generate a copy-paste ready file with indented lines. You can just paste it into the correct place of your Echo project JSON file.
