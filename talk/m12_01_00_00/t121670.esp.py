"""TALK ESD STATE MACHINE 1"""
from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_6


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_7


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_8, State_12, State_14, State_15, State_16, State_18, State_21]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_2


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_6


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_6


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_0, State_2, State_4, State_5, State_11, State_13, State_15, State_17, State_18, State_20]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1125) == 0 and GetDistanceToPlayer() <= 5:
            return State_15
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(11210541) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1125) == 0:
            return State_1
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1128) == 1 and GetFlagState(71210096) == 1:
            return State_14
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1128) == 1 and GetFlagState(71210096) == 0 and GetFlagState(71210095) == 1:
            return State_12
        if GetFlagState(1128) == 1 and GetFlagState(71210095) == 0 and GetOneLineHelpStatus() == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2:
            return State_16


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_12, State_14, State_16]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_18
        if GetFlagState(1124) == 1:
            return State_10
        if GetFlagState(71210099) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71210098) == 1:
            return State_21
        if GetFlagState(71210098) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_8
        if GetFlagState(71210099) == 1:
            return State_10
        else:
            return State_10

    def exit(self):
        RemoveMyAggro()


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(talk_param_id=56005000, unk1=-1, unk2=-1)
        SetFlagState(flag=71210098, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71210098, state=1)

    def test(self):
        return State_11


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_11


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_9, State_10, State_22]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_6


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(talk_param_id=56000010, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71210096, state=1)

    def test(self):
        return State_6


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(talk_param_id=56000020, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_6, State_19]

    def enter(self):
        TalkToPlayer(talk_param_id=56005010, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(talk_param_id=56000000, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        SetFlagState(flag=71210095, state=1)

    def test(self):
        return State_6


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(talk_param_id=56005010, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_8, State_21]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_15

    def exit(self):
        RemoveMyAggro()


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71210097, state=1)
        SetFlagState(flag=71210095, state=0)
        SetFlagState(flag=71210096, state=0)

    def test(self):
        return State_6


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(talk_param_id=56005010, unk1=-1, unk2=-1)
        SetFlagState(flag=71210099, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71210099, state=1)

    def test(self):
        return State_11
