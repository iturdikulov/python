from datetime import datetime

from pydantic import BaseModel, ValidationError


class Meeting(BaseModel):
    when: datetime
    where: bytes


#                          _
#   ___ ___   ___ _ __ ___(_) ___  _ __
#  / __/ _ \ / _ \ '__/ __| |/ _ \| '_ \
# | (_| (_) |  __/ | | (__| | (_) | | | |
#  \___\___/ \___|_|  \___|_|\___/|_| |_|
#
m = Meeting.model_validate({'when': '2020-01-01T12:00', 'where': 'home'})
print(m)
#> when=datetime.datetime(2020, 1, 1, 12, 0) where=b'home'


#      _        _      _
#  ___| |_ _ __(_) ___| |_
# / __| __| '__| |/ __| __|
# \__ \ |_| |  | | (__| |_
# |___/\__|_|  |_|\___|\__|
try:
    m = Meeting.model_validate(
        {'when': '2020-01-01T12:00', 'where': 'home'}, strict=True  # Enable strict validation
    )
except ValidationError as e:
    print(e)
    """
    2 validation errors for Meeting
    when
      Input should be a valid datetime [type=datetime_type, input_value='2020-01-01T12:00', input_type=str]
    where
      Input should be a valid bytes [type=bytes_type, input_value='home', input_type=str]
    """

m_json = Meeting.model_validate_json(
    '{"when": "2020-01-01T12:00", "where": "home"}'
)
print(m_json)
#> when=datetime.datetime(2020, 1, 1, 12, 0) where=b'home'
