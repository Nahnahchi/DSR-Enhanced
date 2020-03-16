from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """0: Quelaag [start]"""

    def test(self):
        return State_1


class State_1(State):
    """1: Quelaag [conditions]"""

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
    """2: Quelaag [talk NO RING]"""

    def enter(self):
        TalkToPlayer(conversation=62000100, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_3


class State_3(State):
    """3: Quelaag [pass]"""

    def test(self):
        if GetFlagState(11402799) == 1 or GetDistanceToPlayer() >= 25:
            return State_1


class State_4(State):
    """4: Quelaag [talk 1]"""

    def enter(self):
        TalkToPlayer(conversation=24000000, unk1=-1, unk2=-1)
        SetFlagState(flag=11402798, state=1)

    def test(self):
        if GetFlagState(11402799) == 0:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1


class State_5(State):
    """5: Quelaag [talk 2]"""

    def enter(self):
        TalkToPlayer(conversation=24000100, unk1=-1, unk2=-1)
        SetFlagState(flag=11402797, state=1)

    def test(self):
        if GetFlagState(11402799) == 0:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1


class State_6(State):
    """6: Quelaag [talk 3]"""

    def enter(self):
        TalkToPlayer(conversation=24000200, unk1=-1, unk2=-1)
        SetFlagState(flag=11402796, state=1)

    def test(self):
        if GetFlagState(11402799) == 0:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1


class State_7(State):
    """7: Quelaag [talk 4]"""

    def enter(self):
        TalkToPlayer(conversation=24000300, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1 and GetDistanceToPlayer() >= 25:
            return State_1
