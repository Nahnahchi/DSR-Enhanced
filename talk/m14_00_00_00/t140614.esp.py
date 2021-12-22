from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_1


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_0, State_3, State_4, State_5, State_6, State_7]

    def test(self):
        if GetFlagState(9) == 0 and GetFlagState(11402799) == 0 and GetDistanceToPlayer() <= 10:
            return State_2
        if GetFlagState(9) == 0 and GetFlagState(11402799) == 1 and GetFlagState(11402796) == 1 and GetDistanceToPlayer() <= 10:
            return State_7
        if GetFlagState(9) == 0 and GetFlagState(11402799) == 1 and GetFlagState(11402797) == 1 and GetDistanceToPlayer() <= 10:
            return State_6
        if GetFlagState(9) == 0 and GetFlagState(11402799) == 1 and GetFlagState(11402798) == 1 and GetDistanceToPlayer() <= 10:
            return State_5
        if GetFlagState(9) == 0 and GetFlagState(11402799) == 1 and GetFlagState(11402798) == 0 and GetDistanceToPlayer() <= 10:
            return State_4


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_1, State_4, State_5, State_6]

    def enter(self):
        TalkToPlayer(conversation=62000100, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_3


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_2]

    def test(self):
        if GetFlagState(11402799) == 1 or GetDistanceToPlayer() >= 25:
            return State_1


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        TalkToPlayer(conversation=24000000, unk1=-1, unk2=-1)
        SetFlagState(flag=11402798, state=1)

    def test(self):
        if GetFlagState(11402799) == 0:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        TalkToPlayer(conversation=24000100, unk1=-1, unk2=-1)
        SetFlagState(flag=11402797, state=1)

    def test(self):
        if GetFlagState(11402799) == 0:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        TalkToPlayer(conversation=24000200, unk1=-1, unk2=-1)
        SetFlagState(flag=11402796, state=1)

    def test(self):
        if GetFlagState(11402799) == 0:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        TalkToPlayer(conversation=24000300, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1
