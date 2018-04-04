# alexa-json_generator
An echo ready json generator for data fetched with APIs.

### What does it do?
If you need to extract a ton of data into slot values using APIs or a ready JSON file (with very slight modifications to the code in the second case), you can just input what you want into the arguments on line 40 and you'll get a copy-paste ready file with indented lines, and it's content can be immediately pasted into your echo-skill JSON file, in the correct place.

This script is absolutely necessary for projects that will have over 1000 lines of JSON for even simple slots, but is also very helpful with smaller slots as well, as it's completely fool proof and has access all of the modification options that the amazon provided builder allows you to utilize (name, value, synonyms).

To run, simply replace the foo arguments on line 40 with correct values. This script supports simple slots with an id, name and a number of synonyms. Then run it like a normal python script.

### create_json() arguments explained:
* query

Your HTTP request query goes there
* name

The name of your slot goes there
* api_value

Look, in the API of your choice, for the name of the value you're looking to input into the "value" slot of the JSON
* *args

This is used for Synonyms and is optional. Input them the same way you did with `api_value`, but in a list.

Example for the abovage usage is accessible at line 38 in form of a comment.
An Example output file is accessible as the "example.txt" in this repository.
