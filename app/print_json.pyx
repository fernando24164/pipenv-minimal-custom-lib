import json
from pathlib import Path


class MyClass:

    def __init__(self):
        self.path_config = Path(__file__).parent.absolute()

    def print_config(self):
        """
        Print config message
        """
        with open(str(self.path_config) + "/config.json") as f:
            data = json.load(f)

        print(data["message"])