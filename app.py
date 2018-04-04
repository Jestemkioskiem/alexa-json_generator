import json, requests

def create_json(query, name, api_value, *args):
	slots_dict = {"name":name, "values":[]}
	response = requests.get(query)
	data = json.loads(response.text)

	syn_dict = []
	if args is not None:
		for syns in args:
			for value in syns:
				syn_dict.append(value)

	counter = 0

	for x in data:
		_dict = []
		try:
			for value in syn_dict:
				_dict.append(x[value])

			_ = {}
			_["id"] = str(counter)
			_["name"] = {"value":x[api_value],
				     "synonyms":_dict}
		except KeyError:
			raise Exception("Incorrect API values")

		slots_dict["values"].append(_)
		counter += 1
	answer = str(slots_dict).replace("'", "\"")

	return json.loads(answer)

filename = "output.txt" # Set the file name of your JSON output file 
with open(filename,'w') as f:
	# Example of how to use the create_json arguments (query, name, api_value and synonyms respectively):
	#print (json.dumps(create_json("https://api.coinmarketcap.com/v1/ticker/?limit=500", "Coins", "id", ["symbol", "name"]), indent=1, sort_keys=False), file=f)

	print (json.dumps(create_json("foo_query","foo_name","foo_api_value",["foo_synonym", "foo_synonym2"]), indent=1, sort_keys=False), file=f)

# This will generate a copy-paste ready file with indented lines. You can just paste it into the correct place of your Echo project JSON file.
