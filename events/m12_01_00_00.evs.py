"""
Oolacile / Chasm of the Abyss

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m12_01_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11210992()
    Event_11210999(0, character=Characters.c2300_ttn1, item_lot=0)
    Event_11210999(1, character=Characters.c4180_chn1, item_lot=0)
    Event_11210700()
    SkipLinesIfClient(10)
    DisableObject(Objects.o2912_0001)
    DeleteVFX(VFX.MultiplayerFog4, erase_root_only=False)
    DisableObject(Objects.o2913)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o2914)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o2917_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    DisableObject(Objects.o2920_0000)
    DeleteVFX(VFX.MultiplayerFog5, erase_root_only=False)
    DisableMapCollision(collision=Collisions.h0095B1_0000)
    if FlagEnabled(11210539):
        EnableMapCollision(collision=Collisions.h0095B1_0000)
        DisableMapCollision(collision=Collisions.h0095B1)
    Event_11215090()
    Event_11215091()
    Event_11215092()
    DisableSoundEvent(sound_id=Sounds.SanctuaryGuardianMusic)
    if FlagEnabled(Flags.SanctuaryGuardianDead):
        Event_11210000()
        DisableObject(Objects.o2909_0001)
        DeleteVFX(VFX.SanctuaryGuardianEntranceFog, erase_root_only=False)
        DisableObject(Objects.o2910_0001)
        DeleteVFX(VFX.SanctuaryGuardianExitFog, erase_root_only=False)
    else:
        Event_11215000()
        Event_11215001()
        Event_11215002()
        Event_11215003()
        Event_11215004()
        Event_11215005()
        Event_11210000()
        Event_11215006(0, character=Characters.c3472_0000, character_1=Characters.c3471_0000, item_lot=34720000)
    Event_11215006(1, character=Characters.c3472_0001, character_1=Characters.c3471_0001, item_lot=34720010)
    Event_11215006(2, character=Characters.c3472_0002, character_1=Characters.c3471_0002, item_lot=34720020)
    Event_11215007()
    Event_11215008()
    Event_11215009()
    DisableSoundEvent(sound_id=Sounds.ArtoriasMusic)
    if FlagEnabled(Flags.ArtoriasDead):
        Event_11210001()
        DisableObject(Objects.o2915_0000)
        DeleteVFX(VFX.ArtoriasEntranceFog, erase_root_only=False)
        DisableObject(Objects.o2916_0000)
        DeleteVFX(VFX.ArtoriasExitFog, erase_root_only=False)
        DisableMapCollision(collision=Collisions.h7400B1)
    else:
        Event_11215010()
        Event_11215011()
        Event_11215012()
        Event_11215013()
        Event_11215014()
        Event_11215015()
        Event_11210001()
    DisableSoundEvent(sound_id=Sounds.ManusMusic)
    if FlagEnabled(Flags.ManusDead):
        Event_11210002()
        DisableObject(Objects.o2911_0001)
        DeleteVFX(VFX.ManusEntranceFog, erase_root_only=False)
    else:
        Event_11215020()
        Event_11215021()
        Event_11215022()
        Event_11215027()
        Event_11215023()
        Event_11215024()
        Event_11215025()
        Event_11210002()
    Event_11215026()
    DisableSoundEvent(sound_id=Sounds.KalameetMusic)
    AND_1.Add(FlagEnabled(Flags.KalameetShotDown))
    AND_1.Add(FlagDisabled(Flags.KalameetDead))
    SkipLinesIfConditionTrue(3, AND_1)
    DisableObject(Objects.o2919_0000)
    DeleteVFX(VFX.KalameetEntranceFog, erase_root_only=False)
    DisableMapCollision(collision=Collisions.h7400B1)
    if FlagDisabled(Flags.KalameetDead):
        Event_11215060()
        Event_11215061()
        Event_11215062()
        Event_11215063()
        Event_11215064()
        Event_11215066()
        Event_11215065()
        Event_11210005()
    if FlagEnabled(Flags.ManusDead):
        RegisterBonfire(bonfire_flag=11210992, obj=Objects.o0200_0003)
    RegisterBonfire(bonfire_flag=11210984, obj=Objects.o0200_0000)
    RegisterBonfire(bonfire_flag=11210976, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11210968, obj=Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11210960, obj=Objects.o0200_0004)
    RegisterLadder(start_climbing_flag=11210210, stop_climbing_flag=11210211, obj=Objects.o2402)
    RegisterLadder(start_climbing_flag=11210212, stop_climbing_flag=11210213, obj=Objects.o2790_0000)
    RegisterLadder(start_climbing_flag=11210214, stop_climbing_flag=11210215, obj=Objects.o2791_0000)
    Event_11215100()
    Event_11215110(0, character=Characters.c4130_0022, region=1212502, radius=0.0, region_1=1212502)
    Event_11215110(1, character=Characters.c4130_0023, region=1212502, radius=0.0, region_1=1212502)
    Event_11215110(2, character=Characters.c4130_0020, region=1212502, radius=10.0, region_1=1212506)
    Event_11215110(3, character=Characters.c4130_0017, region=1212502, radius=10.0, region_1=1212506)
    Event_11215115(0, character=Characters.c4130_0022, region=1212502, region_1=1212501)
    Event_11215115(1, character=Characters.c4130_0023, region=1212502, region_1=1212501)
    Event_11215120(
        0,
        character=Characters.c4130_0019,
        character_1=Characters.c4130_0025,
        character_2=Characters.c4130_0027,
        flag=51210030,
    )
    Event_11215140(
        0,
        character=Characters.c4120_0004,
        region=1212503,
        region_1=1212504,
        region_2=1212505,
        flag=11215151,
        flag_1=11215152,
        flag_2=11215153,
    )
    Event_11215140(
        1,
        character=Characters.c4120_0007,
        region=1212523,
        region_1=1212524,
        region_2=1212525,
        flag=11215154,
        flag_1=11215155,
        flag_2=11215156,
    )
    Event_11210050()
    Event_11210051()
    Event_11210052()
    Event_11210053()
    Event_11210054()
    Event_11210055()
    Event_11210056()
    Event_11210057()
    Event_11210040()
    Event_11210041()
    Event_11210042()
    Event_11210043()
    Event_11210004()
    Event_11215050()
    Event_11215051()
    Event_11215052()
    Event_11210025()
    Event_11210021()
    Event_11215040()
    Event_11215041()
    Event_11210020()
    Event_11215043()
    Event_11215044()
    Event_11210330(0, first_flag=11210310, last_flag=11210315, flag=11210330)
    Event_11210310(0, character=Characters.c4170_0001, flag=11210310)
    Event_11210310(1, character=Characters.c4170_0002, flag=11210311)
    Event_11210310(2, character=Characters.c4170_0003, flag=11210312)
    Event_11210310(3, character=Characters.c4172_0018, flag=11210313)
    Event_11210310(4, character=Characters.c4172_0010, flag=11210314)
    Event_11210310(5, character=Characters.c4171_0005, flag=11210315)
    Event_11210600(0, obj=Objects.o0110_0000, obj_act_id=11210600)
    Event_11210600(1, obj=Objects.o0110_0001, obj_act_id=11210601)
    Event_11210600(2, obj=Objects.o0110_0002, obj_act_id=11210602)
    Event_11210600(4, obj=Objects.o0110_0004, obj_act_id=11210604)
    Event_11210600(5, obj=Objects.o0110_0005, obj_act_id=11210605)
    Event_11210230(0, obj=Objects.o2795_0000, obj_1=Objects.o0500_0100, animation_id=125, animation_id_1=126)
    Event_11210350(0, character=Characters.c3300_0000, item_lot=33007200)
    Event_11210350(1, character=Characters.c3300_0001, item_lot=33007000)
    Event_11210350(2, character=Characters.c3300_0002, item_lot=33007100)
    Event_11210350(3, character=Characters.c3300_0003, item_lot=33007300)
    Event_11210350(4, character=Characters.c3300_0004, item_lot=33007100)
    Event_11210350(5, character=Characters.c4160_0002, item_lot=41601000)
    Event_11210100()
    Event_11210103()
    Event_11210110()
    Event_11210120()
    Event_11210123()
    Event_11210130()
    Event_11210133()
    Event_11210140()
    Event_11210150()
    Event_11219100(0, flag=11218102, obj=Objects.o2700_0000, animation_id=0, state=1, anchor_entity=Objects.o2701_0010)
    Event_11219100(1, flag=11218103, obj=Objects.o2700_0000, animation_id=10, state=0, anchor_entity=Objects.o2701_0000)
    Event_11210170(0, left=11215220, collision=Collisions.h7600B1, region=1212105)
    Event_11210170(1, left=11215221, collision=Collisions.h7601B1, region=1212115)
    Event_11210170(2, left=11215222, collision=Collisions.h7602B1, region=1212125)
    Event_11210170(3, left=11215223, collision=Collisions.h7603B1, region=1212135)
    Event_11210170(4, left=11215224, collision=Collisions.h7604B1, region=1212145)
    DisableSoundEvent(sound_id=Sounds.LightIllusoryWallSound0)
    DisableSoundEvent(sound_id=Sounds.LightIllusoryWallSound1)
    Event_11210200(0, obj=Objects.o2730_0000, region=1212200)
    Event_11210200(1, obj=Objects.o2732_0000, region=1212201)
    Event_11210205(0, anchor_entity=Objects.o2730_0000, region=1212200, flag=11210200)
    Event_11210205(1, anchor_entity=Objects.o2732_0000, region=1212201, flag=11210201)
    Event_11210300()
    Event_11215250(0, obj=Objects.o2610_0000, vfx_id=VFX.ManusRock_o2610_0)
    Event_11215250(1, obj=Objects.o2610_0001, vfx_id=VFX.ManusRock_o2610_1)
    Event_11215250(2, obj=Objects.o2610_0002, vfx_id=VFX.ManusRock_o2610_2)
    Event_11215250(3, obj=Objects.o2611_0000, vfx_id=VFX.ManusRock_o2611_0)
    Event_11215250(4, obj=Objects.o2611_0001, vfx_id=VFX.ManusRock_o2611_1)
    Event_11215250(5, obj=Objects.o2611_0002, vfx_id=VFX.ManusRock_o2611_2)
    Event_11215250(6, obj=Objects.o2611_0003, vfx_id=VFX.ManusRock_o2611_3)
    Event_11215250(7, obj=Objects.o2611_0004, vfx_id=VFX.ManusRock_o2611_4)
    Event_11215250(8, obj=Objects.o2611_0005, vfx_id=VFX.ManusRock_o2611_5)
    Event_11215250(9, obj=Objects.o2612_0000, vfx_id=VFX.ManusRock_o2612_0)
    Event_11215250(10, obj=Objects.o2612_0001, vfx_id=VFX.ManusRock_o2612_1)
    Event_11215250(11, obj=Objects.o2612_0002, vfx_id=VFX.ManusRock_o2612_2)
    Event_11215250(12, obj=Objects.o2612_0003, vfx_id=VFX.ManusRock_o2612_3)
    Event_11215250(13, obj=Objects.o2612_0004, vfx_id=VFX.ManusRock_o2612_4)
    Event_11215250(14, obj=Objects.o2612_0005, vfx_id=VFX.ManusRock_o2612_5)
    Event_11215250(15, obj=Objects.o2613_0000, vfx_id=VFX.ManusRock_o2613_0)
    Event_11215250(16, obj=Objects.o2613_0001, vfx_id=VFX.ManusRock_o2613_1)
    Event_11215250(17, obj=Objects.o2613_0002, vfx_id=VFX.ManusRock_o2613_2)
    Event_11215250(18, obj=Objects.o2613_0003, vfx_id=VFX.ManusRock_o2613_3)
    Event_11215250(19, obj=Objects.o2613_0004, vfx_id=VFX.ManusRock_o2613_4)
    Event_11215250(20, obj=Objects.o2613_0005, vfx_id=VFX.ManusRock_o2613_5)
    Event_11215250(21, obj=Objects.o2613_0006, vfx_id=VFX.ManusRock_o2613_6)
    Event_11215250(22, obj=Objects.o2613_0007, vfx_id=VFX.ManusRock_o2613_7)
    Event_11215250(23, obj=Objects.o2613_0008, vfx_id=VFX.ManusRock_o2613_8)
    Event_11215160(0, character=Characters.c2780_0000)
    Event_11215165(0, character=Characters.c2780_0000)
    Event_11215170(0, character=Characters.c2780_0000)
    Event_11215175(0, character=Characters.c2780_0000)
    Event_11215180(0, character=Characters.c2780_0000, region=1212180)
    Event_11210680(0, character=Characters.c2780_0000)
    Event_11215185(0, character=Characters.c2780_0000)
    SetNetworkUpdateRate(Characters.c2780_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Event_11215160(1, character=Characters.c2780_0001)
    Event_11215165(1, character=Characters.c2780_0001)
    Event_11215170(1, character=Characters.c2780_0001)
    Event_11215175(1, character=Characters.c2780_0001)
    Event_11215180(1, character=Characters.c2780_0001, region=1212181)
    Event_11210680(1, character=Characters.c2780_0001)
    Event_11215185(1, character=Characters.c2780_0001)
    Event_11219113()
    Event_11219114()
    RunEvent(4294967295, slot=0, args=(0,))
    Event_11213888()
    Event_11215846(0, left=Flags.SanctuaryGuardianDead, obj=Objects.o2909_0001, vfx_id=VFX.SanctuaryGuardianEntranceFog)
    Event_11215843(
        0,
        left=Flags.SanctuaryGuardianDead,
        line_intersects=1211790,
        anchor_entity=1212888,
        target_entity=1212887,
    )
    Event_11215846(1, left=Flags.ArtoriasDead, obj=Objects.o2915_0000, vfx_id=VFX.ArtoriasEntranceFog)
    Event_11215843(1, left=Flags.ArtoriasDead, line_intersects=1211890, anchor_entity=1212898, target_entity=1212897)
    Event_11215846(2, left=Flags.KalameetDead, obj=Objects.o2919_0000, vfx_id=VFX.KalameetEntranceFog)
    Event_11215843(2, left=Flags.KalameetDead, line_intersects=1211690, anchor_entity=1212908, target_entity=1212907)
    Event_11215846(3, left=Flags.ManusDead, obj=Objects.o2911_0001, vfx_id=VFX.ManusEntranceFog)
    Event_11215843(3, left=Flags.ManusDead, line_intersects=1211990, anchor_entity=1212998, target_entity=1212997)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableCharacter(Characters.c4090_0001)
    Event_11215030(
        1,
        character=Characters.c4090_0002,
        flag=11215036,
        flag_1=11215035,
        flag_2=11210901,
        anchor_entity=1212082,
        region=1212083,
        flag_3=11215032,
        flag_4=11210900,
    )
    Event_11210900(0, character=Characters.c4090_0001)
    Event_11210900(1, character=Characters.c4090_0002)
    Event_11210905(
        0,
        character=Characters.c4090_0001,
        flag=11215035,
        destination=1212080,
        set_draw_parent=Collisions.h0105B1,
        flag_1=11210900,
        flag_2=11215032,
    )
    Event_11210905(
        1,
        character=Characters.c4090_0002,
        flag=11215036,
        destination=1212082,
        set_draw_parent=Collisions.h0103B1,
        flag_1=11210901,
        flag_2=11215033,
    )
    Event_11210510(0, character=Characters.c4110_0000, flag=1822)
    Event_11210520(0, character=Characters.c4110_0000, first_flag=1820, last_flag=1839, flag=1823)
    Event_11210530(0, character=Characters.c4110_0000, first_flag=1820, last_flag=1839, flag=1821)
    Event_11210535()
    Event_11210910()
    Event_11210912()
    Event_11210915()
    if FlagEnabled(1842):
        DisableObject(Objects.o2253)
        DeleteVFX(VFX.ChesterCandlestick, erase_root_only=False)
    Event_11210510(1, character=Characters.c4090_0000, flag=1841)
    Event_11210520(1, character=Characters.c4090_0000, first_flag=1840, last_flag=1859, flag=1842)
    Event_11210544()
    Event_11210538()
    Event_11210520(2, character=Characters.c4140_0000, first_flag=1870, last_flag=1889, flag=1872)
    if FlagDisabled(Flags.ArtoriasDead):
        DisableObject(Objects.o2760_0000)
    OR_1.Add(FlagEnabled(1861))
    OR_1.Add(FlagEnabled(CommonFlags.CiaranGivenSoul))
    SkipLinesIfConditionTrue(1, OR_1)
    DisableCharacter(Characters.c0000_0013)
    Event_11210510(3, character=Characters.c0000_0013, flag=1863)
    Event_11210520(3, character=Characters.c0000_0013, first_flag=1860, last_flag=1869, flag=CommonFlags.CiaranDead)
    Event_11210531(0, character=Characters.c0000_0013, first_flag=1860, last_flag=1869, flag=1861)
    Event_11210532(
        0,
        character=Characters.c0000_0013,
        first_flag=1860,
        last_flag=1869,
        flag=CommonFlags.CiaranGivenSoul,
    )
    Event_11210533(0, character=Characters.c0000_0013, first_flag=1860, last_flag=1869, flag=1865)
    Event_11210534(0, character=Characters.c0000_0013, first_flag=1860, last_flag=1869, flag=1865)
    Event_11210543()
    DisableCharacter(Characters.c0000_0006)
    SkipLinesIfClient(3)
    Event_11210540()
    Event_11210541()
    Event_11210542()
    if FlagDisabled(11210345):
        DisableFlagRange((11210340, 11210345))
    DisableGravity(Characters.c4531_0000)
    EnableImmortality(Characters.c4531_0000)
    DisableHealthBar(Characters.c4531_0000)
    AddSpecialEffect(Characters.c4531_0000, 5300)
    EnableObjectInvulnerability(Objects.o2621_0000)
    Event_11210340()
    Event_11210341()
    Event_11210345()
    Event_11210346()
    Event_11210347()
    EndOfAnimation(obj=Objects.o0110_0006, animation_id=0)
    EndOfAnimation(obj=Objects.o0110_0007, animation_id=0)
    Event_11217000()
    Event_11210015()


@ContinueOnRest(11210992)
def Event_11210992():
    """Event 11210992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c3471_0000, 7101)
    AddSpecialEffect(Characters.c3471_0001, 7101)
    AddSpecialEffect(Characters.c3471_0002, 7101)
    AddSpecialEffect(Characters.c4100_0000, 7101)
    AddSpecialEffect(Characters.c4500_0000, 7101)
    AddSpecialEffect(Characters.c4510_0000, 7101)
    AddSpecialEffect(Characters.c4510_0001, 7101)
    AddSpecialEffect(Characters.c4090_0001, 7100)
    AddSpecialEffect(Characters.c4090_0002, 7100)
    AddSpecialEffect(Characters.c4110_0000, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c3471_0000, 7101)
    RemoveSpecialEffect(Characters.c3471_0001, 7101)
    RemoveSpecialEffect(Characters.c3471_0002, 7101)
    RemoveSpecialEffect(Characters.c4100_0000, 7101)
    RemoveSpecialEffect(Characters.c4500_0000, 7101)
    RemoveSpecialEffect(Characters.c4510_0000, 7101)
    RemoveSpecialEffect(Characters.c4510_0001, 7101)
    RemoveSpecialEffect(Characters.c4090_0001, 7100)
    RemoveSpecialEffect(Characters.c4090_0002, 7100)
    RemoveSpecialEffect(Characters.c4110_0000, 7100)
    Restart()


@RestartOnRest(11210999)
def Event_11210999(_, character: Character | int, item_lot: int):
    """Event 11210999"""
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


@ContinueOnRest(11210090)
def Event_11210090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11210090"""
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


@RestartOnRest(11215090)
def Event_11215090():
    """Event 11215090"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c4120_0011)
        DisableCharacter(Characters.c4120_0012)
        DisableCharacter(Characters.c4120_0013)
        DisableCharacter(1210903)
        DisableCharacter(1210904)
        DisableCharacter(Characters.c4130_0039)
        DisableCharacter(Characters.c4130_0040)
        DisableCharacter(Characters.c4130_0041)
        DisableCharacter(Characters.c4130_0042)
        DisableCharacter(1210909)
        DisableCharacter(1210910)
        DisableCharacter(1210911)
        DisableCharacter(Characters.c4130_0046)
        DisableCharacter(Characters.c4130_0047)
        DisableCharacter(Characters.c4130_0048)
        DisableCharacter(Characters.c4130_0049)
        DisableCharacter(Characters.c4150_0028)
        DisableCharacter(Characters.c4150_0029)
        DisableCharacter(Characters.c4160_0012)
        DisableCharacter(1210919)
        DisableCharacter(Characters.c4150_0030)
        DisableCharacter(Characters.c4160_0015)
        DisableCharacter(Characters.c4180_0003)
        DisableCharacter(1210923)
        DisableCharacter(Characters.c4180_0006)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11215091)
def Event_11215091():
    """Event 11215091"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c4120_0011)
    Kill(Characters.c4120_0012)
    Kill(Characters.c4120_0013)
    Kill(1210903)
    Kill(1210904)
    Kill(Characters.c4130_0039)
    Kill(Characters.c4130_0040)
    Kill(Characters.c4130_0041)
    Kill(Characters.c4130_0042)
    Kill(1210909)
    Kill(1210910)
    Kill(1210911)
    Kill(Characters.c4130_0046)
    Kill(Characters.c4130_0047)
    Kill(Characters.c4130_0048)
    Kill(Characters.c4130_0049)
    Kill(Characters.c4150_0028)
    Kill(Characters.c4150_0029)
    Kill(Characters.c4160_0012)
    Kill(1210919)
    Kill(Characters.c4150_0030)
    Kill(Characters.c4160_0015)
    Kill(Characters.c4180_0003)
    Kill(1210923)
    Kill(Characters.c4180_0006)


@RestartOnRest(11215092)
def Event_11215092():
    """Event 11215092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=OOLACILE))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11210080))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=OOLACILE))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11210080))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=OOLACILE))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11210080))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=OOLACILE))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11210080))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=OOLACILE))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11210080))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=OOLACILE))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11210080))
    if not OR_6:
        return RESTART
    EnableFlag(11210080)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=OOLACILE))
    if not AND_7:
        return RESTART
    DisableFlag(11210080)
    EnableFlag(11215095)


@RestartOnRest(11215000)
def Event_11215000():
    """Event 11215000"""
    AND_1.Add(FlagDisabled(Flags.SanctuaryGuardianDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212888,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1211790,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212887)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@ContinueOnRest(11215001)
def Event_11215001():
    """Event 11215001"""
    AND_1.Add(FlagDisabled(Flags.SanctuaryGuardianDead))
    AND_1.Add(FlagEnabled(11215003))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212888,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211790,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212887)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11215002)
def Event_11215002():
    """Event 11215002"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(Flags.SanctuaryGuardianDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1212886))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c3471_0000, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c3471_0000)


@RestartOnRest(11215003)
def Event_11215003():
    """Event 11215003"""
    if ThisEventFlagDisabled():
        DisableAI(Characters.c3471_0000)
        AND_1.Add(FlagEnabled(11215002))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1212886))
    
        MAIN.Await(AND_1)
    
        EnableAI(Characters.c3471_0000)
    EnableBossHealthBar(Characters.c3471_0000, name=3471)
    ForceAnimation(Characters.c3471_0000, 3017, wait_for_completion=True)


@ContinueOnRest(11215004)
def Event_11215004():
    """Event 11215004"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(Flags.SanctuaryGuardianDead))
    AND_1.Add(FlagEnabled(11215003))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11215001))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212886))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.SanctuaryGuardianMusic)


@ContinueOnRest(11215005)
def Event_11215005():
    """Event 11215005"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215004))
    AND_1.Add(FlagEnabled(Flags.SanctuaryGuardianDead))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.SanctuaryGuardianMusic)


@RestartOnRest(Flags.SanctuaryGuardianDead)
def Event_11210000():
    """Event 11210000"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3471_0000)
        Kill(Characters.c3471_0000)
        DisableCharacter(Characters.c3472_0000)
        Kill(Characters.c3472_0000)
        End()
    
    MAIN.Await(HealthRatio(Characters.c3471_0000) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(Characters.c3471_0000, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.c3471_0000))
    
    EnableFlag(Flags.SanctuaryGuardianDead)
    KillBoss(game_area_param_id=1210800)
    DisableObject(Objects.o2909_0001)
    DeleteVFX(VFX.SanctuaryGuardianEntranceFog)
    DisableObject(Objects.o2910_0001)
    DeleteVFX(VFX.SanctuaryGuardianExitFog)


@RestartOnRest(11215006)
def Event_11215006(_, character: int, character_1: int, item_lot: int):
    """Event 11215006"""
    DisableCharacter(character)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(character_1, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(character_1, bit_index=1, switch_type=OnOffChange.Off)
        AICommand(character_1, command_id=20, command_slot=0)
        End()
    if FlagDisabled(Flags.SanctuaryGuardianDead):
        AND_1.Add(FlagEnabled(11215002))
    AND_1.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(character_1, npc_part_id=3471, part_index=NPCPartType.Part1, part_health=200)
    AND_2.Add(CharacterPartHealth(character_1, npc_part_id=3471) <= 0)
    AND_3.Add(HealthRatio(character_1) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    Move(
        character,
        destination=character_1,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=character_1,
    )
    EnableCharacter(character)
    ResetAnimation(character_1)
    ForceAnimation(character_1, 8000)
    ForceAnimation(character, 8100)
    SetDisplayMask(character_1, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character_1, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(character_1, command_id=20, command_slot=0)
    ReplanAI(character_1)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@RestartOnRest(11215008)
def Event_11215008():
    """Event 11215008"""
    MAIN.Await(FlagEnabled(11215007))
    
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0037B1))
    OR_2.Add(PlayerStandingOnCollision(Collisions.h0070B1))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212003))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=OR_1)
    SetNest(Characters.c3471_0001, region=1212010)
    SetNest(Characters.c3471_0002, region=1212011)
    SkipLines(2)
    SetNest(Characters.c3471_0001, region=1212007)
    SetNest(Characters.c3471_0002, region=1212008)
    AICommand(Characters.c3471_0001, command_id=10, command_slot=1)
    AICommand(Characters.c3471_0002, command_id=10, command_slot=1)
    OR_2.Add(PlayerStandingOnCollision(Collisions.h0037B1))
    OR_2.Add(PlayerStandingOnCollision(Collisions.h0070B1))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212003))
    
    MAIN.Await(not OR_2)
    
    AICommand(Characters.c3471_0001, command_id=-1, command_slot=1)
    AICommand(Characters.c3471_0002, command_id=-1, command_slot=1)
    Restart()


@RestartOnRest(11215007)
def Event_11215007():
    """Event 11215007"""
    MAIN.Await(FlagEnabled(Flags.ArtoriasDead))
    
    DisableAI(Characters.c3471_0001)
    DisableAI(Characters.c3471_0002)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212004))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1212001))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1212002))
    OR_1.Add(AND_1)
    OR_1.Add(Attacked(attacked_entity=Characters.c3471_0001, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c3471_0002, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.c3471_0001)
    ForceAnimation(Characters.c3471_0001, 3017)
    WaitFrames(frames=15)
    EnableAI(Characters.c3471_0002)
    ForceAnimation(Characters.c3471_0002, 3017)
    WaitFrames(frames=15)
    ReplanAI(Characters.c3471_0001)
    ReplanAI(Characters.c3471_0002)


@RestartOnRest(11215009)
def Event_11215009():
    """Event 11215009"""
    MAIN.Await(FlagEnabled(Flags.ArtoriasDead))
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212006))
    
    Move(
        Characters.c3471_0001,
        destination=1212007,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    Move(
        Characters.c3471_0002,
        destination=1212008,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0001, region=1212007)
    SetNest(Characters.c3471_0002, region=1212008)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212009))
    
    Move(
        Characters.c3471_0001,
        destination=1212010,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    Move(
        Characters.c3471_0002,
        destination=1212011,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0001, region=1212010)
    SetNest(Characters.c3471_0002, region=1212011)
    Restart()


@ContinueOnRest(11217000)
def Event_11217000():
    """Event 11217000"""
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212005))
    AND_4.Add(CharacterOutsideRegion(PLAYER, region=1212005))
    if AND_4:
        return
    AND_1.Add(CharacterDead(Characters.c3471_0001))
    AND_2.Add(CharacterDead(Characters.c3471_0002))
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    Move(
        Characters.c3471_0001,
        destination=1212007,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0001, region=1212007)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(
        Characters.c3471_0002,
        destination=1212008,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c3471_0000,
    )
    SetNest(Characters.c3471_0002, region=1212008)


@RestartOnRest(11215010)
def Event_11215010():
    """Event 11215010"""
    AND_1.Add(FlagDisabled(Flags.ArtoriasDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1211890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@ContinueOnRest(11215011)
def Event_11215011():
    """Event 11215011"""
    AND_1.Add(FlagDisabled(Flags.ArtoriasDead))
    AND_1.Add(FlagEnabled(11215013))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11215012)
def Event_11215012():
    """Event 11215012"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(Flags.ArtoriasDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1212896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c4100_0000, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c4100_0000)
    EnableFlag(11210537)


@RestartOnRest(11215013)
def Event_11215013():
    """Event 11215013"""
    if FlagEnabled(Flags.ArtoriasDead):
        DisableCharacter(Characters.c4100_0000)
        Kill(Characters.c4100_0000)
        End()
    if FlagDisabled(11210030):
        DisableCharacter(Characters.c4100_0000)
        DisableObject(Objects.o2800_0000)
        DisableObject(Objects.o2801_0000)
    DisableAI(Characters.c4100_0000)
    SkipLinesIfThisEventFlagEnabled(11)
    AND_1.Add(FlagEnabled(11215012))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212896))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(9, 11210030)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120110, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(120110, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableObject(Objects.o2800_0000)
    EnableObject(Objects.o2801_0000)
    EnableCharacter(Characters.c4100_0000)
    EnableFlag(11210030)
    EnableAI(Characters.c4100_0000)
    EnableBossHealthBar(Characters.c4100_0000, name=4100)
    EnableMapCollision(collision=Collisions.h7400B1)


@ContinueOnRest(11215014)
def Event_11215014():
    """Event 11215014"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(Flags.ArtoriasDead))
    AND_1.Add(FlagEnabled(11215013))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11215011))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212896))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.ArtoriasMusic)


@ContinueOnRest(11215015)
def Event_11215015():
    """Event 11215015"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215014))
    AND_1.Add(FlagEnabled(Flags.ArtoriasDead))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.ArtoriasMusic)


@RestartOnRest(Flags.ArtoriasDead)
def Event_11210001():
    """Event 11210001"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c4100_0000)
        Kill(Characters.c4100_0000)
        DisableBackread(Characters.c4100_0000)
        EnableCharacter(Characters.c3471_0001)
        EnableCharacter(Characters.c3471_0002)
        End()
    DisableBackread(Characters.c4110_0000)
    DisableCharacter(Characters.c3471_0001)
    DisableCharacter(Characters.c3471_0002)
    
    MAIN.Await(HealthRatio(Characters.c4100_0000) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(Characters.c4100_0000, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.c4100_0000))
    
    EnableFlag(Flags.ArtoriasDead)
    EnableFlag(121)
    KillBoss(game_area_param_id=1210820)
    DisableFlag(11217060)
    DisableFlag(11217070)
    DisableFlag(11217080)
    DisableFlag(11217090)
    DisableObject(Objects.o2915_0000)
    DeleteVFX(VFX.ArtoriasEntranceFog)
    DisableObject(Objects.o2916_0000)
    DeleteVFX(VFX.ArtoriasExitFog)
    DisableMapCollision(collision=Collisions.h7400B1)
    Wait(17.0)
    DisableBackread(Characters.c4100_0000)
    EnableBackread(Characters.c4110_0000)
    EnableCharacter(Characters.c3471_0001)
    EnableCharacter(Characters.c3471_0002)


@ContinueOnRest(11210015)
def Event_11210015():
    """Event 11210015"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(Flags.ArtoriasDead))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.c4110_0000, radius=80.0))
    
    MAIN.Await(AND_1)
    
    DisableBackread(Characters.c4110_0000)
    AND_2.Add(FlagEnabled(Flags.ArtoriasDead))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.c4110_0000, radius=80.0))
    
    MAIN.Await(AND_2)
    
    EnableBackread(Characters.c4110_0000)
    Restart()


@RestartOnRest(11215020)
def Event_11215020():
    """Event 11215020"""
    AND_1.Add(FlagDisabled(Flags.ManusDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1211990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@ContinueOnRest(11215021)
def Event_11215021():
    """Event 11215021"""
    AND_1.Add(FlagDisabled(Flags.ManusDead))
    AND_1.Add(FlagEnabled(11215023))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11215022)
def Event_11215022():
    """Event 11215022"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(Flags.ManusDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1212996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c4500_0000, authority_level=UpdateAuthority.Forced)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    ActivateMultiplayerBuffs(Characters.c4500_0000)


@ContinueOnRest(11215027)
def Event_11215027():
    """Event 11215027"""
    AND_1.Add(FlagEnabled(11215020))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212996))
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120140, cutscene_flags=0, player_id=10000, move_to_region=1212022, game_map=OOLACILE)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120140,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1212022,
        game_map=OOLACILE,
    )
    SkipLines(1)
    PlayCutscene(120140, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11210031)


@RestartOnRest(11215026)
def Event_11215026():
    """Event 11215026"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212021))
    
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@RestartOnRest(11215023)
def Event_11215023():
    """Event 11215023"""
    if FlagEnabled(17):
        return
    if ThisEventFlagDisabled():
        DisableAI(Characters.c4500_0000)
    
        MAIN.Await(CharacterInsideRegion(PLAYER, region=1212021))
    
        EnableAI(Characters.c4500_0000)
    EnableBossHealthBar(Characters.c4500_0000, name=4500)


@ContinueOnRest(11215024)
def Event_11215024():
    """Event 11215024"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(Flags.ManusDead))
    AND_1.Add(FlagEnabled(11215023))
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(11215021))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212996))
    SkipLines(1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.ManusMusic)


@ContinueOnRest(11215025)
def Event_11215025():
    """Event 11215025"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215024))
    AND_1.Add(FlagEnabled(Flags.ManusDead))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.ManusMusic)


@ContinueOnRest(Flags.ManusDead)
def Event_11210002():
    """Event 11210002"""
    DisableObject(Objects.o0200_0003)
    DisableObject(Objects.o0200_0003)
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c4500_0000)
        Kill(Characters.c4500_0000)
        EnableObject(Objects.o0200_0003)
        End()
    
    MAIN.Await(HealthRatio(Characters.c4500_0000) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(Characters.c4500_0000, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.c4500_0000))
    
    EnableFlag(Flags.ManusDead)
    EnableFlag(17)
    KillBoss(game_area_param_id=1210840)
    DisableObject(Objects.o2911_0001)
    DeleteVFX(VFX.ManusEntranceFog)
    DeleteVFX(VFX.SifSummonSign)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=Objects.o0200_0003, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(Objects.o0200_0003)
    RegisterBonfire(bonfire_flag=11210992, obj=Objects.o0200_0003)


@ContinueOnRest(11215250)
def Event_11215250(_, obj: int, vfx_id: VFXEvent | int):
    """Event 11215250"""
    DeleteVFX(vfx_id, erase_root_only=False)
    if FlagEnabled(Flags.ManusDead):
        DisableObject(obj)
        End()
    OR_1.Add(ObjectDestroyed(obj))
    OR_1.Add(CharacterDead(Characters.c4500_0000))
    
    MAIN.Await(OR_1)
    
    DestroyObject(obj)
    ForceAnimation(obj, 0, wait_for_completion=True)
    DisableObject(obj)


@RestartOnRest(11215060)
def Event_11215060():
    """Event 11215060"""
    AND_1.Add(FlagEnabled(Flags.KalameetShotDown))
    AND_1.Add(FlagDisabled(Flags.KalameetDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212908,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1211690,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212907)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@ContinueOnRest(11215061)
def Event_11215061():
    """Event 11215061"""
    AND_1.Add(FlagEnabled(Flags.KalameetShotDown))
    AND_1.Add(FlagDisabled(Flags.KalameetDead))
    AND_1.Add(FlagEnabled(11215062))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212908,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211690,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1212907)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11215062)
def Event_11215062():
    """Event 11215062"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(Flags.KalameetShotDown))
        AND_1.Add(FlagDisabled(Flags.KalameetDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1212909))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c4510_0001, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c4510_0001)


@RestartOnRest(11215063)
def Event_11215063():
    """Event 11215063"""
    EnableInvincibility(Characters.c4510_0001)
    if ThisEventFlagDisabled():
        DisableAI(Characters.c4510_0001)
        AND_1.Add(FlagEnabled(11215062))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1212906))
        OR_1.Add(PlayerStandingOnCollision(Collisions.h0023B1))
        OR_1.Add(PlayerStandingOnCollision(Collisions.h0024B1))
        OR_1.Add(PlayerStandingOnCollision(Collisions.h0018B1))
        AND_1.Add(OR_1)
    
        MAIN.Await(AND_1)
    
        EnableAI(Characters.c4510_0001)
    DisableInvincibility(Characters.c4510_0001)
    EnableBossHealthBar(Characters.c4510_0001, name=4510)
    EnableMapCollision(collision=Collisions.h7400B1)


@ContinueOnRest(11215064)
def Event_11215064():
    """Event 11215064"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(Flags.KalameetDead))
    AND_1.Add(FlagEnabled(11215063))
    SkipLinesIfHost(2)
    AND_1.Add(FlagEnabled(11215061))
    AND_1.Add(FlagEnabled(11215067))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212900))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.KalameetMusic)


@ContinueOnRest(11215065)
def Event_11215065():
    """Event 11215065"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215064))
    AND_1.Add(FlagEnabled(Flags.KalameetDead))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.KalameetMusic)


@ContinueOnRest(11215066)
def Event_11215066():
    """Event 11215066"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(Flags.KalameetShotDown))
    AND_1.Add(FlagDisabled(Flags.KalameetDead))
    AND_1.Add(FlagEnabled(11215062))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1212908,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211690,
    ))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=75)
    EnableFlag(11215067)


@ContinueOnRest(11210005)
def Event_11210005():
    """Event 11210005"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(HealthRatio(Characters.c4510_0001) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(Characters.c4510_0001, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.c4510_0001))
    
    EnableFlag(Flags.KalameetDead)
    EnableFlag(11210005)
    EnableFlag(121)
    KillBoss(game_area_param_id=1210401)
    DisableObject(Objects.o2919_0000)
    DeleteVFX(VFX.KalameetEntranceFog)
    DisableMapCollision(collision=Collisions.h7400B1)


@ContinueOnRest(11210340)
def Event_11210340():
    """Event 11210340"""
    if ThisEventFlagEnabled():
        if FlagEnabled(11210341):
            return
        Move(
            Characters.c4531_0000,
            destination=1212331,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=Characters.c4531_0000,
        )
        End()
    AND_1.Add(Host())
    OR_1.Add(EntityWithinDistance(entity=Characters.c4531_0000, other_entity=PLAYER, radius=7.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c4531_0000, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation_Unknown_2003_46(
        entity=Characters.c4531_0000,
        animation=7003,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        unk1=5.0,
    )
    DisableCharacter(Characters.c4531_0000)
    Move(
        Characters.c4531_0000,
        destination=1212331,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c4531_0000,
    )
    EnableCharacter(Characters.c4531_0000)


@ContinueOnRest(11210341)
def Event_11210341():
    """Event 11210341"""
    if ThisEventSlotFlagEnabled():
        Move(
            Characters.c4531_0000,
            destination=1212332,
            destination_type=CoordEntityType.Region,
            copy_draw_parent=Characters.c4531_0000,
        )
        End()
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11210340))
    OR_1.Add(EntityWithinDistance(entity=Characters.c4531_0000, other_entity=PLAYER, radius=12.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c4531_0000, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation_Unknown_2003_46(
        entity=Characters.c4531_0000,
        animation=7003,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        unk1=5.0,
    )
    DisableCharacter(Characters.c4531_0000)
    Move(
        Characters.c4531_0000,
        destination=1212332,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c4531_0000,
    )
    EnableCharacter(Characters.c4531_0000)


@ContinueOnRest(11210345)
def Event_11210345():
    """Event 11210345"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c4531_0000)
        DeleteVFX(VFX.IllusoryFloorLandingAura, erase_root_only=False)
        End()
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11210341))
    OR_1.Add(EntityWithinDistance(entity=Characters.c4531_0000, other_entity=PLAYER, radius=12.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c4531_0000, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation_Unknown_2003_46(
        entity=Characters.c4531_0000,
        animation=7003,
        loop=False,
        wait_for_completion=True,
        skip_transition=False,
        unk1=5.0,
    )
    DisableCharacter(Characters.c4531_0000)
    DeleteVFX(VFX.IllusoryFloorLandingAura)


@ContinueOnRest(11210346)
def Event_11210346():
    """Event 11210346"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11210345))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212335))
    AND_2.Add(FlagEnabled(11210345))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    AddSpecialEffect(PLAYER, 4161)
    Restart()


@ContinueOnRest(11210347)
def Event_11210347():
    """Event 11210347"""
    SkipLinesIfFlagEnabled(1, 11215045)
    SkipLinesIfFlagDisabled(2, 11210345)
    DisableObject(Objects.o2621_0000)
    End()
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212336))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11215045)
    if ObjectDestroyed(Objects.o2621_0000):
        return
    DisableObjectInvulnerability(Objects.o2621_0000)
    DestroyObject(Objects.o2621_0000)
    ForceAnimation(Objects.o2621_0000, 0)
    PlaySoundEffect(Objects.o2621_0000, 262000000, sound_type=SoundType.o_Object)


@ContinueOnRest(11210025)
def Event_11210025():
    """Event 11210025"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o2620_0000)
        End()
    
    MAIN.Await(ObjectDestroyed(Objects.o2620_0000))
    
    End()


@RestartOnRest(11210310)
def Event_11210310(_, character: Character | int, flag: Flag | int):
    """Event 11210310"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    EnableFlag(flag)


@ContinueOnRest(11210330)
def Event_11210330(_, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210330"""
    MAIN.Await(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    
    EnableFlag(flag)


@ContinueOnRest(11210021)
def Event_11210021():
    """Event 11210021"""
    DisableAI(Characters.c4520_0002)
    EnableInvincibility(Characters.c4520_0002)
    if FlagEnabled(11210330):
        DisableCharacter(Characters.c4520_0002)
        DropMandatoryTreasure(Characters.c4520_0002)
        DeleteVFX(VFX.SifBarrier, erase_root_only=False)
        DisableObject(Objects.o2630_0000)
        End()
    
    MAIN.Await(FlagEnabled(11210330))
    
    Wait(6.0)
    ForceAnimation(Characters.c4520_0002, 7010, wait_for_completion=True)
    DisableCharacter(Characters.c4520_0002)
    DropMandatoryTreasure(Characters.c4520_0002)
    DeleteVFX(VFX.SifBarrier)
    DisableObject(Objects.o2630_0000)


@RestartOnRest(11215040)
def Event_11215040():
    """Event 11215040"""
    DisableAI(Characters.c4520_0000)
    DisableCharacter(Characters.c4520_0000)
    AND_1.Add(FlagDisabled(17))
    AND_1.Add(FlagEnabled(11210021))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=50000000,
        anchor_entity=1212300,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayBattlefieldMessage(140010, display_location_index=0)
    SkipLinesIfClient(1)
    ForceAnimation(Characters.c4520_0001, 7008)
    WaitFrames(frames=30)
    DisableCharacter(Characters.c4520_0001)
    EnableFlag(11215042)
    DeleteVFX(VFX.SifSummonSign)
    Wait(10.0)
    EnableCharacter(Characters.c4520_0000)
    EnableAI(Characters.c4520_0000)
    SetTeamType(Characters.c4520_0000, TeamType.WhitePhantom)
    ForceAnimation(Characters.c4520_0000, 7004)
    SkipLinesIfClient(2)
    DisplayBattlefieldMessage(20001110, display_location_index=0)
    SkipLines(1)
    DisplayBattlefieldMessage(20001111, display_location_index=0)
    WaitFrames(frames=140)


@RestartOnRest(11215041)
def Event_11215041():
    """Event 11215041"""
    DisableCharacter(Characters.c4520_0001)
    DisableAI(Characters.c4520_0001)
    DisableAnimations(Characters.c4520_0001)
    if Client():
        return
    AND_1.Add(FlagEnabled(11210021))
    AND_1.Add(FlagDisabled(17))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212300))
    AND_1.Add(CharacterHuman(PLAYER))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11215042):
        return
    EnableCharacter(Characters.c4520_0001)
    ForceAnimation(Characters.c4520_0001, 7006, wait_for_completion=True)
    ForceAnimation(Characters.c4520_0001, 7007, loop=True)
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212300))
    AND_2.Add(FlagEnabled(11215020))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(Characters.c4520_0001, 7008, wait_for_completion=True)
    DisableCharacter(Characters.c4520_0001)
    Restart()


@RestartOnRest(11215044)
def Event_11215044():
    """Event 11215044"""
    DeleteVFX(VFX.SifSummonSign)
    if Client():
        return
    AND_1.Add(FlagDisabled(17))
    AND_1.Add(FlagEnabled(11210021))
    AND_1.Add(CharacterHuman(PLAYER))
    
    MAIN.Await(AND_1)
    
    CreateVFX(VFX.SifSummonSign)
    AND_2.Add(FlagDisabled(17))
    AND_2.Add(FlagEnabled(11210021))
    AND_2.Add(CharacterHuman(PLAYER))
    
    MAIN.Await(not AND_2)
    
    Restart()


@ContinueOnRest(11210020)
def Event_11210020():
    """Event 11210020"""
    if FlagEnabled(17):
        return
    AND_1.Add(CharacterDead(Characters.c4500_0000))
    AND_1.Add(CharacterAlive(Characters.c4520_0000))
    AND_1.Add(FlagEnabled(11215040))
    AND_2.Add(CharacterDead(Characters.c4520_0000))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_2)
    DisableAI(Characters.c4520_0000)
    WaitFrames(frames=120)
    ForceAnimation(Characters.c4520_0000, 7005, wait_for_completion=True)
    DisableCharacter(Characters.c4520_0000)
    End()
    DisplayBattlefieldMessage(20001115, display_location_index=0)


@RestartOnRest(11215043)
def Event_11215043():
    """Event 11215043"""
    if ThisEventFlagDisabled():
        MAIN.Await(HealthRatio(Characters.c4520_0000) <= 0.30000001192092896)
    AddSpecialEffect(Characters.c4520_0000, 5401)


@RestartOnRest(11215100)
def Event_11215100():
    """Event 11215100"""
    if ThisEventFlagEnabled():
        return
    DisableAI(Characters.c4130_0016)
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_3.Add(not AND_7)
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212502))
    OR_3.Add(AND_3)
    OR_3.Add(Attacked(attacked_entity=Characters.c4130_0016, attacker=PLAYER))
    AND_1.Add(OR_3)
    AND_2.Add(not AND_7)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212500))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(Characters.c4130_0016, cancel_animation=9060)
    EnableAI(Characters.c4130_0016)
    EndIfFinishedConditionTrue(input_condition=AND_1)
    SetNest(Characters.c4130_0016, region=1212501)
    AICommand(Characters.c4130_0016, command_id=10, command_slot=0)
    ReplanAI(Characters.c4130_0016)
    Wait(6.0)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212502))
    OR_2.Add(Attacked(attacked_entity=Characters.c4130_0016, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AICommand(Characters.c4130_0016, command_id=-1, command_slot=0)
    ReplanAI(Characters.c4130_0016)


@RestartOnRest(11215110)
def Event_11215110(_, character: int, region: Region | int, radius: float, region_1: Region | int):
    """Event 11215110"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_7)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11215115)
def Event_11215115(_, character: int, region: Region | int, region_1: Region | int):
    """Event 11215115"""
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    SetNest(character, region=region_1)


@RestartOnRest(11215120)
def Event_11215120(
    _,
    character: Character | int,
    character_1: Character | int,
    character_2: Character | int,
    flag: Flag | int,
):
    """Event 11215120"""
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(character)
        SetStandbyAnimationSettings(character_1)
        SetStandbyAnimationSettings(character_2)
        End()
    DisableAI(character)
    DisableAI(character_1)
    DisableAI(character_2)
    AND_1.Add(Host())
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character_1, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character_2, attacker=PLAYER))
    SkipLinesIfClient(2)
    if FlagDisabled(flag):
        AND_1.Add(FlagEnabled(flag))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    EnableAI(character)
    EnableAI(character_1)
    EnableAI(character_2)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    SetStandbyAnimationSettings(character_1, cancel_animation=9060)
    SetStandbyAnimationSettings(character_2, cancel_animation=9060)


@RestartOnRest(11215130)
def Event_11215130(_, character: Character | int, other_entity: int, radius: float, seconds: float):
    """Event 11215130"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    OR_1.Add(Attacked(attacked_entity=1210108, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=1210109, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=1210110, attacker=PLAYER))
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_7)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11215140)
def Event_11215140(
    _,
    character: int,
    region: Region | int,
    region_1: Region | int,
    region_2: Region | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 11215140"""
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_2.Add(CharacterInsideRegion(character, region=region_1))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_3.Add(CharacterInsideRegion(character, region=region_2))
    AND_3.Add(FlagDisabled(flag_2))
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_1)
    EnableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_2)
    DisableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_3)
    DisableFlag(flag)
    DisableFlag(flag_1)
    EnableFlag(flag_2)
    ResetAnimation(character)
    ForceAnimation(character, 7000, skip_transition=True)
    WaitFrames(frames=25)
    ForceAnimation(character, 9000, skip_transition=True)
    WaitFrames(frames=190)
    ForceAnimation(character, 9060)
    WaitFrames(frames=35)
    Restart()


@ContinueOnRest(11210600)
def Event_11210600(_, obj: Object | int, obj_act_id: int):
    """Event 11210600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11210350)
def Event_11210350(_, character: Character | int, item_lot: int):
    """Event 11210350"""
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


@RestartOnRest(11210150)
def Event_11210150():
    """Event 11210150"""
    if FlagEnabled(11210160):
        return
    Move(
        Characters.c4150_0026,
        destination=1212143,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0107B1,
    )
    Move(
        Characters.c4150_0026,
        destination=1212150,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0107B1,
    )
    SetNest(Characters.c4150_0026, region=1212150)


@ContinueOnRest(11210100)
def Event_11210100():
    """Event 11210100"""
    if FlagEnabled(11210101):
        EndOfAnimation(obj=Objects.o2700_0000, animation_id=0)
    if FlagDisabled(11210101):
        EndOfAnimation(obj=Objects.o2700_0000, animation_id=10)
    
    MAIN.Await(FlagEnabled(11210103))
    
    MAIN.Await(FlagDisabled(11215220))
    
    AND_1.Add(FlagDisabled(11210101))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212101))
    AND_2.Add(FlagEnabled(11210102))
    AND_2.Add(FlagEnabled(11210101))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212100))
    AND_3.Add(FlagEnabled(11210102))
    AND_3.Add(FlagDisabled(11210101))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212102))
    AND_4.Add(FlagEnabled(11210101))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212103))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215220)
    SkipLinesIfFinishedConditionTrue(26, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(25, input_condition=AND_4)
    EnableFlag(11210102)
    EnableFlag(11218102)
    SkipLinesIfFinishedConditionTrue(11, input_condition=AND_1)
    OR_2.Add(AllPlayersOutsideRegion(region=1212102))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212103))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    AND_7.Add(FlagDisabled(11218102))
    AND_7.Add(FlagDisabled(11218103))
    AND_7.Add(OR_2)
    
    MAIN.Await(AND_7)
    
    DisableFlag(11215220)
    Restart()
    OR_2.Add(AllPlayersOutsideRegion(region=1212100))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212103))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    AND_7.Add(FlagDisabled(11218102))
    AND_7.Add(FlagDisabled(11218103))
    AND_7.Add(OR_2)
    
    MAIN.Await(AND_7)
    
    DisableFlag(11215220)
    Restart()
    EnableFlag(11218103)
    SkipLinesIfFinishedConditionTrue(11, input_condition=AND_2)
    OR_3.Add(AllPlayersOutsideRegion(region=1212103))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212102))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    AND_8.Add(FlagDisabled(11218102))
    AND_8.Add(FlagDisabled(11218103))
    AND_8.Add(OR_3)
    
    MAIN.Await(AND_8)
    
    DisableFlag(11215220)
    Restart()
    OR_3.Add(AllPlayersOutsideRegion(region=1212101))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212102))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    AND_8.Add(FlagDisabled(11218102))
    AND_8.Add(FlagDisabled(11218103))
    AND_8.Add(OR_3)
    
    MAIN.Await(AND_8)
    
    DisableFlag(11215220)
    Restart()


@ContinueOnRest(11219100)
def Event_11219100(_, flag: Flag | int, obj: int, animation_id: int, state: uchar, anchor_entity: int):
    """Event 11219100"""
    MAIN.Await(FlagEnabled(flag))
    
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=anchor_entity, model_point=101, anchor_type=CoordEntityType.Object)
    SetFlagState(11210101, state)
    CreateObjectVFX(obj, vfx_id=191, model_point=120029)
    ForceAnimation(obj, animation_id)
    WaitFrames(frames=180)
    DeleteObjectVFX(obj, erase_root=False)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(11210103)
def Event_11210103():
    """Event 11210103"""
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_7)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212104))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11210103)


@ContinueOnRest(11210110)
def Event_11210110():
    """Event 11210110"""
    if FlagEnabled(11210111):
        EndOfAnimation(obj=Objects.o2700_0001, animation_id=11)
    if FlagDisabled(11210111):
        EndOfAnimation(obj=Objects.o2700_0001, animation_id=1)
    
    MAIN.Await(FlagDisabled(11215221))
    
    AND_1.Add(FlagEnabled(11210111))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212111))
    AND_2.Add(FlagDisabled(11210111))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212110))
    AND_3.Add(FlagEnabled(11210111))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212112))
    AND_4.Add(FlagDisabled(11210111))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212113))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215221)
    SkipLinesIfFinishedConditionTrue(24, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(23, input_condition=AND_4)
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0011,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    DisableFlag(11210111)
    CreateObjectVFX(Objects.o2700_0001, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0001, 1)
    WaitFrames(frames=140)
    DeleteObjectVFX(Objects.o2700_0001, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_1)
    OR_2.Add(AllPlayersOutsideRegion(region=1212112))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212113))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215221)
    Restart()
    OR_2.Add(AllPlayersOutsideRegion(region=1212110))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212113))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215221)
    Restart()
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0001,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    EnableFlag(11210111)
    CreateObjectVFX(Objects.o2700_0001, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0001, 11)
    WaitFrames(frames=140)
    DeleteObjectVFX(Objects.o2700_0001, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    OR_3.Add(AllPlayersOutsideRegion(region=1212113))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212112))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215221)
    Restart()
    OR_3.Add(AllPlayersOutsideRegion(region=1212111))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212112))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215221)
    Restart()


@ContinueOnRest(11210120)
def Event_11210120():
    """Event 11210120"""
    if FlagEnabled(11210121):
        EndOfAnimation(obj=Objects.o2700_0002, animation_id=2)
    if FlagDisabled(11210121):
        EndOfAnimation(obj=Objects.o2700_0002, animation_id=12)
    
    MAIN.Await(FlagEnabled(11210123))
    
    MAIN.Await(FlagDisabled(11215222))
    
    AND_1.Add(FlagDisabled(11210121))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212121))
    AND_2.Add(FlagEnabled(11210122))
    AND_2.Add(FlagEnabled(11210121))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212120))
    AND_3.Add(FlagEnabled(11210122))
    AND_3.Add(FlagDisabled(11210121))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212122))
    AND_4.Add(FlagEnabled(11210121))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212123))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215222)
    SkipLinesIfFinishedConditionTrue(25, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(24, input_condition=AND_4)
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0012,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    EnableFlag(11210121)
    EnableFlag(11210122)
    CreateObjectVFX(Objects.o2700_0002, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0002, 2)
    WaitFrames(frames=140)
    DeleteObjectVFX(Objects.o2700_0002, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_1)
    OR_2.Add(AllPlayersOutsideRegion(region=1212122))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212123))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215222)
    Restart()
    OR_2.Add(AllPlayersOutsideRegion(region=1212120))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212123))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215222)
    Restart()
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0002,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    DisableFlag(11210121)
    CreateObjectVFX(Objects.o2700_0002, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0002, 12)
    WaitFrames(frames=140)
    DeleteObjectVFX(Objects.o2700_0002, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    OR_3.Add(AllPlayersOutsideRegion(region=1212123))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212122))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215222)
    Restart()
    OR_3.Add(AllPlayersOutsideRegion(region=1212121))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212122))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215222)
    Restart()


@ContinueOnRest(11210123)
def Event_11210123():
    """Event 11210123"""
    AND_7.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_7)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212124))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11210123)


@ContinueOnRest(11210130)
def Event_11210130():
    """Event 11210130"""
    if FlagEnabled(11210131):
        EndOfAnimation(obj=Objects.o2700_0003, animation_id=3)
    if FlagDisabled(11210131):
        EndOfAnimation(obj=Objects.o2700_0003, animation_id=13)
    
    MAIN.Await(FlagEnabled(11210133))
    
    MAIN.Await(FlagDisabled(11215223))
    
    AND_1.Add(FlagDisabled(11210131))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212131))
    AND_2.Add(FlagEnabled(11210132))
    AND_2.Add(FlagEnabled(11210131))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212130))
    AND_3.Add(FlagEnabled(11210132))
    AND_3.Add(FlagDisabled(11210131))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212132))
    AND_4.Add(FlagEnabled(11210131))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212133))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215223)
    SkipLinesIfFinishedConditionTrue(25, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(24, input_condition=AND_4)
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0013,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    EnableFlag(11210131)
    EnableFlag(11210132)
    CreateObjectVFX(Objects.o2700_0003, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0003, 3)
    WaitFrames(frames=240)
    DeleteObjectVFX(Objects.o2700_0003, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_1)
    OR_2.Add(AllPlayersOutsideRegion(region=1212132))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212133))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215223)
    Restart()
    OR_2.Add(AllPlayersOutsideRegion(region=1212130))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212133))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215223)
    Restart()
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0003,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    DisableFlag(11210131)
    CreateObjectVFX(Objects.o2700_0003, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0003, 13)
    WaitFrames(frames=240)
    DeleteObjectVFX(Objects.o2700_0003, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    OR_3.Add(AllPlayersOutsideRegion(region=1212133))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212132))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215223)
    Restart()
    OR_3.Add(AllPlayersOutsideRegion(region=1212131))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212132))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215223)
    Restart()


@ContinueOnRest(11210133)
def Event_11210133():
    """Event 11210133"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212134))
    
    EnableFlag(11210133)


@ContinueOnRest(11210140)
def Event_11210140():
    """Event 11210140"""
    if FlagEnabled(11210141):
        EndOfAnimation(obj=Objects.o2700_0004, animation_id=4)
    if FlagDisabled(11210141):
        EndOfAnimation(obj=Objects.o2700_0004, animation_id=14)
    
    MAIN.Await(FlagDisabled(11215224))
    
    AND_1.Add(FlagDisabled(11210141))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212141))
    AND_2.Add(FlagEnabled(11210141))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212140))
    AND_3.Add(FlagDisabled(11210141))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212142))
    AND_4.Add(FlagEnabled(11210141))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1212143))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215224)
    EnableFlag(11210160)
    SkipLinesIfFinishedConditionTrue(24, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(23, input_condition=AND_4)
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0014,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    EnableFlag(11210141)
    CreateObjectVFX(Objects.o2700_0004, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0004, 4)
    WaitFrames(frames=180)
    DeleteObjectVFX(Objects.o2700_0004, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_1)
    OR_2.Add(AllPlayersOutsideRegion(region=1212142))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212143))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215224)
    Restart()
    OR_2.Add(AllPlayersOutsideRegion(region=1212140))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1212143))
    AND_5.Add(Host())
    AND_5.Add(TimeElapsed(seconds=1.0))
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    DisableFlag(11215224)
    Restart()
    CreateTemporaryVFX(
        vfx_id=120030,
        anchor_entity=Objects.o2701_0004,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    DisableFlag(11210141)
    CreateObjectVFX(Objects.o2700_0004, vfx_id=191, model_point=120029)
    ForceAnimation(Objects.o2700_0004, 14)
    WaitFrames(frames=180)
    DeleteObjectVFX(Objects.o2700_0004, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    OR_3.Add(AllPlayersOutsideRegion(region=1212143))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212142))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215224)
    Restart()
    OR_3.Add(AllPlayersOutsideRegion(region=1212141))
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1212142))
    AND_6.Add(Host())
    AND_6.Add(TimeElapsed(seconds=1.0))
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    DisableFlag(11215224)
    Restart()


@ContinueOnRest(11210170)
def Event_11210170(_, left: Flag | int, collision: Collision | int, region: Region | int):
    """Event 11210170"""
    DisableMapCollision(collision=collision)
    if ValueEqual(left=left, right=11215220):
        AND_1.Add(AllPlayersOutsideRegion(region=1212100))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(FlagEnabled(left))
    
    MAIN.Await(AND_1)
    
    EnableMapCollision(collision=collision)
    if ValueEqual(left=left, right=11215220):
        AND_7.Add(CharacterInsideRegion(PLAYER, region=1212100))
        AND_7.Add(TimeElapsed(seconds=2.0))
        OR_1.Add(AND_7)
    OR_1.Add(AllPlayersOutsideRegion(region=region))
    OR_1.Add(FlagDisabled(left))
    
    MAIN.Await(OR_1)
    
    Wait(5.0)
    Restart()


@ContinueOnRest(11210300)
def Event_11210300():
    """Event 11210300"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=11210650))
    
    EnableFlag(11210650)
    DisplayDialog(text=10010884, anchor_entity=Objects.o2720_0000, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11210050)
def Event_11210050():
    """Event 11210050"""
    DisableGravity(Characters.c4510_0000)
    EnableInvincibility(Characters.c4510_0000)
    DisableCharacterCollision(Characters.c4510_0000)
    DisableCharacter(Characters.c4510_0000)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c4510_0000, authority_level=UpdateAuthority.Forced)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212050))
    
    EnableFlag(11210050)
    SetNetworkUpdateRate(Characters.c4510_0000, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(Characters.c4510_0000)
    Move(
        Characters.c4510_0000,
        destination=1212051,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0066B1,
    )
    ForceAnimation(Characters.c4510_0000, 7000)
    WaitFrames(frames=420)
    DisableCharacter(Characters.c4510_0000)


@RestartOnRest(11210051)
def Event_11210051():
    """Event 11210051"""
    DisableAI(Characters.c4510_0002)
    EnableImmortality(Characters.c4510_0002)
    DisableGravity(Characters.c4510_0002)
    DisableCharacterCollision(Characters.c4510_0002)
    if ThisEventFlagDisabled():
        DisableCharacter(Characters.c4510_0002)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c4510_0002, authority_level=UpdateAuthority.Forced)
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212052))
    AND_1.Add(FlagDisabled(11210535))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(Characters.c4510_0002, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(Characters.c4510_0002)
    ForceAnimation(Characters.c4510_0002, 7006, skip_transition=True)
    WaitFrames(frames=240)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    EnableFlag(11210062)
    EnableFlag(11210069)
    End()


@RestartOnRest(11210052)
def Event_11210052():
    """Event 11210052"""
    if FlagEnabled(11210535):
        DisableFlagRange((11210063, 11210067))
        DisableCharacter(Characters.c4510_0002)
        End()
    DisableFlagRange((11210070, 11210073))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11210070, 11210073))
    EnableFlag(11210068)
    AND_1.Add(HealthRatio(Characters.c4510_0002) <= 0.009999999776482582)
    AND_1.Add(FlagEnabled(11210062))
    AND_1.Add(FlagDisabled(11210535))
    AND_1.Add(FlagDisabled(11210067))
    OR_2.Add(FlagEnabled(11215056))
    OR_2.Add(FlagEnabled(11215058))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(11210062))
    AND_2.Add(FlagDisabled(11210535))
    AND_2.Add(FlagDisabled(11210067))
    OR_3.Add(FlagEnabled(11215055))
    OR_3.Add(FlagEnabled(11215057))
    AND_3.Add(OR_3)
    AND_3.Add(FlagEnabled(11210062))
    AND_3.Add(FlagDisabled(11210535))
    AND_3.Add(FlagDisabled(11210067))
    AND_4.Add(not AND_1)
    AND_4.Add(not AND_2)
    AND_4.Add(not AND_3)
    AND_4.Add(FlagEnabled(11210062))
    AND_4.Add(FlagDisabled(11210535))
    AND_4.Add(FlagDisabled(11210067))
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(AND_3)
    OR_5.Add(AND_4)
    
    MAIN.Await(OR_5)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(6, input_condition=AND_4)
    EnableFlag(11210063)
    SkipLines(5)
    EnableFlag(11210065)
    SkipLines(3)
    EnableFlag(11210064)
    SkipLines(1)
    EnableFlag(11210066)
    EnableFlag(11210067)
    Restart()


@RestartOnRest(11210053)
def Event_11210053():
    """Event 11210053"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c4510_0001)
        DisableCharacter(Characters.c4510_0002)
        End()
    AND_1.Add(FlagEnabled(11210063))
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Characters.c4510_0002, 7004, skip_transition=True)
    WaitFrames(frames=176)
    DisableCharacter(Characters.c4510_0002)
    Kill(Characters.c4510_0002, award_souls=True)


@RestartOnRest(11210054)
def Event_11210054():
    """Event 11210054"""
    AND_1.Add(FlagDisabled(11210065))
    AND_1.Add(FlagEnabled(11210064))
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11210069):
        ForceAnimation(Characters.c4510_0002, 7010, skip_transition=True)
        WaitFrames(frames=561)
    else:
        ForceAnimation(Characters.c4510_0002, 7002, skip_transition=True)
        WaitFrames(frames=461)
    AND_2.Add(HealthRatio(Characters.c4510_0002) <= 0.009999999776482582)
    SkipLinesIfConditionTrue(26, AND_2)
    SkipLinesIfFlagEnabled(3, 11210070)
    SkipLinesIfFlagEnabled(7, 11210071)
    SkipLinesIfFlagEnabled(12, 11210072)
    SkipLinesIfFlagEnabled(17, 11210073)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7001, skip_transition=True)
    WaitFrames(frames=269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    WaitFrames(frames=60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    WaitFrames(frames=120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    WaitFrames(frames=180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210064)
    Restart()


@RestartOnRest(11210055)
def Event_11210055():
    """Event 11210055"""
    AND_1.Add(FlagEnabled(11210065))
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11210069):
        ForceAnimation(Characters.c4510_0002, 7011, skip_transition=True)
        WaitFrames(frames=514)
    else:
        ForceAnimation(Characters.c4510_0002, 7003, skip_transition=True)
        WaitFrames(frames=414)
    AND_2.Add(HealthRatio(Characters.c4510_0002) <= 0.009999999776482582)
    SkipLinesIfConditionTrue(26, AND_2)
    SkipLinesIfFlagEnabled(3, 11210070)
    SkipLinesIfFlagEnabled(7, 11210071)
    SkipLinesIfFlagEnabled(12, 11210072)
    SkipLinesIfFlagEnabled(17, 11210073)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7001, skip_transition=True)
    WaitFrames(frames=269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    WaitFrames(frames=60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    WaitFrames(frames=120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(frames=6)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=194)
    WaitFrames(frames=180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210065)
    Restart()


@RestartOnRest(11210056)
def Event_11210056():
    """Event 11210056"""
    AND_1.Add(FlagDisabled(11210064))
    AND_1.Add(FlagDisabled(11210065))
    AND_1.Add(FlagEnabled(11210066))
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagDisabled(11, 11210069)
    ForceAnimation(Characters.c4510_0002, 7009, skip_transition=True)
    WaitFrames(frames=30)
    SkipLinesIfFlagEnabled(1, 11210070)
    WaitFrames(frames=15)
    SkipLinesIfFlagEnabled(1, 11210071)
    WaitFrames(frames=30)
    SkipLinesIfFlagEnabled(1, 11210072)
    WaitFrames(frames=45)
    SkipLinesIfFlagEnabled(1, 11210073)
    WaitFrames(frames=60)
    SkipLines(11)
    ForceAnimation(Characters.c4510_0002, 7008, skip_transition=True)
    WaitFrames(frames=200)
    if FlagDisabled(11210070):
        WaitFrames(frames=15)
    if FlagDisabled(11210071):
        WaitFrames(frames=30)
    if FlagDisabled(11210072):
        WaitFrames(frames=45)
    if FlagDisabled(11210073):
        WaitFrames(frames=60)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210066)
    Restart()


@RestartOnRest(11210057)
def Event_11210057():
    """Event 11210057"""
    AND_1.Add(FlagEnabled(11210070))
    AND_1.Add(FlagEnabled(11210068))
    AND_2.Add(FlagEnabled(11210071))
    AND_2.Add(FlagEnabled(11210068))
    AND_3.Add(FlagEnabled(11210072))
    AND_3.Add(FlagEnabled(11210068))
    AND_4.Add(FlagEnabled(11210073))
    AND_4.Add(FlagEnabled(11210068))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(8, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(13, input_condition=AND_3)
    SkipLinesIfFinishedConditionTrue(18, input_condition=AND_4)
    EnableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    EnableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    EnableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    EnableFlag(11210073)
    DisableFlag(11210068)
    Restart()


@RestartOnRest(11210040)
def Event_11210040():
    """Event 11210040"""
    AND_1.Add(Host())
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212054))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212062))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11215055)
    AND_2.Add(Host())
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212054))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212062))
    
    MAIN.Await(AND_2)
    
    DisableFlag(11215055)
    Restart()


@RestartOnRest(11210041)
def Event_11210041():
    """Event 11210041"""
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212055))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11215056)
    AND_2.Add(Host())
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212055))
    
    MAIN.Await(AND_2)
    
    DisableFlag(11215056)
    Restart()


@RestartOnRest(11210042)
def Event_11210042():
    """Event 11210042"""
    AND_1.Add(Client())
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212054))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212062))
    AND_1.Add(OR_1)
    AND_1.Add(FramesElapsed(frames=30))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11215057)
    WaitFrames(frames=90)
    DisableFlag(11215057)
    Restart()


@RestartOnRest(11210043)
def Event_11210043():
    """Event 11210043"""
    AND_1.Add(Client())
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212055))
    AND_1.Add(FramesElapsed(frames=30))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11215058)
    WaitFrames(frames=90)
    DisableFlag(11215058)
    Restart()


@ContinueOnRest(Flags.KalameetDead)
def Event_11210004():
    """Event 11210004"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c4510_0001)
        End()
    OR_1.Add(CharacterDead(Characters.c4510_0001))
    OR_1.Add(CharacterDead(Characters.c4510_0002))
    
    MAIN.Await(OR_1)
    
    EnableFlag(Flags.KalameetDead)


@RestartOnRest(11215050)
def Event_11215050():
    """Event 11215050"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212057))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212059))
    AND_2.Add(AllPlayersOutsideRegion(region=1212057))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1212058))
    AND_3.Add(AllPlayersOutsideRegion(region=1212057))
    AND_3.Add(AllPlayersOutsideRegion(region=1212059))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_4.Add(OR_1)
    AND_4.Add(FlagEnabled(11215063))
    
    MAIN.Await(AND_4)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_2)
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_3)
    SetEventPoint(Characters.c4510_0001, region=1212060, reaction_range=2.0)
    SkipLines(3)
    SetEventPoint(Characters.c4510_0001, region=1212060, reaction_range=2.0)
    SkipLines(1)
    SetEventPoint(Characters.c4510_0001, region=1212061, reaction_range=2.0)
    Wait(1.0)
    Restart()


@RestartOnRest(11215051)
def Event_11215051():
    """Event 11215051"""
    DisableCharacter(Characters.c4511_0000)
    SkipLinesIfFlagEnabled(7, 11215054)
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SetDisplayMask(Characters.c4510_0001, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c4510_0001, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c4510_0001, command_id=20, command_slot=0)
    End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c4510_0001))
    
    CreateNPCPart(Characters.c4510_0001, npc_part_id=4510, part_index=NPCPartType.Part1, part_health=200)
    DisableFlag(11215054)
    AND_1.Add(CharacterPartHealth(Characters.c4510_0001, npc_part_id=4510) <= 0)
    AND_2.Add(HealthRatio(Characters.c4510_0001) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    if FlagEnabled(11215053):
        SetNPCPartHealth(Characters.c4510_0001, npc_part_id=4510, desired_health=10, overwrite_max=False)
        EnableFlag(11215054)
        Restart()
    Move(
        Characters.c4511_0000,
        destination=Characters.c4510_0001,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=Characters.c4510_0001,
    )
    EnableCharacter(Characters.c4511_0000)
    ResetAnimation(Characters.c4510_0001)
    ForceAnimation(Characters.c4510_0001, 8000)
    ForceAnimation(Characters.c4511_0000, 8100)
    SetDisplayMask(Characters.c4510_0001, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c4510_0001, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(Characters.c4510_0001, 5434)
    AICommand(Characters.c4510_0001, command_id=20, command_slot=0)
    ReplanAI(Characters.c4510_0001)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(45110000, host_only=True)


@RestartOnRest(11215052)
def Event_11215052():
    """Event 11215052"""
    MAIN.Await(CharacterHasTAEEvent(Characters.c4510_0001, tae_event_id=10))
    
    EnableFlag(11215053)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c4510_0001, tae_event_id=20))
    
    DisableFlag(11215053)
    Restart()


@RestartOnRest(11215160)
def Event_11215160(_, character: int):
    """Event 11215160"""
    AND_1.Add(HealthRatio(character) > 0.0)
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


@RestartOnRest(11215165)
def Event_11215165(_, character: int):
    """Event 11215165"""
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


@RestartOnRest(11215170)
def Event_11215170(_, character: Character | int):
    """Event 11215170"""
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


@RestartOnRest(11215175)
def Event_11215175(_, character: Character | int):
    """Event 11215175"""
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


@RestartOnRest(11215180)
def Event_11215180(_, character: int, region: int):
    """Event 11215180"""
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


@RestartOnRest(11210680)
def Event_11210680(_, character: Character | int):
    """Event 11210680"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@RestartOnRest(11215185)
def Event_11215185(_, character: int):
    """Event 11215185"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(character))
    if AND_1:
        return
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 0)
    ReplanAI(character)


@ContinueOnRest(11210200)
def Event_11210200(_, obj: int, region: Region | int):
    """Event 11210200"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 620))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 6950))
    OR_1.Add(SkullLanternActive())
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(obj, 262000000, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 1, wait_for_completion=True)
    DisableObject(obj)


@ContinueOnRest(11210205)
def Event_11210205(_, anchor_entity: int, region: Region | int, flag: Flag | int):
    """Event 11210205"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    if FlagEnabled(flag):
        return
    PlaySoundEffect(anchor_entity, 120199999, sound_type=SoundType.o_Object)
    Wait(2.0)
    Restart()


@ContinueOnRest(11210230)
def Event_11210230(_, obj: Object | int, obj_1: int, animation_id: int, animation_id_1: int):
    """Event 11210230"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj_1, animation_id=animation_id_1)
        PostDestruction(obj)
        EnableTreasure(obj=obj_1)
        End()
    DisableTreasure(obj=obj_1)
    SkipLinesIfClient(1)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=99005)
    ForceAnimation(obj_1, animation_id, loop=True)
    
    MAIN.Await(ObjectDestroyed(obj))
    
    ForceAnimation(obj_1, animation_id_1, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(obj_1)
    EnableTreasure(obj=obj_1)


@ContinueOnRest(11210510)
def Event_11210510(_, character: Character | int, flag: Flag | int):
    """Event 11210510"""
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


@ContinueOnRest(11210910)
def Event_11210910():
    """Event 11210910"""
    if ThisEventFlagDisabled():
        SetAIParamID(Characters.c4110_0000, ai_param_id=411001)
    
    MAIN.Await(FlagEnabled(11210911))
    
    SetAIParamID(Characters.c4110_0000, ai_param_id=411000)


@ContinueOnRest(11210912)
def Event_11210912():
    """Event 11210912"""
    MAIN.Await(FlagEnabled(1822))
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1212040))
    
    SetAIParamID(Characters.c4110_0000, ai_param_id=411001)
    SetNest(Characters.c4110_0000, region=1212041)
    AICommand(Characters.c4110_0000, command_id=10, command_slot=0)
    ReplanAI(Characters.c4110_0000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212040))
    
    WaitFrames(frames=30)
    SetAIParamID(Characters.c4110_0000, ai_param_id=411000)
    AICommand(Characters.c4110_0000, command_id=-1, command_slot=0)
    ReplanAI(Characters.c4110_0000)
    Restart()


@ContinueOnRest(11210915)
def Event_11210915():
    """Event 11210915"""
    if FlagEnabled(1822):
        return
    
    MAIN.Await(FlagEnabled(1822))
    
    ForceAnimation(Characters.c4110_0000, 9060)


@ContinueOnRest(11210520)
def Event_11210520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11210530)
def Event_11210530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210530"""
    AND_1.Add(FlagDisabled(1822))
    AND_1.Add(FlagEnabled(1820))
    AND_1.Add(FlagEnabled(11210300))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11210535)
def Event_11210535():
    """Event 11210535"""
    if ThisEventFlagEnabled():
        return
    DisableCharacter(Characters.c4510_0001)
    AND_1.Add(FlagEnabled(1821))
    AND_1.Add(FlagEnabled(Flags.KalameetShotDown))
    
    MAIN.Await(AND_1)
    
    DisableFlag(121)
    SkipLinesIfMultiplayer(1)
    PlayCutscene(120100, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(120100, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11210539)
    EnableCharacter(Characters.c4510_0001)
    DisableCharacter(Characters.c4510_0002)
    EnableObject(Objects.o2919_0000)
    CreateVFX(VFX.KalameetEntranceFog)
    EnableMapCollision(collision=Collisions.h0095B1_0000)
    DisableMapCollision(collision=Collisions.h0095B1)


@ContinueOnRest(11210544)
def Event_11210544():
    """Event 11210544"""
    MAIN.Await(ObjectDestroyed(Objects.o2253))
    
    DeleteVFX(VFX.ChesterCandlestick)


@ContinueOnRest(11210531)
def Event_11210531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210531"""
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(710))
    AND_1.Add(FlagEnabled(1860))
    AND_1.Add(FlagEnabled(Flags.ArtoriasDead))
    
    MAIN.Await(AND_1)
    
    if ThisEventFlagDisabled():
        return
    EnableCharacter(character)
    EnableObject(Objects.o2760_0000)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11210532)
def Event_11210532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210532"""
    AND_1.Add(FlagDisabled(1863))
    AND_1.Add(FlagEnabled(1861))
    AND_1.Add(FlagEnabled(11210590))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11210533)
def Event_11210533(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210533"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1863))
    AND_1.Add(FlagDisabled(1865))
    AND_1.Add(FlagEnabled(CommonFlags.CiaranGivenSoul))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11210534)
def Event_11210534(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11210534"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1863))
    AND_1.Add(FlagDisabled(CommonFlags.CiaranDead))
    AND_1.Add(FlagDisabled(1865))
    AND_1.Add(FlagEnabled(11210591))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11210543)
def Event_11210543():
    """Event 11210543"""
    AND_1.Add(FlagDisabled(11215210))
    AND_1.Add(CharacterInsideRegion(Characters.c0000_0013, region=1212351))
    AND_2.Add(FlagEnabled(11215210))
    AND_2.Add(CharacterInsideRegion(Characters.c0000_0013, region=1212350))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_2)
    EnableFlag(11215210)
    SetNest(Characters.c0000_0013, region=1212353)
    Restart()
    DisableFlag(11215210)
    SetNest(Characters.c0000_0013, region=1212352)
    Restart()


@ContinueOnRest(11210540)
def Event_11210540():
    """Event 11210540"""
    AND_1.Add(FlagEnabled(1127))
    AND_1.Add(FlagEnabled(Flags.ManusDead))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(2, 1126)
    SkipLinesIfFlagEnabled(1, 1125)
    DisableFlagRange((1120, 1139))
    DisableFlag(1127)
    EnableFlag(1128)
    Move(
        Characters.c0000_0006,
        destination=Characters.c4500_0000,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=Characters.c4500_0000,
    )
    RequestAnimation(Characters.c0000_0006, animation_id=7915, loop=True)
    EnableCharacter(Characters.c0000_0006)


@ContinueOnRest(11210541)
def Event_11210541():
    """Event 11210541"""
    if ThisEventFlagEnabled():
        DropMandatoryTreasure(Characters.c0000_0006)
        End()
    EnableImmortality(Characters.c0000_0006)
    
    MAIN.Await(HealthRatio(Characters.c0000_0006) <= 0.009999999776482582)
    
    ForceAnimation(Characters.c0000_0006, 7917, wait_for_completion=True)
    DisableCharacter(Characters.c0000_0006)
    DisableImmortality(Characters.c0000_0006)
    Kill(Characters.c0000_0006, award_souls=True)
    Kill(Characters.c4140_0000)
    DisableFlagRange((1120, 1139))
    EnableFlag(1125)


@ContinueOnRest(11210542)
def Event_11210542():
    """Event 11210542"""
    if FlagEnabled(11210541):
        End()
    
    MAIN.Await(Attacked(attacked_entity=Characters.c0000_0006, attacker=PLAYER))
    
    ForceAnimation(Characters.c0000_0006, 7916, wait_for_completion=True)
    Restart()


@ContinueOnRest(11210538)
def Event_11210538():
    """Event 11210538"""
    if ThisEventFlagEnabled():
        DropMandatoryTreasure(Characters.c4140_0000)
        End()
    
    MAIN.Await(FlagEnabled(1125))
    
    DropMandatoryTreasure(Characters.c4140_0000)
    DisableFlagRange((1870, 1889))
    EnableFlag(1872)


@ContinueOnRest(11215030)
def Event_11215030(
    _,
    character: int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    anchor_entity: int,
    region: Region | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
):
    """Event 11215030"""
    if FlagEnabled(flag):
        return
    DisableCharacter(character)
    if FlagEnabled(17):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(1842))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagEnabled(flag_1))
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag_4))
    AND_2.Add(OR_2)
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableCharacter(Characters.c4090_0000)
    EnableCharacter(character)
    DisplayBattlefieldMessage(20001100, display_location_index=0)
    if ThisEventSlotFlagDisabled():
        CreateTemporaryVFX(vfx_id=130, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
        ForceAnimation(character, 7000)
        ReplanAI(character)
    EnableFlag(flag)
    EnableFlag(11210536)


@ContinueOnRest(11210900)
def Event_11210900(_, character: Character | int):
    """Event 11210900"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    if OR_1:
        return
    DisplayBattlefieldMessage(20001105, display_location_index=0)
    EnableCharacter(Characters.c4090_0000)


@ContinueOnRest(11210905)
def Event_11210905(
    _,
    character: int,
    flag: Flag | int,
    destination: int,
    set_draw_parent: MapPart | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 11210905"""
    if FlagEnabled(flag_2):
        DisableCharacter(character)
        End()
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212084))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212085))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_2)
    ForceAnimation(character, 7001)
    WaitFrames(frames=80)
    DisableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=set_draw_parent)
    DisplayBattlefieldMessage(20001101, display_location_index=0)
    EnableCharacter(Characters.c4090_0000)


@ContinueOnRest(11219010)
def Event_11219010():
    """Event 11219010"""
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(7000, 7749)))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212715))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212714))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212713))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212797))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212793))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212702))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212701))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212700))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212794))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1212796))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1218900))
    
    MAIN.Await(AND_2)
    
    DisableFlagRange((7000, 7749))


@ContinueOnRest(11219111)
def Event_11219111():
    """Event 11219111"""
    AND_1.Add(ArenaMatchmaking())
    AND_1.Add(FlagDisabled(11211900))
    
    MAIN.Await(AND_1)
    
    EnableObject(Objects.o2920_0001)
    CreateVFX(VFX.MultiplayerFog6)
    EnableFlag(11211900)
    Restart()


@ContinueOnRest(11219112)
def Event_11219112():
    """Event 11219112"""
    AND_1.Add(ArenaMatchmaking())
    AND_2.Add(not AND_1)
    AND_2.Add(FlagEnabled(11211900))
    
    MAIN.Await(AND_2)
    
    DisableObject(Objects.o2920_0001)
    DeleteVFX(VFX.MultiplayerFog6)
    DisableFlag(11211900)
    Restart()


@ContinueOnRest(11219114)
def Event_11219114():
    """Event 11219114"""
    if Multiplayer():
        return
    AND_1.Add(PlayerDoesNotHaveGood(118))
    AND_1.Add(ActionButton(
        prompt_text=60000112,
        anchor_entity=1219001,
        anchor_type=CoordEntityType.Region,
        button=1211690,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1219001, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(PLAYER, target_entity=1212777)
    ForceAnimation(PLAYER, 7410)
    DisableObject(Objects.o2920_0001)
    DeleteVFX(VFX.MultiplayerFog6)
    Wait(1.5)
    AwardItemLot(2200, host_only=False)
    Restart()


@ContinueOnRest(11219113)
def Event_11219113():
    """Event 11219113"""
    AND_2.Add(Client())
    if AND_2:
        return
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(118))
    
    MAIN.Await(AND_1)
    
    DisableObject(Objects.o2920_0001)
    DeleteVFX(VFX.MultiplayerFog6, erase_root_only=False)
    End()


@ContinueOnRest(11212787)
def Event_11212787():
    """Event 11212787"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1212778))
    
    EnableFlag(11212785)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1212778))
    
    DisableFlag(11212785)
    Restart()


@ContinueOnRest(11212786)
def Event_11212786():
    """Event 11212786"""
    MAIN.Await(FlagEnabled(11212785))
    
    MAIN.Await(FlagDisabled(11212785))
    
    Restart()


@ContinueOnRest(11213888)
def Event_11213888():
    """Event 11213888"""
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1218900))
    if AND_1:
        return
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    End()


@ContinueOnRest(11215843)
def Event_11215843(_, left: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11215843"""
    SkipLinesIfValueEqual(1, left=left, right=11210001)
    SkipLines(3)
    AND_2.Add(FlagEnabled(Flags.KalameetShotDown))
    AND_2.Add(FlagDisabled(Flags.KalameetDead))
    AND_1.Add(not AND_2)
    AND_1.Add(Host())
    AND_1.Add(Multiplayer())
    AND_1.Add(FlagEnabled(left))
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


@ContinueOnRest(11215846)
def Event_11215846(_, left: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11215846"""
    SkipLinesIfValueEqual(1, left=left, right=11210001)
    SkipLines(3)
    AND_4.Add(FlagEnabled(Flags.KalameetShotDown))
    AND_4.Add(FlagDisabled(Flags.KalameetDead))
    AND_1.Add(not AND_4)
    OR_1.Add(Multiplayer())
    OR_1.Add(UnknownPlayerType5())
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(left))
    
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


@ContinueOnRest(11210700)
def Event_11210700():
    """Event 11210700"""
    Event_7999()
    Event_7998()
    Event_11219010()
    SkipLinesIfClient(1)
    DisableFlagRange((11215350, 11215365))
    DisableFlag(11215891)
    DisableFlag(11219902)
    DisableFlag(11215398)
    DisableFlagRange((11215342, 11215345))
    DisableFlagRange((11214350, 11214359))
    DisableFlag(11210810)
    DisableFlag(11218145)
    DeleteVFX(VFX.Arena_Wanted_1vs1_s_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_1vs1_s_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_s_D, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_s_D, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_1vs1_b_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_1vs1_b_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_Wanted_2vs2_b_D, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_A, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_B, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_C, erase_root_only=False)
    DeleteVFX(VFX.Arena_BR_Searching_b_D, erase_root_only=False)
    Event_11210838()
    Event_11210839()
    Event_11210876()
    Event_11210932()
    Event_11210830()
    Event_11210828(0, flag=11218990, flag_1=11215360, flag_2=11215362, region=1212700)
    Event_11210828(1, flag=11218991, flag_1=11215360, flag_2=11215362, region=1212713)
    Event_11210827(0, flag=11218992, first_flag=11215360, last_flag=11215363, region=1212701)
    Event_11210827(1, flag=11218993, first_flag=11215360, last_flag=11215363, region=1212714)
    Event_11210827(2, flag=11218994, first_flag=11215360, last_flag=11215363, region=1212702)
    Event_11210827(3, flag=11218995, first_flag=11215360, last_flag=11215363, region=1212715)
    Event_11210827(4, flag=11218996, first_flag=11215360, last_flag=11215365, region=1212796)
    Event_11210827(5, flag=11218997, first_flag=11215360, last_flag=11215365, region=1212793)
    Event_11210827(6, flag=11218998, first_flag=11215360, last_flag=11215365, region=1212794)
    Event_11210827(7, flag=11218999, first_flag=11215360, last_flag=11215365, region=1212797)
    Event_11210835(0, seconds=150.0, seconds_1=30.0, seconds_2=270.0, seconds_3=30.0)
    Event_11210836()
    Event_11210877()
    Event_11210878()
    Event_11215398()
    Event_11210875(0, left=6980, message_id=60000102, concatenator_base_flag=7290)
    Event_11210875(1, left=6981, message_id=60000103, concatenator_base_flag=7340)
    Event_11210875(2, left=6982, message_id=60000105, concatenator_base_flag=7440)
    Event_11210875(3, left=6983, message_id=60000109, concatenator_base_flag=7390)
    Event_11210875(4, left=6984, message_id=60000106, concatenator_base_flag=7490)
    Event_11210875(5, left=6985, message_id=60000107, concatenator_base_flag=7540)
    Event_11210875(6, left=6986, message_id=60000108, concatenator_base_flag=7590)
    Event_11210875(7, left=6987, message_id=60000110, concatenator_base_flag=7690)
    Event_11210875(8, left=6988, message_id=60000104, concatenator_base_flag=7640)
    Event_11210875(9, left=6989, message_id=60000111, concatenator_base_flag=7740)
    Event_11210875(10, left=6990, message_id=0, concatenator_base_flag=0)
    Event_11210727()
    Event_11210845()
    Event_11210846()
    Event_11210847()
    Event_11210848()
    Event_11210860()
    Event_11210861()
    Event_11210849()
    Event_11210826()
    Event_11210837()
    Event_11210817()
    Event_11210401()
    Event_11210402()
    Event_11219901()
    Event_11219111()
    Event_11219112()
    Event_11210404(0, flag=7290, flag_1=11215408, flag_2=11218001)
    Event_11210404(1, flag=7340, flag_1=11215392, flag_2=11218001)
    Event_11210404(2, flag=7390, flag_1=11215402, flag_2=11218001)
    Event_11210404(3, flag=7440, flag_1=11215395, flag_2=11218001)
    Event_11210404(4, flag=7490, flag_1=11215405, flag_2=11218001)
    Event_11210404(5, flag=7540, flag_1=11215408, flag_2=11218000)
    Event_11210404(6, flag=7590, flag_1=11215392, flag_2=11218000)
    Event_11210404(7, flag=7640, flag_1=11215402, flag_2=11218000)
    Event_11210404(8, flag=7690, flag_1=11215395, flag_2=11218000)
    Event_11210404(9, flag=7740, flag_1=11215405, flag_2=11218000)
    Event_11210800(0, region=1217700, flag=11215350, unk1=0)
    Event_11210800(1, region=1217701, flag=11215352, unk1=0)
    Event_11210800(2, region=1217600, flag=11215350, unk1=1)
    Event_11210800(3, region=1217601, flag=11215351, unk1=1)
    Event_11210800(4, region=1217602, flag=11215352, unk1=1)
    Event_11210800(5, region=1217603, flag=11215353, unk1=1)
    Event_11210800(6, region=1217800, flag=11215350, unk1=1)
    Event_11210800(7, region=1217801, flag=11215351, unk1=1)
    Event_11210800(8, region=1217802, flag=11215352, unk1=1)
    Event_11210800(9, region=1217803, flag=11215353, unk1=1)
    Event_11210800(10, region=1217804, flag=11215354, unk1=1)
    Event_11210800(11, region=1217805, flag=11215355, unk1=1)
    Event_11210800(12, region=1217500, flag=11215350, unk1=1)
    Event_11210800(13, region=1217501, flag=11215351, unk1=1)
    Event_11210800(14, region=1217502, flag=11215352, unk1=1)
    Event_11210800(15, region=1217503, flag=11215353, unk1=1)
    Event_11210800(16, region=1217900, flag=11215350, unk1=1)
    Event_11210800(17, region=1217901, flag=11215351, unk1=1)
    Event_11210800(18, region=1217902, flag=11215352, unk1=1)
    Event_11210800(19, region=1217903, flag=11215353, unk1=1)
    Event_11210800(20, region=1217904, flag=11215354, unk1=1)
    Event_11210800(21, region=1217905, flag=11215355, unk1=1)
    Event_11210800(22, region=1217200, flag=11215350, unk1=0)
    Event_11210800(23, region=1217201, flag=11215352, unk1=0)
    Event_11210800(24, region=1217100, flag=11215350, unk1=1)
    Event_11210800(25, region=1217101, flag=11215351, unk1=1)
    Event_11210800(26, region=1217102, flag=11215352, unk1=1)
    Event_11210800(27, region=1217103, flag=11215353, unk1=1)
    Event_11210800(28, region=1217300, flag=11215350, unk1=1)
    Event_11210800(29, region=1217301, flag=11215351, unk1=1)
    Event_11210800(30, region=1217302, flag=11215352, unk1=1)
    Event_11210800(31, region=1217303, flag=11215353, unk1=1)
    Event_11210800(32, region=1217304, flag=11215354, unk1=1)
    Event_11210800(33, region=1217305, flag=11215355, unk1=1)
    Event_11210800(34, region=1217000, flag=11215350, unk1=1)
    Event_11210800(35, region=1217001, flag=11215351, unk1=1)
    Event_11210800(36, region=1217002, flag=11215352, unk1=1)
    Event_11210800(37, region=1217003, flag=11215353, unk1=1)
    Event_11210800(38, region=1217400, flag=11215350, unk1=1)
    Event_11210800(39, region=1217401, flag=11215351, unk1=1)
    Event_11210800(40, region=1217402, flag=11215352, unk1=1)
    Event_11210800(41, region=1217403, flag=11215353, unk1=1)
    Event_11210800(42, region=1217404, flag=11215354, unk1=1)
    Event_11210800(43, region=1217405, flag=11215355, unk1=1)
    Event_11210820(0, left=11215350, flag=11215360, event_id=11210825, event_slot=0)
    Event_11210820(1, left=11215351, flag=11215361, event_id=11210825, event_slot=1)
    Event_11210820(2, left=11215352, flag=11215362, event_id=11210825, event_slot=2)
    Event_11210820(3, left=11215353, flag=11215363, event_id=11210825, event_slot=3)
    Event_11210820(4, left=11215354, flag=11215364, event_id=11210825, event_slot=4)
    Event_11210820(5, left=11215355, flag=11215365, event_id=11210825, event_slot=5)
    Event_11219950(0, flag=11215360)
    Event_11219950(1, flag=11215361)
    Event_11219950(2, flag=11215362)
    Event_11219950(3, flag=11215363)
    Event_11219950(4, flag=11215364)
    Event_11219950(5, flag=11215365)
    Event_11210825(0, flag=11215360, flag_1=11218501)
    Event_11210825(1, flag=11215361, flag_1=11218502)
    Event_11210825(2, flag=11215362, flag_1=11218503)
    Event_11210825(3, flag=11215363, flag_1=11218504)
    Event_11210825(4, flag=11215364, flag_1=11218505)
    Event_11210825(5, flag=11215365, flag_1=11218506)
    Event_11210701(0, flag=11215350, flag_1=11218348, flag_2=11218354, flag_3=11218355, flag_4=11218501)
    Event_11210701(1, flag=11215351, flag_1=11218349, flag_2=11218354, flag_3=11218355, flag_4=11218502)
    Event_11210701(2, flag=11215352, flag_1=11218350, flag_2=11218355, flag_3=11218354, flag_4=11218503)
    Event_11210701(3, flag=11215353, flag_1=11218351, flag_2=11218355, flag_3=11218354, flag_4=11218504)
    Event_11210701(4, flag=11215354, flag_1=11218352, flag_2=11218354, flag_3=11218355, flag_4=11218505)
    Event_11210701(5, flag=11215355, flag_1=11218353, flag_2=11218355, flag_3=11218354, flag_4=11218506)
    Event_11210434()
    Event_11210430(
        0,
        flag=11215350,
        flag_1=11218348,
        flag_2=11218350,
        flag_3=11218354,
        flag_4=11218355,
        flag_5=11218501,
    )
    Event_11210430(
        1,
        flag=11215351,
        flag_1=11218349,
        flag_2=11218351,
        flag_3=11218354,
        flag_4=11218355,
        flag_5=11218502,
    )
    Event_11210430(
        2,
        flag=11215352,
        flag_1=11218350,
        flag_2=11218348,
        flag_3=11218355,
        flag_4=11218354,
        flag_5=11218503,
    )
    Event_11210430(
        3,
        flag=11215353,
        flag_1=11218351,
        flag_2=11218349,
        flag_3=11218355,
        flag_4=11218354,
        flag_5=11218504,
    )
    Event_11210430(
        4,
        flag=11215354,
        flag_1=11218352,
        flag_2=11218353,
        flag_3=11218354,
        flag_4=11218355,
        flag_5=11218505,
    )
    Event_11210430(
        5,
        flag=11215355,
        flag_1=11218353,
        flag_2=11218352,
        flag_3=11218355,
        flag_4=11218354,
        flag_5=11218506,
    )
    Event_11210435(
        0,
        flag=11215350,
        flag_1=11218348,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218501,
    )
    Event_11210435(
        1,
        flag=11215351,
        flag_1=11218349,
        flag_2=11218348,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218502,
    )
    Event_11210435(
        2,
        flag=11215352,
        flag_1=11218350,
        flag_2=11218349,
        flag_3=11218348,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218503,
    )
    Event_11210435(
        3,
        flag=11215353,
        flag_1=11218351,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218348,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218504,
    )
    Event_11210435(
        4,
        flag=11215354,
        flag_1=11218352,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218348,
        flag_6=11218353,
        flag_7=11218505,
    )
    Event_11210435(
        5,
        flag=11215355,
        flag_1=11218353,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218348,
        flag_7=11218506,
    )
    Event_11214435(0, flag=11215350, flag_1=11218501)
    Event_11214435(1, flag=11215351, flag_1=11218502)
    Event_11214435(2, flag=11215352, flag_1=11218503)
    Event_11214435(3, flag=11215353, flag_1=11218504)
    Event_11214435(4, flag=11215354, flag_1=11218505)
    Event_11214435(5, flag=11215355, flag_1=11218506)
    Event_11210870(0, flag=11215350, flag_1=11218348, flag_2=11218354, flag_3=11218355)
    Event_11210870(1, flag=11215351, flag_1=11218349, flag_2=11218354, flag_3=11218355)
    Event_11210870(2, flag=11215352, flag_1=11218350, flag_2=11218355, flag_3=11218354)
    Event_11210870(3, flag=11215353, flag_1=11218351, flag_2=11218355, flag_3=11218354)
    Event_11210870(4, flag=11215354, flag_1=11218352, flag_2=11218354, flag_3=11218355)
    Event_11210870(5, flag=11215355, flag_1=11218353, flag_2=11218355, flag_3=11218354)
    Event_11210831(0, flag=11215360, flag_1=11218348)
    Event_11210831(1, flag=11215361, flag_1=11218349)
    Event_11210831(2, flag=11215362, flag_1=11218350)
    Event_11210831(3, flag=11215363, flag_1=11218351)
    Event_11210831(4, flag=11215364, flag_1=11218352)
    Event_11210831(5, flag=11215365, flag_1=11218353)
    Event_11210891(
        0,
        flag=11218342,
        flag_1=11215350,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218347,
    )
    Event_11210891(
        1,
        flag=11218343,
        flag_1=11215351,
        flag_2=11218342,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218347,
    )
    Event_11210891(
        2,
        flag=11218344,
        flag_1=11215352,
        flag_2=11218343,
        flag_3=11218342,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218347,
    )
    Event_11210891(
        3,
        flag=11218345,
        flag_1=11215353,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218342,
        flag_5=11218346,
        flag_6=11218347,
    )
    Event_11210891(
        4,
        flag=11218346,
        flag_1=11215354,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218342,
        flag_6=11218347,
    )
    Event_11210891(
        5,
        flag=11218347,
        flag_1=11215355,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218342,
    )
    Event_11210840(0, flag=11215350, flag_1=11218501, flag_2=11218511)
    Event_11210840(1, flag=11215351, flag_1=11218502, flag_2=11218512)
    Event_11210840(2, flag=11215352, flag_1=11218503, flag_2=11218513)
    Event_11210840(3, flag=11215353, flag_1=11218504, flag_2=11218514)
    Event_11210840(4, flag=11215354, flag_1=11218505, flag_2=11218515)
    Event_11210840(5, flag=11215355, flag_1=11218506, flag_2=11218516)
    Event_11210777(0, flag=11215350, flag_1=11218511)
    Event_11210777(1, flag=11215351, flag_1=11218512)
    Event_11210777(2, flag=11215352, flag_1=11218513)
    Event_11210777(3, flag=11215353, flag_1=11218514)
    Event_11210777(4, flag=11215354, flag_1=11218515)
    Event_11210777(5, flag=11215355, flag_1=11218516)
    Event_11210850(0, flag=11215350, flag_1=11218511, region=1212700, first_region=1215700, last_region=1215725)
    Event_11210850(1, flag=11215352, flag_1=11218513, region=1212700, first_region=1215700, last_region=1215725)
    Event_11210850(2, flag=11215350, flag_1=11218511, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(3, flag=11215351, flag_1=11218512, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(4, flag=11215352, flag_1=11218513, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(5, flag=11215353, flag_1=11218514, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(6, flag=11215350, flag_1=11218511, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(7, flag=11215351, flag_1=11218512, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(8, flag=11215352, flag_1=11218513, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(9, flag=11215353, flag_1=11218514, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(10, flag=11215354, flag_1=11218515, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(11, flag=11215355, flag_1=11218516, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(12, flag=11215350, flag_1=11218511, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(13, flag=11215351, flag_1=11218512, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(14, flag=11215352, flag_1=11218513, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(15, flag=11215353, flag_1=11218514, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(16, flag=11215350, flag_1=11218511, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(17, flag=11215351, flag_1=11218512, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(18, flag=11215352, flag_1=11218513, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(19, flag=11215353, flag_1=11218514, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(20, flag=11215354, flag_1=11218515, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(21, flag=11215355, flag_1=11218516, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(22, flag=11215350, flag_1=11218511, region=1212713, first_region=1215200, last_region=1215233)
    Event_11210850(23, flag=11215352, flag_1=11218513, region=1212713, first_region=1215200, last_region=1215233)
    Event_11210850(24, flag=11215350, flag_1=11218511, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(25, flag=11215351, flag_1=11218512, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(26, flag=11215352, flag_1=11218513, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(27, flag=11215353, flag_1=11218514, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(28, flag=11215350, flag_1=11218511, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(29, flag=11215351, flag_1=11218512, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(30, flag=11215352, flag_1=11218513, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(31, flag=11215353, flag_1=11218514, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(32, flag=11215354, flag_1=11218515, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(33, flag=11215355, flag_1=11218516, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(34, flag=11215350, flag_1=11218511, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(35, flag=11215351, flag_1=11218512, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(36, flag=11215352, flag_1=11218513, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(37, flag=11215353, flag_1=11218514, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(38, flag=11215350, flag_1=11218511, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(39, flag=11215351, flag_1=11218512, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(40, flag=11215352, flag_1=11218513, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(41, flag=11215353, flag_1=11218514, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(42, flag=11215354, flag_1=11218515, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(43, flag=11215355, flag_1=11218516, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210886(0, flag=11215350, flag_1=11218511)
    Event_11210886(1, flag=11215351, flag_1=11218512)
    Event_11210886(2, flag=11215352, flag_1=11218513)
    Event_11210886(3, flag=11215353, flag_1=11218514)
    Event_11210886(4, flag=11215354, flag_1=11218515)
    Event_11210886(5, flag=11215355, flag_1=11218516)
    Event_11210688(0, flag=11215350, flag_1=11218511)
    Event_11210688(1, flag=11215351, flag_1=11218512)
    Event_11210688(2, flag=11215352, flag_1=11218513)
    Event_11210688(3, flag=11215353, flag_1=11218514)
    Event_11210688(4, flag=11215354, flag_1=11218515)
    Event_11210688(5, flag=11215355, flag_1=11218516)
    Event_11210890()
    Event_11219877()
    Event_11219121()
    Event_11219122()
    Event_11210702()
    Event_11210829()
    Event_11210832()


@ContinueOnRest(11210702)
def Event_11210702():
    """Event 11210702"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(11215390))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Restart()


@ContinueOnRest(11210878)
def Event_11210878():
    """Event 11210878"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4610)
    if FlagDisabled(11215398):
        AddSpecialEffect(PLAYER, 4613)
    Wait(1.0)
    Restart()


@ContinueOnRest(11215398)
def Event_11215398():
    """Event 11215398"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212740))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212741))
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(PLAYER, 4613)
    Restart()


@ContinueOnRest(11210876)
def Event_11210876():
    """Event 11210876"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11215394))
    
    Wait(5.0)
    DisableFlag(11215394)
    if FlagDisabled(11215391):
        DisableInvincibility(PLAYER)
        RemoveSpecialEffect(PLAYER, 90000)
    Restart()


@ContinueOnRest(11210800)
def Event_11210800(_, region: Region | int, flag: Flag | int, unk1: int):
    """Event 11210800"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(FlagDisabled(11215390))
    
    MAIN.Await(AND_1)
    
    Unknown_2008_04()
    DisableFlagRange((11215350, 11215355))
    EnableFlag(flag)
    DisableAI(PLAYER)
    Unknown_2004_50()
    EqualRecovery()
    Unknown_2004_51(unk1=unk1)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11210820)
def Event_11210820(_, left: Flag | int, flag: Flag | int, event_id: int, event_slot: int):
    """Event 11210820"""
    AND_1.Add(Multiplayer())
    if ValueNotEqual(left=left, right=11215350):
        AND_1.Add(Client())
    AND_1.Add(FlagEnabled(left))
    AND_1.Add(TimeElapsed(seconds=3.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    RestartEvent(event_id=event_id, event_slot=event_slot)
    Restart()


@ContinueOnRest(11210825)
def Event_11210825(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210825"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(TimeElapsed(seconds=10.0))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag_1):
        return RESTART
    DisableFlag(flag)
    Restart()


@ContinueOnRest(11210827)
def Event_11210827(_, flag: Flag | int, first_flag: Flag | int, last_flag: Flag | int, region: Region | int):
    """Event 11210827"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(FlagRangeAllEnabled(flag_range=(first_flag, last_flag)))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(Multiplayer())
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11215360, 11215365)) >= 2)
    AND_2.Add(FlagDisabled(11215390))
    AND_2.Add(TimeElapsed(seconds=40.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((11218990, 11218999))
    EnableFlag(flag)
    if FlagDisabled(flag):
        return RESTART


@ContinueOnRest(11210828)
def Event_11210828(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, region: Region | int):
    """Event 11210828"""
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((11218990, 11218999))
    EnableFlag(flag)
    if FlagDisabled(flag):
        return RESTART


@ContinueOnRest(11210829)
def Event_11210829():
    """Event 11210829"""
    If_Unknown_3_23(AND_1, unk1=0, unk2=0)
    AND_2.Add(FlagEnabled(11215390))
    AND_2.Add(FlagDisabled(6990))
    AND_2.Add(not AND_1)
    
    MAIN.Await(AND_2)
    
    EnableFlag(6990)
    Restart()


@ContinueOnRest(11210832)
def Event_11210832():
    """Event 11210832"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    AND_1.Add(OR_1)
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagEnabled(6990))
    
    MAIN.Await(AND_1)
    
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Restart()


@ContinueOnRest(11210932)
def Event_11210932():
    """Event 11210932"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagRangeAllDisabled(flag_range=(11215350, 11215355)))
    
    MAIN.Await(AND_1)
    
    DisableAI(PLAYER)
    DisplayBattlefieldMessage(150001, display_location_index=1)
    DisableFlagRange((6980, 6990))
    Wait(3.0)
    EnableAI(PLAYER)
    ArenaExitRequest()


@ContinueOnRest(11210830)
def Event_11210830():
    """Event 11210830"""
    OR_1.Add(FlagEnabled(11218990))
    OR_1.Add(FlagEnabled(11218991))
    OR_1.Add(FlagEnabled(11218992))
    OR_1.Add(FlagEnabled(11218993))
    OR_1.Add(FlagEnabled(11218994))
    OR_1.Add(FlagEnabled(11218995))
    OR_1.Add(FlagEnabled(11218996))
    OR_1.Add(FlagEnabled(11218997))
    OR_1.Add(FlagEnabled(11218998))
    OR_1.Add(FlagEnabled(11218999))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11215340)
    DisableFlag(11215392)
    DisableFlag(11215395)
    DisableFlag(11215402)
    DisableFlag(11215405)
    DisableFlag(11218000)
    DisableFlag(11218001)
    EnableFlagRange((6980, 6989))
    DisableFlag(6990)
    If_Unknown_3_23(AND_3, unk1=0, unk2=0)
    SkipLinesIfConditionTrue(1, AND_3)
    DisableFlagRange((6980, 6989))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1212794))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1212796))
    SkipLinesIfConditionTrue(1, OR_2)
    SkipLines(2)
    EnableFlag(11218000)
    DisableFlagRange((6980, 6984))
    SkipLinesIfConditionTrue(1, OR_3)
    SkipLines(2)
    EnableFlag(11218001)
    DisableFlagRange((6985, 6989))
    SkipLinesIfFlagEnabled(2, 11218990)
    SkipLinesIfFlagEnabled(1, 11218991)
    SkipLines(5)
    EnableFlag(11215408)
    DisableFlagRange((6981, 6984))
    DisableFlagRange((6986, 6989))
    EnableFlag(11218348)
    EnableFlag(11218350)
    SkipLinesIfFlagEnabled(2, 11218992)
    SkipLinesIfFlagEnabled(1, 11218993)
    SkipLines(7)
    EnableFlag(11215392)
    DisableFlag(6980)
    DisableFlag(6985)
    DisableFlagRange((6982, 6984))
    DisableFlagRange((6987, 6989))
    EnableFlag(11218354)
    EnableFlag(11218355)
    SkipLinesIfFlagEnabled(2, 11218994)
    SkipLinesIfFlagEnabled(1, 11218995)
    SkipLines(6)
    EnableFlag(11215395)
    DisableFlagRange((6980, 6981))
    DisableFlagRange((6985, 6986))
    DisableFlagRange((6983, 6984))
    DisableFlagRange((6988, 6989))
    EnableFlagRange((11218348, 11218351))
    SkipLinesIfFlagEnabled(2, 11218996)
    SkipLinesIfFlagEnabled(1, 11218997)
    SkipLines(7)
    EnableFlag(11215402)
    DisableFlagRange((6980, 6982))
    DisableFlagRange((6985, 6987))
    DisableFlag(6984)
    DisableFlag(6989)
    EnableFlag(11218354)
    EnableFlag(11218355)
    SkipLinesIfFlagEnabled(2, 11218998)
    SkipLinesIfFlagEnabled(1, 11218999)
    SkipLines(4)
    EnableFlag(11215405)
    DisableFlagRange((6980, 6983))
    DisableFlagRange((6985, 6988))
    EnableFlagRange((11218348, 11218353))
    Wait(8.0)
    SkipLinesIfFlagEnabled(5, 11215402)
    SkipLinesIfFlagEnabled(4, 11215405)
    SkipLinesIfFlagEnabled(3, 11215395)
    SkipLinesIfFlagEnabled(2, 11215392)
    DisplayBattlefieldMessage(150215, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(150205, display_location_index=1)
    Wait(2.0)
    DisplayBanner(BannerType.BeginMatch)
    EnableFlag(11215390)
    
    MAIN.Await(FlagDisabled(11215390))
    
    Restart()


@ContinueOnRest(11210831)
def Event_11210831(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210831"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(2, 11215402)
    SkipLinesIfFlagEnabled(1, 11215392)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11210835)
def Event_11210835(_, seconds: float, seconds_1: float, seconds_2: float, seconds_3: float):
    """Event 11210835"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(5, 11215405)
    SkipLinesIfFlagEnabled(4, 11215402)
    SkipLinesIfFlagEnabled(3, 11215395)
    SkipLinesIfFlagEnabled(2, 11215392)
    Wait(seconds)
    SkipLines(1)
    Wait(seconds_2)
    if FlagDisabled(904):
        EnableFlag(11215396)
    SkipLinesIfFlagEnabled(5, 11215405)
    SkipLinesIfFlagEnabled(4, 11215402)
    SkipLinesIfFlagEnabled(3, 11215395)
    SkipLinesIfFlagEnabled(2, 11215392)
    Wait(seconds_1)
    SkipLines(1)
    Wait(seconds_3)
    
    MAIN.Await(FlagDisabled(904))
    
    EnableFlag(11215391)
    Restart()


@ContinueOnRest(11210836)
def Event_11210836():
    """Event 11210836"""
    MAIN.Await(FlagEnabled(11215396))
    
    EnableFlag(11215396)
    DisplayBattlefieldMessage(150110, display_location_index=0)
    
    MAIN.Await(FlagEnabled(11215391))
    
    EnableFlag(11215391)
    DisplayBattlefieldMessage(150300, display_location_index=0)
    
    MAIN.Await(FlagDisabled(11215391))
    
    Restart()


@ContinueOnRest(11210887)
def Event_11210887(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int, flag_4: Flag | int):
    """Event 11210887"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Unknown_4_15(MAIN, unk1=1)
    SkipLinesIfFlagEnabled(4, 11215392)
    SkipLinesIfFlagEnabled(3, 11215402)
    SkipLinesIfFlagDisabled(2, flag_4)
    EqualRecovery()
    Unknown_2004_51(unk1=1)
    AND_2.Add(FlagDisabled(11215392))
    AND_2.Add(FlagDisabled(11215402))
    SkipLinesIfConditionTrue(1, AND_2)
    Unknown_2004_51(unk1=1)
    EnableFlag(flag_1)
    SkipLinesIfFlagEnabled(2, 11215395)
    SkipLinesIfFlagEnabled(1, 11215405)
    EnableFlag(flag_2)
    if FlagDisabled(11215408):
        EnableFlag(flag_3)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    Restart()


@ContinueOnRest(11210889)
def Event_11210889(_, flag: Flag | int):
    """Event 11210889"""
    MAIN.Await(FlagDisabled(flag))
    
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    Restart()


@ContinueOnRest(11210888)
def Event_11210888(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210888"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    IncrementEventValue(flag_1, bit_count=6, max_value=63)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(11210891)
def Event_11210891(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 11210891"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(FlagDisabled(flag_4))
    AND_1.Add(FlagDisabled(flag_5))
    AND_1.Add(FlagDisabled(flag_6))
    
    MAIN.Await(AND_1)
    
    Unknown_2007_13(unk1=10000)
    Restart()


@ContinueOnRest(11210892)
def Event_11210892(
    _,
    flag: Flag | int,
    left_flag: Flag | int,
    right_flag: Flag | int,
    right_flag_1: Flag | int,
    right_flag_2: Flag | int,
    right_flag_3: Flag | int,
    right_flag_4: Flag | int,
    flag_1: Flag | int,
):
    """Event 11210892"""
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagDisabled(11215392))
    AND_1.Add(FlagDisabled(11215402))
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_1,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_2,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_3,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_4,
        right_bit_count=6,
    ))
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    Restart()


@ContinueOnRest(11210893)
def Event_11210893():
    """Event 11210893"""
    MAIN.Await(FlagEnabled(11218360))
    
    WaitFrames(frames=6)
    DisableFlag(11218360)
    Restart()


@ContinueOnRest(11210894)
def Event_11210894(
    _,
    flag: Flag | int,
    left_flag: Flag | int,
    right_flag: Flag | int,
    right_flag_1: Flag | int,
    right_flag_2: Flag | int,
    right_flag_3: Flag | int,
    right_flag_4: Flag | int,
    flag_1: Flag | int,
):
    """Event 11210894"""
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagDisabled(11215392))
    AND_1.Add(FlagDisabled(11215402))
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_1,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_2,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_3,
        right_bit_count=6,
    ))
    OR_1.Add(EventsComparison(
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_4,
        right_bit_count=6,
    ))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11210895)
def Event_11210895(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210895"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11215392))
    AND_1.Add(FlagDisabled(11215402))
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EqualRecovery()
    Unknown_2004_51(unk1=1)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11212222)
def Event_11212222(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
):
    """Event 11212222"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(HealthValue(PLAYER) == 1)
    
    MAIN.Await(AND_1)
    
    Unknown_4_16(AND_2, unk1=0, unk2=0, unk3=0)
    SkipLinesIfConditionTrue(2, AND_2)
    WaitFrames(frames=7)
    Restart()
    SkipLinesIfFlagEnabled(7, 11215392)
    SkipLinesIfFlagEnabled(6, 11215402)
    EnableFlag(flag_2)
    SkipLinesIfFlagEnabled(6, 11215408)
    EnableFlag(flag_1)
    EnableFlag(flag_3)
    EnableFlag(flag_4)
    EnableFlag(flag_5)
    SkipLinesIfFlagEnabled(2, 11215395)
    SkipLinesIfFlagEnabled(1, 11215405)
    EnableFlag(flag_6)
    WaitFrames(frames=7)
    Restart()


@ContinueOnRest(11210840)
def Event_11210840(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 11210840"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(HealthValue(PLAYER) == 1)
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90001)
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    AddSpecialEffect(PLAYER, 4611)
    if FlagEnabled(flag):
        DisplayBattlefieldMessage(506107, display_location_index=3)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    DisableFlag(flag_2)
    if FlagDisabled(flag):
        DisableInvincibility(PLAYER)
    RemoveSpecialEffect(PLAYER, 4611)
    ResetAnimation(PLAYER, disable_interpolation=True)
    if FlagDisabled(flag):
        ForceAnimation_Unknown_2003_44(
            entity=PLAYER,
            animation=6951,
            loop=False,
            wait_for_completion=True,
            skip_transition=False,
            unk1=0,
        )
    else:
        ForceAnimation_Unknown_2003_44(
            entity=PLAYER,
            animation=6951,
            loop=False,
            wait_for_completion=True,
            skip_transition=False,
            unk1=0,
        )
    ResetAnimation(PLAYER, disable_interpolation=True)
    DisableFlag(flag_1)
    Restart()


@ContinueOnRest(11210833)
def Event_11210833():
    """Event 11210833"""
    DisableNetworkSync()
    
    MAIN.Await(HealthValue(PLAYER) == 1)
    
    WaitFrames(frames=6)
    EqualRecovery()
    if FlagDisabled(11215408):
        Unknown_2004_51(unk1=1)
    Restart()


@ContinueOnRest(11210777)
def Event_11210777(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210777"""
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FramesElapsed(frames=120))
    
    MAIN.Await(AND_2)
    
    if FlagDisabled(flag):
        CreateTemporaryVFX(vfx_id=20176, anchor_entity=PLAYER, model_point=220, anchor_type=CoordEntityType.Character)
    else:
        Unknown_2003_48(
            entity=PLAYER,
            unk1=0,
            model_point=220,
            magic_id=5310,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Restart()


@ContinueOnRest(11210850)
def Event_11210850(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    region: Region | int,
    first_region: Region | int,
    last_region: Region | int,
):
    """Event 11210850"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DisableAI(PLAYER)
    Wait(2.0)
    SkipLinesIfFlagEnabled(3, 11215392)
    SkipLinesIfFlagEnabled(2, 11215402)
    PlayCutsceneAndRandomlyWarpPlayer_2002_6(
        120130,
        cutscene_flags=CutsceneFlags.Unskippable,
        first_region=first_region,
        last_region=last_region,
        game_map=OOLACILE,
    )
    SkipLines(1)
    PlayCutsceneAndRandomlyWarpPlayer_2002_7(
        120130,
        cutscene_flags=CutsceneFlags.Unskippable,
        first_region=first_region,
        last_region=last_region,
        game_map=OOLACILE,
    )
    WaitFrames(frames=1)
    EnableAI(PLAYER)
    EqualRecovery()
    if FlagDisabled(11215408):
        Unknown_2004_51(unk1=1)
    DisableFlag(flag_1)
    Wait(6.0)
    RemoveSpecialEffect(PLAYER, 90001)
    DisableInvincibility(PLAYER)
    Restart()


@ContinueOnRest(11210886)
def Event_11210886(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210886"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    FadeOutCharacter(character=PLAYER, duration=2.0)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(TimeElapsed(seconds=3.0))
    
    MAIN.Await(AND_2)
    
    FadeInCharacter(character=PLAYER, duration=1.0)
    Restart()


@ContinueOnRest(11210688)
def Event_11210688(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11210688"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FramesElapsed(frames=30))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(PLAYER, 4611)
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_3)
    
    Restart()


@ContinueOnRest(11210870)
def Event_11210870(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 11210870"""
    DisableNetworkSync()
    If_Unknown_3_23(AND_7, unk1=0, unk2=0)
    SkipLinesIfConditionFalse(1, AND_7)
    EnableFlag(11219000)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagEnabled(11215391))
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90000)
    Wait(6.0)
    EnableFlag(11215397)
    SkipLinesIfFlagEnabled(2, 11215392)
    SkipLinesIfFlagEnabled(1, 11215402)
    AND_3.Add(FlagEnabled(flag_1))
    SkipLinesIfFlagEnabled(3, 11215408)
    SkipLinesIfFlagEnabled(2, 11215405)
    SkipLinesIfFlagEnabled(1, 11215395)
    AND_3.Add(FlagEnabled(flag_2))
    SkipLinesIfFlagEnabled(2, 11215392)
    SkipLinesIfFlagEnabled(1, 11215402)
    AND_5.Add(FlagDisabled(flag_1))
    SkipLinesIfFlagEnabled(3, 11215408)
    SkipLinesIfFlagEnabled(2, 11215405)
    SkipLinesIfFlagEnabled(1, 11215395)
    AND_5.Add(FlagDisabled(flag_2))
    SkipLinesIfFlagEnabled(13, 11215402)
    SkipLinesIfFlagEnabled(12, 11215392)
    SkipLinesIfFlagEnabled(1, 11215350)
    OR_1.Add(FlagEnabled(11218348))
    SkipLinesIfFlagEnabled(1, 11215351)
    OR_1.Add(FlagEnabled(11218349))
    SkipLinesIfFlagEnabled(1, 11215352)
    OR_1.Add(FlagEnabled(11218350))
    SkipLinesIfFlagEnabled(1, 11215353)
    OR_1.Add(FlagEnabled(11218351))
    SkipLinesIfFlagEnabled(1, 11215354)
    OR_1.Add(FlagEnabled(11218352))
    SkipLinesIfFlagEnabled(1, 11215355)
    OR_1.Add(FlagEnabled(11218353))
    SkipLinesIfFlagEnabled(3, 11215408)
    SkipLinesIfFlagEnabled(2, 11215395)
    SkipLinesIfFlagEnabled(1, 11215405)
    OR_1.Add(FlagEnabled(flag_3))
    AND_6.Add(AND_3)
    AND_6.Add(OR_1)
    AND_2.Add(AND_3)
    AND_2.Add(not OR_1)
    SkipLinesIfFlagRangeAllDisabled(1, (11218342, 11218347))
    DisplayBattlefieldMessage(150420, display_location_index=3)
    SkipLinesIfConditionTrue(3, AND_2)
    SkipLinesIfConditionTrue(17, AND_5)
    SkipLinesIfConditionTrue(9, AND_6)
    SkipLines(8)
    EnableFlag(11215393)
    DisplayBanner(BannerType.YouWin)
    Wait(2.0)
    if FlagEnabled(11219000):
        DisplayBattlefieldMessage(150050, display_location_index=1)
    if FlagDisabled(11219000):
        DisplayBattlefieldMessage(150051, display_location_index=1)
    SkipLines(38)
    DisplayBanner(BannerType.Draw)
    Wait(2.0)
    if FlagEnabled(11219000):
        DisplayBattlefieldMessage(150055, display_location_index=1)
    if FlagDisabled(11219000):
        DisplayBattlefieldMessage(150056, display_location_index=1)
    SkipLines(7)
    Event_11210871()
    DisplayBanner(BannerType.YouLose)
    Wait(2.0)
    if FlagEnabled(11219000):
        DisplayBattlefieldMessage(150060, display_location_index=1)
    if FlagDisabled(11219000):
        DisplayBattlefieldMessage(150061, display_location_index=1)
    SkipLinesIfConditionTrue(1, AND_5)
    SkipLines(10)
    if FlagEnabled(11215408):
        Unknown_2003_43(flag=6040, bit_count=10, unk1=0, unk2=2)
    if FlagEnabled(11215392):
        Unknown_2003_43(flag=6090, bit_count=10, unk1=1, unk2=2)
    if FlagEnabled(11215402):
        Unknown_2003_43(flag=6140, bit_count=10, unk1=2, unk2=2)
    if FlagEnabled(11215395):
        Unknown_2003_43(flag=6190, bit_count=10, unk1=3, unk2=2)
    if FlagEnabled(11215405):
        Unknown_2003_43(flag=6240, bit_count=10, unk1=4, unk2=2)
    SkipLinesIfConditionTrue(1, OR_1)
    SkipLines(10)
    if FlagEnabled(11215408):
        Unknown_2003_43(flag=6040, bit_count=10, unk1=0, unk2=1)
    if FlagEnabled(11215392):
        Unknown_2003_43(flag=6090, bit_count=10, unk1=1, unk2=1)
    if FlagEnabled(11215402):
        Unknown_2003_43(flag=6140, bit_count=10, unk1=2, unk2=1)
    if FlagEnabled(11215395):
        Unknown_2003_43(flag=6190, bit_count=10, unk1=3, unk2=1)
    if FlagEnabled(11215405):
        Unknown_2003_43(flag=6240, bit_count=10, unk1=4, unk2=1)
    Wait(8.0)
    EnableFlag(11215891)
    DisableInvincibility(PLAYER)
    Unknown_2004_52()
    EqualRecovery()
    RemoveSpecialEffect(PLAYER, 90000)
    RemoveSpecialEffect(PLAYER, 4612)
    RemoveSpecialEffect(PLAYER, 4614)
    RemoveSpecialEffect(PLAYER, 4615)
    RemoveSpecialEffect(PLAYER, 4616)
    RemoveSpecialEffect(PLAYER, 4617)
    RemoveSpecialEffect(PLAYER, 4618)
    ArenaExitRequest()
    DisableFlag(11219000)
    EnableFlag(11218900)


@ContinueOnRest(11210871)
def Event_11210871():
    """Event 11210871"""
    if FlagEnabled(11215408):
        DisableFlagRange((7040, 7049))
        DisableFlagRange((7250, 7299))
        DisableFlagRange((7500, 7549))
    if FlagEnabled(11215392):
        DisableFlagRange((7090, 7099))
        DisableFlagRange((7300, 7349))
        DisableFlagRange((7550, 7599))
    if FlagEnabled(11215402):
        DisableFlagRange((7140, 7149))
        DisableFlagRange((7350, 7399))
        DisableFlagRange((7600, 7649))
    if FlagEnabled(11215395):
        DisableFlagRange((7190, 7199))
        DisableFlagRange((7400, 7449))
        DisableFlagRange((7650, 7699))
    if FlagEnabled(11215405):
        DisableFlagRange((7240, 7249))
        DisableFlagRange((7450, 7499))
        DisableFlagRange((7700, 7749))


@ContinueOnRest(11210875)
def Event_11210875(_, left: Flag | int, message_id: int, concatenator_base_flag: Flag | int):
    """Event 11210875"""
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1218900))
    AND_2.Add(FlagEnabled(left))
    
    MAIN.Await(AND_2)
    
    DisableFlag(left)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Wait(0.0)
    if ValueNotEqual(left=left, right=6990):
        DisplayConcatenatedMessage(
            message_id=message_id,
            pad_enabled=True,
            concatenator_base_flag=concatenator_base_flag,
            bit_count=10,
        )
    Restart()


@ContinueOnRest(11210705)
def Event_11210705():
    """Event 11210705"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11215392))
    AND_1.Add(FlagDisabled(11215395))
    AND_1.Add(FlagEnabled(11215393))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11215380):
        IncrementEventValue(7000, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7000,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6000,
            right_bit_count=10,
        ))
    if FlagEnabled(11215381):
        IncrementEventValue(7050, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7050,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6050,
            right_bit_count=10,
        ))
    if FlagEnabled(11215382):
        IncrementEventValue(7100, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7100,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6100,
            right_bit_count=10,
        ))
    if FlagEnabled(11215383):
        IncrementEventValue(7150, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7150,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6150,
            right_bit_count=10,
        ))
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, AND_2)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()
    if FlagEnabled(11215380):
        IncrementEventValue(6000, bit_count=10, max_value=1000)
    if FlagEnabled(11215381):
        IncrementEventValue(6050, bit_count=10, max_value=1000)
    if FlagEnabled(11215382):
        IncrementEventValue(6100, bit_count=10, max_value=1000)
    if FlagEnabled(11215383):
        IncrementEventValue(6150, bit_count=10, max_value=1000)
    AND_3.Add(EventsComparison(
        left_flag=7200,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6200,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_3)
    IncrementEventValue(6200, bit_count=10, max_value=1000)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()


@ContinueOnRest(11210706)
def Event_11210706():
    """Event 11210706"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215392))
    AND_1.Add(FlagDisabled(11215395))
    AND_1.Add(FlagEnabled(11215393))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11215380):
        IncrementEventValue(7250, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7250,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6250,
            right_bit_count=10,
        ))
    if FlagEnabled(11215381):
        IncrementEventValue(7300, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7300,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6300,
            right_bit_count=10,
        ))
    if FlagEnabled(11215382):
        IncrementEventValue(7350, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7350,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6350,
            right_bit_count=10,
        ))
    if FlagEnabled(11215383):
        IncrementEventValue(7400, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7400,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6400,
            right_bit_count=10,
        ))
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, AND_2)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()
    if FlagEnabled(11215380):
        IncrementEventValue(6250, bit_count=10, max_value=1000)
    if FlagEnabled(11215381):
        IncrementEventValue(6300, bit_count=10, max_value=1000)
    if FlagEnabled(11215382):
        IncrementEventValue(6350, bit_count=10, max_value=1000)
    if FlagEnabled(11215383):
        IncrementEventValue(6400, bit_count=10, max_value=1000)
    AND_3.Add(EventsComparison(
        left_flag=7450,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6450,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_3)
    IncrementEventValue(6450, bit_count=10, max_value=1000)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()


@ContinueOnRest(11210707)
def Event_11210707():
    """Event 11210707"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11215392))
    AND_1.Add(FlagEnabled(11215395))
    AND_1.Add(FlagEnabled(11215393))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(11215380):
        IncrementEventValue(7500, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7500,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6500,
            right_bit_count=10,
        ))
    if FlagEnabled(11215381):
        IncrementEventValue(7550, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7550,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6550,
            right_bit_count=10,
        ))
    if FlagEnabled(11215382):
        IncrementEventValue(7600, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7600,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6600,
            right_bit_count=10,
        ))
    if FlagEnabled(11215383):
        IncrementEventValue(7650, bit_count=10, max_value=1000)
        AND_2.Add(EventsComparison(
            left_flag=7650,
            left_bit_count=10,
            comparison_type=ComparisonType.GreaterThan,
            right_flag=6650,
            right_bit_count=10,
        ))
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, AND_2)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()
    if FlagEnabled(11215380):
        IncrementEventValue(6500, bit_count=10, max_value=1000)
    if FlagEnabled(11215381):
        IncrementEventValue(6550, bit_count=10, max_value=1000)
    if FlagEnabled(11215382):
        IncrementEventValue(6600, bit_count=10, max_value=1000)
    if FlagEnabled(11215383):
        IncrementEventValue(6650, bit_count=10, max_value=1000)
    AND_3.Add(EventsComparison(
        left_flag=7700,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6700,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_3)
    IncrementEventValue(6700, bit_count=10, max_value=1000)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()


@ContinueOnRest(11210727)
def Event_11210727():
    """Event 11210727"""
    DisableNetworkSync()
    If_Unknown_3_23(AND_1, unk1=0, unk2=0)
    if not AND_1:
        return
    
    MAIN.Await(FlagEnabled(11215393))
    
    SkipLinesIfFlagDisabled(55, 11218001)
    SkipLinesIfFlagDisabled(10, 11215408)
    IncrementEventValue(7290, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7290, destination_flag=7040, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7250,
        destination_flag__left_flag__right_flag__source_flag=6250,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6000,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7260,
        destination_flag__left_flag__right_flag__source_flag=6260,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6010,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7270,
        destination_flag__left_flag__right_flag__source_flag=6270,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6020,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7280,
        destination_flag__left_flag__right_flag__source_flag=6280,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6030,
    )
    SkipLinesIfFlagDisabled(10, 11215392)
    IncrementEventValue(7340, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7340, destination_flag=7090, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7300,
        destination_flag__left_flag__right_flag__source_flag=6300,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6050,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7310,
        destination_flag__left_flag__right_flag__source_flag=6310,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6060,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7320,
        destination_flag__left_flag__right_flag__source_flag=6320,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6070,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7330,
        destination_flag__left_flag__right_flag__source_flag=6330,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6080,
    )
    SkipLinesIfFlagDisabled(10, 11215402)
    IncrementEventValue(7390, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7390, destination_flag=7140, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7350,
        destination_flag__left_flag__right_flag__source_flag=6350,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6100,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7360,
        destination_flag__left_flag__right_flag__source_flag=6360,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6110,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7370,
        destination_flag__left_flag__right_flag__source_flag=6370,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6120,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7380,
        destination_flag__left_flag__right_flag__source_flag=6380,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6130,
    )
    SkipLinesIfFlagDisabled(10, 11215395)
    IncrementEventValue(7440, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7440, destination_flag=7190, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7400,
        destination_flag__left_flag__right_flag__source_flag=6400,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6150,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7410,
        destination_flag__left_flag__right_flag__source_flag=6410,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6160,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7420,
        destination_flag__left_flag__right_flag__source_flag=6420,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6170,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7430,
        destination_flag__left_flag__right_flag__source_flag=6430,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6180,
    )
    SkipLinesIfFlagDisabled(10, 11215405)
    IncrementEventValue(7490, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7490, destination_flag=7240, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7450,
        destination_flag__left_flag__right_flag__source_flag=6450,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6200,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7460,
        destination_flag__left_flag__right_flag__source_flag=6460,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6210,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7470,
        destination_flag__left_flag__right_flag__source_flag=6470,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6220,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7480,
        destination_flag__left_flag__right_flag__source_flag=6480,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6230,
    )
    SkipLinesIfFlagDisabled(55, 11218000)
    SkipLinesIfFlagDisabled(10, 11215408)
    IncrementEventValue(7540, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7540, destination_flag=7040, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7500,
        destination_flag__left_flag__right_flag__source_flag=6500,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6000,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7510,
        destination_flag__left_flag__right_flag__source_flag=6510,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6010,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7520,
        destination_flag__left_flag__right_flag__source_flag=6520,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6020,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7530,
        destination_flag__left_flag__right_flag__source_flag=6530,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6030,
    )
    SkipLinesIfFlagDisabled(10, 11215392)
    IncrementEventValue(7590, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7590, destination_flag=7090, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7550,
        destination_flag__left_flag__right_flag__source_flag=6550,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6050,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7560,
        destination_flag__left_flag__right_flag__source_flag=6560,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6060,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7570,
        destination_flag__left_flag__right_flag__source_flag=6570,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6070,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7580,
        destination_flag__left_flag__right_flag__source_flag=6580,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6080,
    )
    SkipLinesIfFlagDisabled(10, 11215402)
    IncrementEventValue(7640, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7640, destination_flag=7140, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7600,
        destination_flag__left_flag__right_flag__source_flag=6600,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6100,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7610,
        destination_flag__left_flag__right_flag__source_flag=6610,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6110,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7620,
        destination_flag__left_flag__right_flag__source_flag=6620,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6120,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7630,
        destination_flag__left_flag__right_flag__source_flag=6630,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6130,
    )
    SkipLinesIfFlagDisabled(10, 11215395)
    IncrementEventValue(7690, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7690, destination_flag=7190, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7650,
        destination_flag__left_flag__right_flag__source_flag=6650,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6150,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7660,
        destination_flag__left_flag__right_flag__source_flag=6660,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6160,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7670,
        destination_flag__left_flag__right_flag__source_flag=6670,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6170,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7680,
        destination_flag__left_flag__right_flag__source_flag=6680,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6180,
    )
    SkipLinesIfFlagDisabled(10, 11215405)
    IncrementEventValue(7740, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7740, destination_flag=7240, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7700,
        destination_flag__left_flag__right_flag__source_flag=6700,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6200,
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7710,
        destination_flag__left_flag__right_flag__source_flag=6710,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6210,
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7720,
        destination_flag__left_flag__right_flag__source_flag=6720,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6220,
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7730,
        destination_flag__left_flag__right_flag__source_flag=6730,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6230,
    )
    DisableFlag(11215393)
    Restart()


@ContinueOnRest(11210717)
def Event_11210717(
    _,
    left_flag__source_flag: Flag | int,
    destination_flag__left_flag__right_flag__source_flag: Flag | int,
    unk1: uchar,
    left_flag__source_flag_1: Flag | int,
    destination_flag__right_flag: Flag | int,
    destination_flag__right_flag_1: Flag | int,
    destination_flag__right_flag_2: Flag | int,
):
    """Event 11210717"""
    DisableNetworkSync()
    IncrementEventValue(left_flag__source_flag, bit_count=10, max_value=1000)
    AND_1.Add(EventsComparison(
        left_flag=left_flag__source_flag,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__left_flag__right_flag__source_flag,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_1)
    CopyEventValue(
        source_flag=left_flag__source_flag,
        destination_flag=destination_flag__left_flag__right_flag__source_flag,
        bit_count=10,
    )
    AND_4.Add(EventsComparison(
        left_flag=destination_flag__left_flag__right_flag__source_flag,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__right_flag_2,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_4)
    CopyEventValue(
        source_flag=destination_flag__left_flag__right_flag__source_flag,
        destination_flag=destination_flag__right_flag_2,
        bit_count=10,
    )
    AND_2.Add(EventsComparison(
        left_flag=left_flag__source_flag_1,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__right_flag,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_2)
    CopyEventValue(source_flag=left_flag__source_flag_1, destination_flag=destination_flag__right_flag, bit_count=10)
    AND_3.Add(EventsComparison(
        left_flag=destination_flag__left_flag__right_flag__source_flag,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__right_flag_1,
        right_bit_count=10,
    ))
    SkipLinesIfConditionFalse(1, AND_3)
    CopyEventValue(
        source_flag=destination_flag__left_flag__right_flag__source_flag,
        destination_flag=destination_flag__right_flag_1,
        bit_count=10,
    )
    Unknown_2003_43(flag=destination_flag__right_flag_1, bit_count=10, unk1=unk1, unk2=0)
    End()


@ContinueOnRest(11210838)
def Event_11210838():
    """Event 11210838"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    
    MAIN.Await(OR_1)
    
    EqualRecovery()


@ContinueOnRest(11210839)
def Event_11210839():
    """Event 11210839"""
    DisableNetworkSync()
    DisableFlagRange((8140, 8146))


@ContinueOnRest(11210877)
def Event_11210877():
    """Event 11210877"""
    DisableNetworkSync()
    AND_7.Add(FlagEnabled(11215390))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(11215380, 11215383)))
    
    MAIN.Await(AND_7)
    
    AND_1.Add(PlayerLevel() <= 50)
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(11215380)
    Restart()
    AND_2.Add(PlayerLevel() > 50)
    AND_2.Add(PlayerLevel() <= 100)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(11215381)
    Restart()
    AND_3.Add(PlayerLevel() > 100)
    AND_3.Add(PlayerLevel() <= 200)
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(11215382)
    Restart()
    EnableFlag(11215383)
    Restart()


@ContinueOnRest(11210890)
def Event_11210890():
    """Event 11210890"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    AND_1.Add(FlagDisabled(8146))
    AND_1.Add(Singleplayer())
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 4612)
    RemoveSpecialEffect(PLAYER, 4614)
    RemoveSpecialEffect(PLAYER, 4615)
    RemoveSpecialEffect(PLAYER, 4616)
    RemoveSpecialEffect(PLAYER, 4617)
    RemoveSpecialEffect(PLAYER, 4618)
    SkipLinesIfFlagEnabled(3, 11218145)
    SkipLinesIfFlagEnabled(2, 8140)
    SkipLinesIfFlagEnabled(1, 11215350)
    DisplayBattlefieldMessage(150040, display_location_index=1)
    Wait(3.0)
    ArenaExitRequest()
    Restart()


@ContinueOnRest(11210701)
def Event_11210701(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int, flag_4: Flag | int):
    """Event 11210701"""
    AND_1.Add(Multiplayer())
    OR_1.Add(FlagDisabled(11215396))
    OR_1.Add(FlagEnabled(11215397))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215891))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_4))
    AND_2.Add(FlagDisabled(11215408))
    AND_2.Add(FlagDisabled(11215395))
    AND_2.Add(FlagDisabled(11215405))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(FlagEnabled(flag_2))
    OR_5.Add(FlagEnabled(11215395))
    OR_5.Add(FlagEnabled(11215405))
    OR_5.Add(FlagEnabled(11215408))
    AND_3.Add(OR_5)
    AND_3.Add(FlagEnabled(flag_1))
    if FlagDisabled(11215350):
        AND_3.Add(FlagDisabled(11218348))
    if FlagDisabled(11215352):
        AND_3.Add(FlagDisabled(11218350))
    SkipLinesIfFlagEnabled(10, 11215408)
    SkipLinesIfFlagEnabled(1, 11215351)
    AND_3.Add(FlagDisabled(11218349))
    SkipLinesIfFlagEnabled(1, 11215353)
    AND_3.Add(FlagDisabled(11218351))
    SkipLinesIfFlagEnabled(5, 11215408)
    SkipLinesIfFlagEnabled(4, 11215395)
    SkipLinesIfFlagEnabled(1, 11215354)
    AND_3.Add(FlagDisabled(11218352))
    SkipLinesIfFlagEnabled(1, 11215355)
    AND_3.Add(FlagDisabled(11218353))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    AND_4.Add(FlagEnabled(11215342))
    AND_5.Add(FlagEnabled(11215343))
    AND_6.Add(FlagEnabled(11215344))
    AND_7.Add(FlagEnabled(11215345))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_4)
    AddSpecialEffect(PLAYER, 4615)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_5)
    AddSpecialEffect(PLAYER, 4616)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_6)
    AddSpecialEffect(PLAYER, 4617)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_7)
    AddSpecialEffect(PLAYER, 4618)
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_4)
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_5)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_6)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_7)
    AddSpecialEffect(PLAYER, 4612)
    Wait(5.0)
    Restart()


@ContinueOnRest(11210430)
def Event_11210430(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 11210430"""
    AND_1.Add(Multiplayer())
    OR_1.Add(FlagDisabled(11215396))
    OR_1.Add(FlagEnabled(11215397))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215891))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_5))
    AND_2.Add(FlagDisabled(11215395))
    AND_2.Add(FlagDisabled(11215405))
    AND_2.Add(FlagEnabled(11215408))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    OR_4.Add(FlagEnabled(11215392))
    OR_4.Add(FlagEnabled(11215402))
    AND_3.Add(OR_4)
    AND_3.Add(FlagEnabled(flag_3))
    AND_3.Add(FlagEnabled(flag_4))
    OR_2.Add(AND_3)
    OR_2.Add(AND_2)
    AND_1.Add(OR_2)
    OR_3.Add(FlagEnabled(11215399))
    OR_3.Add(FlagEnabled(11215397))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


@ContinueOnRest(11210435)
def Event_11210435(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 11210435"""
    AND_1.Add(Multiplayer())
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215891))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_7))
    OR_5.Add(FlagEnabled(11215395))
    OR_5.Add(FlagEnabled(11215405))
    AND_1.Add(OR_5)
    OR_1.Add(FlagEnabled(11215399))
    OR_1.Add(FlagEnabled(11215397))
    AND_1.Add(OR_1)
    OR_2.Add(FlagDisabled(11215396))
    OR_2.Add(FlagEnabled(11215397))
    AND_1.Add(OR_2)
    AND_1.Add(FlagEnabled(flag_1))
    OR_3.Add(FlagEnabled(flag_2))
    OR_3.Add(FlagEnabled(flag_3))
    OR_3.Add(FlagEnabled(flag_4))
    if FlagEnabled(11215405):
        OR_3.Add(FlagEnabled(flag_5))
        OR_3.Add(FlagEnabled(flag_6))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


@ContinueOnRest(11214435)
def Event_11214435(_, flag: Flag | int, flag_1: Flag | int):
    """Event 11214435"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(11215391))
    AND_2.Add(Singleplayer())
    OR_1.Add(AND_2)
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(PLAYER, 4612)
    RemoveSpecialEffect(PLAYER, 4614)
    RemoveSpecialEffect(PLAYER, 4615)
    RemoveSpecialEffect(PLAYER, 4616)
    RemoveSpecialEffect(PLAYER, 4617)
    RemoveSpecialEffect(PLAYER, 4618)
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagDisabled(flag_1))
    OR_2.Add(FlagDisabled(11215391))
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    Restart()


@ContinueOnRest(11210434)
def Event_11210434():
    """Event 11210434"""
    EnableFlag(11215399)
    End()
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagEnabled(11215408))
    OR_2.Add(FlagRangeAnyEnabled(flag_range=(11215300, 11215305)))
    OR_2.Add(FlagRangeAnyEnabled(flag_range=(11215312, 11215317)))
    AND_1.Add(OR_2)
    AND_2.Add(FlagEnabled(11215390))
    OR_1.Add(FlagEnabled(11215392))
    OR_1.Add(FlagEnabled(11215395))
    AND_2.Add(OR_1)
    OR_3.Add(FlagRangeAnyEnabled(flag_range=(11215300, 11215305)))
    OR_3.Add(FlagRangeAnyEnabled(flag_range=(11215306, 11215311)))
    OR_3.Add(FlagRangeAnyEnabled(flag_range=(11215312, 11215317)))
    OR_3.Add(FlagRangeAnyEnabled(flag_range=(11215318, 11215323)))
    AND_2.Add(OR_3)
    AND_3.Add(FlagEnabled(11215390))
    OR_5.Add(FlagEnabled(11215402))
    OR_5.Add(FlagEnabled(11215405))
    AND_3.Add(OR_1)
    OR_5.Add(FlagRangeAnyEnabled(flag_range=(11215300, 11215305)))
    OR_5.Add(FlagRangeAnyEnabled(flag_range=(11215306, 11215311)))
    OR_5.Add(FlagRangeAnyEnabled(flag_range=(11215312, 11215317)))
    OR_5.Add(FlagRangeAnyEnabled(flag_range=(11215318, 11215323)))
    OR_5.Add(FlagRangeAnyEnabled(flag_range=(11215324, 11215329)))
    OR_5.Add(FlagRangeAnyEnabled(flag_range=(11215330, 11215335)))
    AND_3.Add(OR_5)
    OR_7.Add(AND_1)
    OR_7.Add(AND_2)
    OR_7.Add(AND_3)
    
    MAIN.Await(OR_7)
    
    EnableFlag(11215399)


@ContinueOnRest(11210845)
def Event_11210845():
    """Event 11210845"""
    AND_1.Add(FlagEnabled(11215350))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    ArenaSetNametag1(player_id=10000)


@ContinueOnRest(11210846)
def Event_11210846():
    """Event 11210846"""
    AND_1.Add(FlagEnabled(11215351))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    ArenaSetNametag2(player_id=10000)


@ContinueOnRest(11210847)
def Event_11210847():
    """Event 11210847"""
    AND_1.Add(FlagEnabled(11215352))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    ArenaSetNametag3(player_id=10000)


@ContinueOnRest(11210848)
def Event_11210848():
    """Event 11210848"""
    AND_1.Add(FlagEnabled(11215353))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    ArenaSetNametag4(player_id=10000)


@ContinueOnRest(11210860)
def Event_11210860():
    """Event 11210860"""
    AND_1.Add(FlagEnabled(11215354))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    ArenaSetNametag5(player_id=10000)


@ContinueOnRest(11210861)
def Event_11210861():
    """Event 11210861"""
    AND_1.Add(FlagEnabled(11215355))
    AND_1.Add(FlagEnabled(11215390))
    
    MAIN.Await(AND_1)
    
    ArenaSetNametag6(player_id=10000)


@ContinueOnRest(11219121)
def Event_11219121():
    """Event 11219121"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(9121))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9121)


@ContinueOnRest(11219122)
def Event_11219122():
    """Event 11219122"""
    AND_1.Add(FlagEnabled(9121))
    OR_1.Add(FlagEnabled(CommonFlags.TutorialComplete))
    OR_1.Add(FlagEnabled(CommonFlags.RiteOfKindlingObtained))
    OR_1.Add(FlagEnabled(CommonFlags.BonfireWarpOptionDisplayed))
    AND_1.Add(OR_1)
    DisableFlag(9121)


@ContinueOnRest(11210849)
def Event_11210849():
    """Event 11210849"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 17))
    
    EnableFlag(11215891)
    EnableFlag(8146)
    AND_1.Add(Host())
    SkipLinesIfConditionTrue(2, AND_1)
    EnableFlag(8144)
    SkipLines(1)
    EnableFlag(8145)
    DisplayBattlefieldMessage(150031, display_location_index=1)
    Wait(1.0)
    DisableFlagRange((7000, 7749))
    Unknown_2004_52()
    ArenaExitRequest()
    EqualRecovery()
    Wait(3.0)
    WarpToMap(game_map=OOLACILE, player_start=1218146)
    Restart()


@ContinueOnRest(11210826)
def Event_11210826():
    """Event 11210826"""
    MAIN.Await(FlagEnabled(8145))
    
    EnableFlag(8140)
    EnableFlag(11215891)


@ContinueOnRest(11210837)
def Event_11210837():
    """Event 11210837"""
    AND_1.Add(FlagEnabled(8145))
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    
    MAIN.Await(AND_1)
    
    Unknown_2000_6(unk1=0)
    SkipLinesIfFlagEnabled(4, 11218145)
    SkipLinesIfFlagDisabled(1, 8145)
    SkipLinesIfFlagEnabled(2, 11215350)
    SkipLinesIfFlagEnabled(1, 8145)
    DisplayBattlefieldMessage(150040, display_location_index=1)
    if FlagEnabled(8145):
        Wait(3.0)
        ArenaExitRequest()
    Restart()


@ContinueOnRest(11210817)
def Event_11210817():
    """Event 11210817"""
    AND_1.Add(FlagEnabled(8144))
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagDisabled(11215391))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagDisabled(1, 8145)
    SkipLinesIfFlagEnabled(2, 11215350)
    if FlagDisabled(8144):
        DisplayBattlefieldMessage(20000437, display_location_index=1)
    Restart()


@ContinueOnRest(11210401)
def Event_11210401():
    """Event 11210401"""
    DisableNetworkSync()
    AND_1.Add(Multiplayer())
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11215360, 11215365)) >= 2)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4613))
    AND_1.Add(FlagDisabled(11215340))
    
    MAIN.Await(AND_1)
    
    Wait(5.0)
    if FlagEnabled(11215340):
        return RESTART
    if Singleplayer():
        return RESTART
    DisplayBattlefieldMessage(150000, display_location_index=1)
    Wait(5.0)
    Restart()


@ContinueOnRest(11210402)
def Event_11210402():
    """Event 11210402"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterHasSpecialEffect(PLAYER, 2320))
    OR_2.Add(CharacterHasSpecialEffect(PLAYER, 2330))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 2320)
    RemoveSpecialEffect(PLAYER, 2330)
    Restart()


@ContinueOnRest(11210404)
def Event_11210404(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 11210404"""
    DisableNetworkSync()
    AND_6.Add(FlagEnabled(11215340))
    AND_6.Add(FlagEnabled(flag_1))
    AND_6.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_6)
    
    AND_1.Add(EventValue(flag=flag, bit_count=10) < 10)
    AND_2.Add(EventValue(flag=flag, bit_count=10) >= 10)
    AND_2.Add(EventValue(flag=flag, bit_count=10) < 30)
    AND_3.Add(EventValue(flag=flag, bit_count=10) >= 30)
    AND_3.Add(EventValue(flag=flag, bit_count=10) < 50)
    AND_4.Add(EventValue(flag=flag, bit_count=10) >= 50)
    AND_4.Add(EventValue(flag=flag, bit_count=10) < 100)
    AND_5.Add(EventValue(flag=flag, bit_count=10) >= 100)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(11215342)
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(11215343)
    SkipLinesIfConditionFalse(1, AND_4)
    EnableFlag(11215344)
    SkipLinesIfConditionFalse(1, AND_5)
    EnableFlag(11215345)


@ContinueOnRest(11210407)
def Event_11210407():
    """Event 11210407"""
    DisableNetworkSync()
    if FlagEnabled(11210709):
        DisableFlag(11210709)
        End()
    if Multiplayer():
        return
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    if not OR_1:
        return
    Wait(2.0)
    Event_11216300()
    Event_11216301()
    Event_11216200(0, value=1, text=60000001)
    Event_11216200(1, value=2, text=60000002)
    Event_11216200(2, value=3, text=60000003)
    Event_11216200(3, value=4, text=60000004)
    Event_11216200(4, value=5, text=60000005)
    Event_11216200(5, value=6, text=60000006)
    Event_11216200(6, value=7, text=60000007)
    Event_11216200(7, value=8, text=60000008)
    Event_11216200(8, value=9, text=60000009)
    Event_11216200(9, value=10, text=60000010)
    Event_11216200(10, value=11, text=60000011)
    Event_11216200(11, value=12, text=60000012)
    Event_11216200(12, value=13, text=60000013)
    Event_11216200(13, value=14, text=60000014)
    Event_11216200(14, value=15, text=60000015)
    Event_11216200(15, value=16, text=60000016)
    Event_11216200(16, value=17, text=60000017)
    Event_11216200(17, value=18, text=60000018)
    Event_11216200(18, value=19, text=60000019)
    Event_11216200(19, value=20, text=60000020)
    Event_11216200(20, value=21, text=60000021)
    Event_11216200(21, value=22, text=60000022)
    Event_11216200(22, value=23, text=60000023)
    Event_11216200(23, value=24, text=60000024)
    Event_11216200(24, value=25, text=60000025)
    Event_11216200(25, value=26, text=60000026)
    Event_11216200(26, value=27, text=60000027)
    Event_11216200(27, value=28, text=60000028)
    Event_11216200(28, value=29, text=60000029)
    Event_11216200(29, value=30, text=60000030)
    Event_11216200(30, value=31, text=60000031)
    Event_11216200(31, value=32, text=60000032)
    Event_11216200(32, value=33, text=60000033)
    Event_11216200(33, value=34, text=60000034)
    Event_11216200(34, value=35, text=60000035)
    Event_11216200(35, value=36, text=60000036)
    Event_11216200(36, value=37, text=60000037)
    Event_11216200(37, value=38, text=60000038)
    Event_11216200(38, value=39, text=60000039)
    Event_11216200(39, value=40, text=60000040)
    Event_11216200(40, value=41, text=60000041)
    Event_11216200(41, value=42, text=60000042)
    Event_11216200(42, value=43, text=60000043)
    Event_11216200(43, value=44, text=60000044)
    Event_11216200(44, value=45, text=60000045)
    Event_11216200(45, value=46, text=60000046)
    Event_11216200(46, value=47, text=60000047)
    Event_11216200(47, value=48, text=60000048)
    Event_11216200(48, value=49, text=60000049)
    Event_11216200(49, value=50, text=60000050)
    Event_11216200(50, value=51, text=60000051)
    Event_11216200(51, value=52, text=60000052)
    Event_11216200(52, value=53, text=60000053)
    Event_11216200(53, value=54, text=60000054)
    Event_11216200(54, value=55, text=60000055)
    Event_11216200(55, value=56, text=60000056)
    Event_11216200(56, value=57, text=60000057)
    Event_11216200(57, value=58, text=60000058)
    Event_11216200(58, value=59, text=60000059)
    Event_11216200(59, value=60, text=60000060)
    Event_11216200(60, value=61, text=60000061)
    Event_11216200(61, value=62, text=60000062)
    Event_11216200(62, value=63, text=60000063)
    Event_11216200(63, value=64, text=60000064)
    Event_11216200(64, value=65, text=60000065)
    Event_11216200(65, value=66, text=60000066)
    Event_11216200(66, value=67, text=60000067)
    Event_11216200(67, value=68, text=60000068)
    Event_11216200(68, value=69, text=60000069)
    Event_11216200(69, value=70, text=60000070)
    Event_11216200(70, value=71, text=60000071)
    Event_11216200(71, value=72, text=60000072)
    Event_11216200(72, value=73, text=60000073)
    Event_11216200(73, value=74, text=60000074)
    Event_11216200(74, value=75, text=60000075)
    Event_11216200(75, value=76, text=60000076)
    Event_11216200(76, value=77, text=60000077)
    Event_11216200(77, value=78, text=60000078)
    Event_11216200(78, value=79, text=60000079)
    Event_11216200(79, value=80, text=60000080)
    Event_11216200(80, value=81, text=60000081)
    Event_11216200(81, value=82, text=60000082)
    Event_11216200(82, value=83, text=60000083)
    Event_11216200(83, value=84, text=60000084)
    Event_11216200(84, value=85, text=60000085)
    Event_11216200(85, value=86, text=60000086)
    Event_11216200(86, value=87, text=60000087)
    Event_11216200(87, value=88, text=60000088)
    Event_11216200(88, value=89, text=60000089)
    Event_11216200(89, value=90, text=60000090)
    Event_11216200(90, value=91, text=60000091)
    Event_11216200(91, value=92, text=60000092)
    Event_11216200(92, value=93, text=60000093)
    Event_11216200(93, value=94, text=60000094)
    Event_11216200(94, value=95, text=60000095)
    Event_11216200(95, value=96, text=60000096)
    Event_11216200(96, value=97, text=60000097)
    Event_11216200(97, value=98, text=60000098)
    Event_11216200(98, value=99, text=60000099)
    Event_11216200(99, value=100, text=60000100)


@ContinueOnRest(11216200)
def Event_11216200(_, value: uint, text: EventText | int):
    """Event 11216200"""
    DisableNetworkSync()
    OR_1.Add(EventValue(flag=7200, bit_count=10) == value)
    OR_1.Add(EventValue(flag=7450, bit_count=10) == value)
    OR_1.Add(EventValue(flag=7700, bit_count=10) == value)
    if not OR_1:
        return
    DisplayStatus(text)


@ContinueOnRest(11216300)
def Event_11216300():
    """Event 11216300"""
    DisableNetworkSync()
    AND_1.Add(EventValue(flag=7200, bit_count=10) == 0)
    AND_1.Add(EventValue(flag=7450, bit_count=10) == 0)
    AND_1.Add(EventValue(flag=7700, bit_count=10) == 0)
    if not AND_1:
        return
    DisplayStatus(60000000)


@ContinueOnRest(11216301)
def Event_11216301():
    """Event 11216301"""
    DisableNetworkSync()
    OR_1.Add(EventValue(flag=7200, bit_count=10) > 100)
    OR_1.Add(EventValue(flag=7450, bit_count=10) > 100)
    OR_1.Add(EventValue(flag=7700, bit_count=10) > 100)
    if not OR_1:
        return
    DisplayStatus(59999999)


@ContinueOnRest(11210439)
def Event_11210439():
    """Event 11210439"""
    if Client():
        return
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212700))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212701))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212713))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212714))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212793))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212796))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    if not OR_1:
        return
    SetTeamType(PLAYER, TeamType.Human)


@ContinueOnRest(11219999)
def Event_11219999():
    """Event 11219999"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1219999))
    AND_1.Add(FlagDisabled(11219898))
    
    MAIN.Await(AND_1)
    
    DisableAI(PLAYER)
    EnableFlag(11219898)
    RotateToFaceEntity(PLAYER, target_entity=1212510)
    Wait(10.0)
    EnableAI(PLAYER)
    Restart()


@ContinueOnRest(11219900)
def Event_11219900():
    """Event 11219900"""
    AND_1.Add(Multiplayer())
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(11215360, 11215365)) >= 2)
    AND_1.Add(FlagDisabled(11215390))
    AND_1.Add(TimeElapsed(seconds=60.0))
    
    MAIN.Await(AND_1)


@ContinueOnRest(11219901)
def Event_11219901():
    """Event 11219901"""
    AND_1.Add(Multiplayer())
    AND_1.Add(FlagEnabled(11215360))
    AND_1.Add(FlagDisabled(11215390))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212794))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212797))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212702))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1212715))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11219902)


@ContinueOnRest(11219950)
def Event_11219950(_, flag: Flag | int):
    """Event 11219950"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11215390))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableAI(PLAYER)


@ContinueOnRest(7999)
def Event_7999():
    """Event 7999"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(905))
    AND_2.Add(FlagEnabled(906))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(906):
        DisableFlag(905)
        AddSpecialEffect(PLAYER, 4611)
        Restart()
    DisableFlag(906)
    AddSpecialEffect(PLAYER, 4612)
    Restart()


@ContinueOnRest(7998)
def Event_7998():
    """Event 7998"""
    AND_1.Add(FlagEnabled(5100))
    AND_2.Add(FlagEnabled(5101))
    AND_3.Add(FlagEnabled(5102))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((5100, 5102))
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_2)
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_3)
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    Restart()


@ContinueOnRest(11219876)
def Event_11219876():
    """Event 11219876"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1212778))
    AND_1.Add(FlagDisabled(11212778))
    
    MAIN.Await(AND_1)
    
    Unknown_2003_43(flag=6000, bit_count=10, unk1=0, unk2=0)
    EnableFlag(11212778)
    Restart()
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1212778))
    AND_2.Add(FlagEnabled(11212778))
    
    MAIN.Await(AND_2)
    
    Unknown_2003_43(flag=6000, bit_count=10, unk1=0, unk2=1)
    DisableFlag(11212778)
    Restart()


@ContinueOnRest(11219877)
def Event_11219877():
    """Event 11219877"""
    AND_1.Add(FlagEnabled(11215390))
    OR_1.Add(FlagEnabled(11215392))
    OR_1.Add(FlagEnabled(11215402))
    AND_2.Add(FlagDisabled(11215360))
    AND_2.Add(FlagDisabled(11215361))
    AND_2.Add(FlagDisabled(11215364))
    AND_3.Add(FlagDisabled(11215362))
    AND_3.Add(FlagDisabled(11215363))
    AND_3.Add(FlagDisabled(11215365))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11218145)
    Unknown_2000_6(unk1=2)
    Wait(3.0)
    Unknown_2004_52()
    ArenaExitRequest()
