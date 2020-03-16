from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """0: Prostration [start]"""

    def test(self):
        return State_1


class State_1(State):
    """1: Prostration [condition]"""

    def test(self):
        if GetFlagState(11702999) == 0 and GetFlagState(51702990) == 1:
            return State_2


class State_2(State):
    """2: Prostration [give gesture]"""

    def enter(self):
        AcquireGesture(12)
        SetFlagState(flag=11702999, state=1)