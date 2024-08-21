import json

PATH = "data.json"


def update_js(data):
    with open(PATH, "w") as fileWirte:
        json.dump(data, fileWirte, indent=4)

def load_js():
    with open(PATH, "r") as fileOpen:
        data = json.load(fileOpen)
        return data

