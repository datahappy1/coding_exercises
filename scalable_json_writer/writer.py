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
    generate_row_count = item_count - 1

    def _transform_item_data(data):
        return data + os.linesep if generate_row_count == i else data + "," + os.linesep

    def _construct_item():
        constructed_item = Item()
        constructed_item.id = get_id()
        constructed_item.name = get_random_item_from_list(items=NAMES)
        constructed_item.age = get_random_number(0, 100)
        return constructed_item

    i = 0
    while i < item_count:
        yield _transform_item_data(json.dumps(_construct_item().__dict__))
        i += 1


with open(OUTPUT_FILE_PATH, mode="w") as f:
    f.write("[")
    for item in json_data_generator(item_count=GENERATED_ITEM_COUNT):
        f.write(item)
    f.write("]")
