"""
New Londo Ruins / Valley of Drakes

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m16_00_00_00_enums import *
from ..enums.common_enums import CommonFlags
from ..enums.m10_02_00_00_enums import Objects as m10_02_Objects
from ..enums.m18_00_00_00_enums import Characters as m18_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11600992()
    Event_11600999()
    Event_11602098(0, character=Characters.c2791_gst1)
    Event_11602098(1, character=Characters.c0000_gst2)
    Event_11602098(2, character=Characters.c2670_0000)
    Event_11602098(3, character=Characters.c2670_0001)
    Event_11602098(4, character=Characters.c2670_0002)
    Event_11602098(5, character=Characters.c2670_0003)
    Event_11602098(6, character=Characters.c2670_0004)
    Event_11602098(7, character=Characters.c2670_0005)
    Event_11602098(8, character=Characters.c2670_0007)
    Event_11602098(9, character=Characters.c2670_0008)
    Event_11602098(10, character=Characters.c2670_0010)
    Event_11602098(11, character=Characters.c2670_0012)
    Event_11602098(12, character=Characters.c2670_0013)
    Event_11602098(13, character=Characters.c2670_0014)
    Event_11602098(14, character=Characters.c2670_0015)
    Event_11602098(15, character=Characters.c2670_0016)
    Event_11602098(16, character=Characters.c2670_0017)
    Event_11602098(17, character=Characters.c2670_0018)
    Event_11602098(18, character=Characters.c2670_0019)
    Event_11602098(19, character=Characters.c2670_0020)
    Event_11602098(20, character=Characters.c2670_0021)
    Event_11602098(21, character=Characters.c2670_0022)
    Event_11602098(22, character=Characters.c2670_0023)
    Event_11602098(23, character=Characters.c2670_0024)
    Event_11602098(24, character=Characters.c2670_0025)
    Event_11602098(25, character=Characters.c2670_0026)
    Event_11602098(26, character=Characters.c2670_0028)
    Event_11602098(27, character=Characters.c2670_0029)
    Event_11602098(28, character=Characters.c2670_0030)
    Event_11602098(29, character=Characters.c2670_0031)
    Event_11602098(30, character=Characters.c2680_0000)
    Event_11602098(31, character=Characters.c2680_gst4)
    Event_11602098(32, character=Characters.c4180_prs1)
    if FlagEnabled(CommonFlags.FourKingsDead):
        RegisterBonfire(bonfire_flag=11600920, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11600984, obj=Objects.o0200_0002)
    RegisterLadder(start_climbing_flag=11600010, stop_climbing_flag=11600011, obj=Objects.o6400_0000)
    RegisterLadder(start_climbing_flag=11600012, stop_climbing_flag=11600013, obj=Objects.o6401_0000)
    EnableFlag(11600102)
    SkipLinesIfClient(7)
    EnableFlag(404)
    DisableObject(Objects.o6601_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o6602_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o6603_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableSpawner(entity=1603000)
    Event_11600090(0, obj=Objects.o6604_0000, vfx_id=VFX.CheckpointFog1, destination=1602600, destination_1=1602601)
    Event_11600090(1, obj=Objects.o6605_0000, vfx_id=VFX.CheckpointFog2, destination=1602602, destination_1=1602603)
    Event_11605090()
    Event_11605091()
    Event_11605092()
    Event_11605100()
    Event_11600150()
    Event_11600100()
    Event_11600101(0, obj=Objects.o6110_0000, flag=11600102, animation_id=0)
    Event_11600110(0, obj_act_id=11600110, text=10010872, obj=Objects.o6010_0001)
    Event_11600120(0, obj_act_id=11600120, text=10010867, obj=Objects.o6010_0000, text_1=10010883, item=2008)
    Event_11600160()
    Event_11600200()
    Event_11600250()
    Event_11600199()
    Event_11600210()
    Event_11600251()
    Event_11600220()
    Event_11600252()
    Event_11600230()
    Event_11600253()
    Event_11600810()
    Event_11600400()
    Event_11605397()
    Event_11605398()
    Event_11605360(0, character=10000)
    Event_11605360(1, character=10001)
    Event_11605360(2, character=10002)
    Event_11605360(3, character=10003)
    Event_11605360(4, character=10004)
    Event_11605360(5, character=10005)
    DisableSoundEvent(sound_id=Sounds.FourKingsMusic)
    if FlagEnabled(CommonFlags.FourKingsDead):
        Event_11605392()
        DisableObject(Objects.o6606_0000)
        DeleteVFX(VFX.FourKingsEntranceFog, erase_root_only=False)
    else:
        Event_11605390()
        Event_11605391()
        Event_11605393()
        Event_11605392()
        Event_11600001()
        Event_11605394()
        Event_11605395()
        Event_11605396()
        Event_11605350(0, character=Characters.c5390_0001)
        Event_11605350(1, character=Characters.c5390_0002)
        Event_11605350(2, character=Characters.c5390_0003)
        Event_11605350(3, character=Characters.c5390_0004)
        Event_11605399()
    DisableSoundEvent(sound_id=Sounds.JareelMusic)
    Event_11605150(0, character=Characters.c2670_0004, region=1602850)
    Event_11605150(1, character=Characters.c2670_0016, region=1602850)
    Event_11605150(2, character=Characters.c2670_0003, region=1602850)
    Event_11605150(3, character=Characters.c2670_0031, region=1602850)
    Event_11605150(4, character=Characters.c2670_0002, region=1602850)
    Event_11605150(5, character=Characters.c2670_0020, region=1602850)
    Event_11605150(6, character=Characters.c2670_0021, region=1602850)
    Event_11605150(7, character=Characters.c2670_0022, region=1602850)
    Event_11605150(8, character=Characters.c2670_0012, region=1602851)
    Event_11605150(9, character=Characters.c2670_0013, region=1602851)
    Event_11605150(10, character=Characters.c2670_0014, region=1602851)
    Event_11605150(11, character=Characters.c2670_0008, region=1602852)
    Event_11605150(12, character=Characters.c2670_0007, region=1602852)
    Event_11605150(13, character=Characters.c2670_0015, region=1602852)
    Event_11605150(14, character=Characters.c2670_0026, region=1602852)
    Event_11605150(15, character=1600254, region=1602852)
    Event_11605150(16, character=Characters.c2670_0010, region=1602852)
    Event_11605150(17, character=1600302, region=1602852)
    Event_11605150(18, character=Characters.c2670_0005, region=1602852)
    Event_11605150(19, character=1600353, region=1602852)
    Event_11605150(20, character=1600354, region=1602852)
    Event_11605150(21, character=Characters.c2670_0025, region=1602852)
    Event_11605150(22, character=Characters.c2670_0000, region=1602853)
    Event_11605150(23, character=Characters.c2670_0017, region=1602853)
    Event_11605150(24, character=Characters.c2670_0001, region=1602853)
    Event_11605150(25, character=Characters.c2670_0018, region=1602853)
    Event_11605150(26, character=Characters.c2670_0019, region=1602853)
    Event_11605150(27, character=Characters.c2670_0029, region=1602853)
    Event_11605150(28, character=Characters.c2670_0030, region=1602853)
    Event_11605150(29, character=Characters.c2670_0023, region=1602854)
    Event_11605150(30, character=Characters.c2670_0024, region=1602854)
    Event_11605150(31, character=Characters.c2670_0028, region=1602854)
    Event_11605150(32, character=Characters.c2680_gst4, region=1602860)
    Event_11605150(33, character=Characters.c2680_0000, region=1602860)
    Event_11605001(0, character=Characters.c2670_0008, radius=5.0, cancel_animation=9060)
    Event_11605001(1, character=Characters.c2670_0007, radius=5.0, cancel_animation=9060)
    Event_11605001(2, character=Characters.c2670_0004, radius=7.0, cancel_animation=9060)
    Event_11605001(3, character=Characters.c2670_0001, radius=7.0, cancel_animation=9060)
    Event_11605001(4, character=Characters.c2670_0016, radius=6.0, cancel_animation=9060)
    Event_11605001(5, character=Characters.c2670_0003, radius=6.0, cancel_animation=9060)
    Event_11605001(6, character=Characters.c2670_0015, radius=3.0, cancel_animation=9060)
    Event_11605001(7, character=Characters.c2670_0030, radius=5.0, cancel_animation=9060)
    Event_11605050(0, character=Characters.c2670_0022, region=1602250, cancel_animation=3007, left=0, radius=0.0)
    Event_11605050(1, character=Characters.c2670_0026, region=1602251, cancel_animation=3007, left=0, radius=0.0)
    Event_11605050(2, character=Characters.c2670_0012, region=1602252, cancel_animation=3006, left=1, radius=5.0)
    Event_11605050(3, character=Characters.c2670_0013, region=1602253, cancel_animation=3006, left=1, radius=5.0)
    Event_11605050(4, character=1600254, region=1602254, cancel_animation=3005, left=0, radius=0.0)
    Event_11605050(5, character=Characters.c2670_0014, region=1602255, cancel_animation=3005, left=0, radius=0.0)
    Event_11605050(6, character=Characters.c2670_0018, region=1602270, cancel_animation=9060, left=0, radius=0.0)
    Event_11605050(7, character=Characters.c2670_0019, region=1602270, cancel_animation=9060, left=0, radius=0.0)
    Event_11605050(8, character=Characters.c2670_0029, region=1602270, cancel_animation=9060, left=0, radius=0.0)
    Event_11605050(9, character=Characters.c2670_0031, region=1602271, cancel_animation=9060, left=0, radius=0.0)
    Event_11605200(0, character=Characters.c3500_0000, character_1=Characters.c3501_0000, command_id=1, flag=11600100)
    Event_11605200(1, character=Characters.c3500_0000, character_1=Characters.c3501_0001, command_id=2, flag=11605200)
    Event_11605200(2, character=Characters.c3500_0000, character_1=Characters.c3501_0002, command_id=3, flag=11605201)
    Event_11605200(3, character=Characters.c3500_0000, character_1=Characters.c3501_0003, command_id=4, flag=11605202)
    Event_11605200(4, character=Characters.c3500_0000, character_1=Characters.c3501_0004, command_id=5, flag=11605203)
    Event_11605200(5, character=Characters.c3500_0000, character_1=Characters.c3501_0005, command_id=6, flag=11605204)
    Event_11605200(10, character=Characters.c3500_0001, character_1=Characters.c3501_0006, command_id=1, flag=11600100)
    Event_11605200(11, character=Characters.c3500_0001, character_1=Characters.c3501_0007, command_id=2, flag=11605210)
    Event_11605200(12, character=Characters.c3500_0001, character_1=Characters.c3501_0008, command_id=3, flag=11605211)
    Event_11605200(13, character=Characters.c3500_0001, character_1=Characters.c3501_0009, command_id=4, flag=11605212)
    Event_11605200(14, character=Characters.c3500_0001, character_1=Characters.c3501_0010, command_id=5, flag=11605213)
    Event_11605200(15, character=Characters.c3500_0001, character_1=Characters.c3501_0011, command_id=6, flag=11605214)
    Event_11605250(0, character=Characters.c3501_0000)
    Event_11605250(1, character=Characters.c3501_0001)
    Event_11605250(2, character=Characters.c3501_0002)
    Event_11605250(3, character=Characters.c3501_0003)
    Event_11605250(4, character=Characters.c3501_0004)
    Event_11605250(5, character=Characters.c3501_0005)
    Event_11605250(6, character=Characters.c3501_0006)
    Event_11605250(7, character=Characters.c3501_0007)
    Event_11605250(8, character=Characters.c3501_0008)
    Event_11605250(9, character=Characters.c3501_0009)
    Event_11605250(10, character=Characters.c3501_0010)
    Event_11605250(11, character=Characters.c3501_0011)
    Event_11600850(0, character=Characters.c3500_0000)
    Event_11600850(1, character=Characters.c3500_0001)
    Event_11600850(2, character=Characters.c2791_gst1)
    Event_11600850(3, character=Characters.c0000_gst2)
    Event_11600600(0, obj=Objects.o0110_0000, obj_act_id=11600600)
    Event_11600600(1, obj=Objects.o0110_0001, obj_act_id=11600601)
    Event_11600600(2, obj=Objects.o0110_0002, obj_act_id=11600602)
    Event_11600650(0, obj=Objects.o0500_0003, obj_1=Objects.o6450_0003)
    Event_11600650(1, obj=Objects.o0500_0004, obj_1=Objects.o6450_0009)
    Event_11605843(
        0,
        flag=CommonFlags.FourKingsDead,
        line_intersects=1601990,
        anchor_entity=1602998,
        target_entity=1602997,
    )
    Event_11605846(0, flag=CommonFlags.FourKingsDead, obj=Objects.o6606_0000, vfx_id=VFX.FourKingsEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0006, event_flag=8932)
    Event_11605030()
    Event_11605029()
    Event_11605032()
    Event_11605033()
    Event_11605990(0, flag=11605031, summoned_character=Characters.c0000_0006)
    HumanityRegistration(Characters.c0000_0003, event_flag=8406)
    SkipLinesIfFlagEnabled(2, 1315)
    SkipLinesIfFlagEnabled(1, 1313)
    SkipLines(1)
    DisableCharacter(Characters.c0000_0003)
    Event_11600510(0, character=Characters.c0000_0003, flag=1314)
    Event_11600520(0, character=Characters.c0000_0003, first_flag=1310, last_flag=1319, flag=1315)
    Event_11600530(0, character=Characters.c0000_0003, first_flag=1310, last_flag=1319, flag=1311)
    Event_11600531(0, character=Characters.c0000_0003, first_flag=1310, last_flag=1319, flag=1312)
    Event_11600532(0, character=Characters.c0000_0003, first_flag=1310, last_flag=1319, flag=1313)
    HumanityRegistration(Characters.c0000_0004, event_flag=8414)
    Event_11600510(1, character=Characters.c0000_0004, flag=1381)
    Event_11600520(1, character=Characters.c0000_0004, first_flag=1380, last_flag=1399, flag=1382)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0007, team_type=TeamType.HostileAlly)
    if FlagDisabled(1464):
        DisableCharacter(Characters.c0000_0007)
    Event_11600520(5, character=Characters.c0000_0007, first_flag=1460, last_flag=1489, flag=1462)
    Event_11600545(0, character=Characters.c0000_0007)
    SkipLinesIfFlagDisabled(2, CommonFlags.GwynLordOfCinderDead)
    DisableCharacter(Characters.c5330_0000)
    SkipLinesIfFlagEnabled(11, CommonFlags.GwynLordOfCinderDead)
    EnableImmortality(Characters.c5330_0000)
    SkipLinesIfFlagEnabled(2, 1677)
    SkipLinesIfFlagEnabled(1, 1676)
    SkipLines(1)
    DisableCharacter(Characters.c5330_0000)
    Event_11600537(0, character=Characters.c5330_0000, first_flag=1670, last_flag=1678, flag=1671)
    Event_11600538(0, character=Characters.c5330_0000, first_flag=1670, last_flag=1678, flag=1672)
    Event_11600539(0, character=Characters.c5330_0000, first_flag=1670, last_flag=1678, flag=1673)
    Event_11600540(0, character=Characters.c5330_0000, first_flag=1670, last_flag=1678, flag=1677)
    Event_11600541(0, character=Characters.c5330_0000, first_flag=1670, last_flag=1678, flag=1677)
    Event_11606200()


@RestartOnRest(11600992)
def Event_11600992():
    """Event 11600992"""
    OR_1.Add(Attacked(attacked_entity=1600998, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=1600997, attacker=PLAYER))
    MAIN.Await(OR_1)
    SetTeamType(character=1600998, new_team=TeamType.Enemy)
    SetTeamType(character=1600997, new_team=TeamType.Enemy)


@RestartOnRest(11602098)
def Event_11602098(_, character: Character | int):
    """Event 11602098"""
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_1)
    
    DisableAI(character)
    FadeOutCharacter(character=character, duration=5.0)
    Wait(5.0)
    DisableCharacter(character)
    EnableInvincibility(character)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_2)
    
    EnableCharacter(character)
    FadeInCharacter(character=character, duration=5.0)
    DisableInvincibility(character)
    EnableAI(character)
    Restart()


@RestartOnRest(11600999)
def Event_11600999():
    """Event 11600999"""
    AND_2.Add(EntityBeyondDistance(entity=Characters.c2791_gst1, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_2)
    
    EnableInvincibility(Characters.c2791_gst1)
    DisableAI(Characters.c2791_gst1)
    AND_1.Add(EntityWithinDistance(entity=Characters.c2791_gst1, other_entity=PLAYER, radius=5.0))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_1)
    
    DisableInvincibility(Characters.c2791_gst1)
    EnableAI(Characters.c2791_gst1)


@ContinueOnRest(11600090)
def Event_11600090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11600090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11605090)
def Event_11605090():
    """Event 11605090"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2390_0012)
        DisableCharacter(Characters.c2390_0013)
        DisableCharacter(Characters.c2390_0014)
        DisableCharacter(Characters.c2390_0015)
        DisableCharacter(Characters.c2390_0016)
        DisableCharacter(Characters.c2390_0017)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11605091)
def Event_11605091():
    """Event 11605091"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2390_0012)
    Kill(Characters.c2390_0013)
    Kill(Characters.c2390_0014)
    Kill(Characters.c2390_0015)
    Kill(Characters.c2390_0016)
    Kill(Characters.c2390_0017)


@RestartOnRest(11605092)
def Event_11605092():
    """Event 11605092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11600050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11600050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11600050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11600050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11600050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11600050))
    if not OR_6:
        return RESTART
    EnableFlag(11600050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    if not AND_7:
        return RESTART
    DisableFlag(11600050)
    EnableFlag(11605095)


@ContinueOnRest(11605390)
def Event_11605390():
    """Event 11605390"""
    AND_1.Add(FlagDisabled(CommonFlags.FourKingsDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1601990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1602997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11605391)
def Event_11605391():
    """Event 11605391"""
    AND_1.Add(FlagDisabled(CommonFlags.FourKingsDead))
    AND_1.Add(FlagEnabled(11605393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1601990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1602997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11605393)
def Event_11605393():
    """Event 11605393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.FourKingsDead))
        AND_1.Add(FlagEnabled(11605390))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1602996))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5390_0000)
    ActivateMultiplayerBuffs(Characters.c5390_0001)
    ActivateMultiplayerBuffs(Characters.c5390_0002)
    ActivateMultiplayerBuffs(Characters.c5390_0003)
    ActivateMultiplayerBuffs(Characters.c5390_0004)


@RestartOnRest(11605392)
def Event_11605392():
    """Event 11605392"""
    if FlagEnabled(CommonFlags.FourKingsDead):
        DisableCharacter(Characters.c5390_0000)
        DisableCharacter(Characters.c5390_0001)
        DisableCharacter(Characters.c5390_0002)
        DisableCharacter(Characters.c5390_0003)
        DisableCharacter(Characters.c5390_0004)
        Kill(Characters.c5390_0000)
        Kill(Characters.c5390_0001)
        Kill(Characters.c5390_0002)
        Kill(Characters.c5390_0003)
        Kill(Characters.c5390_0004)
        EnableTreasure(obj=Objects.o0504_0001)
        End()
    DisableAI(Characters.c5390_0000)
    DisableAI(Characters.c5390_0001)
    DisableAI(Characters.c5390_0002)
    DisableAI(Characters.c5390_0003)
    DisableAI(Characters.c5390_0004)
    DisableCharacter(Characters.c5390_0001)
    Kill(Characters.c5390_0002)
    Kill(Characters.c5390_0003)
    Kill(Characters.c5390_0004)
    DisableGravity(Characters.c5390_0000)
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(11605399))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1602999))
    
        MAIN.Await(AND_1)
    
        DisableNetworkSync()
        Wait(7.0)
    EnableCharacter(Characters.c5390_0001)
    ForceAnimation(Characters.c5390_0001, 6200)
    EnableAI(Characters.c5390_0001)
    EnableAI(Characters.c5390_0002)
    EnableAI(Characters.c5390_0003)
    EnableAI(Characters.c5390_0004)
    EnableBossHealthBar(Characters.c5390_0000, name=5390)
    ReferDamageToEntity(Characters.c5390_0001, target_entity=Characters.c5390_0000)
    ReferDamageToEntity(Characters.c5390_0002, target_entity=Characters.c5390_0000)
    ReferDamageToEntity(Characters.c5390_0003, target_entity=Characters.c5390_0000)
    ReferDamageToEntity(Characters.c5390_0004, target_entity=Characters.c5390_0000)


@ContinueOnRest(11600001)
def Event_11600001():
    """Event 11600001"""
    DisableTreasure(obj=Objects.o0504_0001)
    DisableObject(Objects.o0504_0001)
    DisableObject(Objects.o0200_0001)
    AND_1.Add(HealthRatio(Characters.c5390_0000) <= 0.0)
    AND_1.Add(FlagEnabled(11605395))
    
    MAIN.Await(AND_1)
    
    FadeOutCharacter(character=Characters.c5390_0000, duration=3.0)
    FadeOutCharacter(character=Characters.c5390_0001, duration=3.0)
    FadeOutCharacter(character=Characters.c5390_0002, duration=3.0)
    FadeOutCharacter(character=Characters.c5390_0003, duration=3.0)
    FadeOutCharacter(character=Characters.c5390_0004, duration=3.0)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160010, cutscene_flags=0, player_id=10000, move_to_region=1602120, game_map=NEW_LONDO_RUINS)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        160010,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1602120,
        game_map=NEW_LONDO_RUINS,
    )
    SkipLines(1)
    PlayCutscene(160010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    EnableFlag(4047)
    WaitFrames(frames=10)
    DisableCharacter(Characters.c5390_0000)
    DisableCharacter(Characters.c5390_0001)
    DisableCharacter(Characters.c5390_0002)
    DisableCharacter(Characters.c5390_0003)
    DisableCharacter(Characters.c5390_0004)
    Kill(Characters.c5390_0000, award_souls=True)
    Kill(Characters.c5390_0001, award_souls=True)
    Kill(Characters.c5390_0002, award_souls=True)
    Kill(Characters.c5390_0003, award_souls=True)
    Kill(Characters.c5390_0004, award_souls=True)
    
    MAIN.Await(CharacterDead(Characters.c5390_0000))
    
    EnableFlag(CommonFlags.FourKingsDead)
    DisableSpawner(entity=1603000)
    KillBoss(game_area_param_id=1600800)
    DisableObject(Objects.o6606_0000)
    DeleteVFX(VFX.FourKingsEntranceFog)
    EnableTreasure(obj=Objects.o0504_0001)
    EnableObject(Objects.o0504_0001)
    if Client():
        return
    AwardAchievement(achievement_id=37)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=Objects.o0200_0001, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11600920, obj=Objects.o0200_0001)


@ContinueOnRest(11605394)
def Event_11605394():
    """Event 11605394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.FourKingsDead))
    AND_1.Add(FlagEnabled(11605392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11605391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.FourKingsMusic)


@ContinueOnRest(11605395)
def Event_11605395():
    """Event 11605395"""
    DisableNetworkSync()
    AND_1.Add(HealthRatio(Characters.c5390_0000) <= 0.0)
    AND_1.Add(FlagEnabled(11605394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.FourKingsMusic)


@ContinueOnRest(11605396)
def Event_11605396():
    """Event 11605396"""
    MAIN.Await(FlagEnabled(11605392))
    
    AND_7.Add(HealthRatio(Characters.c5390_0000) <= 0.0)
    if AND_7:
        return
    AND_1.Add(CharacterAlive(Characters.c5390_0001))
    SkipLinesIfConditionFalse(5, AND_1)
    AICommand(Characters.c5390_0001, command_id=1, command_slot=0)
    OR_1.Add(CharacterDead(Characters.c5390_0001))
    OR_1.Add(CharacterHasTAEEvent(Characters.c5390_0001, tae_event_id=500))
    
    MAIN.Await(OR_1)
    
    AICommand(Characters.c5390_0001, command_id=-1, command_slot=0)
    AND_2.Add(CharacterAlive(Characters.c5390_0002))
    SkipLinesIfConditionFalse(5, AND_2)
    AICommand(Characters.c5390_0002, command_id=1, command_slot=0)
    OR_2.Add(CharacterDead(Characters.c5390_0002))
    OR_2.Add(CharacterHasTAEEvent(Characters.c5390_0002, tae_event_id=500))
    
    MAIN.Await(OR_2)
    
    AICommand(Characters.c5390_0002, command_id=-1, command_slot=0)
    AND_3.Add(CharacterAlive(Characters.c5390_0003))
    SkipLinesIfConditionFalse(5, AND_3)
    AICommand(Characters.c5390_0003, command_id=1, command_slot=0)
    OR_3.Add(CharacterDead(Characters.c5390_0003))
    OR_3.Add(CharacterHasTAEEvent(Characters.c5390_0003, tae_event_id=500))
    
    MAIN.Await(OR_3)
    
    AICommand(Characters.c5390_0003, command_id=-1, command_slot=0)
    AND_4.Add(CharacterAlive(Characters.c5390_0004))
    SkipLinesIfConditionFalse(5, AND_4)
    AICommand(Characters.c5390_0004, command_id=1, command_slot=0)
    OR_4.Add(CharacterDead(Characters.c5390_0004))
    OR_4.Add(CharacterHasTAEEvent(Characters.c5390_0004, tae_event_id=500))
    
    MAIN.Await(OR_4)
    
    AICommand(Characters.c5390_0004, command_id=-1, command_slot=0)
    Restart()


@ContinueOnRest(11605397)
def Event_11605397():
    """Event 11605397"""
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 2200))
    OR_1.Add(FlagEnabled(CommonFlags.FourKingsDead))
    
    MAIN.Await(OR_1)
    
    DisableMapCollision(collision=Collisions.h9000B0_0000)
    DisableMapCollision(collision=Collisions.h9000B0_0001)
    if FlagEnabled(CommonFlags.FourKingsDead):
        return
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 2200))
    
    EnableMapCollision(collision=Collisions.h9000B0_0000)
    EnableMapCollision(collision=Collisions.h9000B0_0001)
    Restart()


@ContinueOnRest(11605398)
def Event_11605398():
    """Event 11605398"""
    DisableNetworkSync()
    SkipLinesIfFlagDisabled(3, CommonFlags.FourKingsDead)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(7, CommonFlags.FourKingsDead)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2200))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602999))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2200))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602900))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_1)
    DisableCharacterCollision(PLAYER)
    
    MAIN.Await(CharacterDead(PLAYER))
    
    EnableCharacterCollision(PLAYER)
    EnableFlag(8120)
    End()
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@ContinueOnRest(11605399)
def Event_11605399():
    """Event 11605399"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(PlayerStandingOnCollision(Collisions.h0040B0_0000))
    
    MAIN.Await(AND_1)
    
    EnableSpawner(entity=1603000)
    End()


@ContinueOnRest(11605360)
def Event_11605360(_, character: int):
    """Event 11605360"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.FourKingsDead))
    AND_1.Add(CharacterInsideRegion(character, region=1602990))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 2200))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 6084, wait_for_completion=True)
    DisableCharacter(character)
    if ValueNotEqual(left=character, right=10000):
        return
    EnableFlag(8120)


@ContinueOnRest(11605350)
def Event_11605350(_, character: int):
    """Event 11605350"""
    AND_7.Add(Host())
    AND_7.Add(HealthRatio(character) > 0.0)
    
    MAIN.Await(AND_7)
    
    EnableImmortality(character)
    AND_1.Add(Host())
    AND_1.Add(TimeElapsed(seconds=1.0))
    AND_1.Add(HealthRatio(Characters.c5390_0000) > 0.0)
    AND_1.Add(HealthRatio(character) <= 0.009999999776482582)
    AND_2.Add(HealthRatio(Characters.c5390_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_2)
    DisableImmortality(character)
    Kill(character)
    Restart()
    ForceAnimation(character, 7000, wait_for_completion=True)
    DisableCharacter(character)
    DisableImmortality(character)
    Kill(character)


@ContinueOnRest(11605380)
def Event_11605380():
    """Event 11605380"""
    AND_1.Add(FlagDisabled(11600900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
    ))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, target_entity=1602897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1600810)
    Restart()


@ContinueOnRest(11605381)
def Event_11605381():
    """Event 11605381"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11600900))
    AND_1.Add(FlagEnabled(11605380))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1602898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1602897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@RestartOnRest(11605382)
def Event_11605382():
    """Event 11605382"""
    if FlagEnabled(11600900):
        DisableCharacter(1600810)
        Kill(1600810)
        End()
    DisableAI(1600810)
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11605380))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602890))
    
    MAIN.Await(AND_1)
    
    EnableAI(1600810)
    EnableBossHealthBar(1600810, name=2390)


@ContinueOnRest(11600900)
def Event_11600900():
    """Event 11600900"""
    MAIN.Await(CharacterDead(1600810))
    
    KillBoss(game_area_param_id=1600810)
    DisableObject(1601890)
    DeleteVFX(1601891)
    if Client():
        return
    AND_1.Add(PlayerHasGood(2013))
    if AND_1:
        return
    AwardItemLot(1100, host_only=False)


@ContinueOnRest(11605384)
def Event_11605384():
    """Event 11605384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11600900))
    AND_1.Add(FlagEnabled(11605382))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602890))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11605381))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.JareelMusic)


@ContinueOnRest(11605385)
def Event_11605385():
    """Event 11605385"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602890))
    AND_1.Add(CharacterDead(1600810))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.JareelMusic)


@ContinueOnRest(11600150)
def Event_11600150():
    """Event 11600150"""
    if FlagDisabled(11600100):
        DisableMapCollision(collision=Collisions.h0000B0_0002)
        DisableMapCollision(collision=Collisions.h0001B0_0001)
        DisableMapCollision(collision=Collisions.h0002B0_0001)
        DisableMapCollision(collision=Collisions.h0003B0_0001)
        DisableMapCollision(collision=Collisions.h0004B0_0001)
        DisableMapCollision(collision=Collisions.h0005B0_0001)
        DisableMapCollision(collision=Collisions.h0106B0_0000)
        DisableMapCollision(collision=Collisions.h0010B0_0001)
        DisableMapCollision(collision=Collisions.h0011B0_0001)
        DisableMapCollision(collision=Collisions.h0012B0_0001)
        DisableMapCollision(collision=Collisions.h0020B0_0001)
        DisableMapCollision(collision=Collisions.h0021B0_0001)
        DisableMapCollision(collision=Collisions.h0022B0_0001)
        DisableMapCollision(collision=Collisions.h0023B0_0001)
        DisableMapCollision(collision=Collisions.h0024B0_0001)
        DisableMapCollision(collision=Collisions.h0025B0_0001)
        DisableMapCollision(collision=Collisions.h0026B0_0001)
        DisableMapCollision(collision=Collisions.h0027B0_0001)
        DisableMapPiece(map_piece_id=MapPieces.m4000B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4001B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4010B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4011B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4012B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4013B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4014B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4015B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4016B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4017B0_0000)
        DisableMapPiece(map_piece_id=MapPieces.m4018B0_0000)
        DisableMapCollision(collision=Collisions.h0130B0_0000)
        DisableMapCollision(collision=Collisions.h0154B0_0000)
    
        MAIN.Await(FlagEnabled(11600100))
    
        EnableMapCollision(collision=Collisions.h0000B0_0002)
        EnableMapCollision(collision=Collisions.h0001B0_0001)
        EnableMapCollision(collision=Collisions.h0002B0_0001)
        EnableMapCollision(collision=Collisions.h0003B0_0001)
        EnableMapCollision(collision=Collisions.h0004B0_0001)
        EnableMapCollision(collision=Collisions.h0005B0_0001)
        EnableMapCollision(collision=Collisions.h0106B0_0000)
        EnableMapCollision(collision=Collisions.h0010B0_0001)
        EnableMapCollision(collision=Collisions.h0011B0_0001)
        EnableMapCollision(collision=Collisions.h0012B0_0001)
        EnableMapCollision(collision=Collisions.h0020B0_0001)
        EnableMapCollision(collision=Collisions.h0021B0_0001)
        EnableMapCollision(collision=Collisions.h0022B0_0001)
        EnableMapCollision(collision=Collisions.h0023B0_0001)
        EnableMapCollision(collision=Collisions.h0024B0_0001)
        EnableMapCollision(collision=Collisions.h0025B0_0001)
        EnableMapCollision(collision=Collisions.h0026B0_0001)
        EnableMapCollision(collision=Collisions.h0027B0_0001)
        EnableMapPiece(map_piece_id=MapPieces.m4000B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4001B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4010B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4011B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4012B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4013B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4014B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4015B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4016B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4017B0_0000)
        EnableMapPiece(map_piece_id=MapPieces.m4018B0_0000)
        EnableMapCollision(collision=Collisions.h0130B0_0000)
        EnableMapCollision(collision=Collisions.h0154B0_0000)
    DisableSoundEvent(sound_id=Sounds.WaterSound)
    DisableMapCollision(collision=Collisions.h0000B0_0000)
    DisableMapCollision(collision=Collisions.h0001B0_0000)
    DisableMapCollision(collision=Collisions.h0002B0_0000)
    DisableMapCollision(collision=Collisions.h0003B0_0000)
    DisableMapCollision(collision=Collisions.h0004B0_0000)
    DisableMapCollision(collision=Collisions.h0005B0_0000)
    DisableMapCollision(collision=Collisions.h0006B0_0000)
    DisableMapCollision(collision=Collisions.h0010B0_0000)
    DisableMapCollision(collision=Collisions.h0011B0_0000)
    DisableMapCollision(collision=Collisions.h0012B0_0000)
    DisableMapCollision(collision=Collisions.h0020B0_0000)
    DisableMapCollision(collision=Collisions.h0021B0_0000)
    DisableMapCollision(collision=Collisions.h0022B0_0000)
    DisableMapCollision(collision=Collisions.h0023B0_0000)
    DisableMapCollision(collision=Collisions.h0024B0_0000)
    DisableMapCollision(collision=Collisions.h0025B0_0000)
    DisableMapCollision(collision=Collisions.h0026B0_0000)
    DisableMapCollision(collision=Collisions.h0027B0_0000)


@RestartOnRest(11605100)
def Event_11605100():
    """Event 11605100"""
    if FlagEnabled(11600100):
        return
    DisableBackread(Characters.c2390_0011)
    DisableBackread(Characters.c2390_0001)
    DisableBackread(Characters.c2390_0002)
    DisableBackread(Characters.c2390_0003)
    DisableBackread(Characters.c2390_0004)
    DisableBackread(Characters.c2390_0005)
    DisableBackread(Characters.c2390_0006)
    DisableBackread(Characters.c2390_0007)
    DisableBackread(Characters.c2390_0008)
    DisableBackread(Characters.c2390_0009)
    DisableBackread(Characters.c2390_0010)
    DisableBackread(Characters.c3500_0000)
    DisableBackread(Characters.c3500_0001)
    DisableBackread(Characters.c2390_0012)
    DisableBackread(Characters.c2390_0013)
    DisableBackread(Characters.c2390_0014)
    DisableBackread(Characters.c2390_0015)
    DisableBackread(Characters.c2390_0016)
    DisableBackread(Characters.c2390_0017)
    DisableBackread(Characters.c4180_prs1)
    
    MAIN.Await(FlagEnabled(11600100))
    
    EnableBackread(Characters.c2390_0011)
    EnableBackread(Characters.c2390_0001)
    EnableBackread(Characters.c2390_0002)
    EnableBackread(Characters.c2390_0003)
    EnableBackread(Characters.c2390_0004)
    EnableBackread(Characters.c2390_0005)
    EnableBackread(Characters.c2390_0006)
    EnableBackread(Characters.c2390_0007)
    EnableBackread(Characters.c2390_0008)
    EnableBackread(Characters.c2390_0009)
    EnableBackread(Characters.c2390_0010)
    EnableBackread(Characters.c3500_0000)
    EnableBackread(Characters.c3500_0001)
    EnableBackread(Characters.c2390_0012)
    EnableBackread(Characters.c2390_0013)
    EnableBackread(Characters.c2390_0014)
    EnableBackread(Characters.c2390_0015)
    EnableBackread(Characters.c2390_0016)
    EnableBackread(Characters.c2390_0017)
    EnableBackread(Characters.c4180_prs1)


@ContinueOnRest(11600100)
def Event_11600100():
    """Event 11600100"""
    SkipLinesIfFlagEnabled(1, 11600101)
    SkipLinesIfThisEventFlagDisabled(8)
    EndOfAnimation(obj=Objects.o6000_0000, animation_id=10)
    DisableMapCollision(collision=Collisions.h7000B0_0000)
    DisableMapCollision(collision=Collisions.h7000B0_0001)
    DisableMapCollision(collision=Collisions.h8000B0_0000)
    DisableMapCollision(collision=Collisions.h8000B0_0001)
    DisableObject(Objects.o6500_0000)
    DisableFlag(404)
    End()
    EnableMapCollision(collision=Collisions.h8000B0_0000)
    EnableMapCollision(collision=Collisions.h8000B0_0001)
    
    MAIN.Await(FlagEnabled(11600101))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(160000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(160000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11600100)
    Restart()


@ContinueOnRest(11600101)
def Event_11600101(_, obj: int, flag: Flag | int, animation_id: int):
    """Event 11600101"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=Objects.o6000_0000, animation_id=animation_id)
        EndOfAnimation(obj=obj, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010502,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(obj, 0, wait_for_completion=True)
    if FlagEnabled(flag):
        return
    ForceAnimation(Objects.o6000_0000, animation_id, wait_for_completion=True)


@ContinueOnRest(11600110)
def Event_11600110(_, obj_act_id: Flag | int, text: EventText | int, obj: int):
    """Event 11600110"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if Client():
        return
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@ContinueOnRest(11600120)
def Event_11600120(
    _,
    obj_act_id: Flag | int,
    text: EventText | int,
    obj: int,
    text_1: EventText | int,
    item: BaseItemParam | int,
):
    """Event 11600120"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if Client():
        return
    AND_1.Add(PlayerHasGood(item))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=text_1, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@ContinueOnRest(11600160)
def Event_11600160():
    """Event 11600160"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o6410_0000, animation_id=0)
        RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=Objects.o6410_0000)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010500,
        anchor_entity=Objects.o6410_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=194,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    EnableFlag(11600160)
    Move(
        PLAYER,
        destination=Objects.o6410_0000,
        destination_type=CoordEntityType.Object,
        model_point=192,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(Objects.o6410_0000, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=Objects.o6410_0000)


@ContinueOnRest(11600200)
def Event_11600200():
    """Event 11600200"""
    if FlagEnabled(11600201):
        EndOfAnimation(obj=Objects.o6200_0000, animation_id=21)
        DisableObjectActivation(Objects.o6100_0006, obj_act_id=6101)
    else:
        EndOfAnimation(obj=Objects.o6200_0000, animation_id=20)
        DisableObjectActivation(m10_02_Objects.o6100_0000, obj_act_id=6101)
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagDisabled(11600201))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602200))
    AND_2.Add(Singleplayer())
    AND_2.Add(FlagEnabled(11600201))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602201))
    AND_3.Add(Singleplayer())
    AND_3.Add(ObjectActivated(obj_act_id=11020202))
    AND_4.Add(Singleplayer())
    AND_4.Add(ObjectActivated(obj_act_id=11600203))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605120)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_3)
    EnableFlag(11600201)
    DisableObjectActivation(Objects.o6100_0006, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0000, 11, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0000, 1, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602201))
    
    ForceAnimation(Objects.o6200_0000, 21, wait_for_completion=True)
    EnableObjectActivation(m10_02_Objects.o6100_0000, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()
    DisableFlag(11600201)
    DisableObjectActivation(m10_02_Objects.o6100_0000, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0000, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0000, 0, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602200))
    
    ForceAnimation(Objects.o6200_0000, 20, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0006, obj_act_id=6101)
    DisableFlag(11605120)
    Restart()


@ContinueOnRest(11600250)
def Event_11600250():
    """Event 11600250"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605120))
    AND_1.Add(FlagDisabled(11600201))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=m10_02_Objects.o6100_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605120))
    AND_2.Add(FlagEnabled(11600201))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0006,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(Multiplayer())
    AND_3.Add(FlagDisabled(11600201))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1602200))
    AND_4.Add(Multiplayer())
    AND_4.Add(FlagEnabled(11600201))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1602201))
    AND_5.Add(Multiplayer())
    AND_5.Add(ObjectActivated(obj_act_id=11020202))
    AND_6.Add(Multiplayer())
    AND_6.Add(ObjectActivated(obj_act_id=11600203))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11600199)
def Event_11600199():
    """Event 11600199"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11600100))
    
    EnableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    EnableObjectActivation(Objects.o6100_0004, obj_act_id=6101)


@ContinueOnRest(11600210)
def Event_11600210():
    """Event 11600210"""
    if FlagEnabled(11600211):
        EndOfAnimation(obj=Objects.o6200_0001, animation_id=22)
        DisableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    else:
        EndOfAnimation(obj=Objects.o6200_0001, animation_id=21)
        DisableObjectActivation(Objects.o6100_0003, obj_act_id=6101)
    if FlagDisabled(11600100):
        DisableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    AND_1.Add(FlagEnabled(11600100))
    AND_1.Add(FlagDisabled(11600211))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602211))
    AND_2.Add(FlagEnabled(11600100))
    AND_2.Add(FlagEnabled(11600211))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602210))
    AND_3.Add(ObjectActivated(obj_act_id=11600212))
    AND_4.Add(ObjectActivated(obj_act_id=11600213))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605121)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_4)
    EnableFlag(11600211)
    DisableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0001, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0001, 2, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602210))
    
    ForceAnimation(Objects.o6200_0001, 22, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0003, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()
    DisableFlag(11600211)
    DisableObjectActivation(Objects.o6100_0003, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0001, 13, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0001, 3, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602211))
    
    ForceAnimation(Objects.o6200_0001, 21, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0002, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()


@ContinueOnRest(11600251)
def Event_11600251():
    """Event 11600251"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605121))
    AND_1.Add(FlagEnabled(11600211))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605121))
    AND_2.Add(FlagDisabled(11600211))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagDisabled(11600100))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11600220)
def Event_11600220():
    """Event 11600220"""
    if FlagEnabled(11600221):
        EndOfAnimation(obj=Objects.o6200_0002, animation_id=24)
        DisableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    else:
        EndOfAnimation(obj=Objects.o6200_0002, animation_id=21)
        DisableObjectActivation(Objects.o6100_0005, obj_act_id=6101)
    if FlagDisabled(11600100):
        DisableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    AND_1.Add(FlagEnabled(11600100))
    AND_1.Add(FlagDisabled(11600221))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602221))
    AND_2.Add(FlagEnabled(11600100))
    AND_2.Add(FlagEnabled(11600221))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602220))
    AND_3.Add(ObjectActivated(obj_act_id=11600222))
    AND_4.Add(ObjectActivated(obj_act_id=11600223))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605122)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_4)
    EnableFlag(11600221)
    DisableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0002, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0002, 4, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602220))
    
    ForceAnimation(Objects.o6200_0002, 24, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0005, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()
    DisableFlag(11600221)
    DisableObjectActivation(Objects.o6100_0005, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0002, 15, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0002, 5, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602221))
    
    ForceAnimation(Objects.o6200_0002, 21, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0004, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()


@ContinueOnRest(11600252)
def Event_11600252():
    """Event 11600252"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605122))
    AND_1.Add(FlagEnabled(11600221))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605122))
    AND_2.Add(FlagDisabled(11600221))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0005,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagDisabled(11600100))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11600230)
def Event_11600230():
    """Event 11600230"""
    if FlagEnabled(11600231):
        EndOfAnimation(obj=Objects.o6200_0003, animation_id=26)
        DisableObjectActivation(Objects.o6100_0007, obj_act_id=6101)
    else:
        EndOfAnimation(obj=Objects.o6200_0003, animation_id=21)
        DisableObjectActivation(Objects.o6100_0008, obj_act_id=6101)
    AND_1.Add(FlagDisabled(11600231))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1602231))
    AND_2.Add(FlagEnabled(11600231))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1602230))
    AND_3.Add(ObjectActivated(obj_act_id=11600232))
    AND_4.Add(ObjectActivated(obj_act_id=11600233))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605123)
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_4)
    EnableFlag(11600231)
    DisableObjectActivation(Objects.o6100_0007, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0003, 10, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0003, 6, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602230))
    
    ForceAnimation(Objects.o6200_0003, 26, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0008, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()
    DisableFlag(11600231)
    DisableObjectActivation(Objects.o6100_0008, obj_act_id=6101)
    ForceAnimation(Objects.o6200_0003, 17, wait_for_completion=True)
    ForceAnimation(Objects.o6200_0003, 7, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1602231))
    
    ForceAnimation(Objects.o6200_0003, 21, wait_for_completion=True)
    EnableObjectActivation(Objects.o6100_0007, obj_act_id=6101)
    DisableFlag(11605123)
    Restart()


@ContinueOnRest(11600253)
def Event_11600253():
    """Event 11600253"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11605123))
    AND_1.Add(FlagEnabled(11600231))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0007,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11605123))
    AND_2.Add(FlagDisabled(11600231))
    AND_2.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o6100_0008,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010170)
    Restart()


@RestartOnRest(11605150)
def Event_11605150(_, character: int, region: Region | int):
    """Event 11605150"""
    DisableNetworkSync()
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterOutsideRegion(character, region=region))
    
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(11605001)
def Event_11605001(_, character: int, radius: float, cancel_animation: int):
    """Event 11605001"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 2180))
    
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SetStandbyAnimationSettings(character)
    SkipLines(1)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)
    EnableAI(character)


@RestartOnRest(11605050)
def Event_11605050(_, character: int, region: Region | int, cancel_animation: int, left: int, radius: float):
    """Event 11605050"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 2180))
    
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    if ValueNotEqual(left=left, right=0):
        AND_3.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    if ValueNotEqual(left=left, right=0):
        OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SetStandbyAnimationSettings(character)
    SkipLines(1)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)
    EnableAI(character)


@RestartOnRest(11605101)
def Event_11605101():
    """Event 11605101"""
    if ThisEventFlagEnabled():
        AICommand(Characters.c2680_gst4, command_id=1, command_slot=0)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c2680_gst4, tae_event_id=700))
    
    SetNest(Characters.c2680_gst4, region=1602300)
    AICommand(Characters.c2680_gst4, command_id=0, command_slot=0)
    ReplanAI(Characters.c2680_gst4)
    
    MAIN.Await(CharacterInsideRegion(Characters.c2680_gst4, region=1602301))
    
    AICommand(Characters.c2680_gst4, command_id=1, command_slot=0)


@RestartOnRest(11600810)
def Event_11600810():
    """Event 11600810"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3420_0000)
        End()
    
    MAIN.Await(CharacterDead(Characters.c3420_0000))
    
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    if not OR_1:
        return
    AwardItemLot(34200200, host_only=True)


@RestartOnRest(11600400)
def Event_11600400():
    """Event 11600400"""
    DisableCharacterCollision(Characters.c3420_0000)
    DisableGravity(Characters.c3420_0000)
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(Characters.c3420_0000, cancel_animation=29060)
        End()
    OR_1.Add(EntityWithinDistance(entity=Characters.c3420_0000, other_entity=PLAYER, radius=10.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c3420_0000, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(Characters.c3420_0000)
    ForceAnimation(Characters.c3420_0000, 29060)


@RestartOnRest(11605200)
def Event_11605200(_, character: int, character_1: int, command_id: int, flag: Flag | int):
    """Event 11605200"""
    if ThisEventSlotFlagEnabled():
        MAIN.Await(CharacterBackreadEnabled(character))
    
        AICommand(character, command_id=command_id, command_slot=0)
        End()
    DisableCharacter(character_1)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=300))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=command_id, command_slot=0)
    EnableCharacter(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 8300, wait_for_completion=True)
    AND_1.Add(CharacterDoesNotHaveTAEEvent(character, tae_event_id=300))
    End()


@RestartOnRest(11605250)
def Event_11605250(_, character: Character | int):
    """Event 11605250"""
    DisableNetworkSync()
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=400))
    DisableCharacter(character)


@RestartOnRest(11600850)
def Event_11600850(_, character: Character | int):
    """Event 11600850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(11600600)
def Event_11600600(_, obj: Object | int, obj_act_id: int):
    """Event 11600600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11600650)
def Event_11600650(_, obj: int, obj_1: Object | int):
    """Event 11600650"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=101)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    ForceAnimation(obj, 100, loop=True)
    
    MAIN.Await(ObjectDestroyed(obj_1))
    
    ForceAnimation(obj, 101, wait_for_completion=True)
    EnableTreasure(obj=obj)


@ContinueOnRest(11600510)
def Event_11600510(_, character: Character | int, flag: Flag | int):
    """Event 11600510"""
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventSlotFlagDisabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11600520)
def Event_11600520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600530)
def Event_11600530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600530"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1310))
    AND_1.Add(FlagEnabled(CommonFlags.BonfireWarpOptionDisplayed))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600531)
def Event_11600531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600531"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1311))
    AND_1.Add(FlagEnabled(11600100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600532)
def Event_11600532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600532"""
    AND_1.Add(FlagDisabled(1314))
    AND_1.Add(FlagEnabled(1312))
    AND_1.Add(FlagEnabled(CommonFlags.FourKingsDead))
    AND_1.Add(FlagEnabled(11600593))
    AND_1.Add(OutsideMap(game_map=NEW_LONDO_RUINS))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11600537)
def Event_11600537(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600537"""
    if FlagDisabled(1670):
        return
    DisableCharacter(character)
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(1670))
    AND_1.Add(FlagDisabled(11800100))
    AND_1.Add(FlagEnabled(CommonFlags.FourKingsDead))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    ForceAnimation(character, 9060, wait_for_completion=True)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600538)
def Event_11600538(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600538"""
    AND_1.Add(FlagEnabled(1671))
    AND_1.Add(FlagEnabled(CommonFlags.BonfireWarpOptionDisplayed))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600539)
def Event_11600539(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600539"""
    AND_1.Add(FlagEnabled(1672))
    AND_1.Add(FlagEnabled(11800100))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11600540)
def Event_11600540(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600540"""
    OR_1.Add(FlagEnabled(1672))
    OR_1.Add(FlagEnabled(1678))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11600590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11600541)
def Event_11600541(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11600541"""
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    OR_1.Add(FlagEnabled(11600590))
    AND_2.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(character) > 0.0)
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=15.0))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7005, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11600545)
def Event_11600545(_, character: Character | int):
    """Event 11600545"""
    MAIN.Await(FlagEnabled(1464))
    
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)


@ContinueOnRest(11606200)
def Event_11606200():
    """Event 11606200"""
    OR_1.Add(FlagEnabled(1672))
    OR_1.Add(FlagEnabled(1673))
    OR_1.Add(FlagEnabled(1674))
    AND_1.Add(OR_1)
    AND_1.Add(InsideMap(game_map=NEW_LONDO_RUINS))
    AND_1.Add(FlagEnabled(821))
    
    MAIN.Await(AND_1)
    
    DisableFlag(821)
    EnableFlag(831)
    EnableCharacter(m18_00_Characters.c5330_0017)
    PlayCutscene(160040, cutscene_flags=0, player_id=10000, move_to_region=1802110, game_map=KILN_OF_THE_FIRST_FLAME)
    PlayCutscene(180041, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(823)
    Restart()


@ContinueOnRest(11605029)
def Event_11605029():
    """Event 11605029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0006, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11605034)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11605031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0006)
    if FlagEnabled(CommonFlags.FourKingsDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11605031))
    AND_1.Add(FlagDisabled(11605034))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11200300))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0006))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0006, other_entity=PLAYER, radius=5.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0006,
        region=1602000,
        summon_flag=11605031,
        dismissal_flag=11605034,
    )


@ContinueOnRest(11605030)
def Event_11605030():
    """Event 11605030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0006, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11605034)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11605031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0006)
    if FlagEnabled(CommonFlags.FourKingsDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11200300))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0006))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0006, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0006,
        region=1602000,
        summon_flag=11605031,
        dismissal_flag=11605034,
    )


@ContinueOnRest(11605990)
def Event_11605990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 11605990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11605032)
def Event_11605032():
    """Event 11605032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11605031))
    AND_1.Add(FlagEnabled(11605393))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0006, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0006)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0006, region=1602998))
    
    RotateToFaceEntity(Characters.c0000_0006, target_entity=1602997)
    ForceAnimation(Characters.c0000_0006, 7410)
    AICommand(Characters.c0000_0006, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0006)


@ContinueOnRest(11605033)
def Event_11605033():
    """Event 11605033"""
    AND_1.Add(FlagEnabled(11605031))
    AND_1.Add(CharacterHasSpecialEffect(Characters.c0000_0006, 2200))
    AND_1.Add(CharacterInsideRegion(Characters.c0000_0006, region=1602999))
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(Characters.c0000_0006)
    Wait(2.0)
    DisableInvincibility(Characters.c0000_0006)


@ContinueOnRest(11605843)
def Event_11605843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11605843"""
    AND_1.Add(Host())
    AND_1.Add(Multiplayer())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=line_intersects,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=target_entity)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


@ContinueOnRest(11605846)
def Event_11605846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11605846"""
    OR_1.Add(Multiplayer())
    OR_1.Add(UnknownPlayerType5())
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableObject(obj)
    CreateVFX(vfx_id)
    AND_3.Add(UnknownPlayerType5())
    AND_2.Add(not AND_3)
    AND_2.Add(Singleplayer())
    
    MAIN.Await(AND_2)
    
    DisableObject(obj)
    DeleteVFX(vfx_id)
    Restart()
