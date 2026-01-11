import json


class ConfigLoader:

    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        with open('config.json') as f:
            config_data = json.load(f)
        return config_data
