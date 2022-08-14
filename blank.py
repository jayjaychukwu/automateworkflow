from triggers import Triggers
from actions import Actions
from conditionals import Conditionals

print("testing")


class Blank(Triggers, Actions, Conditionals):
    def __init__(self, name):
        self.name = name
