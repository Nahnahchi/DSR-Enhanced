"""
Demon Ruins / Lost Izalith

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m14_01_00_00_enums import *
from ..enums.common_enums import CommonFlags
from ..enums.m14_00_00_00_enums import Characters as m14_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11410992()
    RunEvent(11410999, slot=0, args=(0,))
    Event_11410998()
    Event_11410997()
    Event_11410995()
    Event_11410994()
    Event_11410993()
    Event_11410996(0, other_entity=Characters.c0000_inf1)
    Event_11410996(1, other_entity=Characters.c0000_inf2)
    Event_11410850(7, character=Characters.c0000_inf2, item_lot=61320000)
    Event_11410850(0, character=Characters.c2230_dem1, item_lot=0)
    Event_11410850(1, character=Characters.c2230_dem2, item_lot=0)
    Event_11410850(2, character=Characters.c2230_dem3, item_lot=0)
    Event_11410850(3, character=Characters.c2230_dem4, item_lot=0)
    Event_11410850(4, character=Characters.c2230_dem5, item_lot=0)
    Event_11410850(5, character=Characters.c2790_blk1, item_lot=0)
    Event_11410850(6, character=Characters.c2231_0000, item_lot=0)
    Event_11410850(8, character=Characters.c0000_ano1, item_lot=0)
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        RegisterBonfire(bonfire_flag=11410920, obj=Objects.o0200_0003)
    RegisterBonfire(bonfire_flag=11410992, obj=Objects.o0200_0004)
    RegisterBonfire(bonfire_flag=11410984, obj=Objects.o0200_0001)
    if FlagEnabled(11410900):
        RegisterBonfire(bonfire_flag=11410976, obj=Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11410968, obj=Objects.o0200_0005)
    RegisterBonfire(bonfire_flag=11410960, obj=Objects.o0200_0006)
    SkipLinesIfClient(14)
    DisableObject(Objects.o4966_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o4967_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o4968_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o4969_0000)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o4970_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    DisableObject(Objects.o4971_0000)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=False)
    DisableObject(Objects.o4973_0000)
    DeleteVFX(VFX.MultiplayerFog7, erase_root_only=False)
    if FlagEnabled(11410291):
        DisableObject(Objects.o4610_0000)
        DeleteVFX(VFX.BedSealRight)
        DeleteVFX(VFX.BedSealRootLeft)
    if FlagEnabled(11410292):
        DisableObject(Objects.o4610_0001)
        DeleteVFX(VFX.BedSealLeft)
        DeleteVFX(VFX.BedSealRootRight)
    Event_11410095()
    Event_11415090()
    Event_11415091()
    Event_11415092()
    Event_11410800()
    Event_11410400()
    Event_11410340()
    Event_11410341()
    Event_11410350()
    Event_11410360()
    Event_11415399()
    Event_11410260()
    Event_11410200()
    Event_11410201(0, obj=Objects.o4620_0000, sound_id=462000000)
    Event_11410201(1, obj=Objects.o4621_0000, sound_id=462100000)
    Event_11410201(2, obj=Objects.o4622_0000, sound_id=462200000)
    Event_11410201(3, obj=Objects.o4623_0000, sound_id=462300000)
    Event_11410201(4, obj=Objects.o4624_0000, sound_id=462400000)
    Event_11410201(5, obj=Objects.o4625_0000, sound_id=462500000)
    Event_11410201(6, obj=Objects.o4626_0000, sound_id=462600000)
    Event_11410201(7, obj=Objects.o4627_0000, sound_id=462700000)
    Event_11410201(8, obj=Objects.o4628_0000, sound_id=462800000)
    Event_11410201(9, obj=Objects.o4629_0000, sound_id=462900000)
    Event_11410201(10, obj=Objects.o4630_0000, sound_id=463000000)
    Event_11410201(11, obj=Objects.o4631_0000, sound_id=463100000)
    Event_11410201(12, obj=Objects.o4632_0000, sound_id=463200000)
    Event_11410250()
    DisableSoundEvent(sound_id=Sounds.CeaselessDischargeMusic)
    if FlagEnabled(11410900):
        Event_11415372()
        DisableObject(Objects.o4961_0000)
        DeleteVFX(VFX.CeaselessEntranceFog, erase_root_only=False)
    else:
        Event_11415370()
        Event_11415371()
        Event_11415373()
        Event_11415372()
        Event_11415374()
        Event_11415376()
        Event_11415377()
        Event_11415378()
        Event_11415379()
        Event_11410900()
    Event_11415310(0, flag=11415376)
    Event_11415310(1, flag=11415310)
    Event_11415310(2, flag=11415311)
    Event_11415310(3, flag=11415312)
    Event_11415310(4, flag=11415313)
    DisableSoundEvent(sound_id=Sounds.FiresageDemonMusic)
    if FlagEnabled(11410410):
        Event_11415342()
        DisableObject(Objects.o4962_0000)
        DeleteVFX(VFX.FiresageEntranceFog, erase_root_only=False)
        DisableObject(Objects.o4963_0000)
        DeleteVFX(VFX.FiresageExitFog, erase_root_only=False)
    else:
        Event_11415340()
        Event_11415341()
        Event_11415343()
        Event_11415342()
        Event_11415344()
        Event_11410410()
        Event_11415345()
    DisableSoundEvent(sound_id=Sounds.CentipedeDemonMusic)
    if FlagEnabled(11410901):
        Event_11415382()
        DisableObject(Objects.o4964_0000)
        DeleteVFX(VFX.CentipedeEntranceFog, erase_root_only=False)
        DisableObject(Objects.o4965_0000)
        DeleteVFX(VFX.CentipedeExitFog, erase_root_only=False)
    else:
        Event_11415380()
        Event_11415381()
        Event_11415383()
        Event_11415382()
        Event_11415384()
        Event_11410901()
        Event_11415386()
    DisableSoundEvent(sound_id=Sounds.BedOfChaosBossMusic)
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        Event_11415392()
        DisableObject(Objects.o4972_0000)
        DeleteVFX(VFX.BedOfChaosEntranceFog, erase_root_only=False)
    else:
        Event_11415390()
        Event_11415391()
        Event_11415393()
        Event_11415392()
        Event_11410001()
        Event_11415394()
        Event_11415395()
        Event_11415396()
        Event_11415397()
        Event_11415398()
        Event_11415300()
    Event_800(0, character=Characters.c3480_0000)
    Event_11410100(4, character=Characters.c3390_0007)
    Event_11410100(6, character=Characters.c0000_0010)
    Event_11410100(7, character=Characters.c3300_0000)
    Event_11410100(8, character=1410150)
    Event_11410100(9, character=1410350)
    Event_11410100(10, character=1410351)
    Event_11410100(11, character=1410352)
    Event_11410100(12, character=1410353)
    Event_11410100(13, character=1410354)
    Event_11410100(14, character=1410355)
    Event_11410100(15, character=1410356)
    Event_11410100(16, character=1410357)
    Event_11410100(17, character=1410358)
    Event_11410100(18, character=1410359)
    Event_11410100(19, character=1410360)
    Event_11410100(20, character=1410361)
    Event_11410100(21, character=1410362)
    Event_11410100(22, character=1410363)
    Event_11410100(23, character=1410364)
    Event_11410100(24, character=1410365)
    Event_11410100(25, character=1410366)
    Event_11410100(26, character=1410367)
    Event_11410100(27, character=1410368)
    Event_11410100(28, character=1410369)
    Event_11410100(29, character=1410370)
    Event_11410100(30, character=1410371)
    Event_11410100(31, character=1410372)
    Event_11410100(32, character=1410373)
    Event_11410100(33, character=1410374)
    Event_11410100(34, character=1410375)
    Event_11410100(35, character=1410376)
    Event_11410100(36, character=1410377)
    Event_11410100(37, character=1410378)
    Event_11410100(38, character=Characters.c2250_0003)
    Event_11410100(39, character=1410451)
    Event_11410100(40, character=Characters.c2250_0005)
    Event_11410100(41, character=1410453)
    Event_11410100(42, character=1410454)
    Event_11410100(43, character=Characters.c2250_0008)
    Event_11410100(44, character=Characters.c2250_0009)
    Event_11415210(0, first_flag=11415250, last_flag=11415263, value=11)
    Event_11415250(
        0,
        character=Characters.c3210_0000,
        character_1=Characters.c3220_0000,
        character_2=Characters.c3220_0001,
        character_3=Characters.c3220_0002,
        character_4=Characters.c3220_0003,
        character_5=Characters.c3220_0004,
    )
    Event_11415250(
        1,
        character=Characters.c3210_0001,
        character_1=Characters.c3220_0005,
        character_2=Characters.c3220_0006,
        character_3=Characters.c3220_0007,
        character_4=Characters.c3220_0008,
        character_5=Characters.c3220_0009,
    )
    Event_11415250(
        2,
        character=Characters.c3210_0002,
        character_1=Characters.c3220_0010,
        character_2=Characters.c3220_0011,
        character_3=Characters.c3220_0012,
        character_4=Characters.c3220_0013,
        character_5=Characters.c3220_0014,
    )
    Event_11415250(
        3,
        character=Characters.c3210_0003,
        character_1=Characters.c3220_0015,
        character_2=Characters.c3220_0016,
        character_3=Characters.c3220_0017,
        character_4=Characters.c3220_0018,
        character_5=Characters.c3220_0019,
    )
    Event_11415250(
        4,
        character=Characters.c3210_0004,
        character_1=Characters.c3220_0020,
        character_2=Characters.c3220_0021,
        character_3=Characters.c3220_0022,
        character_4=Characters.c3220_0023,
        character_5=Characters.c3220_0024,
    )
    Event_11415250(
        5,
        character=Characters.c3210_0005,
        character_1=Characters.c3220_0025,
        character_2=Characters.c3220_0026,
        character_3=Characters.c3220_0027,
        character_4=Characters.c3220_0028,
        character_5=Characters.c3220_0029,
    )
    Event_11415250(
        6,
        character=Characters.c3210_0006,
        character_1=Characters.c3220_0030,
        character_2=Characters.c3220_0031,
        character_3=Characters.c3220_0032,
        character_4=Characters.c3220_0033,
        character_5=Characters.c3220_0034,
    )
    Event_11415250(
        7,
        character=Characters.c3210_0007,
        character_1=Characters.c3220_0035,
        character_2=Characters.c3220_0036,
        character_3=Characters.c3220_0037,
        character_4=Characters.c3220_0038,
        character_5=Characters.c3220_0039,
    )
    Event_11415250(
        8,
        character=Characters.c3210_0008,
        character_1=Characters.c3220_0040,
        character_2=Characters.c3220_0041,
        character_3=Characters.c3220_0042,
        character_4=Characters.c3220_0043,
        character_5=Characters.c3220_0044,
    )
    Event_11415250(
        9,
        character=Characters.c3210_0009,
        character_1=Characters.c3220_0045,
        character_2=Characters.c3220_0046,
        character_3=Characters.c3220_0047,
        character_4=Characters.c3220_0048,
        character_5=Characters.c3220_0049,
    )
    Event_11415250(
        10,
        character=Characters.c3210_0010,
        character_1=Characters.c3220_0050,
        character_2=Characters.c3220_0051,
        character_3=Characters.c3220_0052,
        character_4=Characters.c3220_0053,
        character_5=Characters.c3220_0054,
    )
    Event_11415250(
        11,
        character=Characters.c3210_0011,
        character_1=Characters.c3220_0055,
        character_2=Characters.c3220_0056,
        character_3=Characters.c3220_0057,
        character_4=Characters.c3220_0058,
        character_5=Characters.c3220_0059,
    )
    Event_11415250(
        12,
        character=Characters.c3210_0012,
        character_1=Characters.c3220_0060,
        character_2=Characters.c3220_0061,
        character_3=Characters.c3220_0062,
        character_4=Characters.c3220_0063,
        character_5=Characters.c3220_0064,
    )
    Event_11415250(
        13,
        character=Characters.c3210_0013,
        character_1=Characters.c3220_0065,
        character_2=Characters.c3220_0066,
        character_3=Characters.c3220_0067,
        character_4=Characters.c3220_0068,
        character_5=Characters.c3220_0069,
    )
    Event_11415250(
        14,
        character=Characters.c3210_egg1,
        character_1=Characters.c3220_mgt1,
        character_2=Characters.c3220_mgt2,
        character_3=Characters.c3220_mgt3,
        character_4=Characters.c3220_mgt4,
        character_5=Characters.c3220_mgt5,
    )
    Event_11415250(
        15,
        character=Characters.c3210_egg2,
        character_1=Characters.c3220_mgt6,
        character_2=Characters.c3220_mgt7,
        character_3=Characters.c3220_mgt8,
        character_4=Characters.c3220_mgt9,
        character_5=Characters.c3220_mgt10,
    )
    Event_11415250(
        16,
        character=Characters.c3210_egg3,
        character_1=Characters.c3220_mgt11,
        character_2=Characters.c3220_mgt12,
        character_3=Characters.c3220_mgt13,
        character_4=Characters.c3220_mgt14,
        character_5=Characters.c3220_mgt15,
    )
    Event_11415100(
        0,
        entity=Characters.c3390_0001,
        character=Characters.c3390_0001,
        cancel_animation=9060,
        radius=15.0,
        seconds=0.0,
    )
    Event_11415100(
        1,
        entity=Characters.c3390_0002,
        character=Characters.c3390_0002,
        cancel_animation=9060,
        radius=10.0,
        seconds=0.0,
    )
    Event_11415100(
        2,
        entity=Characters.c3390_0007,
        character=Characters.c3390_0007,
        cancel_animation=9060,
        radius=15.0,
        seconds=0.0,
    )
    Event_11415120(
        0,
        character=10000,
        character_1=Characters.c3390_0003,
        cancel_animation=9060,
        region=1412302,
        seconds=0.30000001192092896,
    )
    Event_11415120(
        1,
        character=10000,
        character_1=Characters.c3390_0004,
        cancel_animation=9060,
        region=1412302,
        seconds=0.10000000149011612,
    )
    Event_11415120(
        2,
        character=10000,
        character_1=Characters.c3390_0005,
        cancel_animation=9060,
        region=1412302,
        seconds=0.0,
    )
    Event_11415120(
        3,
        character=10000,
        character_1=Characters.c3390_0006,
        cancel_animation=9060,
        region=1412302,
        seconds=0.20000000298023224,
    )
    Event_11410150(1, character=Characters.c3390_0001, item_lot=33900000)
    Event_11410150(2, character=Characters.c3390_0002, item_lot=33900000)
    Event_11410150(3, character=Characters.c3390_0003, item_lot=33900000)
    Event_11410150(4, character=Characters.c3390_0004, item_lot=33900000)
    Event_11410150(5, character=Characters.c3390_0005, item_lot=33900000)
    Event_11410150(6, character=Characters.c3390_0006, item_lot=33900000)
    Event_11410600(0, obj=Objects.o0110_0000, obj_act_id=11410600)
    Event_11410600(1, obj=Objects.o0110_0001, obj_act_id=11410601)
    Event_11410600(2, obj=Objects.o0110_0002, obj_act_id=11410602)
    Event_11410600(3, obj=Objects.o0110_0003, obj_act_id=11410603)
    Event_11415843(
        0,
        flag=CommonFlags.BedOfChaosDead,
        line_intersects=1411990,
        anchor_entity=1412998,
        target_entity=1412997,
    )
    Event_11415846(0, flag=CommonFlags.BedOfChaosDead, obj=Objects.o4972_0000, vfx_id=VFX.BedOfChaosEntranceFog)
    Event_11415843(1, flag=11410900, line_intersects=1411790, anchor_entity=1412698, target_entity=1412697)
    Event_11415846(1, flag=11410900, obj=Objects.o4961_0000, vfx_id=VFX.CeaselessEntranceFog)
    Event_11415843(2, flag=11410901, line_intersects=1411890, anchor_entity=1412898, target_entity=1412897)
    Event_11415846(2, flag=11410901, obj=Objects.o4964_0000, vfx_id=VFX.CentipedeEntranceFog)
    Event_11415843(3, flag=11410410, line_intersects=1411410, anchor_entity=1412411, target_entity=1412412)
    Event_11415846(3, flag=11410410, obj=Objects.o4962_0000, vfx_id=VFX.FiresageEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_11410100(0, character=Characters.c3240_0002)
    Event_11410100(1, character=Characters.c3240_0003)
    Event_11410100(2, character=Characters.c3240_0004)
    Event_11410100(3, character=Characters.c3240_0005)
    HumanityRegistration(Characters.c0000_0010, event_flag=8250)
    HumanityRegistration(Characters.c0000_0007, event_flag=CommonFlags.SolaireHumanityFlag)
    HumanityRegistration(Characters.c0000_0008, event_flag=CommonFlags.KirkHumanityFlag)
    HumanityRegistration(Characters.c0000_0009, event_flag=CommonFlags.KirkHumanityFlag)
    Event_11415030()
    Event_11415029()
    Event_11415032()
    Event_11415035()
    Event_11415038()
    Event_11410810(0, character=Characters.c0000_0008, flag=11415036, flag_1=11415037)
    Event_11410810(1, character=Characters.c0000_0009, flag=11415039, flag_1=11415040)
    Event_14015990(0, flag=11415031, summoned_character=Characters.c0000_0007)
    HumanityRegistration(Characters.c0000_0002, event_flag=CommonFlags.SolaireHumanityFlag)
    HumanityRegistration(Characters.c0000_0003, event_flag=CommonFlags.SolaireHumanityFlag)
    SkipLinesIfFlagEnabled(3, 1009)
    SkipLinesIfFlagEnabled(2, 1004)
    SkipLinesIfFlagEnabled(1, 1003)
    DisableCharacter(Characters.c0000_0002)
    SkipLinesIfFlagEnabled(1, 11410580)
    SkipLines(1)
    Move(
        Characters.c0000_0002,
        destination=1412500,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0042B1,
    )
    if FlagDisabled(1002):
        DisableCharacter(Characters.c0000_0003)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0003, team_type=TeamType.HostileAlly)
    Event_11410510(0, character=Characters.c0000_0002, flag=1004)
    Event_11410520(0, character=Characters.c0000_0002, first_flag=1000, last_flag=1029, flag=1005)
    Event_11410530(0, character=Characters.c0000_0002, first_flag=1000, last_flag=1029, flag=1009)
    Event_11410531(0, character=Characters.c0000_0002, first_flag=1000, last_flag=1029, flag=1002)
    Event_11410532(0, character=Characters.c0000_0002, first_flag=1000, last_flag=1029, flag=1003)
    Event_11410533(0, character=6006, first_flag=1000, last_flag=1029, flag=1012)
    Event_11410534(0, character=Characters.c0000_0003, first_flag=1000, last_flag=1029, flag=1011)
    HumanityRegistration(Characters.c0000_0005, event_flag=8446)
    SkipLinesIfFlagRangeAnyEnabled(1, (1503, 1507))
    DisableCharacter(Characters.c0000_0005)
    SkipLinesIfFlagEnabled(3, 1504)
    SkipLinesIfFlagEnabled(2, 1506)
    SkipLinesIfFlagEnabled(1, 1507)
    SkipLines(2)
    AddSpecialEffect(Characters.c0000_0005, 90111)
    Move(Characters.c0000_0005, destination=1412360, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11410593):
        SetStandbyAnimationSettings(Characters.c0000_0005, standby_animation=7855)
    Event_11410501(0, character=Characters.c0000_0005, flag=1512)
    Event_11410546(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1513)
    Event_11410540(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1503)
    Event_11410541(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1504)
    Event_11410542(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1505)
    Event_11410543(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1506)
    Event_11410544(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1507)
    Event_11410545(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1513)
    Event_11410549(0, character=Characters.c0000_0005)
    Event_11410550(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1514)
    Event_11410547(0, character=Characters.c0000_0005)
    Event_11410548(0, character=Characters.c0000_0005)


@ContinueOnRest(11410992)
def Event_11410992():
    """Event 11410992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c5250_0000, 7100)
    AddSpecialEffect(Characters.c2231_0000, 7100)
    AddSpecialEffect(Characters.c5200_0000, 7100)
    AddSpecialEffect(Characters.c0000_0008, 7100)
    AddSpecialEffect(Characters.c0000_0009, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c5250_0000, 7100)
    RemoveSpecialEffect(Characters.c2231_0000, 7100)
    RemoveSpecialEffect(Characters.c5200_0000, 7100)
    RemoveSpecialEffect(Characters.c0000_0008, 7100)
    RemoveSpecialEffect(Characters.c0000_0009, 7100)
    Restart()


@ContinueOnRest(11410993)
def Event_11410993():
    """Event 11410993"""
    AND_1.Add(FlagEnabled(11302998))
    AND_1.Add(FlagEnabled(11512998))
    SkipLinesIfConditionFalse(3, AND_1)
    SkipLinesIfFlagEnabled(2, 11510869)
    SkipLinesIfFlagEnabled(1, 11300861)
    SkipLinesIfFlagDisabled(2, 11412993)
    DisableCharacter(Characters.c0000_ano1)
    End()
    AND_2.Add(FlagEnabled(11417900))
    
    MAIN.Await(AND_2)
    
    EnableFlag(11412993)


@ContinueOnRest(11410994)
def Event_11410994():
    """Event 11410994"""
    if FlagDisabled(11012997):
        AND_1.Add(Attacked(attacked_entity=Characters.c0000_ano1, attacker=PLAYER))
        AND_1.Add(HealthRatio(Characters.c0000_ano1) <= 0.75)
    
        MAIN.Await(AND_1)
    
        EnableFlag(11012997)
        EnableFlag(744)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_ano1, team_type=TeamType.HostileAlly)


@ContinueOnRest(11410995)
def Event_11410995():
    """Event 11410995"""
    EnableImmortality(Characters.c0000_inf1)


@ContinueOnRest(11410996)
def Event_11410996(_, other_entity: int):
    """Event 11410996"""
    AND_1.Add(HealthRatio(PLAYER) == 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=10.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 5210)


@ContinueOnRest(11410997)
def Event_11410997():
    """Event 11410997"""
    SkipLinesIfFlagDisabled(1, CommonFlags.BedOfChaosDead)
    SkipLinesIfFlagEnabled(2, 11417132)
    DisableCharacter(Characters.c0000_inf2)
    End()
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.c0000_inf2, radius=20.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c0000_inf2, 2090)
    RequestAnimation(Characters.c0000_inf2, animation_id=6806)
    SetTeamType(Characters.c0000_inf2, TeamType.HostileAlly)


@ContinueOnRest(11410998)
def Event_11410998():
    """Event 11410998"""
    SkipLinesIfFlagEnabled(22, 11417132)
    SkipLinesIfFlagDisabled(21, 11407132)
    AND_1.Add(Attacked(attacked_entity=Characters.c0000_inf1, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c0000_inf1, 2090)
    DisableInvincibility(Characters.c0000_inf1)
    ForceAnimation(Characters.c0000_inf1, 7702)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_inf1, team_type=TeamType.HostileAlly)
    AND_2.Add(HealthRatio(Characters.c0000_inf1) <= 0.25)
    
    MAIN.Await(AND_2)
    
    EnableFlag(11417132)
    EnableInvincibility(Characters.c0000_inf1)
    AddSpecialEffect(Characters.c0000_inf1, 2091)
    Wait(3.0)
    FadeOutCharacter(character=Characters.c0000_inf1, duration=5.0)
    DisableAI(Characters.c0000_inf1)
    ResetAnimation(Characters.c0000_inf1)
    ForceAnimation(Characters.c0000_inf1, 7570)
    Wait(1.0)
    PlaySoundEffect(Characters.c0000_inf1, 21200, sound_type=SoundType.s_SFX)
    CreateTemporaryVFX(
        vfx_id=22733,
        anchor_entity=Characters.c0000_inf1,
        model_point=236,
        anchor_type=CoordEntityType.Character,
    )
    SetTeamType(Characters.c0000_inf1, TeamType.Ally)
    Wait(6.0)
    DisableCharacter(Characters.c0000_inf1)


@RestartOnRest(11410850)
def Event_11410850(_, character: Character | int, item_lot: int):
    """Event 11410850"""
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


@ContinueOnRest(11410090)
def Event_11410090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11410090"""
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


@RestartOnRest(11415090)
def Event_11415090():
    """Event 11415090"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2240_0007)
        DisableCharacter(Characters.c2240_0008)
        DisableCharacter(Characters.c2240_0009)
        DisableCharacter(Characters.c2240_0010)
        DisableCharacter(Characters.c2240_0011)
        DisableCharacter(Characters.c3240_0009)
        DisableCharacter(Characters.c3240_0010)
        DisableCharacter(Characters.c3240_0011)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11415091)
def Event_11415091():
    """Event 11415091"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2240_0007)
    Kill(Characters.c2240_0008)
    Kill(Characters.c2240_0009)
    Kill(Characters.c2240_0010)
    Kill(Characters.c2240_0011)
    Kill(Characters.c3240_0009)
    Kill(Characters.c3240_0010)
    Kill(Characters.c3240_0011)


@RestartOnRest(11415092)
def Event_11415092():
    """Event 11415092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=LOST_IZALITH))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11410050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=LOST_IZALITH))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11410050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=LOST_IZALITH))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11410050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=LOST_IZALITH))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11410050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=LOST_IZALITH))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11410050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=LOST_IZALITH))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11410050))
    if not OR_6:
        return RESTART
    EnableFlag(11410050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=LOST_IZALITH))
    if not AND_7:
        return RESTART
    DisableFlag(11410050)
    EnableFlag(11415095)


@ContinueOnRest(11410095)
def Event_11410095():
    """Event 11410095"""
    if FlagEnabled(11800100):
        EnableFlag(11410096)
        DisableObject(Objects.o4960_0000)
        DeleteVFX(VFX.GoldenFog, erase_root_only=False)
        DisableFlag(402)
        End()
    if FlagEnabled(11410096):
        DisableObject(Objects.o4960_0000)
        DeleteVFX(VFX.GoldenFog, erase_root_only=False)
        End()
    if Client():
        return
    
    MAIN.Await(ActionButton(
        prompt_text=10010410,
        anchor_entity=1412660,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411710,
    ))
    
    DisplayStatus(10010630)
    Restart()


@ContinueOnRest(11415390)
def Event_11415390():
    """Event 11415390"""
    AND_1.Add(FlagDisabled(CommonFlags.BedOfChaosDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1411990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415391)
def Event_11415391():
    """Event 11415391"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.BedOfChaosDead))
    AND_1.Add(FlagEnabled(11415393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415393)
def Event_11415393():
    """Event 11415393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.BedOfChaosDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1412996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5400_0000)


@RestartOnRest(11415392)
def Event_11415392():
    """Event 11415392"""
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        DisableCharacter(Characters.c5400_0000)
        DisableCharacter(Characters.c5230_0000)
        DisableCharacter(Characters.c5401_0000)
        Kill(Characters.c5400_0000)
        Kill(Characters.c5230_0000)
        Kill(Characters.c5401_0000)
        End()
    SkipLinesIfFlagRangeAnyEnabled(1, (11410291, 11410292))
    DisableCharacter(Characters.c5400_0000)
    SkipLinesIfFlagRangeAllDisabled(1, (11410291, 11410292))
    SetStandbyAnimationSettings(Characters.c5230_0000)
    EnableInvincibility(Characters.c5400_0000)
    EnableInvincibility(Characters.c5230_0000)
    DisableHealthBar(Characters.c5400_0000)
    DisableHealthBar(Characters.c5230_0000)
    DisableAI(Characters.c5230_0000)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=1)
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412996))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagRangeAnyEnabled(2, (11410291, 11410292))
    SetStandbyAnimationSettings(Characters.c5230_0000)
    ForceAnimation(Characters.c5230_0000, 9060)
    EnableAI(Characters.c5230_0000)
    EnableBossHealthBar(Characters.c5401_0000, name=5400)


@ContinueOnRest(11410001)
def Event_11410001():
    """Event 11410001"""
    DisableObject(Objects.o0200_0003)
    
    MAIN.Await(CharacterDead(Characters.c5401_0000))
    
    EnableFlag(CommonFlags.BedOfChaosDead)
    KillBoss(game_area_param_id=1410800)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=36)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=0)
    DisableObject(Objects.o4972_0000)
    DeleteVFX(VFX.BedOfChaosEntranceFog)
    DisableNetworkSync()
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=Objects.o0200_0003, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(Objects.o0200_0003)
    RegisterBonfire(bonfire_flag=11410920, obj=Objects.o0200_0003)


@ContinueOnRest(11415394)
def Event_11415394():
    """Event 11415394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.BedOfChaosDead))
    AND_1.Add(FlagEnabled(11415392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11415391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.BedOfChaosBossMusic)


@ContinueOnRest(11415395)
def Event_11415395():
    """Event 11415395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.BedOfChaosDead))
    AND_1.Add(FlagEnabled(11415394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.BedOfChaosBossMusic)


@RestartOnRest(11415396)
def Event_11415396():
    """Event 11415396"""
    SkipLinesIfFlagRangeAnyEnabled(15, (11410291, 11410292))
    OR_1.Add(FlagEnabled(11410291))
    OR_1.Add(FlagEnabled(11410292))
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFlagEnabled(6, 11410292)
    EnableFlag(11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140116, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140116, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140115, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140115, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(Characters.c5400_0000)
    AND_1.Add(FlagEnabled(11410291))
    AND_1.Add(FlagEnabled(11410292))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c5400_0000, 5130)
    SkipLinesIfFlagEnabled(12, 11410000)
    SkipLinesIfFlagDisabled(5, 11410005)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140117, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140117, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(4)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140118, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140118, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SetStandbyAnimationSettings(Characters.c5400_0000, standby_animation=10000)
    WaitFrames(frames=1)
    EnableFlag(11410000)
    SetStandbyAnimationSettings(Characters.c5400_0000)
    WaitFrames(frames=1)
    ResetAnimation(Characters.c5400_0000, disable_interpolation=True)


@RestartOnRest(11415397)
def Event_11415397():
    """Event 11415397"""
    EnableInvincibility(Characters.c5401_0000)
    AND_1.Add(FlagEnabled(11410291))
    AND_1.Add(FlagEnabled(11410292))
    
    MAIN.Await(AND_1)
    
    DisableInvincibility(Characters.c5401_0000)
    
    MAIN.Await(HealthRatio(Characters.c5401_0000) <= 0.0)
    
    DisableInvincibility(Characters.c5400_0000)
    DisableInvincibility(Characters.c5230_0000)
    Kill(Characters.c5400_0000, award_souls=True)
    Kill(Characters.c5230_0000)


@RestartOnRest(11415398)
def Event_11415398():
    """Event 11415398"""
    OR_1.Add(FlagEnabled(11410291))
    OR_1.Add(FlagEnabled(11410292))
    
    MAIN.Await(OR_1)
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c5400_0000))
    
    AICommand(Characters.c5400_0000, command_id=2, command_slot=0)
    ReplanAI(Characters.c5400_0000)
    AICommand(Characters.c5230_0000, command_id=2, command_slot=0)
    ReplanAI(Characters.c5230_0000)
    AND_1.Add(FlagEnabled(11410291))
    AND_1.Add(FlagEnabled(11410292))
    if FlagDisabled(11410000):
        AND_1.Add(FlagEnabled(11415396))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c5400_0000))
    
    AICommand(Characters.c5400_0000, command_id=3, command_slot=0)
    ReplanAI(Characters.c5400_0000)
    AICommand(Characters.c5230_0000, command_id=3, command_slot=0)
    ReplanAI(Characters.c5230_0000)


@ContinueOnRest(11415399)
def Event_11415399():
    """Event 11415399"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412110))
    
    EnableInvincibility(PLAYER)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1412110))
    
    Wait(3.0)
    DisableInvincibility(PLAYER)


@ContinueOnRest(11415300)
def Event_11415300():
    """Event 11415300"""
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        return
    if ThisEventFlagDisabled():
        EnableFlag(11415300)
        EnableObjectInvulnerability(1411120)
    AND_1.Add(FlagDisabled(11410291))
    AND_1.Add(ObjectDestroyed(Objects.o4610_0000))
    AND_2.Add(FlagDisabled(11410292))
    AND_2.Add(ObjectDestroyed(Objects.o4610_0001))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(CommonFlags.BedOfChaosDead))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        return
    SkipLinesIfFinishedConditionFalse(4, input_condition=AND_1)
    EnableFlag(11410291)
    DeleteVFX(VFX.BedSealRight)
    DeleteVFX(VFX.BedSealRootLeft)
    Restart()
    EnableFlag(11410292)
    DeleteVFX(VFX.BedSealLeft)
    DeleteVFX(VFX.BedSealRootRight)
    Restart()


@ContinueOnRest(11410200)
def Event_11410200():
    """Event 11410200"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o4633_0000)
        DisableObject(Objects.o4634_0000)
        DisableObject(Objects.o4635_0000)
        DisableObject(Objects.o4636_0000)
        DisableObject(Objects.o4637_0000)
        End()
    RestoreObject(Objects.o4633_0000)
    RestoreObject(Objects.o4634_0000)
    RestoreObject(Objects.o4635_0000)
    RestoreObject(Objects.o4636_0000)
    RestoreObject(Objects.o4637_0000)
    EnableObjectInvulnerability(Objects.o4633_0000)
    EnableObjectInvulnerability(Objects.o4634_0000)
    EnableObjectInvulnerability(Objects.o4635_0000)
    EnableObjectInvulnerability(Objects.o4636_0000)
    EnableObjectInvulnerability(Objects.o4637_0000)
    AND_1.Add(FlagEnabled(11410291))
    AND_1.Add(FlagEnabled(11410292))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412100))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11410200)
    DisableObjectInvulnerability(Objects.o4633_0000)
    DisableObjectInvulnerability(Objects.o4634_0000)
    DisableObjectInvulnerability(Objects.o4635_0000)
    DisableObjectInvulnerability(Objects.o4636_0000)
    DisableObjectInvulnerability(Objects.o4637_0000)
    CreateTemporaryVFX(vfx_id=140009, anchor_entity=Objects.o4635_0000, anchor_type=CoordEntityType.Object)
    DestroyObject(Objects.o4633_0000)
    PlaySoundEffect(Objects.o4633_0000, 463300000, sound_type=SoundType.o_Object)
    WaitFrames(frames=4)
    DestroyObject(Objects.o4634_0000)
    PlaySoundEffect(Objects.o4634_0000, 463400000, sound_type=SoundType.o_Object)
    WaitFrames(frames=3)
    DestroyObject(Objects.o4635_0000)
    PlaySoundEffect(Objects.o4635_0000, 463500000, sound_type=SoundType.o_Object)
    WaitFrames(frames=2)
    DestroyObject(Objects.o4636_0000)
    PlaySoundEffect(Objects.o4636_0000, 463600000, sound_type=SoundType.o_Object)
    WaitFrames(frames=1)
    DestroyObject(Objects.o4637_0000)
    PlaySoundEffect(Objects.o4637_0000, 463700000, sound_type=SoundType.o_Object)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(Objects.o4633_0000)
    DisableObject(Objects.o4636_0000)
    DisableObject(Objects.o4637_0000)


@ContinueOnRest(11410201)
def Event_11410201(_, obj: int, sound_id: int):
    """Event 11410201"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    OR_1.Add(FlagEnabled(11410291))
    OR_1.Add(FlagEnabled(11410292))
    
    MAIN.Await(OR_1)
    
    MAIN.Await(EntityWithinDistance(entity=obj, other_entity=PLAYER, radius=8.0))
    
    DisableObjectInvulnerability(obj)
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=140008, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, sound_id, sound_type=SoundType.o_Object)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(obj)


@ContinueOnRest(11410250)
def Event_11410250():
    """Event 11410250"""
    EndIfFlagRangeAllEnabled(flag_range=(11410291, 11410292))
    EnableObjectInvulnerability(Objects.o4840_0000)
    EnableObjectInvulnerability(Objects.o4840_0001)
    EnableObjectInvulnerability(Objects.o4840_0002)
    EnableObjectInvulnerability(Objects.o4840_0003)
    EnableObjectInvulnerability(Objects.o4840_0004)
    EnableObjectInvulnerability(Objects.o4840_0005)
    EnableObjectInvulnerability(Objects.o4840_0006)
    EnableObjectInvulnerability(Objects.o4840_0007)
    EnableObjectInvulnerability(Objects.o4840_0008)
    EnableObjectInvulnerability(Objects.o4840_0009)
    EnableObjectInvulnerability(Objects.o4840_0010)
    EnableObjectInvulnerability(Objects.o4840_0011)
    EnableObjectInvulnerability(Objects.o4840_0012)
    EnableObjectInvulnerability(Objects.o4840_0013)
    EnableObjectInvulnerability(Objects.o4840_0014)
    EnableObjectInvulnerability(Objects.o4840_0015)
    EnableObjectInvulnerability(Objects.o4840_0016)
    EnableObjectInvulnerability(Objects.o4840_0017)
    EnableObjectInvulnerability(Objects.o4840_0018)
    EnableObjectInvulnerability(Objects.o4840_0019)
    EnableObjectInvulnerability(Objects.o4840_0020)
    EnableObjectInvulnerability(Objects.o4840_0021)
    EnableObjectInvulnerability(Objects.o4840_0022)
    EnableObjectInvulnerability(Objects.o4840_0023)
    EnableObjectInvulnerability(Objects.o4840_0024)
    EnableObjectInvulnerability(Objects.o4840_0025)
    EnableObjectInvulnerability(Objects.o4840_0026)
    EnableObjectInvulnerability(Objects.o4840_0027)
    EnableObjectInvulnerability(Objects.o4840_0028)
    EnableObjectInvulnerability(Objects.o4840_0029)
    EnableObjectInvulnerability(Objects.o4840_0030)
    EnableObjectInvulnerability(Objects.o4840_0031)
    EnableObjectInvulnerability(Objects.o4840_0032)
    EnableObjectInvulnerability(Objects.o4840_0033)
    EnableObjectInvulnerability(Objects.o4840_0034)
    EnableObjectInvulnerability(Objects.o4840_0035)
    EnableObjectInvulnerability(Objects.o4840_0036)
    EnableObjectInvulnerability(Objects.o4840_0037)
    EnableObjectInvulnerability(Objects.o4840_0038)
    EnableObjectInvulnerability(Objects.o4840_0039)
    EnableObjectInvulnerability(Objects.o4840_0040)
    EnableObjectInvulnerability(Objects.o4840_0041)
    EnableObjectInvulnerability(Objects.o4840_0042)
    EnableObjectInvulnerability(Objects.o4840_0043)
    EnableObjectInvulnerability(Objects.o4840_0044)
    EnableObjectInvulnerability(Objects.o4840_0045)
    EnableObjectInvulnerability(Objects.o4840_0046)
    EnableObjectInvulnerability(Objects.o4840_0047)
    AND_1.Add(FlagEnabled(11410291))
    AND_1.Add(FlagEnabled(11410292))
    
    MAIN.Await(AND_1)
    
    DisableObjectInvulnerability(Objects.o4840_0000)
    DisableObjectInvulnerability(Objects.o4840_0001)
    DisableObjectInvulnerability(Objects.o4840_0002)
    DisableObjectInvulnerability(Objects.o4840_0003)
    DisableObjectInvulnerability(Objects.o4840_0004)
    DisableObjectInvulnerability(Objects.o4840_0005)
    DisableObjectInvulnerability(Objects.o4840_0006)
    DisableObjectInvulnerability(Objects.o4840_0007)
    DisableObjectInvulnerability(Objects.o4840_0008)
    DisableObjectInvulnerability(Objects.o4840_0009)
    DisableObjectInvulnerability(Objects.o4840_0010)
    DisableObjectInvulnerability(Objects.o4840_0011)
    DisableObjectInvulnerability(Objects.o4840_0012)
    DisableObjectInvulnerability(Objects.o4840_0013)
    DisableObjectInvulnerability(Objects.o4840_0014)
    DisableObjectInvulnerability(Objects.o4840_0015)
    DisableObjectInvulnerability(Objects.o4840_0016)
    DisableObjectInvulnerability(Objects.o4840_0017)
    DisableObjectInvulnerability(Objects.o4840_0018)
    DisableObjectInvulnerability(Objects.o4840_0019)
    DisableObjectInvulnerability(Objects.o4840_0020)
    DisableObjectInvulnerability(Objects.o4840_0021)
    DisableObjectInvulnerability(Objects.o4840_0022)
    DisableObjectInvulnerability(Objects.o4840_0023)
    DisableObjectInvulnerability(Objects.o4840_0024)
    DisableObjectInvulnerability(Objects.o4840_0025)
    DisableObjectInvulnerability(Objects.o4840_0026)
    DisableObjectInvulnerability(Objects.o4840_0027)
    DisableObjectInvulnerability(Objects.o4840_0028)
    DisableObjectInvulnerability(Objects.o4840_0029)
    DisableObjectInvulnerability(Objects.o4840_0030)
    DisableObjectInvulnerability(Objects.o4840_0031)
    DisableObjectInvulnerability(Objects.o4840_0032)
    DisableObjectInvulnerability(Objects.o4840_0033)
    DisableObjectInvulnerability(Objects.o4840_0034)
    DisableObjectInvulnerability(Objects.o4840_0035)
    DisableObjectInvulnerability(Objects.o4840_0036)
    DisableObjectInvulnerability(Objects.o4840_0037)
    DisableObjectInvulnerability(Objects.o4840_0038)
    DisableObjectInvulnerability(Objects.o4840_0039)
    DisableObjectInvulnerability(Objects.o4840_0040)
    DisableObjectInvulnerability(Objects.o4840_0041)
    DisableObjectInvulnerability(Objects.o4840_0042)
    DisableObjectInvulnerability(Objects.o4840_0043)
    DisableObjectInvulnerability(Objects.o4840_0044)
    DisableObjectInvulnerability(Objects.o4840_0045)
    DisableObjectInvulnerability(Objects.o4840_0046)
    DisableObjectInvulnerability(Objects.o4840_0047)


@ContinueOnRest(11415370)
def Event_11415370():
    """Event 11415370"""
    AND_1.Add(FlagDisabled(11410900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412698,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1411790,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412697)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415371)
def Event_11415371():
    """Event 11415371"""
    AND_1.Add(FlagDisabled(11410900))
    AND_1.Add(FlagEnabled(11415373))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412698,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411790,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412697)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415373)
def Event_11415373():
    """Event 11415373"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11410900))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1412696))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c5250_0000, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c5250_0000)
    SetNetworkUpdateRate(Characters.c5250_0000, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableInvincibility(Characters.c5250_0000)


@RestartOnRest(11415372)
def Event_11415372():
    """Event 11415372"""
    if FlagEnabled(11410900):
        DisableBackread(Characters.c5250_0000)
        Kill(Characters.c5250_0000)
        End()
    DisableAI(Characters.c5250_0000)
    DisableHealthBar(Characters.c5250_0000)
    EnableInvincibility(Characters.c5250_0000)
    AND_1.Add(FlagEnabled(11415373))
    AND_1.Add(Host())
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(51410180))
    AND_2.Add(FlagEnabled(11415373))
    AND_2.Add(Attacked(attacked_entity=Characters.c5250_0000, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.c5250_0000)
    EnableBossHealthBar(Characters.c5250_0000, name=5250)


@ContinueOnRest(11410900)
def Event_11410900():
    """Event 11410900"""
    DisableObject(Objects.o0200_0002)
    
    MAIN.Await(CharacterDead(Characters.c5250_0000))
    
    EnableFlag(11410900)
    KillBoss(game_area_param_id=1410600)
    DisableBackread(Characters.c5250_0000)
    EnableFlag(11410800)
    DisableObject(Objects.o4961_0000)
    DeleteVFX(VFX.CeaselessEntranceFog)
    EnableObject(Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11410976, obj=Objects.o0200_0002)
    if FlagEnabled(11800100):
        return
    EnableFlag(402)


@ContinueOnRest(11415374)
def Event_11415374():
    """Event 11415374"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11410900))
    AND_1.Add(FlagEnabled(11415372))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11415371))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412690))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.CeaselessDischargeMusic)
    
    MAIN.Await(FlagEnabled(11410900))
    
    DisableSoundEvent(sound_id=Sounds.CeaselessDischargeMusic)


@RestartOnRest(11415376)
def Event_11415376():
    """Event 11415376"""
    AND_1.Add(CharacterAlive(Characters.c5250_0000))
    AND_1.Add(CharacterInsideRegion(Characters.c5250_0000, region=1412799))
    
    MAIN.Await(AND_1)
    
    Move(Characters.c5250_0000, destination=1412797, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.c5250_0000, 17006, wait_for_completion=True)
    Move(Characters.c5250_0000, destination=1412798, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(11415377)
def Event_11415377():
    """Event 11415377"""
    if ThisEventFlagEnabled():
        RemoveSpecialEffect(Characters.c5250_0000, 5132)
        AddSpecialEffect(Characters.c5250_0000, 5133)
        AICommand(Characters.c5250_0000, command_id=-1, command_slot=1)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5250_0000, tae_event_id=300))
    
    RemoveSpecialEffect(Characters.c5250_0000, 5132)
    AddSpecialEffect(Characters.c5250_0000, 5133)
    AICommand(Characters.c5250_0000, command_id=-1, command_slot=1)
    ReplanAI(Characters.c5250_0000)


@RestartOnRest(11415378)
def Event_11415378():
    """Event 11415378"""
    SkipLinesIfFlagEnabled(4, 0)
    AND_1.Add(Host())
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(51410180))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412796))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c5250_0000, command_id=1, command_slot=1)
    ReplanAI(Characters.c5250_0000)


@RestartOnRest(11415379)
def Event_11415379():
    """Event 11415379"""
    if FlagEnabled(11410900):
        return
    AND_1.Add(FlagRangeAllEnabled(flag_range=(11415310, 11415314)))
    AND_2.Add(HealthRatio(Characters.c5250_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    Kill(Characters.c5250_0000, award_souls=True)


@RestartOnRest(11415310)
def Event_11415310(_, flag: Flag | int):
    """Event 11415310"""
    AND_1.Add(FlagEnabled(11415376))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(Attacked(attacked_entity=Characters.c5250_0000, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    End()


@ContinueOnRest(11410800)
def Event_11410800():
    """Event 11410800"""
    if FlagEnabled(11410801):
        DisableObject(Objects.o4500_0000)
        DisableMapCollision(collision=Collisions.h0008B1)
        DisableSoundEvent(sound_id=Sounds.LavaSound)
        EnableTreasure(obj=Objects.o0500_0005)
        End()
    DisableObject(Objects.o0500_0005)
    DisableTreasure(obj=Objects.o0500_0005)
    DisableMapCollision(collision=Collisions.h1008B1)
    DisableCharacter(Characters.c2250_0003)
    DisableCharacter(1410451)
    DisableCharacter(Characters.c2250_0005)
    DisableCharacter(1410453)
    DisableCharacter(1410454)
    DisableCharacter(Characters.c2250_0008)
    DisableCharacter(Characters.c2250_0009)
    DisableNetworkSync()
    
    MAIN.Await(ThisEventFlagEnabled())
    
    Wait(5.0)
    AND_1.Add(Host())
    AND_1.Add(HealthRatio(PLAYER) <= 0.0)
    if AND_1:
        return
    if Client():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1412530))
    
    PlayCutscene(140100, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11410801)
    DisableObject(Objects.o4500_0000)
    DisableSoundEvent(sound_id=Sounds.LavaSound)
    DisableMapCollision(collision=Collisions.h0008B1)
    EnableMapCollision(collision=Collisions.h1008B1)
    EnableObject(Objects.o0500_0005)
    EnableTreasure(obj=Objects.o0500_0005)
    EnableCharacter(Characters.c2250_0003)
    EnableCharacter(1410451)
    EnableCharacter(Characters.c2250_0005)
    EnableCharacter(1410453)
    EnableCharacter(1410454)
    EnableCharacter(Characters.c2250_0008)
    EnableCharacter(Characters.c2250_0009)


@ContinueOnRest(11415380)
def Event_11415380():
    """Event 11415380"""
    AND_1.Add(FlagDisabled(11410901))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1411890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415381)
def Event_11415381():
    """Event 11415381"""
    AND_1.Add(FlagDisabled(11410901))
    AND_1.Add(FlagEnabled(11415383))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415383)
def Event_11415383():
    """Event 11415383"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11410901))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1412896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5200_0000)


@RestartOnRest(11415382)
def Event_11415382():
    """Event 11415382"""
    DisableObject(Objects.o4450_0000)
    Event_11415385()
    if FlagEnabled(11410901):
        DisableBackread(Characters.c5200_0000)
        End()
    if FlagDisabled(11410002):
        EnableObject(Objects.o4450_0000)
        DisableCharacter(Characters.c5200_0000)
    DisableAI(Characters.c5200_0000)
    AND_1.Add(FlagEnabled(11415383))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412896))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Intruder))
    if OR_1:
        return
    SkipLinesIfFlagEnabled(8, 11410002)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140120, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140120, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(Characters.c5200_0000)
    DisableObject(Objects.o4450_0000)
    EnableFlag(11410002)
    EnableAI(Characters.c5200_0000)
    EnableBossHealthBar(Characters.c5200_0000, name=5200)


@ContinueOnRest(11410901)
def Event_11410901():
    """Event 11410901"""
    MAIN.Await(CharacterDead(Characters.c5200_0000))
    
    EnableFlag(11410901)
    KillBoss(game_area_param_id=1410700)
    EnableFlag(11410901)
    DisableObject(Objects.o4964_0000)
    DeleteVFX(VFX.CentipedeEntranceFog)
    DisableObject(Objects.o4965_0000)
    DeleteVFX(VFX.CentipedeExitFog)
    DisableNetworkSync()
    Wait(10.0)
    DisableCharacter(Characters.c5200_0000)
    DisableBackread(Characters.c5200_0000)


@ContinueOnRest(11415384)
def Event_11415384():
    """Event 11415384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11410901))
    AND_1.Add(FlagEnabled(11410002))
    AND_1.Add(FlagEnabled(11415382))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11415381))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.CentipedeDemonMusic)
    
    MAIN.Await(FlagEnabled(11410901))
    
    DisableSoundEvent(sound_id=Sounds.CentipedeDemonMusic)


@EndOnRest(11415385)
def Event_11415385():
    """Event 11415385"""
    DisableCharacter(Characters.c5201_0000)
    DisableCharacter(Characters.c5201_0001)
    DisableCharacter(Characters.c5201_0002)
    DisableCharacter(Characters.c5201_0003)
    DisableCharacter(Characters.c5201_0004)
    DisableCharacter(Characters.c5202_0000)
    DisableCharacter(Characters.c5202_0001)
    DisableCharacter(Characters.c5202_0002)
    DisableCharacter(Characters.c5202_0003)
    DisableCharacter(Characters.c5202_0004)
    if FlagEnabled(11410901):
        return
    Event_11415350(
        0,
        flag=11415380,
        npc_part_id=5200,
        npc_part_id_1=5200,
        part_health=125,
        character=Characters.c5201_0000,
    )
    Event_11415350(
        1,
        flag=11415350,
        npc_part_id=5201,
        npc_part_id_1=5201,
        part_health=125,
        character=Characters.c5201_0001,
    )
    Event_11415350(
        2,
        flag=11415351,
        npc_part_id=5202,
        npc_part_id_1=5202,
        part_health=125,
        character=Characters.c5201_0002,
    )
    Event_11415350(
        3,
        flag=11415352,
        npc_part_id=5203,
        npc_part_id_1=5203,
        part_health=125,
        character=Characters.c5201_0003,
    )
    Event_11415350(
        4,
        flag=11415353,
        npc_part_id=5204,
        npc_part_id_1=5204,
        part_health=125,
        character=Characters.c5201_0004,
    )
    Event_11415360(
        0,
        flag=11415380,
        npc_part_id=5205,
        npc_part_id_1=5205,
        part_health=95,
        character=Characters.c5202_0000,
    )
    Event_11415360(
        1,
        flag=11415360,
        npc_part_id=5206,
        npc_part_id_1=5206,
        part_health=95,
        character=Characters.c5202_0001,
    )
    Event_11415360(
        2,
        flag=11415361,
        npc_part_id=5207,
        npc_part_id_1=5207,
        part_health=95,
        character=Characters.c5202_0002,
    )
    Event_11415360(
        3,
        flag=11415362,
        npc_part_id=5208,
        npc_part_id_1=5208,
        part_health=95,
        character=Characters.c5202_0003,
    )
    Event_11415360(
        4,
        flag=11415363,
        npc_part_id=5209,
        npc_part_id_1=5209,
        part_health=95,
        character=Characters.c5202_0004,
    )
    Event_11415320(0, flag=11415380, character=Characters.c5201_0000)
    Event_11415320(1, flag=11415350, character=Characters.c5201_0001)
    Event_11415320(2, flag=11415351, character=Characters.c5201_0002)
    Event_11415320(3, flag=11415352, character=Characters.c5201_0003)
    Event_11415320(4, flag=11415353, character=Characters.c5201_0004)
    Event_11415320(5, flag=11415380, character=Characters.c5202_0000)
    Event_11415320(6, flag=11415360, character=Characters.c5202_0001)
    Event_11415320(7, flag=11415361, character=Characters.c5202_0002)
    Event_11415320(8, flag=11415362, character=Characters.c5202_0003)
    Event_11415320(9, flag=11415363, character=Characters.c5202_0004)


@ContinueOnRest(11415386)
def Event_11415386():
    """Event 11415386"""
    if Client():
        return
    OR_1.Add(CharacterDead(Characters.c5200_0000))
    OR_1.Add(CharacterDead(Characters.c5201_0000))
    OR_1.Add(CharacterDead(Characters.c5201_0001))
    OR_1.Add(CharacterDead(Characters.c5201_0002))
    OR_1.Add(CharacterDead(Characters.c5201_0003))
    OR_1.Add(CharacterDead(Characters.c5201_0004))
    OR_1.Add(CharacterDead(Characters.c5202_0000))
    OR_1.Add(CharacterDead(Characters.c5202_0001))
    OR_1.Add(CharacterDead(Characters.c5202_0002))
    OR_1.Add(CharacterDead(Characters.c5202_0003))
    OR_1.Add(CharacterDead(Characters.c5202_0004))
    
    MAIN.Await(OR_1)
    
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(2670, host_only=True)


@EndOnRest(11415320)
def Event_11415320(_, flag: Flag | int, character: Character | int):
    """Event 11415320"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasTAEEvent(Characters.c5200_0000, tae_event_id=400))
    AND_1.Add(HealthRatio(Characters.c5200_0000) > 0.0)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(HealthRatio(Characters.c5200_0000) <= 0.0)
    
    Kill(character, award_souls=True)


@EndOnRest(11415350)
def Event_11415350(_, flag: Flag | int, npc_part_id: short, npc_part_id_1: int, part_health: int, character: int):
    """Event 11415350"""
    if ThisEventSlotFlagEnabled():
        EnableCharacter(character)
    if FlagEnabled(11415354):
        SetDisplayMask(Characters.c5200_0000, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(Characters.c5200_0000, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(FlagEnabled(flag))
    
    CreateNPCPart(
        Characters.c5200_0000,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=part_health,
    )
    AND_1.Add(CharacterPartHealth(Characters.c5200_0000, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(Characters.c5200_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    EzstateAIRequest(Characters.c5200_0000, command_id=1001, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5200_0000, tae_event_id=400))
    
    EnableCharacter(character)
    Move(
        character,
        destination=Characters.c5200_0000,
        destination_type=CoordEntityType.Character,
        model_point=140,
        copy_draw_parent=Characters.c5200_0000,
    )
    ForceAnimation(character, 8100)
    SetDisplayMask(Characters.c5200_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c5200_0000, command_id=10, command_slot=0)
    if FlagEnabled(11415353):
        AICommand(Characters.c5200_0000, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5200_0000, tae_event_id=300))
    
    SetDisplayMask(Characters.c5200_0000, bit_index=0, switch_type=OnOffChange.Off)
    SetCollisionMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.On)
    AICommand(Characters.c5200_0000, command_id=-1, command_slot=0)


@EndOnRest(11415360)
def Event_11415360(_, flag: Flag | int, npc_part_id: short, npc_part_id_1: int, part_health: int, character: int):
    """Event 11415360"""
    if ThisEventSlotFlagEnabled():
        EnableCharacter(character)
    if FlagEnabled(11415364):
        SetDisplayMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c5200_0000, bit_index=2, switch_type=OnOffChange.Off)
        AICommand(Characters.c5200_0000, command_id=20, command_slot=1)
        End()
    
    MAIN.Await(FlagEnabled(flag))
    
    CreateNPCPart(
        Characters.c5200_0000,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=part_health,
    )
    AND_1.Add(CharacterPartHealth(Characters.c5200_0000, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(Characters.c5200_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    EzstateAIRequest(Characters.c5200_0000, command_id=1002, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5200_0000, tae_event_id=400))
    
    EnableCharacter(character)
    Move(
        character,
        destination=Characters.c5200_0000,
        destination_type=CoordEntityType.Character,
        model_point=141,
        copy_draw_parent=Characters.c5200_0000,
    )
    ForceAnimation(character, 8100)
    SetDisplayMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5200_0000, bit_index=2, switch_type=OnOffChange.Off)
    AICommand(Characters.c5200_0000, command_id=10, command_slot=1)
    if FlagEnabled(11415363):
        AICommand(Characters.c5200_0000, command_id=20, command_slot=1)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5200_0000, tae_event_id=600))
    
    SetDisplayMask(Characters.c5200_0000, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(Characters.c5200_0000, bit_index=2, switch_type=OnOffChange.On)
    AICommand(Characters.c5200_0000, command_id=-1, command_slot=1)


@ContinueOnRest(11410340)
def Event_11410340():
    """Event 11410340"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o4700_0000, animation_id=1)
        End()
    AND_1.Add(Host())
    AND_1.Add(PlayerCovenant(Covenant.ChaosServant))
    AND_1.Add(FlagEnabled(11400598))
    AND_1.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411340,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412200,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411340,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11410340)
    RotateToFaceEntity(PLAYER, target_entity=Objects.o4700_0000)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    ForceAnimation(Objects.o4700_0000, 1)
    CreateTemporaryVFX(vfx_id=140000, anchor_entity=Objects.o4700_0000, anchor_type=CoordEntityType.Object)


@ContinueOnRest(11410341)
def Event_11410341():
    """Event 11410341"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11410340))
    AND_6.Add(Host())
    AND_7.Add(PlayerCovenant(Covenant.ChaosServant))
    AND_6.Add(not AND_7)
    OR_7.Add(AND_6)
    OR_7.Add(FlagDisabled(11400598))
    AND_1.Add(OR_7)
    OR_2.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1411340,
    ))
    AND_1.Add(OR_2)
    AND_2.Add(FlagDisabled(11410340))
    AND_2.Add(Client())
    OR_3.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412200,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411340,
    ))
    OR_3.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=1412201,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411340,
    ))
    AND_2.Add(OR_3)
    AND_3.Add(FlagEnabled(11410340))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(11410340):
        return
    DisplayDialog(
        text=10010160,
        anchor_entity=Objects.o4700_0000,
        display_distance=5.0,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@ContinueOnRest(11410360)
def Event_11410360():
    """Event 11410360"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o4510_0000)
        End()
    
    MAIN.Await(ObjectDestroyed(Objects.o4510_0000))
    
    EnableFlag(11410360)


@ContinueOnRest(11410400)
def Event_11410400():
    """Event 11410400"""
    if FlagEnabled(11410401):
        EndOfAnimation(obj=Objects.o4600_0000, animation_id=0)
    
    MAIN.Await(FlagEnabled(11410410))
    
    AND_1.Add(FlagEnabled(11410401))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412403))
    AND_2.Add(FlagDisabled(11410401))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1412402))
    AND_3.Add(FlagDisabled(11410401))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1412401))
    AND_4.Add(FlagEnabled(11410401))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1412400))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_4)
    if FlagDisabled(11410401):
        EnableFlag(11410401)
        CreateObjectVFX(Objects.o4600_0000, vfx_id=100, model_point=140002)
        ForceAnimation(Objects.o4600_0000, 3, wait_for_completion=True)
        DeleteObjectVFX(Objects.o4600_0000)
    
        MAIN.Await(AllPlayersOutsideRegion(region=1412403))
    
        ForceAnimation(Objects.o4600_0000, 4, wait_for_completion=True)
        Restart()
    DisableFlag(11410401)
    CreateObjectVFX(Objects.o4600_0000, vfx_id=100, model_point=140002)
    ForceAnimation(Objects.o4600_0000, 1, wait_for_completion=True)
    DeleteObjectVFX(Objects.o4600_0000)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1412402))
    
    ForceAnimation(Objects.o4600_0000, 5, wait_for_completion=True)
    Restart()


@ContinueOnRest(11410402)
def Event_11410402():
    """Event 11410402"""
    DisableNetworkSync()
    OR_2.Add(FlagDisabled(11410410))
    OR_2.Add(Multiplayer())
    AND_1.Add(OR_2)
    AND_1.Add(ActionButton(
        prompt_text=10010510,
        anchor_entity=Objects.o4600_0000,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010170, anchor_entity=Objects.o4600_0000, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11415340)
def Event_11415340():
    """Event 11415340"""
    AND_1.Add(FlagDisabled(11410410))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412411,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1411410,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412412)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415341)
def Event_11415341():
    """Event 11415341"""
    AND_1.Add(FlagDisabled(11410410))
    AND_1.Add(FlagEnabled(11415343))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1412411,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1411410,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1412412)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11415343)
def Event_11415343():
    """Event 11415343"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11410410))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1412416))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2231_0000)


@RestartOnRest(11415342)
def Event_11415342():
    """Event 11415342"""
    SkipLinesIfFlagDisabled(8, 11410410)
    SkipLinesIfClient(4)
    DisableObject(Objects.o4962_0000)
    DeleteVFX(VFX.FiresageEntranceFog, erase_root_only=False)
    DisableObject(Objects.o4963_0000)
    DeleteVFX(VFX.FiresageExitFog, erase_root_only=False)
    DisableCharacter(Characters.c2231_0000)
    DisableBackread(Characters.c2231_0000)
    End()
    DisableAI(Characters.c2231_0000)
    AND_1.Add(FlagEnabled(11415343))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412416))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.c2231_0000)
    EnableBossHealthBar(Characters.c2231_0000, name=2230)


@ContinueOnRest(11415344)
def Event_11415344():
    """Event 11415344"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11410410))
    AND_1.Add(FlagEnabled(11415342))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11415341))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412410))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.FiresageDemonMusic)
    
    MAIN.Await(FlagEnabled(11410410))
    
    DisableSoundEvent(sound_id=Sounds.FiresageDemonMusic)


@ContinueOnRest(11415345)
def Event_11415345():
    """Event 11415345"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11415340))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412410))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c5340_0000))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c3210_0000))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c3220_0000))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c3220_0001))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c3220_0002))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c3220_0003))
    OR_1.Add(CharacterBackreadEnabled(m14_00_Characters.c3220_0004))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableBackread(m14_00_Characters.c5340_0000)
    DisableBackread(m14_00_Characters.c3210_0000)
    DisableBackread(m14_00_Characters.c3220_0000)
    DisableBackread(m14_00_Characters.c3220_0001)
    DisableBackread(m14_00_Characters.c3220_0002)
    DisableBackread(m14_00_Characters.c3220_0003)
    DisableBackread(m14_00_Characters.c3220_0004)
    
    MAIN.Await(FlagEnabled(11410410))
    
    Wait(5.0)
    EnableBackread(m14_00_Characters.c5340_0000)
    EnableBackread(m14_00_Characters.c3210_0000)
    EnableBackread(m14_00_Characters.c3220_0000)
    EnableBackread(m14_00_Characters.c3220_0001)
    EnableBackread(m14_00_Characters.c3220_0002)
    EnableBackread(m14_00_Characters.c3220_0003)
    EnableBackread(m14_00_Characters.c3220_0004)


@ContinueOnRest(11410410)
def Event_11410410():
    """Event 11410410"""
    MAIN.Await(CharacterDead(Characters.c2231_0000))
    
    EnableFlag(11410410)
    KillBoss(game_area_param_id=1410400)
    EnableFlag(11410410)
    DisableObject(Objects.o4962_0000)
    DeleteVFX(VFX.FiresageEntranceFog)
    DisableObject(Objects.o4963_0000)
    DeleteVFX(VFX.FiresageExitFog)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(Characters.c2231_0000)
    DisableBackread(Characters.c2231_0000)


@RestartOnRest(11415100)
def Event_11415100(_, entity: int, character: Character | int, cancel_animation: int, radius: float, seconds: float):
    """Event 11415100"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=entity, other_entity=PLAYER, radius=radius))
    
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)


@RestartOnRest(11415120)
def Event_11415120(
    _,
    character: int,
    character_1: Character | int,
    cancel_animation: int,
    region: Region | int,
    seconds: float,
):
    """Event 11415120"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character_1, cancel_animation=cancel_animation)
        End()
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    Wait(seconds)
    SetStandbyAnimationSettings(character_1, cancel_animation=cancel_animation)


@RestartOnRest(11415200)
def Event_11415200():
    """Event 11415200"""
    Event_11415201(0, character=1410500, part_index=1, npc_part_id=0, npc_part_id_1=3290, flag=3290)
    Event_5200(-1, character=1410500, flag=11415201, bit_index=0, bit_index_1=0)
    Event_5200(-1, character=1410500, flag=11415201, bit_index=2, bit_index_1=0)
    Event_5201(-1, character=1410500, flag=11415201, obj=1411500, obj_1=1411501, model_point=120, model_point_1=0)
    Event_5201(-1, character=1410500, flag=11415201, obj=1411502, obj_1=1411503, model_point=126, model_point_1=0)
    Event_5202(
        -1,
        character=1410500,
        flag=11415201,
        character_1=1410550,
        character_2=1410551,
        model_point=120,
        model_point_1=123,
    )
    Event_5202(
        -1,
        character=1410500,
        flag=11415201,
        character_1=1410552,
        character_2=1410553,
        model_point=126,
        model_point_1=129,
    )
    Event_11415201(1, character=1410500, part_index=2, npc_part_id=0, npc_part_id_1=3291, flag=3291)
    Event_5200(-1, character=1410500, flag=11415202, bit_index=5, bit_index_1=0)
    Event_5201(-1, character=1410500, flag=11415202, obj=1411504, obj_1=1411505, model_point=135, model_point_1=0)
    Event_5202(
        -1,
        character=1410500,
        flag=11415202,
        character_1=1410554,
        character_2=1410555,
        model_point=135,
        model_point_1=137,
    )
    Event_5202(
        -1,
        character=1410500,
        flag=11415202,
        character_1=1410556,
        character_2=1410557,
        model_point=153,
        model_point_1=155,
    )
    Event_11415201(2, character=1410500, part_index=3, npc_part_id=0, npc_part_id_1=3292, flag=3292)
    Event_5200(-1, character=1410500, flag=11415203, bit_index=6, bit_index_1=0)
    Event_5200(-1, character=1410500, flag=11415203, bit_index=8, bit_index_1=0)
    Event_5201(-1, character=1410500, flag=11415203, obj=1411506, obj_1=1411507, model_point=138, model_point_1=0)
    Event_5201(-1, character=1410500, flag=11415203, obj=1411508, obj_1=1411509, model_point=144, model_point_1=0)
    Event_5202(
        -1,
        character=1410500,
        flag=11415203,
        character_1=1410558,
        character_2=1410559,
        model_point=138,
        model_point_1=141,
    )
    Event_5202(
        -1,
        character=1410500,
        flag=11415203,
        character_1=1410560,
        character_2=1410561,
        model_point=144,
        model_point_1=150,
    )
    Event_11415201(3, character=1410500, part_index=4, npc_part_id=0, npc_part_id_1=3293, flag=3293)
    Event_5200(-1, character=1410500, flag=11415204, bit_index=4, bit_index_1=0)
    Event_5201(-1, character=1410500, flag=11415204, obj=1411510, obj_1=1411511, model_point=132, model_point_1=0)
    Event_5202(
        -1,
        character=1410500,
        flag=11415204,
        character_1=1410562,
        character_2=1410563,
        model_point=132,
        model_point_1=134,
    )
    Event_5202(
        -1,
        character=1410500,
        flag=11415204,
        character_1=1410564,
        character_2=1410565,
        model_point=150,
        model_point_1=152,
    )


@EndOnRest(11415201)
def Event_11415201(_, character: int, part_index: short, npc_part_id: short, npc_part_id_1: int, flag: Flag | int):
    """Event 11415201"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=100)
    
    MAIN.Await(CharacterPartHealth(character, npc_part_id=npc_part_id_1) <= 0)
    
    DisableFlag(11415290)
    DisableFlag(11415291)
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11415290, 11415291))
    EnableFlag(flag)
    if FlagEnabled(11415290):
        ForceAnimation(character, 8000)
    else:
        ForceAnimation(character, 8010)


@EndOnRest(5200)
def Event_5200(_, character: Character | int, flag: Flag | int, bit_index: uchar, bit_index_1: uchar):
    """Event 5200"""
    if FlagDisabled(flag):
        AND_1.Add(FlagEnabled(flag))
        AND_2.Add(CharacterDead(character))
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfFinishedConditionTrue(input_condition=AND_2)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)


@EndOnRest(5201)
def Event_5201(
    _,
    character: Character | int,
    flag: Flag | int,
    obj: Object | int,
    obj_1: Object | int,
    model_point: short,
    model_point_1: short,
):
    """Event 5201"""
    DisableObject(obj)
    DisableObject(obj_1)
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    EnableObject(obj)
    EnableObject(obj_1)
    MoveObjectToCharacter(obj, character=character, model_point=model_point)
    MoveObjectToCharacter(obj_1, character=character, model_point=model_point_1)
    DestroyObject(obj)
    DestroyObject(obj_1)


@EndOnRest(5202)
def Event_5202(
    _,
    character: int,
    flag: Flag | int,
    character_1: int,
    character_2: int,
    model_point: int,
    model_point_1: int,
):
    """Event 5202"""
    if FlagEnabled(flag):
        return
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(character)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point_1,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)


@RestartOnRest(11415210)
def Event_11415210(_, first_flag: Flag | int, last_flag: Flag | int, value: int):
    """Event 11415210"""
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= value)
    
    DisableSoundEvent(sound_id=Sounds.EggPrayerSound)


@RestartOnRest(11415250)
def Event_11415250(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
):
    """Event 11415250"""
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
        End()
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    
    MAIN.Await(CharacterDead(character))
    
    SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableCharacter(character_5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    Move(
        character_2,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=character,
    )
    Move(
        character_3,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=102,
        copy_draw_parent=character,
    )
    Move(
        character_4,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=103,
        copy_draw_parent=character,
    )
    Move(
        character_5,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=104,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)
    ForceAnimation(character_3, 7000)
    ForceAnimation(character_4, 7000)
    ForceAnimation(character_5, 7000)


@ContinueOnRest(11410350)
def Event_11410350():
    """Event 11410350"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o4810_0000)
        PostDestruction(Objects.o4810_0001)
        EndOfAnimation(obj=Objects.o0500_0000, animation_id=116)
        EnableTreasure(obj=Objects.o0500_0000)
        End()
    DisableObject(Objects.o4810_0001)
    DisableTreasure(obj=Objects.o0500_0000)
    CreateObjectVFX(Objects.o0500_0000, vfx_id=90, model_point=99010)
    ForceAnimation(Objects.o0500_0000, 115, loop=True)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1412350))
    OR_1.Add(ObjectDestroyed(Objects.o4810_0000))
    
    MAIN.Await(OR_1)
    
    DisableObject(Objects.o4810_0000)
    EnableObject(Objects.o4810_0001)
    CreateTemporaryVFX(vfx_id=140001, anchor_entity=Objects.o4810_0001, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(Objects.o4810_0001, 481000001, sound_type=SoundType.o_Object)
    DestroyObject(Objects.o4810_0001)
    ForceAnimation(Objects.o0500_0000, 116, wait_for_completion=True)
    EnableTreasure(obj=Objects.o0500_0000)
    DeleteObjectVFX(Objects.o0500_0000)


@RestartOnRest(11410100)
def Event_11410100(_, character: Character | int):
    """Event 11410100"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueNotEqual(left=character, right=1410110):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(33002000, host_only=True)


@RestartOnRest(11410150)
def Event_11410150(_, character: Character | int, item_lot: int):
    """Event 11410150"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    if not OR_1:
        return
    AwardItemLot(item_lot, host_only=True)


@RestartOnRest(800)
def Event_800(_, character: Character | int):
    """Event 800"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        DisableCharacter(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(11410600)
def Event_11410600(_, obj: Object | int, obj_act_id: int):
    """Event 11410600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11410260)
def Event_11410260():
    """Event 11410260"""
    DisableNetworkSync()
    AND_1.Add(InsideMap(game_map=LOST_IZALITH))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412510))
    AND_1.Add(TimeElapsed(seconds=3.0))
    
    MAIN.Await(AND_1)
    
    ActivateKillplaneForModel(game_map=LOST_IZALITH, y_threshold=-400.0, target_model_id=3240)
    Restart()


@ContinueOnRest(11410510)
def Event_11410510(_, character: Character | int, flag: Flag | int):
    """Event 11410510"""
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


@ContinueOnRest(11410520)
def Event_11410520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11410501)
def Event_11410501(_, character: Character | int, flag: Flag | int):
    """Event 11410501"""
    OR_2.Add(FlagEnabled(1503))
    OR_2.Add(FlagEnabled(1505))
    OR_2.Add(FlagEnabled(1506))
    OR_2.Add(FlagEnabled(1507))
    AND_1.Add(OR_2)
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


@ContinueOnRest(11410530)
def Event_11410530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410530"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1007))
    AND_1.Add(FlagEnabled(11410901))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11410531)
def Event_11410531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410531"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1009))
    AND_1.Add(FlagDisabled(800))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412510))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    EnableCharacter(Characters.c0000_0003)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0003, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11410532)
def Event_11410532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410532"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1009))
    AND_1.Add(FlagEnabled(800))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1412510))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(character, destination=1412500, destination_type=CoordEntityType.Region, set_draw_parent=Collisions.h0042B1)
    EnableFlag(11410580)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    SetNest(character, region=1412500)


@ContinueOnRest(11410533)
def Event_11410533(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410533"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1003))
    AND_1.Add(FlagEnabled(11410595))
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(Host())
    AND_2.Add(FlagDisabled(1004))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11410534)
def Event_11410534(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410534"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1002))
    AND_1.Add(HealthRatio(character) <= 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11410540)
def Event_11410540(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410540"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1502))
    AND_1.Add(FlagEnabled(11400590))
    AND_1.Add(InsideMap(game_map=LOST_IZALITH))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableFlag(814)


@ContinueOnRest(11410541)
def Event_11410541(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410541"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1503))
    OR_1.Add(CharacterAlive(Characters.c3240_0002))
    OR_1.Add(CharacterAlive(Characters.c3240_0003))
    OR_1.Add(CharacterAlive(Characters.c3240_0004))
    OR_1.Add(CharacterAlive(Characters.c3240_0005))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11410590))
    AND_2.Add(FlagDisabled(1512))
    AND_2.Add(FlagEnabled(1504))
    AND_2.Add(ThisEventFlagEnabled())
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SetStandbyAnimationSettings(character)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.FightingAlly)
    AddSpecialEffect(character, 90111)


@ContinueOnRest(11410542)
def Event_11410542(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410542"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1503))
    AND_1.Add(CharacterDead(Characters.c3240_0002))
    AND_1.Add(CharacterDead(Characters.c3240_0003))
    AND_1.Add(CharacterDead(Characters.c3240_0004))
    AND_1.Add(CharacterDead(Characters.c3240_0005))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11410543)
def Event_11410543(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410543"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1504))
    AND_1.Add(HealthRatio(character) < 0.5)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(CharacterDead(Characters.c3240_0002))
    AND_1.Add(CharacterDead(Characters.c3240_0003))
    AND_1.Add(CharacterDead(Characters.c3240_0004))
    AND_1.Add(CharacterDead(Characters.c3240_0005))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SetNest(character, region=1412360)


@ContinueOnRest(11410544)
def Event_11410544(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410544"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1504))
    AND_1.Add(HealthRatio(character) >= 0.5)
    AND_1.Add(CharacterDead(Characters.c3240_0002))
    AND_1.Add(CharacterDead(Characters.c3240_0003))
    AND_1.Add(CharacterDead(Characters.c3240_0004))
    AND_1.Add(CharacterDead(Characters.c3240_0005))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SetNest(character, region=1412360)


@ContinueOnRest(11410545)
def Event_11410545(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410545"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1506))
    AND_1.Add(FlagEnabled(11410591))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1512))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_2)
    Kill(character, award_souls=True)
    RemoveSpecialEffect(character, 90111)
    End()
    DropMandatoryTreasure(character)


@ContinueOnRest(11410546)
def Event_11410546(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410546"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    AND_1.Add(FlagDisabled(1506))
    AND_1.Add(FlagDisabled(1508))
    AND_1.Add(HealthRatio(character) <= 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11410547)
def Event_11410547(_, character: Character | int):
    """Event 11410547"""
    if FlagEnabled(1512):
        return
    SkipLinesIfThisEventSlotFlagDisabled(3)
    SkipLinesIfFlagEnabled(1, 11410593)
    SetStandbyAnimationSettings(character)
    End()
    OR_1.Add(ThisEventFlagEnabled())
    OR_1.Add(FlagEnabled(1503))
    
    MAIN.Await(OR_1)
    
    if ThisEventFlagDisabled():
        MAIN.Await(FlagDisabled(814))
    SetStandbyAnimationSettings(character, cancel_animation=7856)


@ContinueOnRest(11410548)
def Event_11410548(_, character: Character | int):
    """Event 11410548"""
    if FlagEnabled(1512):
        return
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character, standby_animation=7855)
        End()
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1507))
    AND_1.Add(FlagEnabled(11410593))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, standby_animation=7855)


@ContinueOnRest(11410549)
def Event_11410549(_, character: Character | int):
    """Event 11410549"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1507))
    AND_1.Add(FlagEnabled(11410594))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)


@ContinueOnRest(11410550)
def Event_11410550(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11410550"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1505))
    AND_1.Add(FlagEnabled(11410594))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11415030)
def Event_11415030():
    """Event 11415030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11415033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11415031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0007)
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1007))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0007))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0007, other_entity=PLAYER, radius=20.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0007,
        region=1412000,
        summon_flag=11415031,
        dismissal_flag=11415033,
    )


@ContinueOnRest(11415029)
def Event_11415029():
    """Event 11415029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11415033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11415031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0007)
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11415031))
    AND_1.Add(FlagDisabled(11415033))
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1007))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0007))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0007, other_entity=PLAYER, radius=20.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0007,
        region=1412000,
        summon_flag=11415031,
        dismissal_flag=11415033,
    )


@ContinueOnRest(14015990)
def Event_14015990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 14015990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11415032)
def Event_11415032():
    """Event 11415032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11415031))
    AND_1.Add(FlagEnabled(11415383))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0007, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0007)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0007, region=1412898))
    
    RotateToFaceEntity(Characters.c0000_0007, target_entity=1412897)
    ForceAnimation(Characters.c0000_0007, 7410)
    AICommand(Characters.c0000_0007, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0007)


@ContinueOnRest(11415035)
def Event_11415035():
    """Event 11415035"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11415036):
        return
    if FlagEnabled(11410410):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11410810))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1412010))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=Characters.c0000_0008,
        region=1412001,
        summon_flag=11415036,
        dismissal_flag=11415037,
    )
    Wait(20.0)
    Restart()


@ContinueOnRest(11415038)
def Event_11415038():
    """Event 11415038"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11415039):
        return
    if FlagEnabled(CommonFlags.BedOfChaosDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11410811))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1412520))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=Characters.c0000_0009,
        region=1412002,
        summon_flag=11415039,
        dismissal_flag=11415040,
    )
    Wait(20.0)
    Restart()


@ContinueOnRest(11410810)
def Event_11410810(_, character: Character | int, flag: Flag | int, flag_1: Flag | int):
    """Event 11410810"""
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(character)
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(11415843)
def Event_11415843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11415843"""
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


@ContinueOnRest(11415846)
def Event_11415846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11415846"""
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
