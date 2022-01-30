import json
import os
from random import randint
from uuid import uuid4

GENERATED_ITEM_COUNT = 500000
OUTPUT_FILE_PATH = "file.json"
NAMES = ["Alivia Watson", "Louise Carver", "Toyah Mccall", "Daniella Guevara", "Rebekah Emery", "Ellie Martin",
         "Zayd Almond", "Caspian Braun", "Billie-Jo O'Moore", "Kane Kavanagh", "Leela Crawford", "Jules Key",
         "Efan Russell", "Zara Wells", "Dominick Beard", "Nabilah Ramos", "Kealan Dunlap", "Erica Fitzgerald",
         "Harley Kearns", "Zahid Andrade"]


class Item:
    id = str()
    name = str()
    age = int()


def get_id():
    return str(uuid4())


def get_random_item_from_list(items):
    return items[randint(0, len(items) - 1)]


def get_random_number(min_value, max_value):
    return randint(min_value, max_value)


def json_data_generator(item_count):
    def _transform_data(data):
        _base_string = f'"{data[0]}": {data[1]}'
        if item_count - 1 == i:
            return _base_string + os.linesep
        return _base_string + "," + os.linesep

    i = 0
    while i < item_count:
        generated_item = Item()
        generated_item.id = get_id()
        generated_item.name = get_random_item_from_list(items=NAMES)
        generated_item.age = get_random_number(0, 100)

        yield _transform_data((generated_item.id, json.dumps(generated_item.__dict__)))
        i += 1


with open(OUTPUT_FILE_PATH, mode="w") as f:
    f.write("{")
    for item in json_data_generator(item_count=GENERATED_ITEM_COUNT):
        f.write(item)
    f.write("}")
