"""
Anor Londo

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m15_01_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11510992()
    Event_11510997()
    Event_11510998()
    Event_11510999()
    if FlagEnabled(CommonFlags.OrnsteinSmoughDead):
        RegisterBonfire(bonfire_flag=11510920, obj=Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11510992, obj=Objects.o0200_0000, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11510984, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11510976, obj=Objects.o0200_0003)
    RegisterLadder(start_climbing_flag=11510010, stop_climbing_flag=11510011, obj=Objects.o5410_0000)
    RegisterLadder(start_climbing_flag=11510012, stop_climbing_flag=11510013, obj=Objects.o5410_0001)
    DisableFlag(11510304)
    SkipLinesIfClient(2)
    DisableObject(Objects.o5863_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o5611_0000)
    DisableMapCollision(collision=Collisions.h0010B1_0002)
    DisableMapCollision(collision=Collisions.h0010B1_0001)
    DisableMapCollision(collision=Collisions.h0010B1_0000)
    SkipLinesIfFlagDisabled(1, 11510300)
    SkipLinesIfFlagDisabled(6, 11510303)
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(obj=Objects.o5610_0000, animation_id=53)
    EnableMapCollision(collision=Collisions.h0010B1_0000)
    SkipLines(13)
    SkipLinesIfFlagDisabled(6, 11510302)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=Objects.o5610_0000, animation_id=50)
    EnableMapCollision(collision=Collisions.h0010B1_0001)
    SkipLines(6)
    if FlagEnabled(11510301):
        EnableFlag(11510301)
        DisableFlag(11510302)
        DisableFlag(11510303)
        EndOfAnimation(obj=Objects.o5610_0000, animation_id=51)
        EnableMapCollision(collision=Collisions.h0010B1_0002)
    DisableObject(Objects.o5905_0000)
    DisableFlag(11510460)
    Event_11510090(0, obj=Objects.o5864_0000, vfx_id=VFX.CheckpointFog1, destination=1512600, destination_1=1512601)
    Event_11510090(1, obj=Objects.o5865_0000, vfx_id=VFX.CheckpointFog2, destination=1512602, destination_1=1512603)
    Event_11515040()
    Event_11515041()
    Event_11515042()
    Event_11510200()
    Event_11510201()
    Event_11510100()
    Event_11510210()
    Event_11510211()
    Event_11510220()
    Event_11510300()
    Event_11510319()
    Event_11510340()
    Event_11510350()
    Event_11510310()
    Event_11515250()
    Event_11515251()
    Event_11510110()
    Event_11510400()
    Event_11510401()
    Event_11510230()
    Event_11510240()
    Event_11515050()
    Event_11510120()
    Event_11510130()
    Event_11510460()
    Event_11510462()
    Event_11510461()
    Event_11510140()
    Event_11510150()
    Event_151()
    Event_11510215()
    Event_11515060(0, character=Characters.c2870_0000)
    Event_11515060(1, character=Characters.c2870_sen2)
    Event_11515060(2, character=Characters.c2870_0002)
    Event_11515060(3, character=Characters.c2870_0003)
    Event_11515060(4, character=Characters.c2870_0004)
    Event_11515060(5, character=Characters.c2870_0005)
    Event_11515060(6, character=1510406)
    Event_11515060(7, character=1510407)
    Event_11515060(8, character=Characters.c2870_0008)
    Event_11515060(9, character=Characters.c2870_0009)
    Event_11515060(10, character=1510410)
    Event_11515060(11, character=1510411)
    Event_11515060(12, character=Characters.c2870_0012)
    Event_11515060(13, character=Characters.c2870_0013)
    Event_11515080(0, character=1510450, character_1=Characters.c5353_0000)
    Event_11515080(1, character=Characters.c5351_grg2, character_1=Characters.c5353_0001)
    Event_11510260(0, flag=11510251, region=1512251, region_1=1512250)
    Event_11510260(1, flag=11510257, region=1512253, region_1=1512252)
    Event_11510260(2, flag=11510258, region=1512255, region_1=1512254)
    DisableSoundEvent(sound_id=Sounds.OrnsteinSmoughMusic)
    if FlagEnabled(CommonFlags.OrnsteinSmoughDead):
        ForceAnimation(Objects.o5630_0000, 0, loop=True)
        ForceAnimation(Objects.o5620_0000, 0, loop=True)
        Event_11515392()
        DisableObject(Objects.o5860_0000)
        DeleteVFX(VFX.OrnsteinSmoughEntranceFog1, erase_root_only=False)
        DisableObject(Objects.o5861_0000)
        DeleteVFX(VFX.OrnsteinSmoughExitFog1, erase_root_only=False)
        DisableObject(Objects.o5862_0000)
        DeleteVFX(VFX.OrnsteinSmoughExitFog2, erase_root_only=False)
    else:
        Event_11515390()
        Event_11515391()
        Event_11515393()
        Event_11515392()
        Event_11510001()
        Event_11515394()
        Event_11515395()
        Event_11515396()
        Event_11515397()
        Event_11515398()
        Event_11515399()
    DisableSoundEvent(sound_id=Sounds.GwyndolinMusic)
    if FlagEnabled(11510900):
        Event_11515382()
        DisableObject(Objects.o5867_0000)
        DeleteVFX(VFX.GwyndolinEntranceFog1, erase_root_only=False)
        DisableObject(Objects.o5868_0000)
        DeleteVFX(VFX.GwyndolinEntranceFog2, erase_root_only=False)
    else:
        Event_11515380()
        Event_11515381()
        Event_11516388()
        Event_11515383()
        Event_11515382()
        Event_11510900()
        Event_11515384()
        Event_11515385()
        Event_11515386()
    Event_11510450()
    Event_11510710(0, obj_act_id=11510251, character=Characters.c2410_0009, region=1512251, region_1=1512250)
    Event_11510710(1, obj_act_id=11510251, character=Characters.c2410_0014, region=1512251, region_1=1512250)
    Event_11510710(2, obj_act_id=11510251, character=Characters.c2410_0015, region=1512251, region_1=1512250)
    Event_11510710(3, obj_act_id=11510251, character=Characters.c2410_0001, region=1512251, region_1=1512250)
    Event_11510710(4, obj_act_id=11510251, character=Characters.c2410_0000, region=1512251, region_1=1512250)
    Event_11510710(5, obj_act_id=11510251, character=Characters.c2410_0002, region=1512251, region_1=1512250)
    Event_11510710(6, obj_act_id=11510251, character=Characters.c2410_0003, region=1512251, region_1=1512250)
    Event_11510710(7, obj_act_id=11510251, character=Characters.c2410_0004, region=1512251, region_1=1512250)
    Event_11510710(8, obj_act_id=11510251, character=Characters.c2410_0006, region=1512251, region_1=1512250)
    Event_11510710(9, obj_act_id=11510251, character=Characters.c2410_0007, region=1512251, region_1=1512250)
    Event_11510710(10, obj_act_id=11510251, character=Characters.c2410_0010, region=1512251, region_1=1512250)
    Event_11510710(11, obj_act_id=11510251, character=Characters.c2410_0011, region=1512251, region_1=1512250)
    Event_11510710(12, obj_act_id=11510251, character=Characters.c2410_0012, region=1512251, region_1=1512250)
    Event_11510710(13, obj_act_id=11510251, character=Characters.c2410_0013, region=1512251, region_1=1512250)
    Event_11510710(20, obj_act_id=11510257, character=Characters.c2410_0009, region=1512253, region_1=1512252)
    Event_11510710(21, obj_act_id=11510257, character=Characters.c2410_0014, region=1512253, region_1=1512252)
    Event_11510710(22, obj_act_id=11510257, character=Characters.c2410_0015, region=1512253, region_1=1512252)
    Event_11510710(23, obj_act_id=11510257, character=Characters.c2410_0001, region=1512253, region_1=1512252)
    Event_11510710(24, obj_act_id=11510257, character=Characters.c2410_0000, region=1512253, region_1=1512252)
    Event_11510710(25, obj_act_id=11510257, character=Characters.c2410_0002, region=1512253, region_1=1512252)
    Event_11510710(26, obj_act_id=11510257, character=Characters.c2410_0003, region=1512253, region_1=1512252)
    Event_11510710(27, obj_act_id=11510257, character=Characters.c2410_0004, region=1512253, region_1=1512252)
    Event_11510710(28, obj_act_id=11510257, character=Characters.c2410_0006, region=1512253, region_1=1512252)
    Event_11510710(29, obj_act_id=11510257, character=Characters.c2410_0007, region=1512253, region_1=1512252)
    Event_11510710(30, obj_act_id=11510257, character=Characters.c2410_0010, region=1512253, region_1=1512252)
    Event_11510710(31, obj_act_id=11510257, character=Characters.c2410_0011, region=1512253, region_1=1512252)
    Event_11510710(32, obj_act_id=11510257, character=Characters.c2410_0012, region=1512253, region_1=1512252)
    Event_11510710(33, obj_act_id=11510257, character=Characters.c2410_0013, region=1512253, region_1=1512252)
    Event_11510710(40, obj_act_id=11510258, character=Characters.c2410_0009, region=1512255, region_1=1512254)
    Event_11510710(41, obj_act_id=11510258, character=Characters.c2410_0014, region=1512255, region_1=1512254)
    Event_11510710(42, obj_act_id=11510258, character=Characters.c2410_0015, region=1512255, region_1=1512254)
    Event_11510710(43, obj_act_id=11510258, character=Characters.c2410_0001, region=1512255, region_1=1512254)
    Event_11510710(44, obj_act_id=11510258, character=Characters.c2410_0000, region=1512255, region_1=1512254)
    Event_11510710(45, obj_act_id=11510258, character=Characters.c2410_0002, region=1512255, region_1=1512254)
    Event_11510710(46, obj_act_id=11510258, character=Characters.c2410_0003, region=1512255, region_1=1512254)
    Event_11510710(47, obj_act_id=11510258, character=Characters.c2410_0004, region=1512255, region_1=1512254)
    Event_11510710(48, obj_act_id=11510258, character=Characters.c2410_0006, region=1512255, region_1=1512254)
    Event_11510710(49, obj_act_id=11510258, character=Characters.c2410_0007, region=1512255, region_1=1512254)
    Event_11510710(50, obj_act_id=11510258, character=Characters.c2410_0010, region=1512255, region_1=1512254)
    Event_11510710(51, obj_act_id=11510258, character=Characters.c2410_0011, region=1512255, region_1=1512254)
    Event_11510710(52, obj_act_id=11510258, character=Characters.c2410_0012, region=1512255, region_1=1512254)
    Event_11510710(53, obj_act_id=11510258, character=Characters.c2410_0013, region=1512255, region_1=1512254)
    Event_11515200(0, character=Characters.c2780_0000)
    Event_11515210(0, character=Characters.c2780_0000)
    Event_11515220(0, character=Characters.c2780_0000)
    Event_11515230(0, character=Characters.c2780_0000)
    Event_11515240(0, character=Characters.c2780_0000, region=1512010)
    Event_11510850(0, character=Characters.c2780_0000)
    Event_11515190(0, character=Characters.c2780_0000)
    Event_11515200(1, character=Characters.c2780_0001)
    Event_11515210(1, character=Characters.c2780_0001)
    Event_11515220(1, character=Characters.c2780_0001)
    Event_11515230(1, character=Characters.c2780_0001)
    Event_11515240(1, character=Characters.c2780_0001, region=1512011)
    Event_11510850(1, character=Characters.c2780_0001)
    Event_11515190(1, character=Characters.c2780_0001)
    Event_11515200(2, character=Characters.c2780_0002)
    Event_11515210(2, character=Characters.c2780_0002)
    Event_11515220(2, character=Characters.c2780_0002)
    Event_11515230(2, character=Characters.c2780_0002)
    Event_11515240(2, character=Characters.c2780_0002, region=1512012)
    Event_11510850(2, character=Characters.c2780_0002)
    Event_11515190(2, character=Characters.c2780_0002)
    Event_11515200(3, character=Characters.c2780_0003)
    Event_11515210(3, character=Characters.c2780_0003)
    Event_11515220(3, character=Characters.c2780_0003)
    Event_11515230(3, character=Characters.c2780_0003)
    Event_11515240(3, character=Characters.c2780_0003, region=1512013)
    Event_11510850(3, character=Characters.c2780_0003)
    Event_11515190(3, character=Characters.c2780_0003)
    Event_11510600(1, obj=Objects.o0110_0001, obj_act_id=11510601)
    Event_11510600(2, obj=Objects.o0110_0002, obj_act_id=11510602)
    Event_11510600(3, obj=Objects.o0110_0003, obj_act_id=11510603)
    Event_11510600(4, obj=Objects.o0110_0004, obj_act_id=11510604)
    Event_11510600(6, obj=Objects.o0110_0006, obj_act_id=11510606)
    Event_11510600(7, obj=Objects.o0110_0007, obj_act_id=11510607)
    Event_11510600(8, obj=Objects.o0110_0008, obj_act_id=11510608)
    Event_11510600(9, obj=Objects.o0110_0009, obj_act_id=11510609)
    Event_11510600(10, obj=Objects.o0110_0010, obj_act_id=11510610)
    Event_11510600(11, obj=Objects.o0110_0011, obj_act_id=11510611)
    Event_11510600(12, obj=Objects.o0110_0012, obj_act_id=11510612)
    Event_11510600(15, obj=Objects.o0110_0015, obj_act_id=11510615)
    Event_11510600(16, obj=Objects.o0110_0016, obj_act_id=11510616)
    Event_11510600(17, obj=Objects.o0110_0017, obj_act_id=11510617)
    Event_11510600(18, obj=Objects.o0110_0018, obj_act_id=11510618)
    Event_11510600(19, obj=Objects.o0110_0019, obj_act_id=11510619)
    Event_11510860(0, character=1510250, item_lot=0)
    Event_11510860(1, character=1510450, item_lot=0)
    Event_11510860(2, character=Characters.c5351_grg2, item_lot=0)
    Event_11510860(3, character=Characters.c0000_0012, item_lot=0)
    Event_11510860(4, character=Characters.c0000_0013, item_lot=0)
    Event_11510860(5, character=Characters.c0000_drk3, item_lot=0)
    Event_11510860(6, character=Characters.c0000_drk1, item_lot=0)
    Event_11510860(7, character=Characters.c0000_drk2, item_lot=0)
    Event_11510860(8, character=Characters.c0000_drg1, item_lot=68070000)
    Event_11510860(9, character=Characters.c0000_ano1, item_lot=0)
    Event_11515843(0, flag=11510902, line_intersects=1511990, anchor_entity=1512998, target_entity=1512997)
    Event_11515846(0, flag=11510902, obj=Objects.o5860_0000, vfx_id=VFX.OrnsteinSmoughEntranceFog1)
    Event_11515843(1, flag=11510903, line_intersects=1511990, anchor_entity=1512998, target_entity=1512997)
    Event_11515846(1, flag=11510903, obj=Objects.o5860_0000, vfx_id=VFX.OrnsteinSmoughEntranceFog1)
    Event_11515843(2, flag=11510900, line_intersects=1511890, anchor_entity=1512898, target_entity=1512897)
    Event_11515846(2, flag=11510900, obj=Objects.o5867_0000, vfx_id=VFX.GwyndolinEntranceFog1)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0012, event_flag=8258)
    HumanityRegistration(Characters.c0000_0013, event_flag=8266)
    HumanityRegistration(Characters.c0000_0011, event_flag=CommonFlags.SolaireHumanityFlag)
    Event_11515030()
    Event_11515029()
    Event_11515032()
    Event_11515033()
    Event_11515990(0, flag=11515031, summoned_character=Characters.c0000_0011)
    HumanityRegistration(Characters.c0000_0006, event_flag=CommonFlags.SolaireHumanityFlag)
    SkipLinesIfFlagEnabled(2, 1008)
    SkipLinesIfFlagEnabled(1, 1004)
    DisableCharacter(Characters.c0000_0006)
    Event_11510510(0, character=Characters.c0000_0006, flag=1004)
    Event_11510520(0, character=Characters.c0000_0006, first_flag=1000, last_flag=1029, flag=1005)
    Event_11510530(0, character=Characters.c0000_0006, first_flag=1000, last_flag=1029, flag=1008)
    HumanityRegistration(Characters.c0000_0003, event_flag=8318)
    Event_11510501(0, character=Characters.c0000_0003, flag=1033)
    Event_11510520(1, character=Characters.c0000_0003, first_flag=1030, last_flag=1036, flag=1034)
    Event_11510531(0, character=Characters.c0000_0003, first_flag=1030, last_flag=1036, flag=1036)
    Event_11510532(0, character=Characters.c0000_0003, first_flag=1030, last_flag=1036, flag=1031)
    Event_11510533(0, character=Characters.c0000_0003)
    DisableCharacter(Characters.c5310_0000)
    Event_11510520(2, character=Characters.c5310_0000, first_flag=1230, last_flag=1239, flag=1232)
    SetTeamType(Characters.c5320_0000, TeamType.Ally)
    SkipLinesIfFlagRangeAnyEnabled(1, (1240, 1249))
    EnableFlag(1240)
    Event_11510520(3, character=Characters.c5320_0000, first_flag=1240, last_flag=1249, flag=1242)
    Event_11510502(0, character=Characters.c5320_0000, flag=1241)
    Event_11515090(0, character=Characters.c2860_0000)
    Event_11515091(0, character=Characters.c2860_0000)
    Event_11515092(0, character=Characters.c2860_0000, obj=Objects.o5965_0000, flag=1361, flag_1=1362)
    Event_11510510(4, character=Characters.c2860_0000, flag=1361)
    Event_11510520(4, character=Characters.c2860_0000, first_flag=1360, last_flag=1363, flag=1362)
    HumanityRegistration(Characters.c0000_0005, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1494)
    SkipLinesIfFlagEnabled(1, 1493)
    DisableCharacter(Characters.c0000_0005)
    Event_11510510(5, character=Characters.c0000_0005, flag=1512)
    Event_11510520(5, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1513)
    Event_11510535(0, character=Characters.c0000_0005, first_flag=1490, last_flag=1514, flag=1494)
    Event_11510536(0, character=Characters.c0000_0005)
    HumanityRegistration(Characters.c0000_0004, event_flag=CommonFlags.LautrecHumanityFlag)
    HumanityRegistration(Characters.c0000_0009, event_flag=8908)
    HumanityRegistration(Characters.c0000_0010, event_flag=8916)
    DisableCharacter(Characters.c0000_0004)
    DisableCharacter(Characters.c0000_0009)
    DisableCharacter(Characters.c0000_0010)
    Event_11510541(0, character=Characters.c0000_0004, first_flag=1570, last_flag=1599, flag=1578)
    Event_11510542(0, character=Characters.c0000_0004, first_flag=1570, last_flag=1599, flag=1575)
    Event_11510543(0, character=Characters.c0000_0004, first_flag=1570, last_flag=1599, flag=1572)
    Event_11510544(0, character=Characters.c0000_0004, first_flag=1570, last_flag=1599, flag=1575)


@ContinueOnRest(11510992)
def Event_11510992():
    """Event 11510992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c5270_0000, 7100)
    AddSpecialEffect(Characters.c5271_0000, 7100)
    AddSpecialEffect(Characters.c2360_0000, 7100)
    AddSpecialEffect(Characters.c2360_0001, 7100)
    AddSpecialEffect(Characters.c5320_0000, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c5270_0000, 7100)
    RemoveSpecialEffect(Characters.c5271_0000, 7100)
    RemoveSpecialEffect(Characters.c2360_0000, 7100)
    RemoveSpecialEffect(Characters.c2360_0001, 7100)
    RemoveSpecialEffect(Characters.c5320_0000, 7100)
    Restart()


@ContinueOnRest(11510998)
def Event_11510998():
    """Event 11510998"""
    SkipLinesIfFlagDisabled(3, 11012998)
    SkipLinesIfFlagEnabled(2, 11010868)
    SkipLinesIfFlagEnabled(1, 11300861)
    SkipLinesIfFlagDisabled(2, 11512998)
    DisableCharacter(Characters.c0000_ano1)
    End()
    OR_1.Add(FlagEnabled(11517900))
    OR_1.Add(FlagEnabled(11517910))
    OR_1.Add(FlagEnabled(11517920))
    OR_1.Add(FlagEnabled(11517930))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11512998)


@ContinueOnRest(11510997)
def Event_11510997():
    """Event 11510997"""
    if FlagDisabled(11012997):
        AND_1.Add(Attacked(attacked_entity=Characters.c0000_ano1, attacker=PLAYER))
        AND_1.Add(HealthRatio(Characters.c0000_ano1) <= 0.75)
    
        MAIN.Await(AND_1)
    
        EnableFlag(11012997)
        EnableFlag(744)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_ano1, team_type=TeamType.HostileAlly)


@ContinueOnRest(11510999)
def Event_11510999():
    """Event 11510999"""
    OR_1.Add(EntityWithinDistance(entity=Characters.c0000_drg1, other_entity=PLAYER, radius=5.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c0000_drg1, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetTeamType(Characters.c0000_drg1, TeamType.Enemy)


@ContinueOnRest(11510090)
def Event_11510090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11510090"""
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


@RestartOnRest(11515040)
def Event_11515040():
    """Event 11515040"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2870_0014)
        DisableCharacter(Characters.c2870_0015)
        DisableCharacter(Characters.c2870_0016)
        DisableCharacter(Characters.c2410_0016)
        DisableCharacter(Characters.c2410_0017)
        DisableCharacter(Characters.c2410_0018)
        DisableCharacter(Characters.c2410_0019)
        DisableCharacter(Characters.c2410_0020)
        DisableCharacter(Characters.c2410_0021)
        DisableCharacter(Characters.c2410_0022)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11515041)
def Event_11515041():
    """Event 11515041"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2870_0014)
    Kill(Characters.c2870_0015)
    Kill(Characters.c2870_0016)
    Kill(Characters.c2410_0016)
    Kill(Characters.c2410_0017)
    Kill(Characters.c2410_0018)
    Kill(Characters.c2410_0019)
    Kill(Characters.c2410_0020)
    Kill(Characters.c2410_0021)
    Kill(Characters.c2410_0022)


@RestartOnRest(11515042)
def Event_11515042():
    """Event 11515042"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=ANOR_LONDO))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11510050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=ANOR_LONDO))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11510050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=ANOR_LONDO))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11510050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=ANOR_LONDO))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11510050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=ANOR_LONDO))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11510050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=ANOR_LONDO))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11510050))
    if not OR_6:
        return RESTART
    EnableFlag(11510050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=ANOR_LONDO))
    if not AND_7:
        return RESTART
    DisableFlag(11510050)
    EnableFlag(11515045)


@ContinueOnRest(11515380)
def Event_11515380():
    """Event 11515380"""
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1511890,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(743)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@ContinueOnRest(11515381)
def Event_11515381():
    """Event 11515381"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(FlagEnabled(11515383))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        boss_version=True,
        line_intersects=1511890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    if FlagDisabled(CommonFlags.DarkAnorLondo):
        PlayCutscene(
            150151,
            cutscene_flags=CutsceneFlags.Unskippable,
            player_id=10000,
            move_to_region=1512901,
            game_map=ANOR_LONDO,
        )
    else:
        PlayCutscene(
            150156,
            cutscene_flags=CutsceneFlags.Unskippable,
            player_id=10000,
            move_to_region=1512901,
            game_map=ANOR_LONDO,
        )
    WaitFrames(frames=1)
    EnableCharacter(Characters.c5320_0000)
    EnableFlag(11515388)
    Restart()


@ContinueOnRest(11516388)
def Event_11516388():
    """Event 11516388"""
    AND_1.Add(FlagEnabled(11515388))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 7410)
    DisableFlag(11515388)
    Restart()


@ContinueOnRest(11515383)
def Event_11515383():
    """Event 11515383"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11510900))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1512896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.c5320_0000, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(Characters.c5320_0000)


@RestartOnRest(11515382)
def Event_11515382():
    """Event 11515382"""
    if FlagEnabled(11510900):
        DisableCharacter(Characters.c5320_0000)
        End()
    DisableAI(Characters.c5320_0000)
    AND_1.Add(FlagEnabled(11515383))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512896))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11515386)
    
    MAIN.Await(FlagEnabled(11515387))
    
    SkipLinesIfClient(2)
    ForceAnimation(PLAYER, -1)
    ResetAnimation(PLAYER, disable_interpolation=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(PlayerCovenant(Covenant.DarkmoonBlade))
    SkipLinesIfConditionFalse(6, AND_2)
    BetrayCurrentCovenant()
    if FlagDisabled(9002):
        IncrementPvPSin()
        EnableFlag(9002)
    EnableFlag(742)
    SaveRequest()
    EnableAI(Characters.c5320_0000)
    SetTeamType(Characters.c5320_0000, TeamType.Boss)
    EnableBossHealthBar(Characters.c5320_0000, name=5320)


@ContinueOnRest(11510900)
def Event_11510900():
    """Event 11510900"""
    MAIN.Await(HealthRatio(Characters.c5320_0000) <= 0.0)
    
    WaitFrames(frames=1)
    SkipLinesIfClient(7)
    EnableFlag(11515389)
    
    MAIN.Await(FlagEnabled(11515389))
    
    if FlagDisabled(CommonFlags.DarkAnorLondo):
        PlayCutscene(150152, cutscene_flags=0, player_id=10000, move_to_region=1512897, game_map=ANOR_LONDO)
    else:
        PlayCutscene(150157, cutscene_flags=0, player_id=10000, move_to_region=1512897, game_map=ANOR_LONDO)
    EnableFlag(4047)
    WaitFrames(frames=10)
    if FlagEnabled(CommonFlags.OrnsteinSmoughDead):
        EnableFlag(120)
    EnableFlag(11510900)
    KillBoss(game_area_param_id=1510650)
    DisableObject(Objects.o5867_0000)
    DeleteVFX(VFX.GwyndolinEntranceFog1)
    if Client():
        return
    DisableFlag(11807170)
    DisableFlag(11807180)
    DisableFlag(11807190)
    DisableFlag(11807230)
    AwardAchievement(achievement_id=39)


@ContinueOnRest(11515384)
def Event_11515384():
    """Event 11515384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(FlagEnabled(11515382))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.GwyndolinMusic)


@ContinueOnRest(11515385)
def Event_11515385():
    """Event 11515385"""
    DisableNetworkSync()
    AND_1.Add(HealthRatio(Characters.c5320_0000) <= 0.0)
    AND_1.Add(FlagEnabled(11515384))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.GwyndolinMusic)


@RestartOnRest(11515386)
def Event_11515386():
    """Event 11515386"""
    AND_1.Add(ThisEventFlagEnabled())
    AND_1.Add(FlagEnabled(CommonFlags.DarkAnorLondo))
    AND_1.Add(Host())
    AND_2.Add(ThisEventFlagEnabled())
    AND_2.Add(Host())
    AND_2.Add(PlayerCovenant(Covenant.DarkmoonBlade))
    AND_3.Add(ThisEventFlagEnabled())
    AND_3.Add(Host())
    AND_3.Add(not AND_1)
    AND_3.Add(not AND_2)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_2.Add(CharacterType(PLAYER, character_type=CharacterType.Intruder))
    if OR_2:
        return
    SkipLinesIfFinishedConditionFalse(10, input_condition=AND_1)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(150155, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150155,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1512900,
        game_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150155, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()
    SkipLinesIfFinishedConditionFalse(10, input_condition=AND_2)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(150161, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150161,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1512900,
        game_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150161, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(150160, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150160,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1512900,
        game_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150160, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()


@ContinueOnRest(11515390)
def Event_11515390():
    """Event 11515390"""
    AND_1.Add(FlagDisabled(CommonFlags.OrnsteinSmoughDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1511990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11515391)
def Event_11515391():
    """Event 11515391"""
    AND_1.Add(FlagDisabled(CommonFlags.OrnsteinSmoughDead))
    AND_1.Add(FlagEnabled(11515393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11515393)
def Event_11515393():
    """Event 11515393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.OrnsteinSmoughDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1512996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5270_0000)
    ActivateMultiplayerBuffs(Characters.c5271_0000)
    ActivateMultiplayerBuffs(Characters.c2360_0000)
    ActivateMultiplayerBuffs(Characters.c2360_0001)


@RestartOnRest(11515392)
def Event_11515392():
    """Event 11515392"""
    if FlagEnabled(CommonFlags.OrnsteinSmoughDead):
        DisableCharacter(Characters.c5270_0000)
        DisableCharacter(Characters.c5271_0000)
        DisableCharacter(Characters.c2360_0000)
        DisableCharacter(Characters.c2360_0001)
        Kill(Characters.c5270_0000)
        Kill(Characters.c5271_0000)
        Kill(Characters.c2360_0000)
        Kill(Characters.c2360_0001)
        End()
    DisableCharacter(Characters.c5271_0000)
    DisableCharacter(Characters.c2360_0001)
    DisableBackread(Characters.c5271_0000)
    if FlagDisabled(11510000):
        DisableCharacter(Characters.c5270_0000)
    DisableAI(Characters.c5270_0000)
    DisableAI(Characters.c2360_0000)
    AND_1.Add(FlagEnabled(11515393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512990))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Intruder))
    if OR_1:
        return
    SkipLinesIfFlagEnabled(8, 11510000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150140, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150140, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(Characters.c5270_0000)
    EnableCharacter(Characters.c2360_0000)
    EnableFlag(11510000)
    EnableAI(Characters.c5270_0000)
    EnableAI(Characters.c2360_0000)
    EnableBossHealthBar(Characters.c5270_0000, name=5270, bar_slot=1)
    EnableBossHealthBar(Characters.c2360_0000, name=2360)


@ContinueOnRest(11510001)
def Event_11510001():
    """Event 11510001"""
    DisableObject(Objects.o0200_0002)
    AND_1.Add(CharacterDead(Characters.c5270_0000))
    AND_2.Add(CharacterDead(Characters.c2360_0000))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(10, input_condition=AND_1)
    
    MAIN.Await(CharacterDead(Characters.c5271_0000))
    
    EnableFlag(11510902)
    PlaySoundEffect(Characters.c5271_0000, 777777777, sound_type=SoundType.s_SFX)
    Kill(Characters.c2360_0001)
    KillBoss(game_area_param_id=1510801)
    DisableFlag(11807100)
    DisableFlag(11807110)
    DisableFlag(11807120)
    DisableFlag(11807130)
    SkipLines(9)
    
    MAIN.Await(CharacterDead(Characters.c2360_0001))
    
    EnableFlag(11510903)
    PlaySoundEffect(Characters.c2360_0001, 777777777, sound_type=SoundType.s_SFX)
    Kill(Characters.c5271_0000)
    KillBoss(game_area_param_id=1510811)
    DisableFlag(11807060)
    DisableFlag(11807070)
    DisableFlag(11807080)
    DisableFlag(11807090)
    EnableFlag(CommonFlags.OrnsteinSmoughDead)
    EnableFlag(120)
    DisableObject(Objects.o5860_0000)
    DeleteVFX(VFX.OrnsteinSmoughEntranceFog1)
    DisableObject(Objects.o5861_0000)
    DeleteVFX(VFX.OrnsteinSmoughExitFog1)
    DisableObject(Objects.o5862_0000)
    DeleteVFX(VFX.OrnsteinSmoughExitFog2)
    EnableObject(Objects.o0200_0002)
    RegisterBonfire(bonfire_flag=11510920, obj=Objects.o0200_0002)
    DisableNetworkSync()
    Wait(3.0)
    ForceAnimation(Objects.o5630_0000, 0, loop=True)
    ForceAnimation(Objects.o5620_0000, 0, loop=True)


@ContinueOnRest(11515394)
def Event_11515394():
    """Event 11515394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.OrnsteinSmoughDead))
    AND_1.Add(FlagEnabled(11515392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11515391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.OrnsteinSmoughMusic)
    EnableBackread(Characters.c5271_0000)


@ContinueOnRest(11515395)
def Event_11515395():
    """Event 11515395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.OrnsteinSmoughDead))
    AND_1.Add(FlagEnabled(11515394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.OrnsteinSmoughMusic)


@ContinueOnRest(11515396)
def Event_11515396():
    """Event 11515396"""
    AND_1.Add(CharacterDead(Characters.c5270_0000))
    AND_2.Add(CharacterDead(Characters.c2360_0000))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(12, input_condition=AND_2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150121, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150121, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(Characters.c5270_0000)
    DisableCharacter(Characters.c2360_0000)
    DisableImmortality(Characters.c2360_0000)
    Kill(Characters.c2360_0000)
    EnableCharacter(Characters.c2360_0001)
    EnableBossHealthBar(Characters.c2360_0001, name=2360)
    End()
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150120, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150120, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(Characters.c2360_0000)
    DisableCharacter(Characters.c5270_0000)
    DisableImmortality(Characters.c5270_0000)
    Kill(Characters.c5270_0000)
    EnableCharacter(Characters.c5271_0000)
    EnableBossHealthBar(Characters.c5271_0000, name=5270, bar_slot=1)


@ContinueOnRest(11515397)
def Event_11515397():
    """Event 11515397"""
    AND_1.Add(HealthRatio(Characters.c5270_0000) <= 0.0)
    AND_2.Add(HealthRatio(Characters.c2360_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    EnableImmortality(Characters.c2360_0000)
    End()
    EnableImmortality(Characters.c5270_0000)


@RestartOnRest(11515398)
def Event_11515398():
    """Event 11515398"""
    AND_1.Add(CharacterDead(Characters.c2360_0000))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2360_0000))
    
    CreateNPCPart(
        Characters.c2360_0000,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(Characters.c2360_0000, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(Characters.c2360_0000, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    
    MAIN.Await(HealthRatio(Characters.c2360_0000) <= 0.0)
    
    SetNPCPartHealth(Characters.c2360_0000, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515399)
def Event_11515399():
    """Event 11515399"""
    AND_1.Add(CharacterDead(Characters.c2360_0001))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2360_0001))
    
    CreateNPCPart(
        Characters.c2360_0001,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(Characters.c2360_0001, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(Characters.c2360_0001, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    
    MAIN.Await(HealthRatio(Characters.c2360_0001) <= 0.0)
    
    SetNPCPartHealth(Characters.c2360_0001, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515060)
def Event_11515060(_, character: Character | int):
    """Event 11515060"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(
        character,
        npc_part_id=2870,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(character, npc_part_id=2870, desired_scaling=0.0)
    SetNPCPartEffects(character, npc_part_id=2870, material_sfx_id=50, material_vfx_id=50)
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    SetNPCPartHealth(character, npc_part_id=2870, desired_health=0, overwrite_max=False)


@RestartOnRest(11515080)
def Event_11515080(_, character: int, character_1: int):
    """Event 11515080"""
    DisableCharacter(character_1)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
        AddSpecialEffect(character, 5434)
        AICommand(character, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(character, npc_part_id=5351, part_index=NPCPartType.Part1, part_health=65)
    AND_1.Add(CharacterPartHealth(character, npc_part_id=5351) <= 0)
    AND_2.Add(HealthRatio(character) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(character)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=110,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    ForceAnimation(character, 8000)
    ForceAnimation(character_1, 8100)
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, 5434)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)
    if ValueNotEqual(left=character, right=1510450):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(53530000, host_only=True)


@ContinueOnRest(11510100)
def Event_11510100():
    """Event 11510100"""
    if ThisEventFlagEnabled():
        PostDestruction(Objects.o5810_0000)
        PostDestruction(Objects.o5801_0000)
        EndOfAnimation(obj=Objects.o0500_0000, animation_id=111)
        EndOfAnimation(obj=Objects.o5800_0000, animation_id=0)
        EndOfAnimation(obj=Objects.o5801_0000, animation_id=1)
        EnableObjectInvulnerability(Objects.o5800_0000)
        EnableTreasure(obj=Objects.o0500_0000)
        End()
    DisableTreasure(obj=Objects.o0500_0000)
    SkipLinesIfClient(1)
    CreateObjectVFX(Objects.o0500_0000, vfx_id=90, model_point=99010)
    ForceAnimation(Objects.o0500_0000, 110, loop=True)
    
    MAIN.Await(ObjectDestroyed(Objects.o5810_0000))
    
    ForceAnimation(Objects.o0500_0000, 111)
    ForceAnimation(Objects.o5800_0000, 0)
    ForceAnimation(Objects.o5801_0000, 0, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(Objects.o0500_0000)
    EnableTreasure(obj=Objects.o0500_0000)
    DestroyObject(Objects.o5801_0000)


@ContinueOnRest(11510110)
def Event_11510110():
    """Event 11510110"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o5730_0000, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5730_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(
        PLAYER,
        destination=Objects.o5730_0000,
        destination_type=CoordEntityType.Object,
        model_point=120,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o5730_0000, 0)


@ContinueOnRest(11510200)
def Event_11510200():
    """Event 11510200"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(Objects.o5760_0000, obj_act_id=-1)
        EndOfAnimation(obj=Objects.o5700_0000, animation_id=0)
        EndOfAnimation(obj=Objects.o5760_0000, animation_id=0)
        End()
    AND_1.Add(FlagDisabled(11510700))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5760_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=Objects.o5760_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5760_0000, 0, wait_for_completion=True)
    ForceAnimation(Objects.o5700_0000, 0)


@ContinueOnRest(11510201)
def Event_11510201():
    """Event 11510201"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510200))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1512000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511000,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160)
    Restart()


@ContinueOnRest(11510210)
def Event_11510210():
    """Event 11510210"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o5710_0000, animation_id=0)
        End()
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_BlacksmithGate, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5710_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(
        PLAYER,
        destination=Objects.o5710_0000,
        destination_type=CoordEntityType.Object,
        model_point=121,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(Objects.o5710_0000, 0)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_BlacksmithGate, navmesh_type=NavmeshType.Solid)


@ContinueOnRest(11510211)
def Event_11510211():
    """Event 11510211"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510210))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5710_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=Objects.o5710_0000)
    Restart()


@ContinueOnRest(11510220)
def Event_11510220():
    """Event 11510220"""
    if ThisEventFlagDisabled():
        MAIN.Await(CharacterInsideRegion(PLAYER, region=1512350))
    ForceAnimation(Objects.o5600_0000, 0)


@ContinueOnRest(11510260)
def Event_11510260(_, flag: Flag | int, region: Region | int, region_1: Region | int):
    """Event 11510260"""
    DisableNetworkSync()
    if FlagDisabled(flag):
        MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
        AddSpecialEffect(PLAYER, 4150)
        Wait(3.0)
        Restart()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@ContinueOnRest(11510710)
def Event_11510710(_, obj_act_id: Flag | int, character: int, region: Region | int, region_1: Region | int):
    """Event 11510710"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
        EnableFlag(obj_act_id)
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterInsideRegion(character, region=region_1))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, 4150)
    Wait(3.0)
    Restart()


@ContinueOnRest(11510300)
def Event_11510300():
    """Event 11510300"""
    AND_1.Add(FlagDisabled(11510301))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11510303))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagEnabled(11510305))
    AND_3.Add(FlagDisabled(11510303))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_4.Add(FlagEnabled(11510305))
    AND_4.Add(FlagEnabled(11510303))
    AND_4.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_5.Add(FlagEnabled(11510305))
    AND_5.Add(FlagDisabled(11510301))
    AND_5.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_6.Add(FlagEnabled(11510305))
    AND_6.Add(FlagDisabled(11510302))
    AND_6.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11515300)
    SkipLinesIfFlagEnabled(20, 11510305)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5610_0000, 10, wait_for_completion=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        cutscene_id=150100,
        cutscene_flags=0,
        player_id=10000,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(4)
    SkipLinesIfFlagDisabled(2, 11510304)
    PlayCutscene(
        cutscene_id=150100,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(1)
    PlayCutscene(150100, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EndOfAnimation(obj=Objects.o5610_0000, animation_id=0)
    DisableMapCollision(collision=Collisions.h0010B1_0000)
    EnableMapCollision(collision=Collisions.h0010B1_0001)
    DisableFlag(11510303)
    EnableFlag(11510302)
    DisableFlag(11510304)
    EnableFlag(11510305)
    DisableFlag(11515300)
    Restart()
    SkipLinesIfFlagDisabled(33, 11510303)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        0,
        animation_id=0,
        collision=Collisions.h0010B1_0000,
        collision_1=Collisions.h0010B1_0001,
        flag=11510303,
        flag_1=11510302,
        frames=180,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_4)
    Move(
        PLAYER,
        destination=Objects.o5750_0002,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0002, 1)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        1,
        animation_id=0,
        collision=Collisions.h0010B1_0000,
        collision_1=Collisions.h0010B1_0001,
        flag=11510303,
        flag_1=11510302,
        frames=180,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_5)
    Move(
        PLAYER,
        destination=Objects.o5750_0003,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0003, 1)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        0,
        animation_id=0,
        animation_id_1=1,
        collision=Collisions.h0010B1_0002,
        flag=11510303,
        flag_1=11510301,
        animation_id_2=11,
        frames=180,
        frames_1=360,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_6)
    Move(
        PLAYER,
        destination=Objects.o5750_0004,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0004, 1)
    ForceAnimation(Objects.o5610_0000, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        2,
        animation_id=0,
        collision=Collisions.h0010B1_0000,
        collision_1=Collisions.h0010B1_0001,
        flag=11510303,
        flag_1=11510302,
        frames=180,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(32, 11510302)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(Objects.o5610_0000, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        3,
        animation_id=1,
        collision=Collisions.h0010B1_0001,
        collision_1=Collisions.h0010B1_0002,
        flag=11510302,
        flag_1=11510301,
        frames=360,
    )
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=101,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(Objects.o5610_0000, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        4,
        animation_id=3,
        collision=Collisions.h0010B1_0001,
        collision_1=Collisions.h0010B1_0000,
        flag=11510302,
        flag_1=11510303,
        frames=180,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_3)
    Move(
        PLAYER,
        destination=Objects.o5750_0001,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0001, 1)
    ForceAnimation(Objects.o5610_0000, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        5,
        animation_id=3,
        collision=Collisions.h0010B1_0001,
        collision_1=Collisions.h0010B1_0000,
        flag=11510302,
        flag_1=11510303,
        frames=180,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_5)
    Move(
        PLAYER,
        destination=Objects.o5750_0003,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0003, 1)
    ForceAnimation(Objects.o5610_0000, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        6,
        animation_id=1,
        collision=Collisions.h0010B1_0001,
        collision_1=Collisions.h0010B1_0002,
        flag=11510302,
        flag_1=11510301,
        frames=360,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(25, 11510301)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    Move(
        PLAYER,
        destination=Objects.o5610_0000,
        destination_type=CoordEntityType.Object,
        model_point=101,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(Objects.o5610_0000, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        7,
        animation_id=2,
        collision=Collisions.h0010B1_0002,
        collision_1=Collisions.h0010B1_0001,
        flag=11510301,
        flag_1=11510302,
        frames=360,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_3)
    Move(
        PLAYER,
        destination=Objects.o5750_0001,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0001, 1)
    ForceAnimation(Objects.o5610_0000, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        1,
        animation_id=2,
        animation_id_1=3,
        collision=Collisions.h0010B1_0000,
        flag=11510301,
        flag_1=11510303,
        animation_id_2=13,
        frames=360,
        frames_1=180,
    )
    SkipLinesIfFinishedConditionFalse(7, input_condition=AND_6)
    Move(
        PLAYER,
        destination=Objects.o5750_0004,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(Objects.o5750_0004, 1)
    ForceAnimation(Objects.o5610_0000, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        8,
        animation_id=2,
        collision=Collisions.h0010B1_0002,
        collision_1=Collisions.h0010B1_0001,
        flag=11510301,
        flag_1=11510302,
        frames=360,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11510319)
def Event_11510319():
    """Event 11510319"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1512310))
    
    EnableFlag(11510304)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1512310))
    
    DisableFlag(11510304)
    Restart()


@ContinueOnRest(11515320)
def Event_11515320(
    _,
    animation_id: int,
    collision: Collision | int,
    collision_1: Collision | int,
    flag: Flag | int,
    flag_1: Flag | int,
    frames: int,
):
    """Event 11515320"""
    DisableMapCollision(collision=collision)
    EnableObject(Objects.o5611_0000)
    ForceAnimation(Objects.o5610_0000, animation_id)
    ForceAnimation(Objects.o5611_0000, animation_id)
    WaitFrames(frames=frames)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    DisableObject(Objects.o5611_0000)
    EnableMapCollision(collision=collision_1)
    DisableFlag(flag)
    EnableFlag(flag_1)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


@ContinueOnRest(11515330)
def Event_11515330(
    _,
    animation_id: int,
    animation_id_1: int,
    collision: Collision | int,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id_2: int,
    frames: int,
    frames_1: int,
):
    """Event 11515330"""
    DisableMapCollision(collision=Collisions.h0010B1_0002)
    DisableMapCollision(collision=Collisions.h0010B1_0001)
    DisableMapCollision(collision=Collisions.h0010B1_0000)
    EnableObject(Objects.o5611_0000)
    ForceAnimation(Objects.o5610_0000, animation_id)
    ForceAnimation(Objects.o5611_0000, animation_id)
    WaitFrames(frames=frames)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    ForceAnimation(Objects.o5610_0000, animation_id_2)
    WaitFrames(frames=130)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    ForceAnimation(Objects.o5610_0000, animation_id_1)
    ForceAnimation(Objects.o5611_0000, animation_id_1)
    WaitFrames(frames=frames_1)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    DisableObject(Objects.o5611_0000)
    EnableMapCollision(collision=collision)
    DisableFlag(flag)
    EnableFlag(flag_1)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


@ContinueOnRest(11510340)
def Event_11510340():
    """Event 11510340"""
    if FlagEnabled(11515300):
        EnableMapCollision(collision=Collisions.h9000B1_0000)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge00, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge01, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge02, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge03, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge04, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagDisabled(11515300))
    
        Restart()
    if FlagEnabled(11510303):
        EnableMapCollision(collision=Collisions.h9000B1_0000)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge00, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge01, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge02, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge03, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge04, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    if FlagEnabled(11510302):
        DisableMapCollision(collision=Collisions.h9000B1_0000)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge00, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge01, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge02, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge03, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge04, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    if FlagEnabled(11510301):
        EnableMapCollision(collision=Collisions.h9000B1_0000)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge00, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge01, navmesh_type=NavmeshType.Solid)
        EnableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge02, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge03, navmesh_type=NavmeshType.Solid)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_RotatingBridge04, navmesh_type=NavmeshType.Solid)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    DisplayDialog(text=10010105)
    Restart()


@ContinueOnRest(11510350)
def Event_11510350():
    """Event 11510350"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11515301))
    AND_1.Add(FlagEnabled(11510301))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(11515301))
    AND_2.Add(FlagEnabled(11510302))
    AND_3.Add(Host())
    AND_3.Add(FlagEnabled(11515301))
    AND_3.Add(FlagEnabled(11510303))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11515301)
    if Singleplayer():
        return RESTART
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=Objects.o5610_0000, animation_id=51)
    EnableMapCollision(collision=Collisions.h0010B1_0002)
    Restart()
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=Objects.o5610_0000, animation_id=50)
    EnableMapCollision(collision=Collisions.h0010B1_0001)
    Restart()
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(obj=Objects.o5610_0000, animation_id=53)
    EnableMapCollision(collision=Collisions.h0010B1_0000)
    Restart()


@ContinueOnRest(11510310)
def Event_11510310():
    """Event 11510310"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11510301))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagEnabled(11510303))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5610_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_2.Add(FlagDisabled(11510305))
    OR_2.Add(FlagEnabled(11510303))
    AND_3.Add(OR_2)
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_3.Add(FlagDisabled(11510305))
    OR_3.Add(FlagDisabled(11510303))
    AND_4.Add(OR_3)
    AND_4.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0002,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_4.Add(FlagDisabled(11510305))
    OR_4.Add(FlagEnabled(11510301))
    AND_5.Add(OR_4)
    AND_5.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0003,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_5.Add(FlagDisabled(11510305))
    OR_5.Add(FlagEnabled(11510302))
    AND_6.Add(OR_5)
    AND_6.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=Objects.o5750_0004,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_7.Add(FlagEnabled(11515300))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_7)
    DisplayDialog(text=10010170)
    Restart()
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()


@ContinueOnRest(CommonFlags.DarkAnorLondo)
def Event_11510400():
    """Event 11510400"""
    DisableMapPiece(map_piece_id=MapPieces.m9500B1_0000)
    if ThisEventFlagEnabled():
        DisableSoundEvent(sound_id=Sounds.GwynevereMusic)
        SetMapDrawParamSlot(map_area_id=15, draw_param_slot=1)
        SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
        DisableMapPiece(map_piece_id=MapPieces.m9000B1_0000)
        EnableMapPiece(map_piece_id=MapPieces.m9500B1_0000)
        DisableObject(Objects.o5900_0000)
        End()
    EnableCharacter(Characters.c5310_0000)
    AND_1.Add(CharacterDead(Characters.c5310_0000))
    AND_1.Add(EntityWithinDistance(entity=Characters.c5310_0000, other_entity=PLAYER, radius=15.0))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    DisableSoundEvent(sound_id=Sounds.GwynevereMusic)
    EnableFlag(743)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerCovenant(Covenant.PrincessGuard))
    SkipLinesIfConditionFalse(4, AND_1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()
    DisableFlag(120)
    if FlagDisabled(11510900):
        PlayCutscene(150110, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(150111, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    SetMapDrawParamSlot(map_area_id=15, draw_param_slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(map_piece_id=MapPieces.m9000B1_0000)
    EnableMapPiece(map_piece_id=MapPieces.m9500B1_0000)
    DisableObject(Objects.o5900_0000)
    AND_2.Add(PlayerHasGood(2510))
    if AND_2:
        return
    AwardItemLot(1090, host_only=True)


@ContinueOnRest(11510401)
def Event_11510401():
    """Event 11510401"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o5900_0000)
        End()
    EnableObjectInvulnerability(Objects.o5900_0000)
    AND_1.Add(FlagEnabled(CommonFlags.DarkAnorLondo))
    AND_1.Add(EntityWithinDistance(entity=Objects.o5900_0000, other_entity=PLAYER, radius=15.0))
    AND_2.Add(Host())
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 2310))
    AND_2.Add(EntityWithinDistance(entity=Objects.o5900_0000, other_entity=PLAYER, radius=15.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableObjectInvulnerability(Objects.o5900_0000)
    DestroyObject(Objects.o5900_0000)
    ForceAnimation(Objects.o5900_0000, 0)
    PlaySoundEffect(Objects.o5900_0000, 590000000, sound_type=SoundType.o_Object)


@RestartOnRest(11510450)
def Event_11510450():
    """Event 11510450"""
    MAIN.Await(CharacterDoesNotHaveTAEEvent(Characters.c5320_0000, tae_event_id=600))
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5320_0000, tae_event_id=600))
    
    DisableCharacter(Characters.c5320_0000)
    Wait(1.0)
    if FlagDisabled(11515110):
        Event_11515110(0, destination=1512710, flag=11515110)
        Restart()
    if FlagDisabled(11515111):
        Event_11515110(1, destination=1512711, flag=11515111)
        Restart()
    if FlagDisabled(11515112):
        Event_11515110(2, destination=1512712, flag=11515112)
        Restart()
    if FlagDisabled(11515113):
        Event_11515110(3, destination=1512713, flag=11515113)
        Restart()
    if FlagDisabled(11515114):
        Event_11515110(4, destination=1512714, flag=11515114)
        Restart()
    if FlagDisabled(11515115):
        Event_11515110(5, destination=1512715, flag=11515115)
        Restart()
    if FlagDisabled(11515116):
        Event_11515110(6, destination=1512716, flag=11515116)
        Restart()
    if FlagDisabled(11515117):
        Event_11515110(7, destination=1512717, flag=11515117)
        Restart()
    if FlagDisabled(11515118):
        Event_11515110(8, destination=1512718, flag=11515118)
        Restart()
    if FlagDisabled(11515119):
        Event_11515110(9, destination=1512719, flag=11515119)
        Restart()
    if FlagDisabled(11515120):
        Event_11515110(10, destination=1512720, flag=11515120)
        Restart()
    if FlagDisabled(11515121):
        Event_11515110(11, destination=1512721, flag=11515121)
        Restart()
    if FlagDisabled(11515122):
        Event_11515110(12, destination=1512722, flag=11515122)
        Restart()
    if FlagDisabled(11515123):
        Event_11515110(13, destination=1512723, flag=11515123)
        Restart()
    if FlagDisabled(11515124):
        Event_11515110(14, destination=1512724, flag=11515124)
        Restart()
    if FlagDisabled(11515125):
        Event_11515110(15, destination=1512725, flag=11515125)
        Restart()
    if FlagDisabled(11515126):
        Event_11515110(16, destination=1512726, flag=11515126)
        Restart()
    if FlagDisabled(11515127):
        Event_11515110(17, destination=1512727, flag=11515127)
        Restart()
    if FlagDisabled(11515128):
        Event_11515110(18, destination=1512728, flag=11515128)
        Restart()
    if FlagDisabled(11515129):
        Event_11515110(19, destination=1512729, flag=11515129)
        Restart()
    if FlagDisabled(11515130):
        Event_11515110(20, destination=1512730, flag=11515130)
        Restart()
    if FlagDisabled(11515131):
        Event_11515110(21, destination=1512731, flag=11515131)
        Restart()
    if FlagDisabled(11515132):
        Event_11515110(22, destination=1512732, flag=11515132)
        Restart()
    if FlagDisabled(11515133):
        Event_11515110(23, destination=1512733, flag=11515133)
        Restart()
    if FlagDisabled(11515134):
        Event_11515110(24, destination=1512734, flag=11515134)
        Restart()
    if FlagDisabled(11515135):
        Event_11515110(25, destination=1512735, flag=11515135)
        Restart()
    if FlagDisabled(11515136):
        Event_11515110(26, destination=1512736, flag=11515136)
        Restart()
    if FlagDisabled(11515137):
        Event_11515110(27, destination=1512737, flag=11515137)
        Restart()
    if FlagDisabled(11515138):
        Event_11515110(28, destination=1512738, flag=11515138)
        Restart()
    if FlagDisabled(11515139):
        Event_11515110(29, destination=1512739, flag=11515139)
        Restart()


@EndOnRest(11515110)
def Event_11515110(_, destination: int, flag: Flag | int):
    """Event 11515110"""
    Move(Characters.c5320_0000, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(Characters.c5320_0000)
    ReplanAI(Characters.c5320_0000)
    ForceAnimation(Characters.c5320_0000, 7000, wait_for_completion=True)
    EnableFlag(flag)
    if FlagEnabled(11515132):
        AICommand(Characters.c5320_0000, command_id=1, command_slot=0)
        ReplanAI(Characters.c5320_0000)


@ContinueOnRest(11510230)
def Event_11510230():
    """Event 11510230"""
    MAIN.Await(ActionButton(
        prompt_text=10010100,
        anchor_entity=1512510,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    AND_1.Add(Singleplayer())
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(384))
    SkipLinesIfConditionTrue(3, AND_1)
    SkipLinesIfClient(1)
    DisplayDialog(text=10010170)
    Restart()
    PlayCutscene(150135, cutscene_flags=0, player_id=10000, move_to_region=1102510, game_map=PAINTED_WORLD)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=1102511)
    SaveRequest()
    Restart()


@ContinueOnRest(11510240)
def Event_11510240():
    """Event 11510240"""
    if Client():
        return
    
    MAIN.Await(InsideMap(game_map=ANOR_LONDO))
    
    MAIN.Await(TimeElapsed(seconds=5.0))
    
    AND_2.Add(FlagDisabled(11515050))
    AND_2.Add(ActionButton(
        prompt_text=10010200,
        anchor_entity=Characters.c2260_0000,
        anchor_type=CoordEntityType.Character,
        max_distance=7.0,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_2)
    
    SkipLinesIfSingleplayer(2)
    DisplayDialog(text=10010170)
    Restart()
    if FlagDisabled(CommonFlags.DarkAnorLondo):
        PlayCutscene(150130, cutscene_flags=0, player_id=10000, move_to_region=1502500, game_map=SENS_FORTRESS)
    else:
        PlayCutscene(150132, cutscene_flags=0, player_id=10000, move_to_region=1502500, game_map=SENS_FORTRESS)
    WaitFrames(frames=1)
    SetMapDrawParamSlot(map_area_id=15, draw_param_slot=0)
    Restart()


@ContinueOnRest(11515050)
def Event_11515050():
    """Event 11515050"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c2260_0000)
        End()
    DisableImmortality(Characters.c2260_0000)
    SetStandbyAnimationSettings(Characters.c2260_0000, standby_animation=9000)
    OR_1.Add(Attacked(attacked_entity=Characters.c2260_0000, attacker=PLAYER))
    OR_1.Add(FlagEnabled(11515050))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11515050)
    ResetAnimation(Characters.c2260_0000, disable_interpolation=True)
    ForceAnimation(Characters.c2260_0000, 9060, wait_for_completion=True)
    DisableCharacter(Characters.c2260_0000)


@ContinueOnRest(11510120)
def Event_11510120():
    """Event 11510120"""
    DisableNetworkSync()
    if Client():
        return
    AND_1.Add(FlagEnabled(743))
    AND_1.Add(FlagEnabled(CommonFlags.OrnsteinSmoughDead))
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(FlagEnabled(CommonFlags.DarkAnorLondo))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1512400))
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0005B1_0000))
    OR_1.Add(PlayerStandingOnCollision(Collisions.h0030B1_0000))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4501)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(11510130)
def Event_11510130():
    """Event 11510130"""
    if FlagDisabled(CommonFlags.DarkAnorLondo):
        DisableCharacter(Characters.c0000_0012)
        DisableCharacter(Characters.c0000_0013)
        DisableCharacter(Characters.c0000_drk1)
        DisableCharacter(Characters.c0000_drk2)
        DisableCharacter(Characters.c0000_drk3)
    
        MAIN.Await(FlagEnabled(CommonFlags.DarkAnorLondo))
    
        EnableCharacter(Characters.c0000_0012)
        EnableCharacter(Characters.c0000_0013)
        EnableCharacter(Characters.c0000_drk1)
        EnableCharacter(Characters.c0000_drk2)
        EnableCharacter(Characters.c0000_drk3)
    DisableCharacter(Characters.c2410_0005)
    DisableCharacter(1510450)
    DisableCharacter(Characters.c5351_grg2)
    DisableCharacter(1510110)
    DisableCharacter(1510111)
    DisableCharacter(Characters.c2260_bat2)
    DisableCharacter(Characters.c2260_0006)
    DisableCharacter(Characters.c2260_0007)
    DisableCharacter(1510115)
    DisableCharacter(1510116)
    DisableCharacter(1510117)
    DisableCharacter(1510118)
    DisableCharacter(Characters.c2260_0012)
    DisableCharacter(Characters.c2260_bat1)
    DisableCharacter(Characters.c2870_0000)
    DisableCharacter(Characters.c2870_sen2)
    DisableCharacter(Characters.c2870_0002)
    DisableCharacter(Characters.c2870_0003)
    DisableCharacter(Characters.c2870_0004)
    DisableCharacter(Characters.c2870_0005)
    DisableCharacter(1510406)
    DisableCharacter(1510407)
    DisableCharacter(Characters.c2870_0008)
    DisableCharacter(Characters.c2870_0009)
    DisableCharacter(1510410)
    DisableCharacter(1510411)
    DisableCharacter(Characters.c2870_0012)
    DisableCharacter(Characters.c2870_0013)
    DisableCharacter(Characters.c2410_slv1)
    DisableCharacter(Characters.c2410_slv2)
    DisableCharacter(Characters.c2410_slv3)
    DisableCharacter(Characters.c2870_sen1)
    if FlagEnabled(1034):
        return
    Move(
        Characters.c0000_0003,
        destination=1512450,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.c5351_grg2,
    )
    SetNest(Characters.c0000_0003, region=1512450)
    SetStandbyAnimationSettings(Characters.c0000_0003)


@ContinueOnRest(11510131)
def Event_11510131():
    """Event 11510131"""
    if Client():
        return
    AND_1.Add(FlagEnabled(CommonFlags.DarkAnorLondo))
    AND_1.Add(InsideMap(game_map=ANOR_LONDO))
    AND_1.Add(Host())
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=1512960)
    SaveRequest()


@ContinueOnRest(11510140)
def Event_11510140():
    """Event 11510140"""
    MAIN.Await(FlagEnabled(11510900))
    
    MoveRemains(source_region=1512420, destination_region=1512421)


@ContinueOnRest(11510150)
def Event_11510150():
    """Event 11510150"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(115))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512101))
    
    MAIN.Await(AND_1)
    
    End()


@ContinueOnRest(11510460)
def Event_11510460():
    """Event 11510460"""
    OR_7.Add(FlagEnabled(11510593))
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_7)
    AND_1.Add(FlagDisabled(11515352))
    AND_1.Add(FlagDisabled(11515350))
    AND_1.Add(FlagDisabled(743))
    AND_1.Add(FlagEnabled(1240))
    AND_1.Add(ActionButton(
        prompt_text=10010210,
        anchor_entity=1512410,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(OR_7)
    AND_2.Add(FlagEnabled(11515352))
    AND_2.Add(FlagDisabled(11515350))
    AND_3.Add(OR_7)
    AND_3.Add(FlagEnabled(11515352))
    AND_3.Add(FlagEnabled(11515350))
    AND_3.Add(Host())
    AND_3.Add(CharacterOutsideRegion(PLAYER, region=1512411))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(10, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    EnableFlag(11515350)
    SkipLinesIfHost(1)
    if ThisEventFlagEnabled():
        ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11515352)
    Restart()
    RemoveSpecialEffect(PLAYER, 4170)
    DisableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventFlagDisabled(2)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11515352)
    Restart()


@ContinueOnRest(11510462)
def Event_11510462():
    """Event 11510462"""
    DisableNetworkSync()
    WaitFrames(frames=2)
    EnableFlag(11510460)


@RestartOnRest(11510860)
def Event_11510860(_, character: Character | int, item_lot: int):
    """Event 11510860"""
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


@ContinueOnRest(11510461)
def Event_11510461():
    """Event 11510461"""
    MAIN.Await(FlagEnabled(11515351))
    
    AddSpecialEffect(PLAYER, 4170)
    RotateToFaceEntity(PLAYER, target_entity=Characters.c5310_0000)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    
    MAIN.Await(FlagDisabled(11515351))
    
    RemoveSpecialEffect(PLAYER, 4170)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    Restart()


@ContinueOnRest(11510600)
def Event_11510600(_, obj: Object | int, obj_act_id: int):
    """Event 11510600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11515200)
def Event_11515200(_, character: int):
    """Event 11515200"""
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


@RestartOnRest(11515210)
def Event_11515210(_, character: int):
    """Event 11515210"""
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


@RestartOnRest(11515220)
def Event_11515220(_, character: Character | int):
    """Event 11515220"""
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


@RestartOnRest(11515230)
def Event_11515230(_, character: Character | int):
    """Event 11515230"""
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


@RestartOnRest(11515240)
def Event_11515240(_, character: int, region: int):
    """Event 11515240"""
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


@RestartOnRest(11510850)
def Event_11510850(_, character: Character | int):
    """Event 11510850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@RestartOnRest(11515190)
def Event_11515190(_, character: int):
    """Event 11515190"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(character))
    if AND_1:
        return
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 0)
    ReplanAI(character)


@RestartOnRest(11515250)
def Event_11515250():
    """Event 11515250"""
    if ThisEventFlagEnabled():
        return
    DisableAI(Characters.c2400_0010)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512050))
    AND_2.Add(Attacked(attacked_entity=Characters.c2400_0010, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    ForceAnimation(Characters.c2400_0010, 500)
    EnableAI(Characters.c2400_0010)


@RestartOnRest(11515251)
def Event_11515251():
    """Event 11515251"""
    if ThisEventFlagEnabled():
        return
    DisableAI(Characters.c2410_0001)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1512060))
    OR_1.Add(Attacked(attacked_entity=Characters.c2410_0001, attacker=PLAYER))
    OR_1.Add(EntityWithinDistance(entity=Characters.c2410_0001, other_entity=PLAYER, radius=4.0))
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.c2410_0001)


@ContinueOnRest(11510215)
def Event_11510215():
    """Event 11510215"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o5740_0000)
        End()
    
    MAIN.Await(ObjectDestroyed(Objects.o5740_0000))
    
    End()


@ContinueOnRest(11510510)
def Event_11510510(_, character: Character | int, flag: Flag | int):
    """Event 11510510"""
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


@ContinueOnRest(11510520)
def Event_11510520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11510501)
def Event_11510501(_, character: Character | int, flag: Flag | int):
    """Event 11510501"""
    OR_2.Add(FlagEnabled(1030))
    OR_2.Add(FlagEnabled(1031))
    OR_2.Add(FlagEnabled(1036))
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1034))
    OR_3.Add(FlagEnabled(1232))
    OR_3.Add(FlagEnabled(1241))
    OR_3.Add(FlagEnabled(1242))
    AND_2.Add(OR_3)
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(ThisEventFlagDisabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11510502)
def Event_11510502(_, character: Character | int, flag: Flag | int):
    """Event 11510502"""
    AND_1.Add(FlagEnabled(1240))
    OR_2.Add(FlagEnabled(1232))
    OR_2.Add(FlagEnabled(11515382))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamType(character, TeamType.Boss)


@ContinueOnRest(11510530)
def Event_11510530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510530"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1001))
    AND_1.Add(FlagEnabled(11010590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11510531)
def Event_11510531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510531"""
    AND_1.Add(FlagDisabled(1033))
    AND_1.Add(FlagEnabled(1030))
    AND_1.Add(FlagEnabled(CommonFlags.BonfireWarpOptionDisplayed))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11510532)
def Event_11510532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510532"""
    AND_1.Add(FlagDisabled(1033))
    OR_1.Add(FlagEnabled(1030))
    OR_1.Add(FlagEnabled(1036))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(711))
    AND_1.Add(FlagEnabled(712))
    AND_1.Add(FlagEnabled(713))
    AND_1.Add(FlagEnabled(714))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11510533)
def Event_11510533(_, character: Character | int):
    """Event 11510533"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    EnableFlag(151)


@ContinueOnRest(11510535)
def Event_11510535(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510535"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1493))
    AND_1.Add(CharacterDead(Characters.c2410_0009))
    AND_1.Add(CharacterDead(Characters.c2410_0014))
    AND_1.Add(CharacterDead(Characters.c2410_0015))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11510536)
def Event_11510536(_, character: Character | int):
    """Event 11510536"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1494))
    AND_1.Add(FlagEnabled(11510590))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)


@ContinueOnRest(11510541)
def Event_11510541(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510541"""
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    OR_1.Add(FlagEnabled(1577))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11510700))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SetTeamType(Characters.c0000_0009, TeamType.WhitePhantom)
    SetTeamType(Characters.c0000_0010, TeamType.WhitePhantom)
    DisableAI(character)
    DisableAI(Characters.c0000_0009)
    DisableAI(Characters.c0000_0010)
    OR_1.Add(FlagEnabled(11510598))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c0000_0009, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c0000_0010, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    EnableAI(Characters.c0000_0009)
    EnableAI(Characters.c0000_0010)


@ContinueOnRest(11510542)
def Event_11510542(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510542"""
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(8102)


@ContinueOnRest(11510543)
def Event_11510543(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510543"""
    DisableObject(Objects.o5870_0000)
    DeleteVFX(VFX.LautrecInvasionFog1, erase_root_only=False)
    DisableObject(Objects.o5871_0000)
    DeleteVFX(VFX.LautrecInvasionFog2, erase_root_only=False)
    DisableObject(Objects.o5869_0000)
    DeleteVFX(VFX.LautrecInvasionFog3, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(11510700))
    
    EnableObject(Objects.o5870_0000)
    CreateVFX(VFX.LautrecInvasionFog1)
    EnableObject(Objects.o5871_0000)
    CreateVFX(VFX.LautrecInvasionFog2)
    EnableObject(Objects.o5869_0000)
    CreateVFX(VFX.LautrecInvasionFog3)
    DisableFlag(8104)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(Characters.c2870_0012)
    DisableCharacter(Characters.c2870_0013)
    DisableCharacter(Characters.c2410_0005)
    EnableCharacter(character)
    EnableCharacter(Characters.c0000_0009)
    EnableCharacter(Characters.c0000_0010)
    if FlagDisabled(8101):
        EnableFlag(8101)
        End()
    EnableFlag(8100)


@ContinueOnRest(11510544)
def Event_11510544(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11510544"""
    if ThisEventFlagEnabled():
        EnableTreasure(obj=Objects.o0500_0008)
        End()
    DisableObject(Objects.o0500_0008)
    DisableTreasure(obj=Objects.o0500_0008)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11510700))
    AND_1.Add(FlagEnabled(8102))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    SkipLinesIfConditionFalse(3, OR_1)
    AwardItemLot(2060, host_only=True)
    AwardItemLot(6300, host_only=True)
    RemoveGoodFromPlayer(item=115)
    EnableObject(Objects.o0500_0008)
    EnableTreasure(obj=Objects.o0500_0008)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(151)
def Event_151():
    """Event 151"""
    DisableNetworkSync()
    AND_1.Add(ThisEventFlagEnabled())
    AND_1.Add(ActionButton(
        prompt_text=10010182,
        anchor_entity=Objects.o0200_0000,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(
        text=10010184,
        anchor_entity=Objects.o0200_0000,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@RestartOnRest(11515090)
def Event_11515090(_, character: Character | int):
    """Event 11515090"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=500))
    
    EzstateAIRequest(character, command_id=1500, command_slot=0)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(character, tae_event_id=500))
    
    Restart()


@RestartOnRest(11515091)
def Event_11515091(_, character: Character | int):
    """Event 11515091"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=1400))
    
    Wait(10.0)
    EzstateAIRequest(character, command_id=1501, command_slot=0)
    Restart()


@RestartOnRest(11515092)
def Event_11515092(_, character: Character | int, obj: int, flag: Flag | int, flag_1: Flag | int):
    """Event 11515092"""
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    DisableCharacterCollision(character)
    DisableGravity(character)
    EnableObjectInvulnerability(obj)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableObjectInvulnerability(obj)
    WaitFrames(frames=1)
    DestroyObject(obj)
    PlaySoundEffect(obj, 596500000, sound_type=SoundType.o_Object)


@ContinueOnRest(11515030)
def Event_11515030():
    """Event 11515030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0011, authority_level=UpdateAuthority.Forced)
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c0000_0006)
    SkipLinesIfFlagEnabled(3, 11515034)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11515031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0011)
    if FlagEnabled(CommonFlags.OrnsteinSmoughDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0011))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0011, other_entity=PLAYER, radius=30.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0011,
        region=1512001,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(Characters.c0000_0006)
    
    MAIN.Await(FlagEnabled(11515031))
    
    SetNest(Characters.c0000_0011, region=1512002)


@ContinueOnRest(11515990)
def Event_11515990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 11515990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11515029)
def Event_11515029():
    """Event 11515029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0011, authority_level=UpdateAuthority.Forced)
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c0000_0006)
    SkipLinesIfFlagEnabled(3, 11515034)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11515031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0011)
    if FlagEnabled(CommonFlags.OrnsteinSmoughDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11515031))
    AND_1.Add(FlagDisabled(11515034))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0011))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0011, other_entity=PLAYER, radius=30.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0011,
        region=1512001,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(Characters.c0000_0006)
    
    MAIN.Await(FlagEnabled(11515031))
    
    SetNest(Characters.c0000_0011, region=1512002)


@ContinueOnRest(11515032)
def Event_11515032():
    """Event 11515032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11515031))
    AND_1.Add(FlagEnabled(11515393))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0011, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0011)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0011, region=1512998))
    
    RotateToFaceEntity(Characters.c0000_0011, target_entity=1512997)
    ForceAnimation(Characters.c0000_0011, 7410)
    AICommand(Characters.c0000_0011, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0011)


@ContinueOnRest(11515033)
def Event_11515033():
    """Event 11515033"""
    AND_1.Add(FlagEnabled(11515031))
    AND_1.Add(FlagDisabled(11515390))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512801))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0011, command_id=8, command_slot=0)
    ReplanAI(Characters.c0000_0011)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1512801))
    
    AICommand(Characters.c0000_0011, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0011)
    Restart()


@ContinueOnRest(11515843)
def Event_11515843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11515843"""
    AND_1.Add(FlagEnabled(120))
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


@ContinueOnRest(11515846)
def Event_11515846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11515846"""
    AND_1.Add(FlagEnabled(120))
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
