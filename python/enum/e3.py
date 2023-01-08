from enum import Enum


class Color(Enum):
    red = 'w23wdsd'
    yellow = 'w2wfwdsd'
    blue = 'w77adswdsfdsd'


pride = Color.red
pakan = Color.blue

if pride == pakan:
    print('color same')
else:
    print('color not same')
