from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_1


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_0]

    def test(self):
        if GetFlagState(11702999) == 0 and GetFlagState(51702990) == 1:
            return State_2


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        AcquireGesture(12)
        SetFlagState(flag=11702999, state=1)
