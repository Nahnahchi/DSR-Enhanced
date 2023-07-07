"""
Great Hollow / Ash Lake

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m13_02_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11320998()
    Event_11320999()
    Event_11320850(0, character=Characters.c0000_drg1, item_lot=0)
    RegisterBonfire(bonfire_flag=11320992, obj=Objects.o0200_0000, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11320984, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11320976, obj=Objects.o0200_0002)
    RegisterLadder(start_climbing_flag=11320010, stop_climbing_flag=11320011, obj=Objects.o3240_0000)
    RegisterLadder(start_climbing_flag=11320012, stop_climbing_flag=11320013, obj=Objects.o3241_0000)
    RegisterLadder(start_climbing_flag=11320014, stop_climbing_flag=11320015, obj=Objects.o3242_0000)
    RegisterLadder(start_climbing_flag=11320016, stop_climbing_flag=11320017, obj=Objects.o3243_0000)
    RegisterStatue(obj=Objects.o0101_0000, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0001, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0002, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0003, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0004, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0005, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0006, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0101_0007, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    SkipLinesIfClient(2)
    DisableObject(Objects.o3970_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    Event_11320090(0, obj=Objects.o3971_0000, vfx_id=VFX.CheckpointFog1, destination=1322600, destination_1=1322601)
    Event_11325000()
    Event_11320800()
    Event_11325001()
    Event_11320200(0, obj=Objects.o3450_0000, flag=11320200)
    Event_11320200(1, obj=Objects.o3451_0000, flag=11320201)
    Event_11320580()
    if FlagEnabled(11320100):
        Event_11320100()
    else:
        Event_11320110()
        Event_11320100()
        Event_11325100()
    Event_11320101()
    Event_11325150(0, character=Characters.c3250_0000, radius=15.0)
    Event_11325150(1, character=Characters.c3250_0001, radius=15.0)
    Event_11325150(2, character=Characters.c3250_0002, radius=10.0)
    Event_11320300(1, character=Characters.c3300_0001, first_flag=11325203, last_flag=11325205, flag=11325203)
    Event_11320300(2, character=Characters.c3300_0002, first_flag=11325206, last_flag=11325208, flag=11325206)
    Event_11320300(3, character=Characters.c3300_0003, first_flag=11325209, last_flag=11325211, flag=11325209)
    Event_11320300(4, character=Characters.c3300_0004, first_flag=11325212, last_flag=11325214, flag=11325212)
    Event_11320300(5, character=Characters.c3300_0005, first_flag=11325215, last_flag=11325217, flag=11325215)
    Event_11320300(6, character=Characters.c3300_0006, first_flag=11325218, last_flag=11325220, flag=11325218)
    Event_11320300(7, character=Characters.c3300_0007, first_flag=11325221, last_flag=11325223, flag=11325221)
    Event_11320300(8, character=Characters.c3300_0008, first_flag=11325224, last_flag=11325226, flag=11325224)
    Event_11320300(9, character=Characters.c3300_0009, first_flag=11325227, last_flag=11325229, flag=11325227)
    Event_11320300(10, character=Characters.c3300_0010, first_flag=11325230, last_flag=11325232, flag=11325230)
    Event_11320600(0, obj=Objects.o0110_0000, obj_act_id=11320600)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0004, event_flag=8446)
    if FlagDisabled(1511):
        DisableCharacter(Characters.c0000_0004)
    Event_11320534(0, character=Characters.c0000_0004, first_flag=1490, last_flag=1539, flag=1511)
    Event_11320535(0, character=Characters.c0000_0004, first_flag=1490, last_flag=1539, flag=1514)
    HumanityRegistration(Characters.c0000_0005, event_flag=8454)
    SkipLinesIfFlagEnabled(2, 1547)
    SkipLinesIfFlagEnabled(1, 1546)
    DisableCharacter(Characters.c0000_0005)
    Event_11320510(1, character=Characters.c0000_0005, flag=1547)
    Event_11320520(1, character=Characters.c0000_0005, first_flag=1540, last_flag=1569, flag=1548)
    Event_11320540(0, character=Characters.c0000_0005, first_flag=1540, last_flag=1569, flag=1546)
    Event_11320541(0, character=Characters.c0000_0005, first_flag=1540, last_flag=1569, flag=1549)
    EnableImmortality(Characters.c3450_0000)


@ContinueOnRest(11320998)
def Event_11320998():
    """Event 11320998"""
    OR_1.Add(EntityWithinDistance(entity=Characters.c0000_drg1, other_entity=PLAYER, radius=5.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c0000_drg1, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetTeamType(Characters.c0000_drg1, TeamType.Enemy)


@ContinueOnRest(11320999)
def Event_11320999():
    """Event 11320999"""
    AddSpecialEffect(Characters.c0000_drg1, 2090)


@RestartOnRest(11320850)
def Event_11320850(_, character: Character | int, item_lot: int):
    """Event 11320850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@ContinueOnRest(11320090)
def Event_11320090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11320090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id)
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


@RestartOnRest(11325090)
def Event_11325090():
    """Event 11325090"""
    DisableCharacter(1320900)
    OR_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    OR_1.Add(FlagEnabled(11325090))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11325090)
    EnableCharacter(1320900)
    
    MAIN.Await(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    
    Kill(1320900)


@RestartOnRest(11320110)
def Event_11320110():
    """Event 11320110"""
    DisableFlag(11325100)
    DisableFlag(11325101)
    DisableCharacter(Characters.c3531_0000)
    DisableCharacter(Characters.c3531_0001)
    DisableCharacter(Characters.c3531_0002)
    DisableCharacter(Characters.c3531_0003)
    DisableCharacter(Characters.c3531_0004)
    DisableCharacter(Characters.c3531_0005)
    DisableCharacter(Characters.c3531_0006)
    if FlagEnabled(11320100):
        return
    Event_11325121()
    Event_11325110(
        0,
        part_index=1,
        npc_part_id=3530,
        npc_part_id_1=3530,
        character=Characters.c3531_0000,
        model_point=91,
        bit_index=0,
        bit_index_1=1,
        special_effect=5430,
    )
    Event_11325110(
        1,
        part_index=2,
        npc_part_id=3531,
        npc_part_id_1=3531,
        character=Characters.c3531_0001,
        model_point=92,
        bit_index=1,
        bit_index_1=2,
        special_effect=5431,
    )
    Event_11325110(
        2,
        part_index=3,
        npc_part_id=3532,
        npc_part_id_1=3532,
        character=Characters.c3531_0002,
        model_point=93,
        bit_index=2,
        bit_index_1=3,
        special_effect=5432,
    )
    Event_11325110(
        3,
        part_index=4,
        npc_part_id=3533,
        npc_part_id_1=3533,
        character=Characters.c3531_0003,
        model_point=94,
        bit_index=3,
        bit_index_1=4,
        special_effect=5433,
    )
    Event_11325110(
        4,
        part_index=5,
        npc_part_id=3534,
        npc_part_id_1=3534,
        character=Characters.c3531_0004,
        model_point=95,
        bit_index=4,
        bit_index_1=5,
        special_effect=5434,
    )
    Event_11325110(
        5,
        part_index=6,
        npc_part_id=3535,
        npc_part_id_1=3535,
        character=Characters.c3531_0005,
        model_point=96,
        bit_index=5,
        bit_index_1=6,
        special_effect=5435,
    )
    Event_11325110(
        6,
        part_index=8,
        npc_part_id=3536,
        npc_part_id_1=3536,
        character=Characters.c3531_0006,
        model_point=97,
        bit_index=6,
        bit_index_1=7,
        special_effect=5436,
    )


@RestartOnRest(11325100)
def Event_11325100():
    """Event 11325100"""
    AND_1.Add(CharacterBackreadEnabled(Characters.c3530_0000))
    AND_1.Add(CharacterHasTAEEvent(Characters.c3530_0000, tae_event_id=300))
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(11325101):
        EnableFlag(11325101)
        Move(Characters.c3530_0000, destination=1322700, destination_type=CoordEntityType.Region, short_move=True)
        ForceAnimation(Characters.c3530_0000, 3011, wait_for_completion=True)
        Move(Characters.c3530_0000, destination=1322710, destination_type=CoordEntityType.Region, short_move=True)
        SetNest(Characters.c3530_0000, region=1322710)
        ForceAnimation(Characters.c3530_0000, 9060, wait_for_completion=True)
        ReplanAI(Characters.c3530_0000)
        Restart()
    DisableFlag(11325101)
    Move(Characters.c3530_0000, destination=1322701, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.c3530_0000, 3014, wait_for_completion=True)
    Move(Characters.c3530_0000, destination=1322711, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(Characters.c3530_0000, region=1322711)
    ForceAnimation(Characters.c3530_0000, 9060, wait_for_completion=True)
    ReplanAI(Characters.c3530_0000)
    Restart()


@EndOnRest(11325110)
def Event_11325110(
    _,
    part_index: short,
    npc_part_id: short,
    npc_part_id_1: int,
    character: int,
    model_point: int,
    bit_index: uchar,
    bit_index_1: uchar,
    special_effect: int,
):
    """Event 11325110"""
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(Characters.c3530_0000, bit_index=bit_index, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c3530_0000, bit_index=bit_index_1, switch_type=OnOffChange.Off)
        AddSpecialEffect(Characters.c3530_0000, special_effect)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c3530_0000))
    
    CreateNPCPart(Characters.c3530_0000, npc_part_id=npc_part_id, part_index=part_index, part_health=270)
    AND_1.Add(CharacterPartHealth(Characters.c3530_0000, npc_part_id=npc_part_id_1) <= 0)
    AND_1.Add(FlagDisabled(11325120))
    AND_1.Add(Attacked(attacked_entity=Characters.c3530_0000, attacker=PLAYER))
    AND_2.Add(HealthRatio(Characters.c3530_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(Characters.c3530_0000)
    Move(
        character,
        destination=Characters.c3530_0000,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=Characters.c3530_0000,
    )
    EnableCharacter(character)
    ForceAnimation(character, 8100)
    ForceAnimation(Characters.c3530_0000, 8000)
    SetDisplayMask(Characters.c3530_0000, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3530_0000, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c3530_0000, special_effect)


@EndOnRest(11325121)
def Event_11325121():
    """Event 11325121"""
    MAIN.Await(CharacterHasTAEEvent(Characters.c3530_0000, tae_event_id=500))
    
    EnableFlag(11325120)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c3530_0000, tae_event_id=600))
    
    DisableFlag(11325120)
    Restart()


@RestartOnRest(11320100)
def Event_11320100():
    """Event 11320100"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3530_0000)
        DisableCharacter(Characters.c3531_0000)
        DisableCharacter(Characters.c3531_0001)
        DisableCharacter(Characters.c3531_0002)
        DisableCharacter(Characters.c3531_0003)
        DisableCharacter(Characters.c3531_0004)
        DisableCharacter(Characters.c3531_0005)
        DisableCharacter(Characters.c3531_0006)
        End()
    
    MAIN.Await(CharacterDead(Characters.c3530_0000))
    
    AwardItemLot(35300000, host_only=False)


@ContinueOnRest(11320101)
def Event_11320101():
    """Event 11320101"""
    if FlagEnabled(11320100):
        return
    AND_1.Add(FlagEnabled(11325110))
    AND_1.Add(FlagEnabled(11325111))
    AND_1.Add(FlagEnabled(11325112))
    AND_1.Add(FlagEnabled(11325113))
    AND_1.Add(FlagEnabled(11325114))
    AND_1.Add(FlagEnabled(11325115))
    AND_1.Add(FlagEnabled(11325116))
    
    MAIN.Await(AND_1)
    
    Kill(Characters.c3530_0000, award_souls=True)


@RestartOnRest(11325150)
def Event_11325150(_, character: int, radius: float):
    """Event 11325150"""
    if ThisEventSlotFlagEnabled():
        return
    SetStandbyAnimationSettings(character, standby_animation=9000)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@ContinueOnRest(11325000)
def Event_11325000():
    """Event 11325000"""
    if ThisEventFlagEnabled():
        return
    SetStandbyAnimationSettings(Characters.c3450_0000, standby_animation=9000)
    AND_1.Add(Host())
    AND_1.Add(EntityWithinDistance(entity=Characters.c3450_0000, other_entity=PLAYER, radius=30.0))
    
    MAIN.Await(AND_1)
    
    SetStandbyAnimationSettings(Characters.c3450_0000, cancel_animation=9060)


@ContinueOnRest(11320800)
def Event_11320800():
    """Event 11320800"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3450_0000)
        End()
    
    MAIN.Await(CharacterDead(Characters.c3450_0000))
    
    EnableFlag(11320800)


@RestartOnRest(11325001)
def Event_11325001():
    """Event 11325001"""
    DisableCharacter(Characters.c3451_0000)
    if FlagEnabled(11320800):
        return
    if ThisEventFlagEnabled():
        SetDisplayMask(Characters.c3450_0000, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c3450_0000, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(Characters.c3450_0000, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c3450_0000))
    
    CreateNPCPart(Characters.c3450_0000, npc_part_id=3451, part_index=NPCPartType.Part1, part_health=200)
    AND_1.Add(CharacterPartHealth(Characters.c3450_0000, npc_part_id=3451) <= 0)
    AND_2.Add(HealthRatio(Characters.c3450_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ForceAnimation(Characters.c3450_0000, 8000)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c3450_0000, tae_event_id=400))
    
    EnableCharacter(Characters.c3451_0000)
    Move(
        Characters.c3451_0000,
        destination=Characters.c3450_0000,
        destination_type=CoordEntityType.Character,
        model_point=19,
        copy_draw_parent=Characters.c3450_0000,
    )
    ForceAnimation(Characters.c3451_0000, 8100)
    SetDisplayMask(Characters.c3450_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c3450_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c3450_0000, command_id=20, command_slot=0)
    ReplanAI(Characters.c3450_0000)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(34510000, host_only=True)


@ContinueOnRest(11320200)
def Event_11320200(_, obj: Object | int, flag: Flag | int):
    """Event 11320200"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    
    MAIN.Await(ObjectDestroyed(obj))
    
    EnableFlag(flag)


@RestartOnRest(11320300)
def Event_11320300(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11320300"""
    DisableCharacter(character)
    if ThisEventSlotFlagEnabled():
        return
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableCharacter(character)
    
    MAIN.Await(CharacterDead(character))
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(33000000, host_only=True)
    End()


@ContinueOnRest(11320600)
def Event_11320600(_, obj: Object | int, obj_act_id: int):
    """Event 11320600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11320510)
def Event_11320510(_, character: Character | int, flag: Flag | int):
    """Event 11320510"""
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
    SetTeamType(character, TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11320520)
def Event_11320520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11320520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11320534)
def Event_11320534(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11320534"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagDisabled(1548))
    AND_1.Add(FlagEnabled(1507))
    AND_1.Add(FlagEnabled(11410593))
    AND_1.Add(FlagEnabled(11020606))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11320535)
def Event_11320535(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11320535"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1511))
    OR_1.Add(FlagEnabled(11320591))
    OR_1.Add(FlagEnabled(1548))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11320540)
def Event_11320540(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11320540"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1545))
    AND_1.Add(FlagEnabled(11020606))
    AND_1.Add(FlagEnabled(1511))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11320541)
def Event_11320541(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11320541"""
    AND_1.Add(FlagDisabled(1547))
    AND_1.Add(FlagEnabled(1546))
    AND_1.Add(FlagEnabled(11320591))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11320580)
def Event_11320580():
    """Event 11320580"""
    MAIN.Await(FlagEnabled(11325030))
    
    RotateToFaceEntity(PLAYER, target_entity=Characters.c3450_0000)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    
    MAIN.Await(FlagDisabled(11325030))
    
    SetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()
