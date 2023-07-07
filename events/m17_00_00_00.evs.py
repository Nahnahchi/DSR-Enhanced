"""
Duke's Archives / Crystal Cave

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m17_00_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11700992()
    Event_11700998()
    Event_11700999()
    Event_11702098(0, character=Characters.c0000_mai2)
    Event_11705071(0, character=Characters.c2860_gnt1)
    Event_11705070(0, character=Characters.c2860_gnt1)
    if FlagEnabled(CommonFlags.SeathDead):
        RegisterBonfire(bonfire_flag=11700920, obj=Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11700992, obj=Objects.o0200_0000)
    RegisterBonfire(bonfire_flag=11700984, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11700976, obj=Objects.o0200_0003)
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=Objects.o7300)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=Objects.o7301)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=Objects.o7302)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=Objects.o7303)
    RegisterStatue(obj=Objects.o0101_0000, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0001, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0002, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0003, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0004, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0005, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0006, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=Objects.o0101_0007, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    SkipLinesIfClient(5)
    EnableFlag(405)
    DisableObject(Objects.o7902_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o7908_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    if FlagEnabled(11700140):
        DisableFlag(405)
    SkipLinesIfClient(9)
    SkipLinesIfFlagDisabled(6, 61700105)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702410))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1702402))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1702403))
    AND_1.Add(OR_1)
    SkipLinesIfConditionTrue(2, AND_1)
    EnableFlag(61700105)
    SkipLines(1)
    DisableFlag(61700105)
    if FlagEnabled(11700002):
        EndOfAnimation(obj=Objects.o7402, animation_id=0)
    if FlagEnabled(61700105):
        ForceAnimation(Objects.o7404, 1)
    Event_11700083(0, obj=Objects.o7906_0000, vfx_id=VFX.CheckpointFog2, destination=1702606, destination_1=1702607)
    Event_11700085()
    Event_11705080()
    Event_11705081()
    Event_11705082()
    Event_11705380()
    Event_11705381()
    Event_11705386()
    Event_11705382()
    Event_11705383()
    Event_11705384()
    Event_11705385()
    Event_11700110()
    Event_11700120(0, obj_act_id=11700120, obj=Objects.o7250, obj_1=Objects.o7201_00, animation_id=0, left=0)
    Event_11700120(5, obj_act_id=11700125, obj=Objects.o7251, obj_1=1701126, animation_id=1, left=1)
    Event_11700160(
        0,
        flag=11700100,
        destination=Objects.o7240,
        obj_act_id=11700210,
        obj_act_id_1=11700211,
        flag_1=11705090,
        flag_2=11705180,
        flag_3=11705181,
    )
    Event_11700105(
        0,
        flag=11700100,
        obj=Objects.o7240,
        obj_1=Objects.o7201_01,
        obj_2=Objects.o7201_05,
        flag_1=11705090,
        flag_2=11705180,
        flag_3=11705181,
    )
    Event_11700160(
        1,
        flag=11700102,
        destination=Objects.o7241,
        obj_act_id=11700220,
        obj_act_id_1=11700221,
        flag_1=11705091,
        flag_2=11705182,
        flag_3=11705183,
    )
    Event_11700105(
        2,
        flag=11700102,
        obj=Objects.o7241,
        obj_1=Objects.o7201_03,
        obj_2=Objects.o7201_06,
        flag_1=11705091,
        flag_2=11705182,
        flag_3=11705183,
    )
    Event_11700090(0, flag=11700100, state=0, anchor_entity=Objects.o7201_01, flag_1=11705090)
    Event_11700090(1, flag=11700100, state=1, anchor_entity=Objects.o7201_05, flag_1=11705090)
    Event_11700090(2, flag=11700102, state=0, anchor_entity=Objects.o7201_03, flag_1=11705091)
    Event_11700090(3, flag=11700102, state=1, anchor_entity=Objects.o7201_06, flag_1=11705091)
    Event_11705150(0, flag=11700205, destination=Objects.o7230_00, destination_1=Objects.o7230_01)
    Event_11700200(
        0,
        flag=11700205,
        obj=Objects.o7230_00,
        obj_1=Objects.o7231,
        collision=Collisions.h0124B0,
        collision_1=Collisions.h0124B0_0000,
        navmesh_id=Navigation.Navmesh_BeforeRotatingStairs0,
        navmesh_id_1=Navigation.Navmesh_BeforeRotatingStairs1,
        flag_1=11705151,
    )
    Event_11700200(
        1,
        flag=11700205,
        obj=Objects.o7230_01,
        obj_1=Objects.o7231_01,
        collision=Collisions.h0125B0,
        collision_1=Collisions.h0125B0_0000,
        navmesh_id=Navigation.Navmesh_AfterRotatingStairs0,
        navmesh_id_1=Navigation.Navmesh_AfterRotatingStairs1,
        flag_1=11705152,
    )
    Event_11700150(0, collision=Collisions.h7500B0, region=1702780)
    Event_11700150(1, collision=Collisions.h7501B0, region=1702781)
    Event_11705100()
    Event_11705103()
    Event_11705108()
    Event_11705101()
    Event_11705102()
    Event_11700130()
    RunEvent(11700132, slot=0, args=(0,))
    Event_11700300(0, obj_act_id=11700300, text=10010863, anchor_entity=Objects.o7401_00)
    Event_11700300(1, obj_act_id=11700311, text=10010879, anchor_entity=Objects.o7401_01)
    Event_11700300(2, obj_act_id=11700302, text=10010863, anchor_entity=Objects.o7401_02)
    Event_11700300(3, obj_act_id=11700313, text=10010879, anchor_entity=Objects.o7401_03)
    Event_11700300(4, obj_act_id=11700304, text=10010863, anchor_entity=Objects.o7401_04)
    Event_11700300(5, obj_act_id=11700305, text=10010863, anchor_entity=Objects.o7401_05)
    Event_11700300(6, obj_act_id=11700320, text=10010865, anchor_entity=Objects.o7401_06)
    Event_11700140()
    Event_11700141()
    Event_11705170()
    Event_11700700()
    DisableSoundEvent(sound_id=Sounds.SeathCaveMusic)
    if FlagEnabled(CommonFlags.SeathDead):
        Event_11705392()
        DisableObject(Objects.o7500)
        DisableObject(Objects.o7900_0000)
        DeleteVFX(VFX.SeathCaveEntranceFog, erase_root_only=False)
    else:
        Event_11700000()
        Event_11705390()
        Event_11705391()
        Event_11705393()
        Event_11705392()
        Event_11700001()
        Event_11705394()
        Event_11705395()
        Event_11705396()
        Event_11705397()
    Event_11705200()
    Event_11705270(0, character=Characters.c3250_0000, radius=15.0)
    Event_11705270(1, character=Characters.c3250_0001, radius=15.0)
    Event_11705140(0, character=Characters.c2690_0015, region=1702150)
    Event_11705140(1, character=Characters.c2690_0014, region=1702151)
    Event_11705160(0, character=Characters.c3230_0000, radius=3.0)
    Event_11705160(1, character=Characters.c3230_0001, radius=3.0)
    Event_11705160(2, character=Characters.c3230_0002, radius=10.0)
    Event_11705010(0, character=Characters.c2780_0000)
    Event_11705020(0, character=Characters.c2780_0000)
    Event_11705030(0, character=Characters.c2780_0000)
    Event_11705040(0, character=Characters.c2780_0000)
    Event_11705050(0, character=Characters.c2780_0000, region=1702010)
    Event_11700900(0, character=Characters.c2780_0000)
    Event_11705060(0, character=Characters.c2780_0000)
    Event_11705010(1, character=Characters.c2780_0001)
    Event_11705020(1, character=Characters.c2780_0001)
    Event_11705030(1, character=Characters.c2780_0001)
    Event_11705040(1, character=Characters.c2780_0001)
    Event_11705050(1, character=Characters.c2780_0001, region=1702011)
    Event_11700900(1, character=Characters.c2780_0001)
    Event_11705060(1, character=Characters.c2780_0001)
    Event_11700810(0, character=Characters.c0000_crs1, left=0, item_lot=0)
    Event_11700810(1, character=Characters.c3300_0000, left=1, item_lot=33001000)
    Event_11700810(2, character=Characters.c3300_0001, left=1, item_lot=33001000)
    Event_11700810(3, character=Characters.c3300_0002, left=1, item_lot=33001000)
    Event_11700810(4, character=Characters.c3300_0003, left=1, item_lot=33001000)
    Event_11700810(5, character=Characters.c3461_0000, left=0, item_lot=0)
    Event_11700810(6, character=Characters.c3461_0001, left=0, item_lot=0)
    Event_11700810(10, character=Characters.c2711_0001, left=0, item_lot=0)
    Event_11700810(11, character=Characters.c2711_0002, left=0, item_lot=0)
    Event_11700810(12, character=Characters.c3330_0003, left=0, item_lot=0)
    Event_11700810(13, character=Characters.c3330_0004, left=0, item_lot=0)
    Event_11700810(14, character=Characters.c2860_gnt1, left=0, item_lot=0)
    Event_11700810(15, character=Characters.c3461_pig1, left=0, item_lot=0)
    Event_11700810(16, character=Characters.c3461_pig2, left=0, item_lot=0)
    Event_11700810(16, character=Characters.c0000_mai1, left=0, item_lot=0)
    Event_11705280(0, character=Characters.c3230_0000)
    Event_11705280(1, character=Characters.c3230_0001)
    Event_11700600(1, obj=Objects.o0110_0001, obj_act_id=11700601)
    Event_11700600(2, obj=Objects.o0110_0002, obj_act_id=11700602)
    Event_11700600(3, obj=Objects.o0110_0003, obj_act_id=11700603)
    Event_11700600(4, obj=Objects.o0110_0004, obj_act_id=11700604)
    Event_11700600(5, obj=1701655, obj_act_id=11700605)
    Event_11700600(6, obj=Objects.o0110_0006, obj_act_id=11700606)
    Event_11700600(7, obj=1701657, obj_act_id=11700607)
    Event_11700600(8, obj=Objects.o0110_0008, obj_act_id=11700608)
    Event_11700600(9, obj=Objects.o0110_0009, obj_act_id=11700609)
    Event_11700600(10, obj=Objects.o0110_0010, obj_act_id=11700610)
    Event_11700600(11, obj=1701661, obj_act_id=11700611)
    Event_11700600(12, obj=1701662, obj_act_id=11700612)
    Event_11700600(13, obj=Objects.o0110_0013, obj_act_id=11700613)
    Event_11700600(14, obj=Objects.o0110_0014, obj_act_id=11700614)
    Event_11700600(15, obj=Objects.o0110_0015, obj_act_id=11700615)
    Event_11700600(16, obj=Objects.o0110_0016, obj_act_id=11700616)
    Event_11705110(0, character=Characters.c3330_0000)
    Event_11705110(1, character=Characters.c3330_0001)
    Event_11705110(2, character=Characters.c3330_0002)
    Event_11705110(3, character=Characters.c3330_0009)
    Event_11705110(4, character=Characters.c3330_0010)
    Event_11705110(5, character=Characters.c3330_0012)
    Event_11705110(6, character=Characters.c3330_0006)
    Event_11705110(7, character=Characters.c3330_0007)
    Event_11705110(8, character=Characters.c3330_0008)
    Event_11705110(9, character=1700119)
    Event_11705110(10, character=Characters.c3330_0005)
    Event_11705110(11, character=1700121)
    Event_11705110(12, character=1700122)
    Event_11705110(13, character=1700123)
    Event_11705110(14, character=1700124)
    Event_11705110(15, character=1700125)
    Event_11705110(16, character=1700126)
    Event_11705110(17, character=1700127)
    Event_11705110(18, character=Characters.c3330_0020)
    Event_11705110(19, character=Characters.c3330_0021)
    Event_11705843(0, flag=CommonFlags.SeathDead, line_intersects=1701990, anchor_entity=1702998, target_entity=1702997)
    Event_11705846(0, flag=CommonFlags.SeathDead, obj=Objects.o7900_0000, vfx_id=VFX.SeathCaveEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_crs1, event_flag=8988)
    HumanityRegistration(Characters.c0000_0002, event_flag=8334)
    HumanityRegistration(Characters.c0000_0006, event_flag=8334)
    SkipLinesIfFlagRangeAnyEnabled(1, (1093, 1096))
    DisableCharacter(Characters.c0000_0002)
    if FlagDisabled(1099):
        DisableCharacter(Characters.c0000_0006)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0006, team_type=TeamType.HostileAlly)
    if FlagEnabled(11700594):
        Move(
            Characters.c0000_0002,
            destination=1702501,
            destination_type=CoordEntityType.Region,
            set_draw_parent=Collisions.h0041B0,
        )
    Event_11700510(0, character=Characters.c0000_0002, flag=1096)
    Event_11700520(0, character=Characters.c0000_0002, first_flag=1090, last_flag=1109, flag=1097)
    Event_11700520(1, character=Characters.c0000_0006, first_flag=1090, last_flag=1109, flag=1097)
    Event_11700530(0, character=Characters.c0000_0002, first_flag=1090, last_flag=1109, flag=1093)
    Event_11700531(0, character=Characters.c0000_0002, first_flag=1090, last_flag=1109, flag=1094)
    Event_11700532(0, character=Characters.c0000_0002, first_flag=1090, last_flag=1109, flag=1095)
    Event_11700533(
        0,
        character=Characters.c0000_0002,
        first_flag=1090,
        last_flag=1109,
        flag=1099,
        character_1=Characters.c0000_0006,
    )
    HumanityRegistration(Characters.c0000_0004, event_flag=8454)
    SkipLinesIfFlagEnabled(2, 1547)
    SkipLinesIfFlagEnabled(1, 1542)
    DisableCharacter(Characters.c0000_0004)
    Event_11700510(2, character=Characters.c0000_0004, flag=1547)
    Event_11700520(2, character=Characters.c0000_0004, first_flag=1540, last_flag=1569, flag=1548)
    Event_11700538(0, character=Characters.c0000_0004, first_flag=1540, last_flag=1569, flag=1541)
    Event_11700539(0, character=Characters.c0000_0004, first_flag=1540, last_flag=1569, flag=1542)
    Event_11700540(0, character=Characters.c0000_0004, first_flag=1540, last_flag=1569, flag=1543)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0003, team_type=TeamType.HostileAlly)
    if FlagDisabled(1181):
        DisableCharacter(Characters.c0000_0003)
    Event_11700520(3, character=Characters.c0000_0003, first_flag=1170, last_flag=1189, flag=1177)
    Event_11700545(0, character=Characters.c0000_0003, first_flag=1170, last_flag=1189, flag=1181)


@ContinueOnRest(11702098)
def Event_11702098(_, character: Character | int):
    """Event 11702098"""
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_1)
    
    DisableAI(character)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_2)
    
    EnableAI(character)
    Restart()


@ContinueOnRest(11700992)
def Event_11700992():
    """Event 11700992"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(Characters.c0000_mai2))
    
    AwardItemLot(26900100, host_only=True)


@RestartOnRest(11700998)
def Event_11700998():
    """Event 11700998"""
    MAIN.Await(PlayerHasGood(9012, including_storage=True))
    
    RemoveGoodFromPlayer(item=9012, quantity=1)


@RestartOnRest(11700999)
def Event_11700999():
    """Event 11700999"""
    DisableAI(Characters.c0000_mai2)
    SetTeamType(Characters.c0000_mai2, TeamType.Ally)
    
    MAIN.Await(Attacked(attacked_entity=Characters.c0000_mai2, attacker=PLAYER))
    
    EnableAI(Characters.c0000_mai2)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_mai2, team_type=TeamType.Enemy)


@RestartOnRest(11705071)
def Event_11705071(_, character: Character | int):
    """Event 11705071"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=500))
    
    EzstateAIRequest(character, command_id=1500, command_slot=0)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(character, tae_event_id=500))
    
    Restart()


@RestartOnRest(11705070)
def Event_11705070(_, character: Character | int):
    """Event 11705070"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=1400))
    
    Wait(5.0)
    EzstateAIRequest(character, command_id=1501, command_slot=0)
    Restart()


@ContinueOnRest(11700080)
def Event_11700080(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11700080"""
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
    AND_3.Add(FlagEnabled(11700080))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11700080)
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@ContinueOnRest(11700083)
def Event_11700083(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11700083"""
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


@RestartOnRest(11705080)
def Event_11705080():
    """Event 11705080"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2370_0002)
        DisableCharacter(Characters.c2370_0003)
        DisableCharacter(Characters.c2370_0004)
        DisableCharacter(Characters.c2370_0005)
        DisableCharacter(Characters.c2710_0015)
        DisableCharacter(Characters.c2710_0016)
        DisableCharacter(Characters.c2710_0017)
        DisableCharacter(Characters.c2710_0018)
        DisableCharacter(Characters.c3330_0020)
        DisableCharacter(Characters.c3330_0021)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11705081)
def Event_11705081():
    """Event 11705081"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2370_0002)
    Kill(Characters.c2370_0003)
    Kill(Characters.c2370_0004)
    Kill(Characters.c2370_0005)
    Kill(Characters.c2710_0015)
    Kill(Characters.c2710_0016)
    Kill(Characters.c2710_0017)
    Kill(Characters.c2710_0018)
    Kill(Characters.c3330_0020)
    Kill(Characters.c3330_0021)


@RestartOnRest(11705082)
def Event_11705082():
    """Event 11705082"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11700050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11700050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11700050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11700050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11700050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=DUKES_ARCHIVES))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11700050))
    if not OR_6:
        return RESTART
    EnableFlag(11700050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=DUKES_ARCHIVES))
    if not AND_7:
        return RESTART
    DisableFlag(11700050)
    EnableFlag(11705085)


@ContinueOnRest(11700085)
def Event_11700085():
    """Event 11700085"""
    if FlagEnabled(11800100):
        EnableFlag(11700086)
        DisableObject(Objects.o7907_0000)
        DeleteVFX(VFX.GoldenFog, erase_root_only=False)
        End()
    if FlagEnabled(11700086):
        DisableObject(Objects.o7907_0000)
        DeleteVFX(VFX.GoldenFog, erase_root_only=False)
        End()
    if Client():
        return
    
    MAIN.Await(ActionButton(
        prompt_text=10010410,
        anchor_entity=1702610,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1701710,
    ))
    
    DisplayStatus(10010630)
    Restart()


@RestartOnRest(11700000)
def Event_11700000():
    """Event 11700000"""
    if ThisEventFlagEnabled():
        return
    DisableObject(Objects.o7900_0000)
    DeleteVFX(VFX.SeathCaveEntranceFog, erase_root_only=False)
    DisableCharacter(Characters.c5290_0001)
    EnableObjectInvulnerability(Objects.o7500)
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5290_0001)
    EnableFlag(11705390)
    EnableFlag(11705391)
    EnableFlag(11705393)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170000, cutscene_flags=0, player_id=10000, move_to_region=1702801, game_map=DUKES_ARCHIVES)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        170000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1702801,
        game_map=DUKES_ARCHIVES,
    )
    SkipLines(1)
    PlayCutscene(170000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObjectInvulnerability(Objects.o7500)
    EnableObject(Objects.o7900_0000)
    CreateVFX(VFX.SeathCaveEntranceFog)
    Move(Characters.c5290_0001, destination=1702800, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(Characters.c5290_0001)


@ContinueOnRest(11705380)
def Event_11705380():
    """Event 11705380"""
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1701890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1702897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11705381)
def Event_11705381():
    """Event 11705381"""
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(FlagEnabled(11705386))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1702897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11705386)
def Event_11705386():
    """Event 11705386"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11700000))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1702896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5290_0000)


@ContinueOnRest(11705382)
def Event_11705382():
    """Event 11705382"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(ActionButton(
        prompt_text=10010404,
        anchor_entity=1702895,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1702894)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    DisableBossHealthBar(Characters.c5290_0000, name=5290)
    Restart()


@RestartOnRest(11705383)
def Event_11705383():
    """Event 11705383"""
    DisableAI(Characters.c5290_0000)
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(FlagEnabled(11705386))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702890))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.c5290_0000)
    EnableBossHealthBar(Characters.c5290_0000, name=5290)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1702890))
    
    Restart()


@ContinueOnRest(11705384)
def Event_11705384():
    """Event 11705384"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=Sounds.SeathTowerMusic)
    AND_1.Add(FlagDisabled(11700000))
    AND_1.Add(FlagEnabled(11705386))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.SeathTowerMusic)
    OR_1.Add(FlagEnabled(11700000))
    OR_1.Add(CharacterOutsideRegion(PLAYER, region=1702890))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(11705385)
def Event_11705385():
    """Event 11705385"""
    EnableImmortality(Characters.c5290_0000)
    AddSpecialEffect(Characters.c5290_0000, 5441)
    AddSpecialEffect(Characters.c5290_0000, 5442)
    AddSpecialEffect(Characters.c5290_0000, 5443)
    
    MAIN.Await(FlagEnabled(11700000))
    
    DisableCharacter(Characters.c5290_0000)
    DisableObject(Objects.o7510)
    DisableObject(Objects.o7901_0000)
    DeleteVFX(VFX.SeathTowerEntranceFog)


@ContinueOnRest(11705390)
def Event_11705390():
    """Event 11705390"""
    AND_1.Add(FlagDisabled(CommonFlags.SeathDead))
    AND_1.Add(FlagEnabled(11700000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1701990,
    ))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, target_entity=1702997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(Characters.c5290_0001)
    Restart()


@ContinueOnRest(11705391)
def Event_11705391():
    """Event 11705391"""
    AND_1.Add(FlagDisabled(CommonFlags.SeathDead))
    AND_1.Add(FlagEnabled(11705393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterAlive(Characters.c5290_0001))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1702998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1702997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11705393)
def Event_11705393():
    """Event 11705393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(11700000))
        AND_1.Add(FlagDisabled(CommonFlags.SeathDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1702996))
        AND_2.Add(ThisEventFlagEnabled())
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfFinishedConditionTrue(input_condition=AND_2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5290_0001)


@RestartOnRest(11705392)
def Event_11705392():
    """Event 11705392"""
    if FlagEnabled(CommonFlags.SeathDead):
        DisableCharacter(Characters.c5290_0001)
        Kill(Characters.c5290_0001)
        DisableCharacter(Characters.c5291_0000)
        Kill(Characters.c5291_0000)
        End()
    DisableAI(Characters.c5290_0001)
    AND_1.Add(FlagEnabled(11705393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702990))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.c5290_0001)
    EnableBossHealthBar(Characters.c5290_0001, name=5290)


@ContinueOnRest(11700001)
def Event_11700001():
    """Event 11700001"""
    DisableObject(Objects.o0200_0002)
    
    MAIN.Await(CharacterDead(Characters.c5290_0001))
    
    EnableFlag(CommonFlags.SeathDead)
    KillBoss(game_area_param_id=1700800)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=38)
    DisableObject(Objects.o7900_0000)
    DeleteVFX(VFX.SeathCaveEntranceFog)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=Objects.o0200_0002, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11700920, obj=Objects.o0200_0002)


@ContinueOnRest(11705394)
def Event_11705394():
    """Event 11705394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.SeathDead))
    AND_1.Add(FlagEnabled(11705392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11705391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.SeathCaveMusic)


@ContinueOnRest(11705395)
def Event_11705395():
    """Event 11705395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.SeathDead))
    AND_1.Add(FlagEnabled(11705394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.SeathCaveMusic)


@RestartOnRest(11705396)
def Event_11705396():
    """Event 11705396"""
    AddSpecialEffect(Characters.c5290_0001, 5440)
    AddSpecialEffect(Characters.c5290_0001, 5441)
    AddSpecialEffect(Characters.c5290_0001, 5442)
    AddSpecialEffect(Characters.c5290_0001, 5443)
    EnableImmortality(Characters.c5290_0001)
    CreateObjectVFX(Objects.o7500, vfx_id=100, model_point=170004)
    
    MAIN.Await(ObjectDestroyed(Objects.o7500))
    
    DeleteObjectVFX(1703100)
    ForceAnimation(Characters.c5290_0001, 7000)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5290_0001, tae_event_id=500))
    
    RemoveSpecialEffect(Characters.c5290_0001, 5440)
    RemoveSpecialEffect(Characters.c5290_0001, 5441)
    RemoveSpecialEffect(Characters.c5290_0001, 5442)
    RemoveSpecialEffect(Characters.c5290_0001, 5443)
    DisableImmortality(Characters.c5290_0001)


@RestartOnRest(11705397)
def Event_11705397():
    """Event 11705397"""
    DisableCharacter(Characters.c5291_0000)
    if FlagEnabled(CommonFlags.SeathDead):
        return
    if ThisEventFlagEnabled():
        SetDisplayMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(Characters.c5290_0001, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c5290_0001))
    
    CreateNPCPart(Characters.c5290_0001, npc_part_id=5290, part_index=NPCPartType.Part1, part_health=330)
    AND_1.Add(HealthRatio(Characters.c5290_0001) > 0.0)
    AND_1.Add(CharacterPartHealth(Characters.c5290_0001, npc_part_id=5290) <= 0)
    AND_2.Add(HealthRatio(Characters.c5290_0001) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ForceAnimation(Characters.c5290_0001, 8000)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5290_0001, tae_event_id=400))
    
    Move(
        Characters.c5291_0000,
        destination=Characters.c5290_0001,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=Characters.c5290_0001,
    )
    EnableCharacter(Characters.c5291_0000)
    SetDisplayMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5290_0001, bit_index=1, switch_type=OnOffChange.Off)
    ForceAnimation(Characters.c5291_0000, 8100)
    AICommand(Characters.c5290_0001, command_id=20, command_slot=0)
    ReplanAI(Characters.c5290_0001)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(52910000, host_only=True)


@ContinueOnRest(11700160)
def Event_11700160(
    _,
    flag: Flag | int,
    destination: int,
    obj_act_id: int,
    obj_act_id_1: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 11700160"""
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_3.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_1)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_2)
    SkipLinesIfFlagEnabled(8, flag)
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(destination, 0)
    WaitFrames(frames=105)
    EnableFlag(flag_2)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(destination, 2)
    WaitFrames(frames=105)
    EnableFlag(flag_3)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()


@ContinueOnRest(11700105)
def Event_11700105(
    _,
    flag: Flag | int,
    obj: int,
    obj_1: Object | int,
    obj_2: Object | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 11700105"""
    if FlagEnabled(flag):
        EndOfAnimation(obj=obj, animation_id=11)
        EnableObjectActivation(obj_1, obj_act_id=-1)
        DisableObjectActivation(obj_2, obj_act_id=-1)
    else:
        DisableObjectActivation(obj_1, obj_act_id=-1)
        EnableObjectActivation(obj_2, obj_act_id=-1)
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(flag_2))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(flag_3))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_2)
    EnableFlag(flag)
    ForceAnimation(obj, 1)
    WaitFrames(frames=300)
    DisableFlag(flag_1)
    Restart()
    DisableFlag(flag)
    ForceAnimation(obj, 3)
    WaitFrames(frames=344)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11700090)
def Event_11700090(_, flag: Flag | int, state: uchar, anchor_entity: int, flag_1: Flag | int):
    """Event 11700090"""
    DisableNetworkSync()
    AND_1.Add(FlagState(state, FlagType.Absolute, flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=195,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010170, anchor_entity=anchor_entity)
    Restart()


@ContinueOnRest(11705150)
def Event_11705150(_, flag: Flag | int, destination: int, destination_1: int):
    """Event 11705150"""
    AND_1.Add(ActionButton(
        prompt_text=10010503,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010503,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    if FlagDisabled(flag):
        ForceAnimation(destination, 0)
    else:
        ForceAnimation(destination, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_2)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    if FlagDisabled(flag):
        ForceAnimation(destination_1, 0)
    else:
        ForceAnimation(destination_1, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    EnableFlag(11705151)
    EnableFlag(11705152)
    AND_3.Add(FlagDisabled(11705151))
    AND_3.Add(FlagDisabled(11705152))
    
    MAIN.Await(AND_3)
    
    Restart()


@ContinueOnRest(11700200)
def Event_11700200(
    _,
    flag: Flag | int,
    obj: int,
    obj_1: int,
    collision: Collision | int,
    collision_1: Collision | int,
    navmesh_id: NavigationEvent | int,
    navmesh_id_1: NavigationEvent | int,
    flag_1: Flag | int,
):
    """Event 11700200"""
    DisableObject(obj_1)
    if FlagDisabled(flag):
        EndOfAnimation(obj=obj, animation_id=3)
        DisableMapCollision(collision=collision_1)
        DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Solid)
    else:
        EndOfAnimation(obj=obj, animation_id=1)
        DisableMapCollision(collision=collision)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    if FlagDisabled(flag):
        ForceAnimation(obj, 1)
        DisableMapCollision(collision=collision)
        EnableObject(obj_1)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
        ForceAnimation(obj_1, 1)
        WaitFrames(frames=180)
        DisableObject(obj_1)
        EnableMapCollision(collision=collision_1)
        EnableFlag(flag)
        DisableFlag(flag_1)
        Restart()
    ForceAnimation(obj, 3)
    DisableMapCollision(collision=collision_1)
    EnableObject(obj_1)
    EnableNavmeshType(navmesh_id=navmesh_id_1, navmesh_type=NavmeshType.Solid)
    ForceAnimation(obj_1, 3)
    WaitFrames(frames=180)
    DisableObject(obj_1)
    EnableMapCollision(collision=collision)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11700110)
def Event_11700110():
    """Event 11700110"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(Objects.o7201_04, obj_act_id=-1)
        EndOfAnimation(obj=Objects.o7200_00, animation_id=0)
        DisableObject(Objects.o7199)
        DisableMapCollision(collision=Collisions.h0042B0)
        End()
    DisableObject(Objects.o7199)
    DisableMapCollision(collision=Collisions.h0043B0)
    
    MAIN.Await(ObjectActivated(obj_act_id=11700110))
    
    DisableMapCollision(collision=Collisions.h0042B0)
    EnableObject(Objects.o7199)
    ForceAnimation(Objects.o7200_00, 0)
    ForceAnimation(Objects.o7199, 0, wait_for_completion=True)
    DisableObject(Objects.o7199)
    EnableMapCollision(collision=Collisions.h0043B0)


@ContinueOnRest(11700120)
def Event_11700120(_, obj_act_id: Flag | int, obj: int, obj_1: Object | int, animation_id: int, left: int):
    """Event 11700120"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SkipLinesIfValueEqual(1, left=left, right=1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    End()
    if ValueNotEqual(left=left, right=0):
        OR_1.Add(FlagEnabled(11700140))
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    
    MAIN.Await(OR_1)
    
    EnableFlag(obj_act_id)
    ForceAnimation(obj, animation_id)


@ContinueOnRest(11700150)
def Event_11700150(_, collision: Collision | int, region: Region | int):
    """Event 11700150"""
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    EnableMapCollision(collision=collision)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DisableMapCollision(collision=collision)
    Restart()


@ContinueOnRest(11705100)
def Event_11705100():
    """Event 11705100"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702890))
    AND_1.Add(Host())
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=1702900)
    SaveRequest()


@ContinueOnRest(11705101)
def Event_11705101():
    """Event 11705101"""
    AND_1.Add(Host())
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(51700990))
    AND_1.Add(FlagDisabled(11705101))
    AND_1.Add(FlagDisabled(11700133))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702100))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(11705106))
    AND_3.Add(Host())
    AND_3.Add(FlagEnabled(11705107))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFlagEnabled(9, 11700002)
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170010, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(170010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    ForceAnimation(Objects.o7402, 0)
    EnableFlag(11700002)
    EnableFlag(61700105)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_3)
    if FlagDisabled(61700105):
        Event_11705108()
        Restart()
    EnableSoundEvent(sound_id=Sounds.SirenSound)
    ForceAnimation(Objects.o7404, 0)
    WaitFrames(frames=150)
    ForceAnimation(Objects.o7404, 1)
    Event_11705108()
    Restart()
    if FlagEnabled(61700105):
        Event_11705108()
        Restart()
    DisableSoundEvent(sound_id=Sounds.SirenSound)
    EnableFlag(11700133)
    ForceAnimation(Objects.o7404, 2)
    WaitFrames(frames=50)
    Event_11705108()
    Restart()


@ContinueOnRest(11705102)
def Event_11705102():
    """Event 11705102"""
    DisableNetworkSync()
    if FlagDisabled(61700105):
        DisableSoundEvent(sound_id=Sounds.SirenSound)


@ContinueOnRest(11705103)
def Event_11705103():
    """Event 11705103"""
    AND_1.Add(FlagEnabled(61700105))
    AND_1.Add(ObjectActivated(obj_act_id=11705105))
    AND_2.Add(FlagDisabled(61700105))
    AND_2.Add(ObjectActivated(obj_act_id=11705105))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    EnableFlag(11705106)
    Restart()
    EnableFlag(11705107)
    Restart()


@ContinueOnRest(11705108)
def Event_11705108():
    """Event 11705108"""
    DisableNetworkSync()
    AND_1.Add(FramesElapsed(frames=10))
    AND_1.Add(InsideMap(game_map=DUKES_ARCHIVES))
    
    MAIN.Await(AND_1)
    
    EnableObjectActivation(Objects.o7202, obj_act_id=-1)


@RestartOnRest(11705110)
def Event_11705110(_, character: Character | int):
    """Event 11705110"""
    AND_1.Add(FlagEnabled(61700105))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1702100))
    OR_7.Add(CharacterInsideRegion(PLAYER, region=1702101))
    AND_1.Add(OR_7)
    AND_2.Add(FlagEnabled(61700105))
    AND_2.Add(AllPlayersOutsideRegion(region=1702100))
    AND_2.Add(AllPlayersOutsideRegion(region=1702101))
    AND_3.Add(FlagDisabled(61700105))
    AND_3.Add(FlagEnabled(11700002))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_1)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    AND_7.Add(AllPlayersOutsideRegion(region=1702100))
    AND_7.Add(AllPlayersOutsideRegion(region=1702101))
    OR_2.Add(AND_7)
    OR_2.Add(FlagDisabled(61700105))
    
    MAIN.Await(OR_2)
    
    Restart()
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_2)
    AICommand(character, command_id=2, command_slot=0)
    ReplanAI(character)
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1702100))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1702101))
    OR_3.Add(FlagDisabled(61700105))
    
    MAIN.Await(OR_3)
    
    Restart()
    AICommand(character, command_id=3, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(FlagEnabled(61700105))
    
    Restart()


@RestartOnRest(11700130)
def Event_11700130():
    """Event 11700130"""
    if Client():
        return
    if FlagEnabled(51700990):
        DisableCharacter(Characters.c2690_0000)
        Kill(Characters.c2690_0000)
        End()
    DisableCharacterCollision(Characters.c2690_0000)
    DisableGravity(Characters.c2690_0000)


@RestartOnRest(11705140)
def Event_11705140(_, character: int, region: Region | int):
    """Event 11705140"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11705101))
    
    SetNest(character, region=region)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(OR_1)
    
    ClearTargetList(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@ContinueOnRest(11700140)
def Event_11700140():
    """Event 11700140"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o7400, animation_id=0)
        End()
    AND_1.Add(PlayerHasGood(2005))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o7400,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(FlagEnabled(CommonFlags.SeathDead))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(405)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=Objects.o7400, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o7400, 0)
    if Client():
        return
    DisplayDialog(text=10010864, anchor_entity=Objects.o7400, button_type=ButtonType.Yes_or_No)
    End()


@ContinueOnRest(11700141)
def Event_11700141():
    """Event 11700141"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11700140))
    AND_1.Add(PlayerDoesNotHaveGood(2005))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o7400,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11700140))
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o7400,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010163, anchor_entity=Objects.o7400)
    Restart()


@RestartOnRest(CommonFlags.InArchivesPrison)
def Event_11705170():
    """Event 11705170"""
    DisableNetworkSync()
    if Client():
        return
    DisableFlag(CommonFlags.InArchivesPrison)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1702402))
    
    EnableFlag(CommonFlags.InArchivesPrison)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1702402))
    
    Restart()


@RestartOnRest(11705160)
def Event_11705160(_, character: int, radius: float):
    """Event 11705160"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    
    SetStandbyAnimationSettings(character, cancel_animation=13000)


@RestartOnRest(11705250)
def Event_11705250(_, region: Region | int, character: int, animation_id: int):
    """Event 11705250"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, animation_id, wait_for_completion=True)
    EnableAI(character)


@RestartOnRest(11705270)
def Event_11705270(_, character: int, radius: float):
    """Event 11705270"""
    if ThisEventSlotFlagEnabled():
        return
    SetStandbyAnimationSettings(character, standby_animation=9000)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@ContinueOnRest(11700300)
def Event_11700300(_, obj_act_id: Flag | int, text: EventText | int, anchor_entity: int):
    """Event 11700300"""
    if Client():
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11705200)
def Event_11705200():
    """Event 11705200"""
    Event_11705240(0, character=Characters.c2370_0002)
    Event_11705240(1, character=Characters.c2370_0003)
    Event_11705240(2, character=Characters.c2370_0004)
    Event_11705240(3, character=Characters.c2370_0005)
    Event_11705201(0, flag=11705200, character=Characters.c2370_0000, region=1702301, flag_1=11705202)
    Event_11705201(1, flag=11705201, character=Characters.c2370_0000, region=1702306, flag_1=11705202)
    Event_11705201(2, flag=11705202, character=Characters.c2370_0000, region=1702305, flag_1=11705202)
    EnableFlag(11705210)
    Event_11705201(10, flag=11705210, character=Characters.c2370_0001, region=1702311, flag_1=11705213)
    Event_11705201(11, flag=11705211, character=Characters.c2370_0001, region=1702312, flag_1=11705213)
    Event_11705201(12, flag=11705212, character=Characters.c2370_0001, region=1702313, flag_1=11705213)
    Event_11705201(13, flag=11705213, character=Characters.c2370_0001, region=1702314, flag_1=11705213)
    EnableFlag(11705220)
    Event_11705201(20, flag=11705220, character=Characters.c2370_0006, region=1702321, flag_1=11705221)
    Event_11705201(21, flag=11705221, character=Characters.c2370_0006, region=1702322, flag_1=11705221)


@RestartOnRest(11705240)
def Event_11705240(_, character: Character | int):
    """Event 11705240"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    AICommand(character, command_id=1, command_slot=0)


@EndOnRest(11705201)
def Event_11705201(_, flag: Flag | int, character: int, region: int, flag_1: Flag | int):
    """Event 11705201"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=1000))
    
    MAIN.Await(AND_1)
    
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(character, region=region)
    ForceAnimation(character, 7000, wait_for_completion=True)
    if FlagEnabled(flag_1):
        AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(11700810)
def Event_11700810(_, character: Character | int, left: int, item_lot: int):
    """Event 11700810"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueNotEqual(left=left, right=0):
        OR_7.Add(CharacterHuman(PLAYER))
        OR_7.Add(CharacterHollow(PLAYER))
        if not OR_7:
            return
        AwardItemLot(item_lot, host_only=True)
    End()


@RestartOnRest(11705280)
def Event_11705280(_, character: Character | int):
    """Event 11705280"""
    MAIN.Await(CharacterAlive(character))
    
    MAIN.Await(CharacterDead(character))
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(32300100, host_only=True)


@ContinueOnRest(11700600)
def Event_11700600(_, obj: Object | int, obj_act_id: int):
    """Event 11700600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11705010)
def Event_11705010(_, character: int):
    """Event 11705010"""
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5421))
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=character,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(11705020)
def Event_11705020(_, character: int):
    """Event 11705020"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5420))
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    AND_7.Add(CharacterBackreadDisabled(character))
    if AND_7:
        return RESTART
    AND_2.Add(CharacterHasSpecialEffect(character, 5421))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_3.Add(CharacterHasSpecialEffect(character, 5422))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_4.Add(CharacterHasSpecialEffect(character, 5423))
    SkipLinesIfConditionFalse(1, AND_4)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_5.Add(CharacterHasSpecialEffect(character, 5424))
    SkipLinesIfConditionFalse(1, AND_5)
    ForceAnimation(character, 3006, wait_for_completion=True)
    ReplanAI(character)
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    Restart()


@RestartOnRest(11705030)
def Event_11705030(_, character: Character | int):
    """Event 11705030"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5421))
    AND_1.Add(CharacterHasSpecialEffect(character, 3150))
    AND_2.Add(CharacterHasSpecialEffect(character, 5420))
    AND_2.Add(CharacterHasSpecialEffect(character, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_2)
    AICommand(character, command_id=200, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=210, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(character, 5420))
    OR_2.Add(CharacterHasSpecialEffect(character, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11705040)
def Event_11705040(_, character: Character | int):
    """Event 11705040"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5422))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 3150))
    AND_2.Add(CharacterHasSpecialEffect(character, 5423))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_2)
    AICommand(character, command_id=201, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=211, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(character, 5420))
    OR_2.Add(CharacterHasSpecialEffect(character, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11705050)
def Event_11705050(_, character: int, region: int):
    """Event 11705050"""
    AND_1.Add(Singleplayer())
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 5421)
    ClearTargetList(character)
    ReplanAI(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    Restart()


@RestartOnRest(11700900)
def Event_11700900(_, character: Character | int):
    """Event 11700900"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@RestartOnRest(11705060)
def Event_11705060(_, character: int):
    """Event 11705060"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(character))
    if AND_1:
        return
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 0)
    ReplanAI(character)


@RestartOnRest(11700700)
def Event_11700700():
    """Event 11700700"""
    MAIN.Await(CharacterAlive(Characters.c2710_0010))
    
    if FlagEnabled(11700700):
        return
    AND_1.Add(DLCOwned())
    AND_1.Add(CharacterDead(Characters.c2710_0010))
    AND_1.Add(FlagEnabled(11200530))
    AND_1.Add(FlagDisabled(1121))
    
    MAIN.Await(AND_1)
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(27100200, host_only=True)


@ContinueOnRest(11700510)
def Event_11700510(_, character: Character | int, flag: Flag | int):
    """Event 11700510"""
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


@ContinueOnRest(11700520)
def Event_11700520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11700530)
def Event_11700530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700530"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1092))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1702410))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11020694)
    EnableCharacter(character)
    DisableFlag(61700320)
    EndOfAnimation(obj=Objects.o7401_06, animation_id=1)
    EnableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=0)
    EnableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=1)
    DisableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=2)
    DisableObjectActivation(Objects.o7401_06, obj_act_id=27401, relative_index=3)


@ContinueOnRest(11700531)
def Event_11700531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700531"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1093))
    AND_1.Add(FlagEnabled(61700320))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11700594)


@ContinueOnRest(11700532)
def Event_11700532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700532"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1094))
    AND_1.Add(Host())
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1702410))
    AND_2.Add(FlagDisabled(1096))
    AND_2.Add(FlagEnabled(1093))
    AND_2.Add(FlagEnabled(CommonFlags.SeathDead))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11700594)
    EnableCharacter(character)
    Move(character, destination=1702501, destination_type=CoordEntityType.Region, set_draw_parent=Collisions.h0041B0)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    SetNest(character, region=1702501)


@ContinueOnRest(11700533)
def Event_11700533(
    _,
    character: Character | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    character_1: Character | int,
):
    """Event 11700533"""
    if FlagDisabled(11700595):
        DisableObject(Objects.o0110_0014)
        DisableObjectActivation(Objects.o0110_0014, obj_act_id=-1)
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(FlagEnabled(1095))
    AND_1.Add(FlagEnabled(CommonFlags.SeathDead))
    AND_1.Add(FlagEnabled(728))
    AND_1.Add(FlagEnabled(11700592))
    AND_2.Add(FlagDisabled(1096))
    AND_2.Add(FlagEnabled(1095))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    EnableCharacter(character_1)
    EnableFlag(11700595)


@ContinueOnRest(11700538)
def Event_11700538(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700538"""
    DisableCharacter(Characters.c2711_0000)
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1540))
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagDisabled(1513))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1501, 1511)))
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(FlagEnabled(1541))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(Characters.c2711_0000)
    SetDisplayMask(Characters.c2711_0000, bit_index=1, switch_type=OnOffChange.Off)


@ContinueOnRest(11700539)
def Event_11700539(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700539"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1541))
    AND_1.Add(CharacterDead(Characters.c2711_0000))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(
        character,
        destination=Characters.c2711_0000,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=Characters.c2711_0000,
    )
    EnableCharacter(character)


@ContinueOnRest(11700540)
def Event_11700540(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700540"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1542))
    AND_1.Add(FlagEnabled(11700593))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(Host())
    AND_2.Add(FlagDisabled(1547))
    AND_2.Add(FlagEnabled(1542))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11700545)
def Event_11700545(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11700545"""
    AND_1.Add(FlagDisabled(1176))
    AND_1.Add(FlagDisabled(1179))
    AND_1.Add(FlagEnabled(1175))
    AND_1.Add(FlagEnabled(724))
    AND_2.Add(FlagEnabled(1181))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11705843)
def Event_11705843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11705843"""
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


@ContinueOnRest(11705846)
def Event_11705846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11705846"""
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
