from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: Imprisoned Maiden [start] """

    def test(self):
        return State_2


class State_1(State):
    """ 1: Imprisoned Maiden [silence] """

    def enter(self):
        TalkToPlayer(conversation=62000000, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1 and GetDistanceToPlayer() > 3:
            return State_2
        if HasTalkEnded() == 1 and GetDistanceToPlayer() <= 3 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0:
            return State_7


class State_2(State):
    """ 2: Imprisoned Maiden [conditionals] """

    def test(self):
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3:
            return State_3
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 3):
            return State_4
        if GetOneLineHelpStatus() == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3:
            return State_1


class State_3(State):
    """ 3: Imprisoned Maiden [press A to talk] """
    
    def enter(self):
        DisplayOneLineHelp(text_id=10010200)    

    def test(self):
        return State_2


class State_4(State):
    """ 4: Imprisoned Maiden [pass] """
    
    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_2


class State_5(State):
    """ 5: Imprisoned Maiden [prompt] """

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
    """ 6: Imprisoned Maiden [Shop] """

    def enter(self):
        OpenRegularShop(6800, 6805)

    def test(self):
        if GetDistanceToPlayer() > 5:
            return State_2
        if IsMenuOpen(11) == 0:
            return State_5


class State_7(State):
    """ 7: Imprisoned Maiden [Prepare] """

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2)
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_5