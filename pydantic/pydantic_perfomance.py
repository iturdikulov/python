import json
import timeit
from urllib.parse import urlparse

import requests

from pydantic import HttpUrl, TypeAdapter

reps = 7
number = 100
r = requests.get("https://api.github.com/emojis")
r.raise_for_status()
emojis_json = r.content

#                                     _   _
#  _ __  _   _ _ __ ___   _ __  _   _| |_| |__   ___  _ __
# | '_ \| | | | '__/ _ \ | '_ \| | | | __| '_ \ / _ \| '_ \
# | |_) | |_| | | |  __/ | |_) | |_| | |_| | | | (_) | | | |
# | .__/ \__,_|_|  \___| | .__/ \__, |\__|_| |_|\___/|_| |_|
# |_|                    |_|    |___/


def emojis_pure_python(raw_data):
    data = json.loads(raw_data)
    output = {}
    for key, value in data.items():
        assert isinstance(key, str)  # key type is str
        url = urlparse(value)  # parse url
        assert url.scheme in ("https", "http")  # str in tuple
        output[key] = url


emojis_pure_python_times = timeit.repeat(
    "emojis_pure_python(emojis_json)",  # function call
    globals={
        "emojis_pure_python": emojis_pure_python,
        "emojis_json": emojis_json,
    },
    repeat=reps,
    number=number,
)
print(f"pure python: {min(emojis_pure_python_times) / number * 1000:0.2f}ms")


#                  _             _   _
#  _ __  _   _  __| | __ _ _ __ | |_(_) ___
# | '_ \| | | |/ _` |/ _` | '_ \| __| |/ __|
# | |_) | |_| | (_| | (_| | | | | |_| | (__
# | .__/ \__, |\__,_|\__,_|_| |_|\__|_|\___|
# |_|    |___/

type_adapter = TypeAdapter(dict[str, HttpUrl])
emojis_pydantic_times = timeit.repeat(
    "type_adapter.validate_json(emojis_json)",
    globals={
        "type_adapter": type_adapter,
        "HttpUrl": HttpUrl,
        "emojis_json": emojis_json,
    },
    repeat=reps,
    number=number,
)
print(f"pydantic: {min(emojis_pydantic_times) / number * 1000:0.2f}ms")
# > pydantic: 1.54ms

print(
    f"Pydantic {min(emojis_pure_python_times) / min(emojis_pydantic_times):0.2f}x faster"
)
