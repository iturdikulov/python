from datetime import datetime

from pydantic import BaseModel

class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str = "No idea"

m = Meeting(when="2020-01-01T12:00", where="home")
print(m.model_dump(exclude_unset=True))  # exclude not explicitly set fields
print(m.model_dump(exclude={'where'}, mode='json'))  # exclude fields by name, "jsonable" mode
print(m.model_dump_json(exclude_defaults=True))  # pure json
