"""TALK ESD STATE MACHINE 1"""
from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_68


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(talk_param_id=42020300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_41


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_42


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        OpenRegularShop(1600, 1699)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_22
        if IsMenuOpen(11) == 0:
            return State_6


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        return State_4


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_4, State_17, State_26]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text_id=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text_id=15000350, required_flag=285)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text_id=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text_id=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_23
        if GetTalkListEntryResult() == 0:
            return State_28
        if GetTalkListEntryResult() == 3:
            return State_34
        if GetTalkListEntryResult() == 1:
            return State_5
        if GetTalkListEntryResult() == 4:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_23
        if GetTalkListEntryResult() == 2:
            return State_67

    def exit(self):
        ClearTalkListData()


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_8, State_22, State_23]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_19


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_22, State_23]

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if GetDistanceToPlayer() >= 12:
            return State_7
        else:
            return State_32


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_10]

    def enter(self):
        SetFlagState(flag=71320063, state=1)

    def test(self):
        return State_11


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(talk_param_id=42021600, unk1=-1, unk2=-1)
        SetFlagState(flag=71320063, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_62
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_24


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_9, State_12, State_13, State_55, State_57]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_19


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_11


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71320060, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(talk_param_id=42021540, unk1=-1, unk2=-1)
        SetFlagState(flag=71320060, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_62
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(talk_param_id=42020100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42020700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_33, State_45, State_51, State_54, State_65, State_71]

    def test(self):
        return State_6


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_1, State_8, State_15, State_16, State_27, State_29, State_31, State_35, State_36, State_38, State_39, State_43, State_44, State_45, State_50, State_52, State_53, State_63, State_64]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_61
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71320063) == 0 and GetSelfHP() <= 90:
            return State_10
        if GetFlagState(1627) == 1:
            return State_12
        if GetFlagState(71320062) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71320061) == 1:
            return State_58
        if GetFlagState(71320061) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71320060) == 1:
            return State_56
        if GetFlagState(71320060) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_14
        if GetFlagState(71320062) == 1:
            return State_12
        else:
            return State_12

    def exit(self):
        RemoveMyAggro()


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_7, State_11, State_20, State_21, State_22, State_25, State_32, State_37, State_46, State_47, State_48, State_49, State_59, State_61, State_66, State_68, State_69, State_70]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1628) == 0 and GetDistanceToPlayer() <= 5:
            return State_37
        if GetFlagState(1627) == 1 and IsPlayerDead() == 1 and GetFlagState(71320074) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_66
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71320064) == 1 and GetFlagState(11026112) == 1:
            return State_39
        if GetFlagState(11026112) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71320064) == 1 and ComparePlayerStatus(12, 0, 0) == 1:
            return State_38
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71320064) == 1 and GetFlagState(11026112) == 0 and ComparePlayerStatus(12, 0, 1) == 1:
            return State_15
        if GetFlagState(71320064) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_29
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1627) == 0 and GetFlagState(1628) == 0:
            return State_20
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_21
        if IsAttackedBySomeone() == 1 and GetFlagState(1628) == 0:
            return State_27


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_19


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_19


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_4, State_67]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_61
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_8
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_7
        else:
            return State_19


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_61
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_8
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_7


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_1, State_10, State_14, State_15, State_16, State_29, State_31, State_35, State_36, State_37, State_38, State_39, State_43, State_44, State_45, State_50, State_52, State_53, State_56, State_58, State_61, State_63, State_64]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_19


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_30, State_40, State_60]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_6


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_18


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 0:
            return State_3
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_2
        else:
            return State_59


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(talk_param_id=42020000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        SetFlagState(flag=71320064, state=1)
        SetFlagState(flag=11026112, state=1)

    def test(self):
        return State_26


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        TalkToPlayer(talk_param_id=42020500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_46
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_8]

    def test(self):
        return State_19


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_16, State_35]

    def enter(self):
        SetFlagState(flag=71320069, state=1)

    def test(self):
        return State_17


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71320072) == 0 and ComparePlayerStatus(12, 0, 0) == 1 and GetFlagState(1600) == 0:
            return State_36
        if GetFlagState(71320072) == 0 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(1600) == 0:
            return State_64
        if GetFlagState(71320071) == 0 and ComparePlayerStatus(12, 0, 0) == 1 and GetFlagState(71510031) == 1:
            return State_63
        if GetFlagState(71320071) == 0 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(71510031) == 1:
            return State_53
        if GetFlagState(71320070) == 0 and ComparePlayerStatus(12, 0, 0) == 1 and GetFlagState(1202) == 0 and GetFlagState(1192) == 0:
            return State_52
        if GetFlagState(71320070) == 0 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(1202) == 0 and GetFlagState(1192) == 0:
            return State_50
        if GetFlagState(71320069) == 0 and ComparePlayerStatus(12, 0, 0) == 1 and GetFlagState(3) == 1:
            return State_35
        if GetFlagState(71320069) == 0 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(3) == 1:
            return State_16
        else:
            return State_45


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42020750, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42021050, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_19, State_62]

    def enter(self):
        TalkToPlayer(talk_param_id=42021700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_19
        if GetDistanceToPlayer() >= 5:
            return State_24


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(talk_param_id=42020150, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(talk_param_id=42020200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_15, State_38]

    def enter(self):
        SetFlagState(flag=71320065, state=1)
        SetFlagState(flag=11026112, state=1)

    def test(self):
        return State_26


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_2]

    def test(self):
        if GetFlagState(71320067) == 1:
            return State_43
        if GetFlagState(71320067) == 0:
            return State_31


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(71320068) == 1:
            return State_44
        if GetFlagState(71320068) == 0:
            return State_1


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        TalkToPlayer(talk_param_id=42020600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(talk_param_id=42020400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42021060, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71320067, state=1)

    def test(self):
        return State_19


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        SetFlagState(flag=71320067, state=0)

    def test(self):
        return State_19


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        SetFlagState(flag=71320068, state=1)

    def test(self):
        return State_19


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        SetFlagState(flag=71320068, state=0)

    def test(self):
        return State_19


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42020800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_50, State_52]

    def enter(self):
        SetFlagState(flag=71320070, state=1)

    def test(self):
        return State_17


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42020850, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42020900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_53, State_63]

    def enter(self):
        SetFlagState(flag=71320071, state=1)

    def test(self):
        return State_17


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=71320061, state=1)

    def test(self):
        return State_11


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(talk_param_id=42021550, unk1=-1, unk2=-1)
        SetFlagState(flag=71320061, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_62
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        SetFlagState(flag=71320062, state=1)

    def test(self):
        return State_11


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(talk_param_id=42021560, unk1=-1, unk2=-1)
        SetFlagState(flag=71320062, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_62
        if HasTalkEnded() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_19


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=71320066, state=1)
        SetFlagState(flag=11026112, state=1)

    def test(self):
        return State_26


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_18, State_22, State_23, State_70]

    def enter(self):
        TalkToPlayer(talk_param_id=42021700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_19
        if GetDistanceToPlayer() >= 5:
            return State_24


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_10, State_14, State_56, State_58]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_37

    def exit(self):
        RemoveMyAggro()


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42020950, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(talk_param_id=42021000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_36, State_64]

    def enter(self):
        SetFlagState(flag=71320072, state=1)

    def test(self):
        return State_17


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(talk_param_id=42021800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71320074, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_19


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9012, 1)
        AcquireGesture(12)
        SetFlagState(flag=285, state=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_22
        if IsMenuOpen(63) == 0:
            return State_72


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71320074, state=0)

    def test(self):
        return State_19


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_19


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_61
        else:
            return State_19


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_17


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_70
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_69
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_71
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_71
