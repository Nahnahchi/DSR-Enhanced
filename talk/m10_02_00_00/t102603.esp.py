"""TALK ESD STATE MACHINE 1"""
from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_14


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        OpenRegularShop(5000, 5019)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if IsMenuOpen(11) == 0:
            return State_3
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_17


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        return State_1


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1, State_12, State_21]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text_id=15000010, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=4, menu_text_id=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if GetTalkListEntryResult() == 0:
            return State_23
        if GetTalkListEntryResult() == 1:
            return State_2
        if GetTalkListEntryResult() == 4:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_18

    def exit(self):
        ClearTalkListData()


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_17, State_18]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_14


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_17, State_18]

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if GetDistanceToPlayer() >= 12:
            return State_4
        else:
            return State_26


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71020039, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(talk_param_id=13011100, unk1=-1, unk2=-1)
        SetFlagState(flag=71020039, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_19


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_14


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_8


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_11(State):
    """ 11: No description. """

    def enter(self):
        TalkToPlayer(talk_param_id=13011000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_12(State):
    """ 12: No description. """

    def test(self):
        return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_5, State_10, State_11, State_22, State_24, State_27, State_28, State_30, State_32, State_35, State_37, State_40, State_41, State_45, State_47, State_48, State_49, State_55]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_33
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71020039) == 0 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1096) == 1:
            return State_9
        if GetFlagState(71020035) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_0, State_4, State_8, State_15, State_16, State_17, State_20, State_26, State_29, State_33, State_39, State_45, State_50, State_51, State_52, State_53, State_54]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1097) == 0 and GetDistanceToPlayer() <= 5:
            return State_29
        if GetFlagState(71020044) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71020045) == 0 and ComparePlayerStatus(5, 4, 15) == 1:
            return State_41
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71020044) == 1 and ComparePlayerStatus(5, 1, 15) == 1:
            return State_40
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71020044) == 0 and ComparePlayerStatus(5, 1, 15) == 1:
            return State_10
        if GetFlagState(721) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71020040) == 1:
            return State_55
        if GetFlagState(71020040) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11026100) == 0:
            return State_37
        if GetFlagState(71020041) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71020042) == 0:
            return State_35
        if GetFlagState(71020040) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71020041) == 0:
            return State_30
        if GetFlagState(71020040) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_24
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1096) == 0 and GetFlagState(1097) == 0:
            return State_15
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_16
        if IsAttackedBySomeone() == 1 and GetFlagState(1097) == 0:
            return State_22


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_14


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_14


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_33
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4
        else:
            return State_14


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_33
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_7, State_10, State_11, State_24, State_27, State_28, State_29, State_30, State_32, State_33, State_35, State_37, State_40, State_41, State_45, State_47, State_48, State_49, State_55]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_14


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_25, State_31, State_36, State_38, State_42, State_55]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_13


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(710) == 1:
            return State_47
        if DidYouDoSomethingInTheMenu(11) == 0:
            return State_44
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_43
        else:
            return State_53


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        SetFlagState(flag=71020040, state=1)
        SetFlagState(flag=11026100, state=1)

    def test(self):
        return State_21


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_5]

    def test(self):
        return State_14


class State_27(State):
    """ 27: No description. """

    def enter(self):
        TalkToPlayer(talk_param_id=13010600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_28(State):
    """ 28: No description. """

    def enter(self):
        TalkToPlayer(talk_param_id=13011100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_14, State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=13011200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_14
        if GetDistanceToPlayer() >= 5:
            return State_19


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71020041, state=1)
        SetFlagState(flag=11026100, state=1)
        SetFlagState(flag=71020042, state=0)

    def test(self):
        return State_21


class State_32(State):
    """ 32: No description. """

    def enter(self):
        TalkToPlayer(talk_param_id=13011200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_13, State_17, State_18]

    def enter(self):
        TalkToPlayer(talk_param_id=13011200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_14
        if GetDistanceToPlayer() >= 5:
            return State_19


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_29

    def exit(self):
        RemoveMyAggro()


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_36
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        SetFlagState(flag=71020042, state=1)
        SetFlagState(flag=11026100, state=1)
        SetFlagState(flag=71020041, state=0)

    def test(self):
        return State_21


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=71020043, state=1)
        SetFlagState(flag=11026100, state=1)

    def test(self):
        return State_21


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_10]

    def enter(self):
        SetFlagState(flag=71020044, state=1)
        SetFlagState(flag=11026100, state=1)

    def test(self):
        return State_14


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        SetFlagState(flag=71020045, state=1)
        SetFlagState(flag=11026100, state=1)
        SetFlagState(flag=71020040, state=1)

    def test(self):
        return State_21


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_45


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_46


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        TalkToPlayer(talk_param_id=13010700, unk1=-1, unk2=-1)
        SetFlagState(flag=71020077, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_44]

    def test(self):
        if GetFlagState(721) == 1:
            return State_49
        if GetFlagState(71020047) == 1:
            return State_49
        if GetFlagState(71020047) == 0:
            return State_48


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        TalkToPlayer(talk_param_id=13011000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        TalkToPlayer(talk_param_id=13010800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        TalkToPlayer(talk_param_id=13010900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        SetFlagState(flag=71020048, state=1)
        SetFlagState(flag=11020603, state=1)

    def test(self):
        return State_14


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        SetFlagState(flag=71020047, state=1)

    def test(self):
        return State_14


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=71020047, state=0)

    def test(self):
        return State_14


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_14


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        SetFlagState(flag=11026100, state=1)

    def test(self):
        return State_14


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(talk_param_id=13010500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19
