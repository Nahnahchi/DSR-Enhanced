from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_6


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=41011200, unk1=-1, unk2=-1)


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=41011500, unk1=-1, unk2=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_4
        if HasTalkEnded() == 1 and IsPlayerDead() == 1 and GetDistanceToPlayer() <= 5:
            return State_1


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_0]

    def test(self):
        if GetDistanceToPlayer() <= 5 and (GetFlagState(1606) == 1 or GetFlagState(1607) == 1):
            return State_2


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        ForceEndTalk(unk1=0)
