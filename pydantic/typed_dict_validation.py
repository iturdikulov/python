from datetime import datetime

from typing_extensions import NotRequired, TypedDict

from pydantic import TypeAdapter  # special class to validate types


class Meeting(TypedDict):
    when: datetime
    where: bytes
    why: NotRequired[str]


meeting_adapter = TypeAdapter(Meeting)
m = meeting_adapter.validate_python(
    {'when': '2020-01-01T12:00', 'where': 'home'}
)
print(m)
#> {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}

print(meeting_adapter.dump_python(m, exclude={'where'}))
#> {'when': datetime.datetime(2020, 1, 1, 12, 0)}

print(meeting_adapter.json_schema())
"""
{
    'properties': {
        'when': {'format': 'date-time', 'title': 'When', 'type': 'string'},
        'where': {'format': 'binary', 'title': 'Where', 'type': 'string'},
        'why': {'title': 'Why', 'type': 'string'},
    },
    'required': ['when', 'where'],
    'title': 'Meeting',
    'type': 'object',
}
"""
