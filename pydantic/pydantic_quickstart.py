from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, ValidationError


# Basic pydantic model
class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

# Advanced pydantic model
class User(BaseModel):
    id: int  # required
    name: str = "John Marshall"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]

external_data = {
    "id": 123,
    "signup_ts": "2020-01-02T03:04:05Z",
    "tastes": {
        "wine": 9,
        b"cheese": 7,
        "cabbage": "1",
    }
}


# m = Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "20"])
# print(repr(m.timestamp))
# print(m.dimensions)

# user = User(**external_data)
# print(user.id)
# print(user.model_dump())

external_data = {'id': 'not an int', 'tastes': {}}

try:
    User(**external_data)
except ValidationError as e:
    print(e.errors())

