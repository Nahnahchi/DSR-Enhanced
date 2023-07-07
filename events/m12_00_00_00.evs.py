"""
Darkroot Garden / Basin

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m12_00_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11200992()
    GiveRingOfFog()
    Event_11200999()
    RegisterBonfire(bonfire_flag=11200984, obj=Objects.o0200_0000)
    RegisterLadder(start_climbing_flag=11200010, stop_climbing_flag=11200011, obj=Objects.o2400)
    RegisterLadder(start_climbing_flag=11200012, stop_climbing_flag=11200013, obj=Objects.o2401)
    CreateProjectileOwner(entity=Characters.c2330_0026)
    SkipLinesIfFlagEnabled(2, 11200000)
    SkipLinesIfFlagEnabled(1, 11200002)
    SkipLines(1)
    DisableObject(Objects.o2300)
    SkipLinesIfClient(10)
    DisableObject(Objects.o2901_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o2902_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o2903_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o2907_0000)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o2908_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    Event_11200090(0, obj=Objects.o2906_0000, vfx_id=VFX.CheckpointFog1, destination=1202600, destination_1=1202601)
    Event_11205080()
    Event_11205081()
    Event_11205082()
    Event_11200100(
        0,
        flag=11200110,
        obj=Objects.o2110,
        model_point=120020,
        anchor_entity=1202500,
        left=0,
        flag_1=61200500,
    )
    Event_11200110(0, flag=11200100, line_intersects=Objects.o2110, anchor_entity=1202500, left=0)
    Event_11200100(
        1,
        flag=11200111,
        obj=Objects.o2111,
        model_point=120021,
        anchor_entity=1202501,
        left=1,
        flag_1=61200501,
    )
    Event_11200110(1, flag=11200101, line_intersects=Objects.o2111, anchor_entity=1202501, left=1)
    Event_11200120()
    Event_11205000()
    Event_11200800()
    Event_11200200()
    Event_11200690()
    Event_11200600(0, obj=Objects.o0110_0000, obj_act_id=11200600)
    Event_11200600(1, obj=Objects.o0110_0001, obj_act_id=11200601)
    DisableSoundEvent(sound_id=Sounds.SifMusic)
    if FlagEnabled(CommonFlags.SifDead):
        Event_11205392()
        DisableObject(Objects.o2900_0000)
        DeleteVFX(VFX.SifEntranceFog, erase_root_only=False)
    else:
        Event_11200000()
        Event_11205390()
        Event_11205391()
        Event_11205393()
        Event_11205392()
        Event_11200001()
        Event_11205394()
        Event_11205395()
        Event_11205396()
    Event_11200002()
    DisableSoundEvent(sound_id=Sounds.MoonlightButterflyMusic)
    if FlagEnabled(CommonFlags.MoonlightButterflyDead):
        Event_11205382()
        DisableObject(Objects.o2904_0000)
        DeleteVFX(VFX.ButterflyEntranceFog, erase_root_only=False)
        DisableObject(Objects.o2905_0000)
        DeleteVFX(VFX.ButterflyExitFog, erase_root_only=False)
    else:
        Event_11205380()
        Event_11205381()
        Event_11205383()
        Event_11205382()
        Event_11200900()
        Event_11205384()
        Event_11205385()
        Event_11205120(0, region=1202220, destination=1202180)
        Event_11205120(1, region=1202221, destination=1202181)
        Event_11205120(2, region=1202222, destination=1202182)
        Event_11205120(3, region=1202223, destination=1202183)
        Event_11205120(4, region=1202224, destination=1202184)
        Event_11205120(5, region=1202225, destination=1202185)
        Event_11205120(6, region=1202226, destination=1202186)
        Event_11205120(7, region=1202227, destination=1202187)
        Event_11205120(8, region=1202228, destination=1202188)
        Event_11205120(9, region=1202229, destination=1202189)
    Event_11200801()
    Event_11205300(
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
    Event_11205300(
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
    Event_11205300(
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
    Event_11205300(
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
    Event_11205300(
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
    Event_11205300(
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
    Event_11205300(
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
    Event_11205250(0, character=Characters.c2330_0003, region=1202110)
    Event_11205290(0, character=Characters.c2330_0004, flag=51200170, seconds=0.0, right=1)
    Event_11205290(1, character=Characters.c2330_0005, flag=51200170, seconds=0.20000000298023224, right=1)
    Event_11205290(2, character=Characters.c2330_0006, flag=51200170, seconds=0.800000011920929, right=1)
    Event_11205250(1, character=Characters.c2330_0007, region=1202111)
    Event_11205290(3, character=Characters.c2330_0008, flag=11205263, seconds=0.0, right=0)
    Event_11205290(4, character=Characters.c2330_0009, flag=11205263, seconds=0.6000000238418579, right=0)
    Event_11205290(5, character=Characters.c2330_0010, flag=11205264, seconds=0.0, right=0)
    Event_11205290(6, character=Characters.c2330_0011, flag=11205264, seconds=0.8999999761581421, right=0)
    Event_11205200(0, character=Characters.c2330_0019, radius=8.0)
    Event_11205200(1, character=Characters.c2330_0021, radius=8.0)
    Event_11205200(2, character=Characters.c2330_0023, radius=5.0)
    Event_11205200(3, character=Characters.c2330_0024, radius=5.0)
    Event_11205200(4, character=Characters.c2330_0025, radius=5.0)
    Event_11205230(0, character=Characters.c3370_0000, radius=3.0)
    Event_11205230(2, character=Characters.c3370_0002, radius=3.0)
    Event_11205240(0, character=Characters.c3370_0000, region=1202710)
    Event_11205240(2, character=Characters.c3370_0002, region=1202712)
    Event_11205280(0, character=Characters.c2380_0000, radius=6.0, region=1202112)
    Event_11205280(1, character=Characters.c2380_0001, radius=2.0, region=1202112)
    Event_11205260(0, character=Characters.c2380_0002, radius=6.0)
    Event_11205260(1, character=Characters.c2380_0003, radius=10.0)
    Event_11205260(2, character=Characters.c2380_0004, radius=8.0)
    Event_11205260(3, character=Characters.c2380_0005, radius=4.0)
    Event_11205260(4, character=Characters.c2380_0006, radius=4.0)
    Event_11205260(5, character=Characters.c2380_0007, radius=4.0)
    Event_11205260(6, character=Characters.c2380_0008, radius=4.0)
    Event_11205260(7, character=Characters.c2380_0009, radius=4.0)
    Event_11205260(8, character=Characters.c2380_0010, radius=4.0)
    Event_11205190(0, character=Characters.c3410_0001, region=1202113, seconds=0.0)
    Event_11205190(1, character=Characters.c3410_0002, region=1202113, seconds=0.5)
    Event_11205190(2, character=Characters.c3410_0003, region=1202113, seconds=1.2000000476837158)
    Event_11205190(3, character=Characters.c3410_0004, region=1202113, seconds=0.699999988079071)
    Event_11205150(0, character=Characters.c2280_0000)
    Event_11205150(1, character=Characters.c2280_0001)
    Event_11205150(2, character=Characters.c2280_0002)
    Event_11205150(3, character=Characters.c2280_0003)
    Event_11205150(4, character=Characters.c2280_0004)
    Event_11205150(5, character=Characters.c2280_0005)
    Event_11205150(6, character=Characters.c2280_0006)
    Event_11205150(7, character=Characters.c2280_0007)
    Event_11205180(0, character=Characters.c5360_0000, left=1)
    Event_11205180(1, character=Characters.c5360_0001, left=0)
    Event_11205180(2, character=Characters.c5360_0002, left=0)
    Event_11200810(0, character=Characters.c3350_0000, left=0, item_lot=0)
    Event_11200810(1, character=Characters.c3350_0001, left=0, item_lot=0)
    Event_11200810(2, character=Characters.c3300_0000, left=0, item_lot=33004000)
    Event_11200810(3, character=Characters.c5360_0000, left=0, item_lot=0)
    Event_11200810(4, character=Characters.c5360_0001, left=0, item_lot=0)
    Event_11200810(5, character=Characters.c5360_0002, left=0, item_lot=0)
    Event_11200810(6, character=Characters.c2795_0000, left=0, item_lot=27901000)
    Event_11200810(7, character=Characters.c0000_0004, left=0, item_lot=0)
    Event_11200810(8, character=Characters.c0000_0007, left=1, item_lot=0)
    Event_11200810(9, character=Characters.c4190_dog1, left=0, item_lot=0)
    Event_11205843(
        0,
        flag=CommonFlags.MoonlightButterflyDead,
        line_intersects=1201890,
        anchor_entity=1202898,
        target_entity=1202894,
    )
    Event_11205846(0, flag=CommonFlags.MoonlightButterflyDead, obj=Objects.o2904_0000, vfx_id=VFX.ButterflyEntranceFog)
    Event_11205843(1, flag=CommonFlags.SifDead, line_intersects=1201990, anchor_entity=1202998, target_entity=1202997)
    Event_11205846(1, flag=CommonFlags.SifDead, obj=Objects.o2900_0000, vfx_id=VFX.SifEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0014, event_flag=8932)
    Event_11205030()
    Event_11205035()
    Event_11205032()
    Event_11200300()
    Event_11205990(0, flag=11205031, summoned_character=Characters.c0000_0014)
    SkipLinesIfClient(2)
    DisableFlagRange((11200210, 11200213))
    DisableFlag(11200215)
    HumanityRegistration(Characters.c0000_0012, event_flag=8350)
    HumanityRegistration(Characters.c0000_0015, event_flag=8350)
    SkipLinesIfClient(6)
    if FlagEnabled(1123):
        DisableFlagRange((1120, 1139))
        EnableFlag(1122)
    if FlagEnabled(1130):
        DisableFlagRange((1120, 1139))
        EnableFlag(1129)
    if FlagDisabled(1121):
        DisableCharacter(Characters.c0000_0012)
    if FlagDisabled(1123):
        DisableCharacter(Characters.c0000_0015)
    if FlagDisabled(1130):
        DisableCharacter(Characters.c0000_0015)
    SetStandbyAnimationSettings(Characters.c0000_0015, standby_animation=7875)
    Event_11200520(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1125)
    Event_11200520(1, character=Characters.c0000_0015, first_flag=1120, last_flag=1139, flag=1125)
    Event_11200530(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1121)
    Event_11200531(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1122)
    Event_11200534(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1123)
    Event_11200532(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1126)
    Event_11200533()
    Event_11205040(0, flag=11200210, destination=1202000, vfx_id=VFX.DuskSummonSign00)
    Event_11205040(1, flag=11200211, destination=1202001, vfx_id=VFX.DuskSummonSign01)
    Event_11205040(2, flag=11200212, destination=1202002, vfx_id=VFX.DuskSummonSign02)
    Event_11205040(3, flag=11200213, destination=1202003, vfx_id=VFX.DuskSummonSign03)
    Event_11200529(0, first_flag=1120, last_flag=1139, flag=1127)
    Event_11200527(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1129)
    Event_11200525(0, character=Characters.c0000_0012, first_flag=1120, last_flag=1139, flag=1130)
    Event_11205070(0, flag=11200210, destination=1202000, vfx_id=VFX.DuskSummonSign00)
    Event_11205070(1, flag=11200211, destination=1202001, vfx_id=VFX.DuskSummonSign01)
    Event_11205070(2, flag=11200212, destination=1202002, vfx_id=VFX.DuskSummonSign02)
    Event_11205070(3, flag=11200213, destination=1202003, vfx_id=VFX.DuskSummonSign03)
    DeleteVFX(VFX.OolacilePortal, erase_root_only=False)
    Event_11200005()
    Event_11200006()
    SkipLinesIfClient(1)
    DisableFlagRange((11205050, 11205068))
    DisableCharacterCollision(Characters.c5361_0000)
    DisableGravity(Characters.c5361_0000)
    EnableImmortality(Characters.c5361_0000)
    SkipLinesIfFlagEnabled(2, 1710)
    SkipLinesIfFlagEnabled(1, 1712)
    DisableCharacter(Characters.c5361_0000)
    Event_11200538(0, character=Characters.c5361_0000, first_flag=1710, last_flag=1712, flag=1711)
    Event_11200539(0, character=Characters.c5361_0000, first_flag=1710, last_flag=1712, flag=1712)
    Event_11200540(0, character=Characters.c5361_0000, first_flag=1710, last_flag=1712, flag=1711)
    Event_11205058()
    Event_11205054()
    Event_11205056()
    Event_11205057()
    Event_11205060(0, character=Characters.c0000_0002)
    Event_11205060(1, character=Characters.c0000_0013)
    Event_11205060(2, character=Characters.c0000_0003)
    Event_11205060(3, character=Characters.c0000_0004)
    Event_11205060(4, character=Characters.c0000_0005)
    Event_11205060(5, character=Characters.c0000_0006)
    Event_11205060(6, character=Characters.c0000_0007)
    Event_11205060(7, character=Characters.c0000_0008)
    Event_11205060(8, character=Characters.c4190_dog1)
    HumanityRegistration(Characters.c0000_0002, event_flag=8470)
    HumanityRegistration(Characters.c0000_0013, event_flag=8900)
    DisableCharacter(Characters.c0000_0002)
    DisableCharacter(Characters.c0000_0013)
    Event_11200520(2, character=Characters.c0000_0002, first_flag=1600, last_flag=1619, flag=1604)
    Event_11200520(3, character=Characters.c0000_0013, first_flag=1760, last_flag=1769, flag=1764)
    Event_11200501(0, character=Characters.c0000_0002, flag=1603)
    Event_11200535(0, character=Characters.c0000_0002)


@ContinueOnRest(11200992)
def Event_11200992():
    """Event 11200992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c5210_0000, 7100)
    AddSpecialEffect(Characters.c3530_0000, 7100)
    AddSpecialEffect(Characters.c3230_0000, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c5210_0000, 7100)
    RemoveSpecialEffect(Characters.c3530_0000, 7100)
    RemoveSpecialEffect(Characters.c3230_0000, 7100)
    Restart()


@ContinueOnRest(11200998)
def GiveRingOfFog():
    """Event 11200998"""
    if ThisEventSlotFlagEnabled():
        End()
    AND_1.Add(FlagEnabled(11200813))
    AND_1.Add(FlagEnabled(11200814))
    AND_1.Add(FlagEnabled(11200815))
    MAIN.Await(AND_1)
    AwardItemLotToHostOnly(item_lot=68070100)


@ContinueOnRest(11200999)
def Event_11200999():
    """Event 11200999"""
    if FlagDisabled(11402885):
        return
    DisableCharacter(Characters.c0000_0002)
    DisableCharacter(Characters.c0000_0013)


@ContinueOnRest(11200090)
def Event_11200090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11200090"""
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


@RestartOnRest(11205080)
def Event_11205080():
    """Event 11205080"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2380_0007)
        DisableCharacter(Characters.c2380_0008)
        DisableCharacter(Characters.c2380_0009)
        DisableCharacter(Characters.c2380_0010)
        DisableCharacter(Characters.c2280_0008)
        DisableCharacter(Characters.c2280_0009)
        DisableCharacter(Characters.c2280_0010)
        DisableCharacter(Characters.c2280_0011)
        DisableCharacter(Characters.c2270_0002)
        DisableCharacter(Characters.c2270_0003)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11205081)
def Event_11205081():
    """Event 11205081"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2380_0007)
    Kill(Characters.c2380_0008)
    Kill(Characters.c2380_0009)
    Kill(Characters.c2380_0010)
    Kill(Characters.c2280_0008)
    Kill(Characters.c2280_0009)
    Kill(Characters.c2280_0010)
    Kill(Characters.c2280_0011)
    Kill(Characters.c2270_0002)
    Kill(Characters.c2270_0003)


@RestartOnRest(11205082)
def Event_11205082():
    """Event 11205082"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11200050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11200050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11200050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11200050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11200050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11200050))
    if not OR_6:
        return RESTART
    EnableFlag(11200050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=DARKROOT_GARDEN))
    if not AND_7:
        return RESTART
    DisableFlag(11200050)
    EnableFlag(11205085)


@RestartOnRest(11200000)
def Event_11200000():
    """Event 11200000"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(11200002):
        return
    DisableCharacter(Characters.c5210_0000)
    DisableObject(Objects.o2900_0000)
    DeleteVFX(VFX.SifEntranceFog, erase_root_only=False)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(11210021))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5210_0000)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120000, cutscene_flags=0, player_id=10000, move_to_region=1202801, game_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1202801,
        game_map=DARKROOT_GARDEN,
    )
    SkipLines(1)
    PlayCutscene(120000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(Objects.o2300)
    Move(Characters.c5210_0000, destination=1202800, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(Characters.c5210_0000)
    EnableObject(Objects.o2900_0000)
    CreateVFX(VFX.SifEntranceFog)
    EnableFlag(11200002)


@ContinueOnRest(11200002)
def Event_11200002():
    """Event 11200002"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(11200000):
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11210021))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5210_0000)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120003, cutscene_flags=0, player_id=10000, move_to_region=1202802, game_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120003,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1202802,
        game_map=DARKROOT_GARDEN,
    )
    SkipLines(1)
    PlayCutscene(120003, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(Objects.o2300)
    EnableCharacter(Characters.c5210_0000)
    EnableObject(Objects.o2900_0000)
    CreateVFX(VFX.SifEntranceFog)
    EnableFlag(11200000)


@ContinueOnRest(11205390)
def Event_11205390():
    """Event 11205390"""
    AND_1.Add(FlagDisabled(CommonFlags.SifDead))
    AND_1.Add(FlagEnabled(11200000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205391)
def Event_11205391():
    """Event 11205391"""
    AND_1.Add(FlagDisabled(CommonFlags.SifDead))
    AND_1.Add(FlagEnabled(11205393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1201990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205393)
def Event_11205393():
    """Event 11205393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(11200000))
        AND_1.Add(FlagDisabled(CommonFlags.SifDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1202996))
        AND_2.Add(ThisEventFlagEnabled())
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfFinishedConditionTrue(input_condition=AND_2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5210_0000)


@RestartOnRest(11205392)
def Event_11205392():
    """Event 11205392"""
    if FlagEnabled(CommonFlags.SifDead):
        DisableCharacter(Characters.c5210_0000)
        Kill(Characters.c5210_0000)
        End()
    DisableAI(Characters.c5210_0000)
    AND_1.Add(FlagEnabled(11200000))
    AND_1.Add(FlagEnabled(11205393))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.c5210_0000)
    EnableBossHealthBar(Characters.c5210_0000, name=5210)


@ContinueOnRest(11200001)
def Event_11200001():
    """Event 11200001"""
    MAIN.Await(CharacterDead(Characters.c5210_0000))
    
    EnableFlag(CommonFlags.SifDead)
    KillBoss(game_area_param_id=1200800)
    DisableObject(Objects.o2900_0000)
    DeleteVFX(VFX.SifEntranceFog)


@ContinueOnRest(11205394)
def Event_11205394():
    """Event 11205394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.SifDead))
    AND_1.Add(FlagEnabled(11205392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11205391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.SifMusic)


@ContinueOnRest(11205395)
def Event_11205395():
    """Event 11205395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.SifDead))
    AND_1.Add(FlagEnabled(11205394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.SifMusic)


@RestartOnRest(11205396)
def Event_11205396():
    """Event 11205396"""
    if ThisEventFlagDisabled():
        MAIN.Await(HealthRatio(Characters.c5210_0000) <= 0.10000000149011612)
    AddSpecialEffect(Characters.c5210_0000, 5401)


@ContinueOnRest(11205380)
def Event_11205380():
    """Event 11205380"""
    AND_1.Add(FlagDisabled(CommonFlags.MoonlightButterflyDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205381)
def Event_11205381():
    """Event 11205381"""
    AND_1.Add(FlagDisabled(CommonFlags.MoonlightButterflyDead))
    AND_1.Add(FlagEnabled(11205383))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1201890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205383)
def Event_11205383():
    """Event 11205383"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.MoonlightButterflyDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1202896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    AddSpecialEffect(PLAYER, 5500)
    ActivateMultiplayerBuffs(Characters.c3230_0000)


@RestartOnRest(11205382)
def Event_11205382():
    """Event 11205382"""
    DisableCharacter(Characters.c2330_0026)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c3230_0000, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(CommonFlags.MoonlightButterflyDead):
        DisableCharacter(Characters.c3230_0000)
        Kill(Characters.c3230_0000)
        End()
    DisableHealthBar(Characters.c3230_0000)
    DisableAI(Characters.c3230_0000)
    SetStandbyAnimationSettings(Characters.c3230_0000, standby_animation=7000)
    
    MAIN.Await(FlagEnabled(11205383))
    
    SetStandbyAnimationSettings(Characters.c3230_0000, cancel_animation=7001)
    EnableAI(Characters.c3230_0000)
    EnableBossHealthBar(Characters.c3230_0000, name=3230)


@ContinueOnRest(CommonFlags.MoonlightButterflyDead)
def Event_11200900():
    """Event 11200900"""
    MAIN.Await(CharacterDead(Characters.c3230_0000))
    
    RemoveSpecialEffect(PLAYER, 5500)
    EnableFlag(CommonFlags.MoonlightButterflyDead)
    KillBoss(game_area_param_id=1200801)
    DisableObject(Objects.o2904_0000)
    DeleteVFX(VFX.ButterflyEntranceFog)
    DisableObject(Objects.o2905_0000)
    DeleteVFX(VFX.ButterflyExitFog)


@ContinueOnRest(11205384)
def Event_11205384():
    """Event 11205384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.MoonlightButterflyDead))
    AND_1.Add(FlagEnabled(11205382))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11205381))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.MoonlightButterflyMusic)


@ContinueOnRest(11205385)
def Event_11205385():
    """Event 11205385"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.MoonlightButterflyDead))
    AND_1.Add(FlagEnabled(11205384))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.MoonlightButterflyMusic)


@ContinueOnRest(11205120)
def Event_11205120(_, region: Region | int, destination: int):
    """Event 11205120"""
    AND_1.Add(CharacterInsideRegion(Characters.c3230_0000, region=region))
    AND_1.Add(CharacterHasTAEEvent(Characters.c3230_0000, tae_event_id=10))
    
    MAIN.Await(AND_1)
    
    Move(Characters.c3230_0000, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(Characters.c3230_0000, tae_event_id=10))
    
    Restart()


@ContinueOnRest(11200100)
def Event_11200100(_, flag: Flag | int, obj: int, model_point: int, anchor_entity: int, left: int, flag_1: Flag | int):
    """Event 11200100"""
    SkipLinesIfFlagEnabled(1, flag_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EndOfAnimation(obj=obj, animation_id=1)
    End()
    CreateObjectVFX(obj, vfx_id=200, model_point=model_point)
    if ValueNotEqual(left=left, right=1):
        AND_1.Add(PlayerHasGood(2002))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=obj,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    RotateToFaceEntity(PLAYER, target_entity=obj)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfValueEqual(1, left=left, right=1)
    SkipLinesIfClient(1)
    if ValueNotEqual(left=left, right=1):
        DisplayDialog(text=10010861, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    ForceAnimation(obj, 1)
    DeleteObjectVFX(obj)


@ContinueOnRest(11200110)
def Event_11200110(_, flag: Flag | int, line_intersects: int, anchor_entity: int, left: int):
    """Event 11200110"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(flag))
    if ValueNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(703))
    if ValueNotEqual(left=left, right=1):
        AND_1.Add(PlayerDoesNotHaveGood(2002))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=line_intersects,
    ))
    AND_2.Add(Client())
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=line_intersects,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    DisplayDialog(text=10010160, anchor_entity=line_intersects, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11200120)
def Event_11200120():
    """Event 11200120"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o2120)
        End()
    
    MAIN.Await(ObjectDestroyed(Objects.o2120))
    
    EnableFlag(11200120)


@RestartOnRest(11205150)
def Event_11205150(_, character: Character | int):
    """Event 11205150"""
    AND_1.Add(HealthRatio(character) <= 0.800000011920929)
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(11205180)
def Event_11205180(_, character: Character | int, left: int):
    """Event 11205180"""
    if ValueNotEqual(left=left, right=0):
        MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
        SetNest(character, region=1202732)
        End()
    if ThisEventSlotFlagDisabled():
        SetStandbyAnimationSettings(character, standby_animation=9000)
        DisableAI(character)
    
        MAIN.Await(HealthRatio(Characters.c5360_0000) <= 0.4000000059604645)
    
        WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
        SetStandbyAnimationSettings(character, cancel_animation=9060)
        EnableAI(character)
    SetNest(character, region=1202732)


@RestartOnRest(11205190)
def Event_11205190(_, character: int, region: Region | int, seconds: float):
    """Event 11205190"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacter(character)
    DisableAI(character)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    Wait(seconds)
    EnableGravity(character)
    EnableCharacter(character)
    ForceAnimation(character, 7000, wait_for_completion=True)
    EnableAI(character)


@RestartOnRest(11205200)
def Event_11205200(_, character: int, radius: float):
    """Event 11205200"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character, attacker=Characters.c0000_0014))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205250)
def Event_11205250(_, character: Character | int, region: Region | int):
    """Event 11205250"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character, attacker=Characters.c0000_0014))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(Characters.c0000_0014, region=region))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205290)
def Event_11205290(_, character: Character | int, flag: Flag | int, seconds: float, right: int):
    """Event 11205290"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character, attacker=Characters.c0000_0014))
    SkipLinesIfValueEqual(1, left=0, right=right)
    SkipLinesIfClient(1)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    Wait(seconds)
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205230)
def Event_11205230(_, character: int, radius: float):
    """Event 11205230"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableCharacterCollision(character)
    DisableGravity(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=Characters.c0000_0014, radius=radius))
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(Attacked(attacked_entity=character, attacker=Characters.c0000_0014))
    AND_1.Add(OR_1)
    AND_2.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    EnableCharacterCollision(character)
    EnableGravity(character)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    SetStandbyAnimationSettings(character, cancel_animation=9063)


@RestartOnRest(11205240)
def Event_11205240(_, character: Character | int, region: Region | int):
    """Event 11205240"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5110))
    
    SetNest(character, region=region)


@RestartOnRest(11205260)
def Event_11205260(_, character: int, radius: float):
    """Event 11205260"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=Characters.c0000_0014, radius=radius))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205280)
def Event_11205280(_, character: int, radius: float, region: Region | int):
    """Event 11205280"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=Characters.c0000_0014, radius=radius))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(Characters.c0000_0014, region=region))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205000)
def Event_11205000():
    """Event 11205000"""
    DisableGravity(Characters.c3350_0000)
    DisableCharacterCollision(Characters.c3350_0000)
    if ThisEventFlagDisabled():
        MAIN.Await(CharacterInsideRegion(PLAYER, region=1202100))
    EnableGravity(Characters.c3350_0000)
    EnableCharacterCollision(Characters.c3350_0000)
    SetNest(Characters.c3350_0000, region=1202101)


@RestartOnRest(11200800)
def Event_11200800():
    """Event 11200800"""
    DisableCharacter(Characters.c2711_0000)
    if ThisEventFlagEnabled():
        return
    if FlagDisabled(11200801):
        OR_1.Add(FlagEnabled(11200801))
        OR_1.Add(FlagEnabled(703))
        AND_1.Add(OR_1)
    
        MAIN.Await(AND_1)
    EnableCharacter(Characters.c2711_0000)
    FadeInCharacter(character=Characters.c2711_0000, duration=5.0)
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2711_0000))
    
    SetDisplayMask(Characters.c2711_0000, bit_index=0, switch_type=OnOffChange.Off)
    
    MAIN.Await(CharacterDead(Characters.c2711_0000))
    
    EnableFlag(11200800)


@RestartOnRest(11200801)
def Event_11200801():
    """Event 11200801"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3530_0000)
        End()
    OR_1.Add(CharacterDead(Characters.c3530_0000))
    AND_1.Add(CharacterDead(Characters.c3531_0000))
    AND_1.Add(CharacterDead(Characters.c3531_0001))
    AND_1.Add(CharacterDead(Characters.c3531_0002))
    AND_1.Add(CharacterDead(Characters.c3531_0003))
    AND_1.Add(CharacterDead(Characters.c3531_0004))
    AND_1.Add(CharacterDead(Characters.c3531_0005))
    AND_1.Add(CharacterDead(Characters.c3531_0006))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    Kill(Characters.c3530_0000, award_souls=True)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(35300100, host_only=True)


@RestartOnRest(11205300)
def Event_11205300(
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
    """Event 11205300"""
    DisableCharacter(character)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(Characters.c3530_0000, bit_index=bit_index, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c3530_0000, bit_index=bit_index_1, switch_type=OnOffChange.Off)
        AddSpecialEffect(Characters.c3530_0000, special_effect)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c3530_0000))
    
    CreateNPCPart(Characters.c3530_0000, npc_part_id=npc_part_id, part_index=part_index, part_health=176)
    AND_1.Add(CharacterPartHealth(Characters.c3530_0000, npc_part_id=npc_part_id_1) <= 0)
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


@ContinueOnRest(11200200)
def Event_11200200():
    """Event 11200200"""
    DisableNetworkSync()
    if Client():
        return
    AND_1.Add(Host())
    AND_2.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(not AND_2)
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0040B0))
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0041B0))
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0042B0))
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0043B0))
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0044B0))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4500)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(11200810)
def Event_11200810(_, character: Character | int, left: int, item_lot: int):
    """Event 11200810"""
    SkipLinesIfThisEventSlotFlagDisabled(6)
    SkipLinesIfValueEqual(3, left=left, right=1)
    DisableCharacter(character)
    Kill(character)
    End()
    DropMandatoryTreasure(character)
    End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@ContinueOnRest(11200600)
def Event_11200600(_, obj: Object | int, obj_act_id: int):
    """Event 11200600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11200690)
def Event_11200690():
    """Event 11200690"""
    if ThisEventFlagDisabled():
        DisableTreasure(obj=Objects.o0504_0000)
        DisableObject(Objects.o0504_0000)
        OR_1.Add(FlagEnabled(1123))
        OR_1.Add(FlagEnabled(1130))
    
        MAIN.Await(OR_1)
    
        EnableObject(Objects.o0504_0000)
    EnableTreasure(obj=Objects.o0504_0000)


@ContinueOnRest(11200510)
def Event_11200510(_, character: Character | int, flag: Flag | int):
    """Event 11200510"""
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


@ContinueOnRest(11200520)
def Event_11200520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200501)
def Event_11200501(_, character: Character | int, flag: Flag | int):
    """Event 11200501"""
    AND_1.Add(FlagDisabled(1603))
    AND_1.Add(FlagEnabled(1600))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1763))
    AND_2.Add(FlagEnabled(1760))
    AND_2.Add(HealthRatio(Characters.c0000_0013) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(Characters.c0000_0013) > 0.0)
    AND_2.Add(Attacked(attacked_entity=Characters.c0000_0013, attacker=PLAYER))
    AND_2.Add(ThisEventFlagDisabled())
    AND_3.Add(FlagEnabled(746))
    AND_3.Add(ThisEventFlagDisabled())
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(1763))
    AND_4.Add(OR_2)
    AND_4.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_4)
    if FlagDisabled(1604):
        EnableFlag(flag)
    if FlagDisabled(1764):
        EnableFlag(1763)
    if FlagDisabled(1604):
        EnableCharacter(character)
    if FlagDisabled(1764):
        EnableCharacter(Characters.c0000_0013)
    SetTeamType(character, TeamType.Enemy)
    SetTeamType(Characters.c0000_0013, TeamType.Enemy)
    SaveRequest()
    EnableFlag(1766)


@ContinueOnRest(11200530)
def Event_11200530(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200530"""
    AND_1.Add(FlagEnabled(1120))
    AND_1.Add(FlagEnabled(11200800))
    
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
    Wait(0.5)
    SetStandbyAnimationSettings(character, standby_animation=7875)
    ForceAnimation(character, 7876)


@ContinueOnRest(11200531)
def Event_11200531(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200531"""
    AND_1.Add(FlagEnabled(1121))
    AND_1.Add(FlagEnabled(11200590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7877, wait_for_completion=True)
    ForceAnimation(character, 8289, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11200532)
def Event_11200532(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200532"""
    AND_1.Add(FlagEnabled(1121))
    AND_1.Add(FlagEnabled(11200591))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7877, wait_for_completion=True)
    ForceAnimation(character, 8289, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11200533)
def Event_11200533():
    """Event 11200533"""
    DeleteVFX(VFX.DuskSummonSign00, erase_root_only=False)
    DeleteVFX(VFX.DuskSummonSign01, erase_root_only=False)
    DeleteVFX(VFX.DuskSummonSign02, erase_root_only=False)
    DeleteVFX(VFX.DuskSummonSign03, erase_root_only=False)
    if Client():
        return
    AND_1.Add(PlayerDoesNotHaveGood(2520))
    AND_1.Add(FlagEnabled(1122))
    AND_2.Add(FlagEnabled(1129))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableRandomFlagInRange(flag_range=(11200210, 11200213))
    if FlagEnabled(11200210):
        CreateVFX(VFX.DuskSummonSign00)
    if FlagEnabled(11200211):
        CreateVFX(VFX.DuskSummonSign01)
    if FlagEnabled(11200212):
        CreateVFX(VFX.DuskSummonSign02)
    if FlagEnabled(11200213):
        CreateVFX(VFX.DuskSummonSign03)


@ContinueOnRest(11205040)
def Event_11205040(_, flag: Flag | int, destination: int, vfx_id: VFXEvent | int):
    """Event 11205040"""
    if FlagEnabled(11200215):
        EnableCharacter(Characters.c0000_0015)
        End()
    AND_1.Add(FlagEnabled(1122))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=50000000,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11200215)
    DeleteVFX(vfx_id)
    Move(
        Characters.c0000_0015,
        destination=destination,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0018B0,
    )
    Wait(5.0)
    EnableCharacter(Characters.c0000_0015)
    CreateTemporaryVFX(vfx_id=120, anchor_entity=destination, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(Characters.c0000_0015, standby_animation=7875)
    ForceAnimation(Characters.c0000_0015, 6951, wait_for_completion=True)
    ForceAnimation(Characters.c0000_0015, 7876)
    EnableFlag(11205310)


@ContinueOnRest(11200534)
def Event_11200534(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200534"""
    AND_1.Add(FlagEnabled(1122))
    AND_1.Add(FlagEnabled(11205310))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200529)
def Event_11200529(_, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200529"""
    if FlagEnabled(17):
        return
    OR_1.Add(FlagEnabled(1122))
    OR_1.Add(FlagEnabled(1125))
    OR_1.Add(FlagEnabled(1126))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerHasGood(2520))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(2, 1125)
    SkipLinesIfFlagEnabled(1, 1126)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200527)
def Event_11200527(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200527"""
    MAIN.Await(FlagEnabled(1128))
    
    SkipLinesIfFlagEnabled(5, 1125)
    SkipLinesIfFlagEnabled(8, 1126)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    End()
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1125)
    DisableCharacter(character)
    End()
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1126)
    DisableCharacter(character)


@ContinueOnRest(11205070)
def Event_11205070(_, flag: Flag | int, destination: int, vfx_id: VFXEvent | int):
    """Event 11205070"""
    if FlagEnabled(11200215):
        EnableCharacter(Characters.c0000_0015)
        End()
    AND_1.Add(FlagEnabled(1129))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=50000000,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11200215)
    DeleteVFX(vfx_id)
    Move(
        Characters.c0000_0015,
        destination=destination,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0018B0,
    )
    Wait(5.0)
    EnableCharacter(Characters.c0000_0015)
    CreateTemporaryVFX(vfx_id=120, anchor_entity=destination, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(Characters.c0000_0015, standby_animation=7875)
    ForceAnimation(Characters.c0000_0015, 6951, wait_for_completion=True)
    ForceAnimation(Characters.c0000_0015, 7876)
    EnableFlag(11205311)


@ContinueOnRest(11200525)
def Event_11200525(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200525"""
    AND_1.Add(FlagEnabled(1129))
    AND_1.Add(FlagEnabled(11205311))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200535)
def Event_11200535(_, character: Character | int):
    """Event 11200535"""
    SkipLinesIfClient(1)
    DisableFlag(11205021)
    SkipLinesIfHost(1)
    if FlagDisabled(11205021):
        AND_1.Add(FlagDisabled(1603))
        AND_1.Add(FlagDisabled(1601))
        AND_1.Add(Host())
        AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    
        MAIN.Await(AND_1)
    if FlagDisabled(1604):
        EnableCharacter(character)
    if FlagDisabled(1764):
        EnableCharacter(Characters.c0000_0013)
        EnableFlag(1766)
    EnableFlag(11205021)


@ContinueOnRest(11200538)
def Event_11200538(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200538"""
    MAIN.Await(Attacked(attacked_entity=character, attacker=PLAYER))
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 9030, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11200539)
def Event_11200539(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200539"""
    AND_1.Add(FlagEnabled(1710))
    AND_1.Add(FlagEnabled(746))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200540)
def Event_11200540(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11200540"""
    AND_1.Add(FlagEnabled(1712))
    AND_1.Add(FlagEnabled(11200596))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7003, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11205054)
def Event_11205054():
    """Event 11205054"""
    AND_7.Add(PlayerCovenant(Covenant.ForestHunter))
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(FlagDisabled(11205055))
    AND_1.Add(FlagEnabled(11205053))
    AND_1.Add(OR_7)
    AND_1.Add(not AND_7)
    AND_1.Add(FlagDisabled(11205050))
    AND_2.Add(FlagDisabled(11205055))
    AND_2.Add(FlagEnabled(11205053))
    AND_2.Add(OR_7)
    AND_2.Add(AND_7)
    OR_6.Add(Attacked(attacked_entity=Characters.c5361_0000, attacker=PLAYER))
    OR_6.Add(FlagEnabled(11205060))
    OR_6.Add(FlagEnabled(11205061))
    OR_6.Add(FlagEnabled(11205062))
    OR_6.Add(FlagEnabled(11205063))
    OR_6.Add(FlagEnabled(11205064))
    OR_6.Add(FlagEnabled(11205065))
    OR_6.Add(FlagEnabled(11205066))
    OR_6.Add(FlagEnabled(11205067))
    OR_6.Add(FlagEnabled(11205068))
    OR_6.Add(FlagEnabled(745))
    AND_2.Add(OR_6)
    AND_3.Add(FlagDisabled(11205055))
    AND_3.Add(FlagDisabled(11205053))
    AND_3.Add(OR_7)
    AND_3.Add(not AND_7)
    AND_3.Add(FlagEnabled(11205050))
    AND_4.Add(FlagDisabled(11205055))
    AND_4.Add(FlagDisabled(11205053))
    AND_4.Add(OR_7)
    AND_4.Add(AND_7)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11205055)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_2)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_3)
    EnableFlag(11205052)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_4)
    EnableFlag(11205052)
    Restart()


@RestartOnRest(11205056)
def Event_11205056():
    """Event 11205056"""
    AND_7.Add(PlayerCovenant(Covenant.ForestHunter))
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(FlagEnabled(11205051))
    AND_1.Add(OR_7)
    AND_1.Add(AND_7)
    AND_2.Add(FlagEnabled(11205051))
    AND_2.Add(OR_7)
    AND_2.Add(not AND_7)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11205051)
    DisableFlag(11205053)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_2)
    OR_6.Add(CharacterHuman(PLAYER))
    OR_6.Add(CharacterHollow(PLAYER))
    SkipLinesIfConditionFalse(3, OR_6)
    BetrayCurrentCovenant()
    if FlagDisabled(9001):
        IncrementPvPSin()
        EnableFlag(9001)
    EnableFlag(742)
    EnableFlag(746)
    SetTeamType(Characters.c0000_0002, TeamType.Enemy)
    SetTeamType(Characters.c0000_0013, TeamType.Enemy)
    SetTeamType(Characters.c0000_0003, TeamType.Enemy)
    SetTeamType(Characters.c0000_0004, TeamType.Enemy)
    SetTeamType(Characters.c0000_0005, TeamType.Enemy)
    SetTeamType(Characters.c0000_0006, TeamType.Enemy)
    SetTeamType(Characters.c0000_0007, TeamType.Enemy)
    SetTeamType(Characters.c0000_0008, TeamType.Enemy)
    SetTeamType(Characters.c4190_dog1, TeamType.Enemy)
    SaveRequest()
    DisableFlag(11205055)
    Restart()


@RestartOnRest(11205057)
def Event_11205057():
    """Event 11205057"""
    MAIN.Await(FlagEnabled(11205052))
    
    DisableFlag(11205052)
    EnableFlag(11205053)
    SetTeamType(Characters.c0000_0002, TeamType.Ally)
    SetTeamType(Characters.c0000_0013, TeamType.Ally)
    SetTeamType(Characters.c0000_0003, TeamType.Ally)
    SetTeamType(Characters.c0000_0004, TeamType.Ally)
    SetTeamType(Characters.c0000_0005, TeamType.Ally)
    SetTeamType(Characters.c0000_0006, TeamType.Ally)
    SetTeamType(Characters.c0000_0007, TeamType.Ally)
    SetTeamType(Characters.c0000_0008, TeamType.Ally)
    SetTeamType(Characters.c4190_dog1, TeamType.Ally)
    ClearTargetList(Characters.c0000_0002)
    ClearTargetList(Characters.c0000_0013)
    ClearTargetList(Characters.c0000_0003)
    ClearTargetList(Characters.c0000_0004)
    ClearTargetList(Characters.c0000_0005)
    ClearTargetList(Characters.c0000_0006)
    ClearTargetList(Characters.c0000_0007)
    ClearTargetList(Characters.c0000_0008)
    ClearTargetList(Characters.c4190_dog1)
    ReplanAI(Characters.c0000_0002)
    ReplanAI(Characters.c0000_0013)
    ReplanAI(Characters.c0000_0003)
    ReplanAI(Characters.c0000_0004)
    ReplanAI(Characters.c0000_0005)
    ReplanAI(Characters.c0000_0006)
    ReplanAI(Characters.c0000_0007)
    ReplanAI(Characters.c0000_0008)
    ReplanAI(Characters.c4190_dog1)
    SaveRequest()
    DisableFlag(11205055)
    Restart()


@ContinueOnRest(11205058)
def Event_11205058():
    """Event 11205058"""
    if FlagEnabled(11205053):
        EnableFlag(11205052)
        End()
    SetTeamType(Characters.c0000_0002, TeamType.Enemy)
    SetTeamType(Characters.c0000_0013, TeamType.Enemy)
    SetTeamType(Characters.c0000_0003, TeamType.Enemy)
    SetTeamType(Characters.c0000_0004, TeamType.Enemy)
    SetTeamType(Characters.c0000_0005, TeamType.Enemy)
    SetTeamType(Characters.c0000_0006, TeamType.Enemy)
    SetTeamType(Characters.c0000_0007, TeamType.Enemy)
    SetTeamType(Characters.c0000_0008, TeamType.Enemy)
    SetTeamType(Characters.c4190_dog1, TeamType.Enemy)
    SaveRequest()


@RestartOnRest(11205060)
def Event_11205060(_, character: Character | int):
    """Event 11205060"""
    if FlagEnabled(746):
        SetTeamType(character, TeamType.Enemy)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_7)
    AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    
    MAIN.Await(AND_1)
    
    End()


@ContinueOnRest(11205030)
def Event_11205030():
    """Event 11205030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0014, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11205033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11205031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0014)
    if FlagEnabled(CommonFlags.MoonlightButterflyDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0014))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0014, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0014,
        region=1202010,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


@ContinueOnRest(11205035)
def Event_11205035():
    """Event 11205035"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0014, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11205033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11205031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0014)
    if FlagEnabled(CommonFlags.MoonlightButterflyDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11205031))
    AND_1.Add(FlagDisabled(11205033))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0014))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0014, other_entity=PLAYER, radius=10.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0014,
        region=1202010,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


@ContinueOnRest(11205990)
def Event_11205990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 11205990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11205032)
def Event_11205032():
    """Event 11205032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11205031))
    AND_1.Add(FlagEnabled(11205383))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0014, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0014)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0014, region=1202898))
    
    RotateToFaceEntity(Characters.c0000_0014, target_entity=1202894)
    ForceAnimation(Characters.c0000_0014, 7410)
    AICommand(Characters.c0000_0014, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0014)


@ContinueOnRest(11200300)
def Event_11200300():
    """Event 11200300"""
    MAIN.Await(FlagEnabled(11205031))
    
    EnableFlag(11200300)


@ContinueOnRest(11200005)
def Event_11200005():
    """Event 11200005"""
    OR_1.Add(FlagEnabled(1125))
    OR_1.Add(FlagEnabled(1126))
    OR_1.Add(FlagEnabled(1127))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerHasGood(2520))
    AND_1.Add(FlagDisabled(17))
    
    MAIN.Await(AND_1)
    
    if Client():
        return
    
    MAIN.Await(Singleplayer())
    
    CreateVFX(VFX.OolacilePortal)
    
    MAIN.Await(Multiplayer())
    
    DeleteVFX(VFX.OolacilePortal)
    Restart()


@ContinueOnRest(11200006)
def Event_11200006():
    """Event 11200006"""
    OR_1.Add(FlagEnabled(1125))
    OR_1.Add(FlagEnabled(1126))
    OR_1.Add(FlagEnabled(1127))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerHasGood(2520))
    AND_1.Add(FlagDisabled(17))
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButton(
        prompt_text=10010100,
        anchor_entity=1202008,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    if Client():
        return
    PlayCutscene(120002, cutscene_flags=0, player_id=10000, move_to_region=1212510, game_map=OOLACILE)
    WaitFrames(frames=1)
    SaveRequest()
    Restart()


@ContinueOnRest(11205843)
def Event_11205843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11205843"""
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


@ContinueOnRest(11205846)
def Event_11205846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11205846"""
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
