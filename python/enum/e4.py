from enum import Enum


class Color(Enum):
    red = 0
    yellow = 1
    blue = 2


red = Color.red
blue = Color.blue
red2 = Color.red

print(red == red2)
print(red == blue)
