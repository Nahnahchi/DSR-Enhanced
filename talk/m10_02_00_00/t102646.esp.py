from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: Dark World Tendency Merchant [start] """

    def test(self):
        return State_2


class State_1(State):
    """ 1: Dark World Tendency Merchant [generic dialogue] """

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=60000700, unk2=1, unk3=0, display_distance=2)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if GetDistanceToPlayer() > 3 or IsTalkingToSomeoneElse() == 1 or IsCharacterDisabled() == 1 or CheckSelfDeath() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120:
            return State_2
        if IsGenericDialogOpen() == 0 and (GetGenericDialogButtonResult() == 1 or GetGenericDialogButtonResult() == 0):
            return State_7


class State_2(State):
    """ 2: Dark World Tendency Merchant [conditionals] """

    def test(self):
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3:
            return State_3
        if GetOneLineHelpStatus() == 1 and (
                IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 3):
            return State_4
        if GetOneLineHelpStatus() == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3:
            return State_1


class State_3(State):
    """ 3: Dark World Tendency Merchant [press A to talk] """

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_2


class State_4(State):
    """ 4: Dark World Tendency Merchant [pass] """

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_2


class State_5(State):
    """ 5: Dark World Tendency Merchant [prompt] """

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if GetTalkListEntryResult() == 0:
            return State_2
        if GetTalkListEntryResult() == 1:
            return State_6
        if GetTalkListEntryResult() == 4:
            return State_2


class State_6(State):
    """ 6: Dark World Tendency Merchant [Shop] """

    def enter(self):
        OpenRegularShop(6850, 6860)

    def test(self):
        if GetDistanceToPlayer() > 5:
            return State_2
        if IsMenuOpen(11) == 0:
            return State_5


class State_7(State):
    """ 7: Dark World Tendency Merchant [Prepare] """

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2)
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_5
