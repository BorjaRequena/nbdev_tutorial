# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['say_hi', 'hiSayer']

# Cell
def say_hi(to):
    "Say hi to someone"
    return f"Hi {to}"

# Cell
class hiSayer:
    "Dumb class that spams hi to someone"
    def __init__(self,to):
        self.to = to

    def say(self):
        "Calls function `say_hi` to say hi"
        return say_hi(self.to)