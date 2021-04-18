from gpio.light import Light
from gpio.input import Input

outputs = {
    "BLUE": Light(25),
    "RED": Light(24),
    "YELLOW": Light(23),
    "GREEN": Light(18),
}

inputs = {
    "BUTTON": Input(22),
}