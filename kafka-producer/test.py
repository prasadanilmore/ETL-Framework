import json

data = []

with open('./kafka-producer/data.json', 'r') as file:
    data_json = []
    for line in file:
        try:
            # Parse each line as a JSON object
            json_data = json.loads(line.strip())
            data_json.append(json_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    for data in data_json:  
        print(f"dataa {data}")      
        message_key = data["customerId"]
        message_value = json.dumps(data)
# Now, 'data' is a list containing all the parsed JSON objects


