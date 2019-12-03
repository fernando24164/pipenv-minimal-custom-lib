import json

def print_config():
    with open('./config/config.json') as f:
        data = json.load(f)

    print(data['message'])