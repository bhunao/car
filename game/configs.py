import json

from typing import List

from .car import car
from .city import store


def load_configs(files: dict) -> dict[str, dict]:
    configs =  {}
    for name, file_name in config_files.items():
        full_path = './jsons/' + file_name
        with  open(full_path) as j:
            configs[name] = json.load(j)
    return configs


config_files =  {'items':'items.json',
                 'places':'places.json'}
configs = load_configs(config_files)

def main():
    from pprint import pprint
    pprint(configs)


if __name__ == '__main__':
    main()