import json

def readJSON():
    with open('temp.tm', 'r') as json_file:
        str_json = json_file.read()
        data = str_json
        read_json = json.loads(data)
        return read_json['config']
