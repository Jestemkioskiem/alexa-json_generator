# alexa-json_generator
An echo ready json generator for data fetched with APIs

To run, simply replace the "foo" arguments on line 24 with correct values. This script supports simple slots with an id, name and a number of synonyms.

### create_json() arguments explained:
* query
Your HTTP request query goes there
* name
The name of your slot goes there
* api_value
Look, in the API of your choice, for the name of the value you're looking to input into the "value" slot of the JSON
* *args
This is used for Synonyms and is optional. Input them the same way you did with `api_value`, but in a list.
