"""
Blighttown / Quelaag's Domain

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m14_00_00_00_enums import *
from ..enums.common_enums import CommonFlags
from ..enums.m10_00_00_00_enums import Flags as m10_00_Flags, Objects as m10_00_Objects


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11400992()
    Event_11400799()
    Event_11400884()
    Event_11400885()
    Event_11400886()
    Event_11400887()
    Event_11400888()
    Event_11400889()
    Event_11400995()
    Event_11400996(0, character=Characters.c3210_egg2, special_effect=0)
    Event_11400996(1, character=Characters.c3210_egg3, special_effect=0)
    Event_11400996(2, character=Characters.c0000_inf2, special_effect=2090)
    Event_11400997()
    Event_11400998()
    Event_11400999(0, other_entity=Characters.c0000_inf2)
    Event_11400999(1, other_entity=Characters.c0000_inf1)
    RegisterBonfire(bonfire_flag=11400992, obj=Objects.o0200_0000, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11400984, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11400976, obj=Objects.o0200_0002)
    RegisterLadder(start_climbing_flag=11400010, stop_climbing_flag=11400011, obj=Objects.o4100_0000)
    RegisterLadder(start_climbing_flag=11400012, stop_climbing_flag=11400013, obj=Objects.o4101_0000)
    RegisterLadder(start_climbing_flag=11400014, stop_climbing_flag=11400015, obj=Objects.o4102_0000)
    RegisterLadder(start_climbing_flag=11400016, stop_climbing_flag=11400017, obj=Objects.o4103_0000)
    RegisterLadder(start_climbing_flag=11400018, stop_climbing_flag=11400019, obj=Objects.o4104_0000)
    RegisterLadder(start_climbing_flag=11400020, stop_climbing_flag=11400021, obj=Objects.o4105_0000)
    RegisterLadder(start_climbing_flag=11400022, stop_climbing_flag=11400023, obj=Objects.o4106_0000)
    RegisterLadder(start_climbing_flag=11400024, stop_climbing_flag=11400025, obj=Objects.o4107_0000)
    RegisterLadder(start_climbing_flag=11400026, stop_climbing_flag=11400027, obj=Objects.o4108_0000)
    RegisterLadder(start_climbing_flag=11400028, stop_climbing_flag=11400029, obj=Objects.o4109_0000)
    RegisterLadder(start_climbing_flag=11400030, stop_climbing_flag=11400031, obj=Objects.o4110_0000)
    RegisterLadder(start_climbing_flag=11400032, stop_climbing_flag=11400033, obj=Objects.o4111_0000)
    RegisterLadder(start_climbing_flag=11400034, stop_climbing_flag=11400035, obj=Objects.o4112_0000)
    RegisterLadder(start_climbing_flag=11400036, stop_climbing_flag=11400037, obj=Objects.o4113_0000)
    RegisterLadder(start_climbing_flag=11400038, stop_climbing_flag=11400039, obj=Objects.o4114_0000)
    RegisterLadder(start_climbing_flag=11400040, stop_climbing_flag=11400041, obj=Objects.o4115_0000)
    RegisterLadder(start_climbing_flag=11400042, stop_climbing_flag=11400043, obj=Objects.o4116_0000)
    RegisterLadder(start_climbing_flag=11400044, stop_climbing_flag=11400045, obj=Objects.o4117_0000)
    RegisterLadder(start_climbing_flag=11400046, stop_climbing_flag=11400047, obj=Objects.o4118_0000)
    RegisterLadder(start_climbing_flag=11400048, stop_climbing_flag=11400049, obj=Objects.o4119_0000)
    RegisterLadder(start_climbing_flag=11400050, stop_climbing_flag=11400051, obj=Objects.o4120_0000)
    RegisterLadder(start_climbing_flag=11400052, stop_climbing_flag=11400053, obj=Objects.o4121_0000)
    RegisterLadder(start_climbing_flag=11400054, stop_climbing_flag=11400055, obj=Objects.o4122_0000)
    RegisterLadder(start_climbing_flag=11400056, stop_climbing_flag=11400057, obj=Objects.o4123_0000)
    RegisterLadder(start_climbing_flag=11400058, stop_climbing_flag=11400059, obj=Objects.o4124_0000)
    RegisterLadder(start_climbing_flag=11400060, stop_climbing_flag=11400061, obj=Objects.o4111_0001)
    RegisterLadder(start_climbing_flag=11400062, stop_climbing_flag=11400063, obj=Objects.o4109_0001)
    RegisterLadder(start_climbing_flag=11400064, stop_climbing_flag=11400065, obj=Objects.o4109_0002)
    RegisterLadder(start_climbing_flag=11400066, stop_climbing_flag=11400067, obj=Objects.o4111_0002)
    RegisterLadder(start_climbing_flag=11400068, stop_climbing_flag=11400069, obj=Objects.o4120_0001)
    RegisterLadder(start_climbing_flag=11400070, stop_climbing_flag=11400071, obj=Objects.o4125_0000)
    SkipLinesIfClient(6)
    DisableObject(Objects.o4952_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o4953_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    DisableObject(Objects.o4954_0000)
    DeleteVFX(VFX.MultiplayerFog3, erase_root_only=False)
    AND_1.Add(FlagEnabled(m10_00_Flags.KirkInvaderKilled))
    AND_1.Add(FlagEnabled(11410810))
    AND_1.Add(FlagEnabled(11410811))
    SkipLinesIfConditionTrue(2, AND_1)
    DisableObject(Objects.o0500_0037)
    SkipLines(1)
    EnableTreasure(obj=Objects.o0500_0037)
    Event_11400090(1, obj=Objects.o4956_0000, vfx_id=VFX.CheckpointFog1, destination=1402602, destination_1=1402603)
    Event_11405090()
    Event_11405091()
    Event_11405092()
    Event_11400900()
    Event_11400800()
    Event_11405000()
    Event_11400200()
    Event_11400210()
    Event_11400220()
    Event_11400230()
    Event_140()
    DisableSoundEvent(sound_id=Sounds.QuelaagMusic)
    if FlagEnabled(CommonFlags.QuelaagDead):
        Event_11405392()
        DisableObject(Objects.o4950_0000)
        DeleteVFX(VFX.QuelaagEntranceFog, erase_root_only=False)
        DisableObject(Objects.o4951_0000)
        DeleteVFX(VFX.QuelaagExitFog, erase_root_only=False)
    else:
        Event_11405390()
        Event_11405391()
        Event_11405393()
        Event_11405392()
        Event_11400001()
        Event_11405394()
        Event_11405395()
    Event_11405100(0, entity=Objects.o4200_0000, region=1402000, region_1=1402001, region_2=1402002)
    Event_11405110(
        0,
        entity=Objects.o4202_0000,
        region=1402020,
        region_1=1402021,
        region_2=1402022,
        region_3=1402023,
        region_4=1402024,
    )
    Event_11405350(
        0,
        character=Characters.c3210_0000,
        character_1=Characters.c3220_0000,
        character_2=Characters.c3220_0001,
        character_3=Characters.c3220_0002,
        character_4=Characters.c3220_0003,
        character_5=Characters.c3220_0004,
        left=1,
    )
    Event_11405350(
        3,
        character=Characters.c3210_egg4,
        character_1=Characters.c3220_0015,
        character_2=Characters.c3220_0016,
        character_3=Characters.c3220_0017,
        character_4=Characters.c3220_0018,
        character_5=Characters.c3220_0019,
        left=0,
    )
    Event_11405350(
        4,
        character=Characters.c3210_0003,
        character_1=Characters.c3220_0020,
        character_2=Characters.c3220_0021,
        character_3=Characters.c3220_0022,
        character_4=Characters.c3220_0023,
        character_5=Characters.c3220_0024,
        left=0,
    )
    Event_11405350(
        5,
        character=Characters.c3210_egg1,
        character_1=Characters.c3220_mgt1,
        character_2=Characters.c3220_mgt2,
        character_3=Characters.c3220_mgt3,
        character_4=Characters.c3220_mgt4,
        character_5=Characters.c3220_mgt5,
        left=0,
    )
    Event_11405350(
        6,
        character=Characters.c3210_egg2,
        character_1=Characters.c3220_mgt6,
        character_2=Characters.c3220_mgt7,
        character_3=Characters.c3220_mgt8,
        character_4=Characters.c3220_mgt9,
        character_5=Characters.c3220_mgt10,
        left=0,
    )
    Event_11405350(
        7,
        character=Characters.c3210_egg3,
        character_1=Characters.c3220_mgt11,
        character_2=Characters.c3220_mgt12,
        character_3=Characters.c3220_mgt13,
        character_4=Characters.c3220_mgt14,
        character_5=0,
        left=0,
    )
    Event_11400100(0, flag=11405340, region=1402200, entity=1403000)
    Event_11400100(1, flag=11405341, region=1402201, entity=1403001)
    Event_11400100(2, flag=11405342, region=1402202, entity=1403002)
    Event_11405200(0, character=Characters.c2060_0012, obj=Objects.o4820_0012)
    Event_11405250(0, character=Characters.c2811_0000)
    Event_11405250(1, character=Characters.c2811_0001)
    Event_11405250(2, character=Characters.c2811_0002)
    Event_11405250(3, character=Characters.c2811_0003)
    Event_11405250(4, character=Characters.c2811_0004)
    Event_11400850(0, character=Characters.c2530_0000, item_lot=25300200)
    Event_11400850(1, character=Characters.c2530_0001, item_lot=25300200)
    Event_11400850(2, character=Characters.c2530_0002, item_lot=25300200)
    Event_11400850(3, character=Characters.c2530_0003, item_lot=25300200)
    Event_11400850(4, character=Characters.c2530_0004, item_lot=25300200)
    Event_11400850(5, character=Characters.c2530_0005, item_lot=25300200)
    Event_11400850(6, character=Characters.c2530_0006, item_lot=25300200)
    Event_11400850(7, character=Characters.c2530_0007, item_lot=25300200)
    Event_11400850(8, character=Characters.c2530_0008, item_lot=25300200)
    Event_11400850(11, character=Characters.c2530_blw1, item_lot=25300200)
    Event_11400850(12, character=Characters.c2530_blw2, item_lot=25300200)
    Event_11400850(13, character=Characters.c2530_blw3, item_lot=25300200)
    Event_11400850(9, character=Characters.c2250_trs1, item_lot=22500210)
    Event_11400850(10, character=Characters.c0000_inf1, item_lot=61330000)
    Event_11400850(20, character=Characters.c0000_inf2, item_lot=61320000)
    Event_11400600(0, obj=Objects.o0110_0000, obj_act_id=11400600)
    Event_11400600(1, obj=Objects.o0110_0001, obj_act_id=11400601)
    Event_11400600(2, obj=Objects.o0110_0002, obj_act_id=11400602)
    Event_11415170()
    Event_11405843(
        0,
        flag=CommonFlags.QuelaagDead,
        line_intersects=1401990,
        anchor_entity=1402998,
        target_entity=1402997,
    )
    Event_11405846(0, flag=CommonFlags.QuelaagDead, obj=Objects.o4950_0000, vfx_id=VFX.QuelaagEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0010, event_flag=8940)
    HumanityRegistration(Characters.c0000_0007, event_flag=8940)
    Event_11405030()
    Event_11405029()
    Event_11405032()
    Event_11405035()
    Event_11400901()
    Event_14005990(0, flag=11405031, summoned_character=Characters.c0000_0010)
    if FlagDisabled(1257):
        DisableCharacter(Characters.c0000_0004)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0004, team_type=TeamType.HostileAlly)
    Event_11400520(0, character=Characters.c0000_0004, first_flag=1250, last_flag=1259, flag=1254)
    Event_11400530(0, character=Characters.c0000_0004, first_flag=1250, last_flag=1259, flag=1257)
    SkipLinesIfFlagRangeAnyEnabled(1, (1270, 1279))
    EnableFlag(1270)
    Event_11400520(1, character=Characters.c5340_0000, first_flag=1270, last_flag=1279, flag=1272)
    if FlagDisabled(1280):
        SetNest(Characters.c3210_0000, region=1402300)
        Move(Characters.c3210_0000, destination=1402300, destination_type=CoordEntityType.Region, short_move=True)
    Event_11400520(2, character=Characters.c3210_0000, first_flag=1280, last_flag=1289, flag=1284)
    Event_11400531(0, character=Characters.c3210_0000, first_flag=1280, last_flag=1289, flag=1281)
    Event_11400532(0, character=Characters.c3210_0000, first_flag=1280, last_flag=1289, flag=1286)
    Event_11400501(0, character=Characters.c3210_0000, flag=1282)
    Event_11400502(0, character=Characters.c3210_0000, flag=1283)
    Event_11400503(0, character=Characters.c3210_0000, flag=1287)
    Event_11400533()
    HumanityRegistration(Characters.c0000_0005, event_flag=8398)
    SkipLinesIfFlagEnabled(2, 1296)
    SkipLinesIfFlagEnabled(1, 1290)
    SkipLines(1)
    DisableCharacter(Characters.c0000_0005)
    Event_11400510(3, character=Characters.c0000_0005, flag=1294)
    Event_11400520(3, character=Characters.c0000_0005, first_flag=1290, last_flag=1309, flag=1295)
    Event_11400536(0, character=Characters.c0000_0005, first_flag=1290, last_flag=1309, flag=1291)
    Event_11400537(0, character=Characters.c0000_0005, first_flag=1290, last_flag=1309, flag=1292)
    Event_11400538(0, character=Characters.c0000_0005, first_flag=1290, last_flag=1309, flag=1293)
    Event_11400539(0, character=Characters.c0000_0005, first_flag=1290, last_flag=1309, flag=1296)
    HumanityRegistration(Characters.c0000_0003, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1502)
    SkipLinesIfFlagEnabled(1, 1501)
    DisableCharacter(Characters.c0000_0003)
    Event_11400510(4, character=Characters.c0000_0003, flag=1512)
    Event_11400520(4, character=Characters.c0000_0003, first_flag=1490, last_flag=1514, flag=1513)
    Event_11400551(0, character=Characters.c0000_0003, first_flag=1490, last_flag=1514, flag=1501)
    Event_11400552(0, character=Characters.c0000_0003, first_flag=1490, last_flag=1514, flag=1502)
    Event_11400553()
    Event_11400554(0, character=Characters.c0000_0003)
    HumanityRegistration(Characters.c0000_0008, event_flag=8470)
    HumanityRegistration(Characters.c0000_0009, event_flag=8900)
    SkipLinesIfClient(1)
    DisableFlag(11405022)
    SkipLinesIfFlagEnabled(8, 11405022)
    AND_1.Add(Host())
    AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(FlagEnabled(1601))
    SkipLinesIfConditionTrue(2, AND_1)
    DisableCharacter(Characters.c0000_0008)
    DisableCharacter(Characters.c0000_0009)
    Event_11400520(5, character=Characters.c0000_0008, first_flag=1600, last_flag=1619, flag=1604)
    Event_11400520(6, character=Characters.c0000_0009, first_flag=1760, last_flag=1769, flag=1764)
    Event_11400504(0, character=Characters.c0000_0008, flag=1603, character_1=Characters.c0000_0009)
    Event_11400560(
        0,
        character=Characters.c0000_0008,
        first_flag=1600,
        last_flag=1619,
        flag=1601,
        character_1=Characters.c0000_0009,
    )
    Event_11400566(0, character=Characters.c0000_0008, character_1=Characters.c0000_0009)
    Event_11400567(0, character=Characters.c0000_0008, character_1=Characters.c0000_0009)
    SkipLinesIfConditionFalse(2, AND_1)
    WaitFrames(frames=1)
    EnableFlag(11405022)
    DisableFlag(1766)


@ContinueOnRest(11400992)
def Event_11400992():
    """Event 11400992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c5280_0000, 7100)
    AddSpecialEffect(Characters.c0000_0010, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c5280_0000, 7100)
    RemoveSpecialEffect(Characters.c0000_0010, 7100)
    Restart()


@ContinueOnRest(11400799)
def Event_11400799():
    """Event 11400799"""
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2190))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11402799)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2190))
    
    MAIN.Await(AND_2)
    
    DisableFlag(11402799)


@ContinueOnRest(11400884)
def Event_11400884():
    """Event 11400884"""
    AND_1.Add(FlagEnabled(11402884))
    AND_1.Add(CharacterDead(Characters.c0000_0008))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(63160, host_only=True)


@ContinueOnRest(11400885)
def Event_11400885():
    """Event 11400885"""
    if FlagEnabled(11402885):
        DisableCharacter(Characters.c0000_0008)
        DisableCharacter(Characters.c0000_0009)


@ContinueOnRest(11400886)
def Event_11400886():
    """Event 11400886"""
    if FlagEnabled(11402886):
        AwardItemLot(63150, host_only=True)
        EnableFlag(11402886)


@ContinueOnRest(11400887)
def Event_11400887():
    """Event 11400887"""
    AND_1.Add(FlagEnabled(11402887))
    
    MAIN.Await(AND_1)
    
    AND_1.Add(PlayerHasWeapon(503000))
    SkipLinesIfConditionFalse(2, AND_1)
    RemoveWeaponFromPlayer(item=503000, quantity=1)
    End()
    AND_2.Add(PlayerHasWeapon(503100))
    SkipLinesIfConditionFalse(2, AND_2)
    RemoveWeaponFromPlayer(item=503100, quantity=1)
    End()
    AND_3.Add(PlayerHasWeapon(503200))
    SkipLinesIfConditionFalse(2, AND_3)
    RemoveWeaponFromPlayer(item=503200, quantity=1)
    End()


@ContinueOnRest(11400888)
def Event_11400888():
    """Event 11400888"""
    AND_1.Add(FlagEnabled(11402888))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(6315, host_only=True)


@ContinueOnRest(11400889)
def Event_11400889():
    """Event 11400889"""
    AND_1.Add(FlagEnabled(11402889))
    
    MAIN.Await(AND_1)
    
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0008, team_type=TeamType.HostileAlly)
    Wait(1.0)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0009, team_type=TeamType.HostileAlly)


@ContinueOnRest(11400995)
def Event_11400995():
    """Event 11400995"""
    if FlagDisabled(11407132):
        AND_1.Add(FlagDisabled(1272))
        AND_1.Add(Attacked(attacked_entity=Characters.c0000_inf2, attacker=PLAYER))
    
        MAIN.Await(AND_1)
    
        EnableFlag(11407132)
        AddSpecialEffect(Characters.c0000_inf2, 2091)
        EnableInvincibility(Characters.c0000_inf2)
        SetTeamTypeAndExitStandbyAnimation(Characters.c0000_inf2, team_type=TeamType.Ally)
        FadeOutCharacter(character=Characters.c0000_inf2, duration=5.0)
        ForceAnimation(Characters.c0000_inf2, 7570)
        Wait(1.0)
        PlaySoundEffect(Characters.c0000_inf2, 21200, sound_type=SoundType.s_SFX)
        CreateTemporaryVFX(
            vfx_id=22733,
            anchor_entity=Characters.c0000_inf2,
            model_point=236,
            anchor_type=CoordEntityType.Character,
        )
        Wait(6.0)
    DisableCharacter(Characters.c0000_inf2)


@ContinueOnRest(11400996)
def Event_11400996(_, character: Character | int, special_effect: int):
    """Event 11400996"""
    AND_1.Add(FlagEnabled(1272))
    
    MAIN.Await(AND_1)
    
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    AddSpecialEffect(character, special_effect)


@ContinueOnRest(11400997)
def Event_11400997():
    """Event 11400997"""
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.c0000_inf1, radius=3.0))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Characters.c0000_inf1, 7702)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_inf1, team_type=TeamType.Enemy)


@ContinueOnRest(11400998)
def Event_11400998():
    """Event 11400998"""
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.c2250_trs1, radius=15.0))
    
    MAIN.Await(AND_1)
    
    SetTeamType(Characters.c2250_trs1, TeamType.Ally)
    EnableInvincibility(Characters.c2250_trs1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.c2250_trs1, radius=5.0))
    
    MAIN.Await(AND_2)
    
    SetTeamType(Characters.c2250_trs1, TeamType.Enemy)
    DisableInvincibility(Characters.c2250_trs1)
    Restart()


@ContinueOnRest(11400999)
def Event_11400999(_, other_entity: int):
    """Event 11400999"""
    AND_1.Add(HealthRatio(PLAYER) == 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=10.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 5210)


@ContinueOnRest(11400090)
def Event_11400090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11400090"""
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


@RestartOnRest(11405090)
def Event_11405090():
    """Event 11405090"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2060_0006)
        DisableCharacter(Characters.c2060_0011)
        DisableCharacter(Characters.c2060_0015)
        DisableCharacter(Characters.c2060_0019)
        DisableCharacter(Characters.c2060_0020)
        DisableCharacter(Characters.c2810_0003)
        DisableCharacter(Characters.c2810_0004)
        DisableCharacter(Characters.c2810_0005)
        DisableCharacter(Characters.c2810_0006)
        DisableCharacter(Characters.c2810_0007)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11405091)
def Event_11405091():
    """Event 11405091"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2060_0006)
    Kill(Characters.c2060_0011)
    Kill(Characters.c2060_0015)
    Kill(Characters.c2060_0019)
    Kill(Characters.c2060_0020)
    Kill(Characters.c2810_0003)
    Kill(Characters.c2810_0004)
    Kill(Characters.c2810_0005)
    Kill(Characters.c2810_0006)
    Kill(Characters.c2810_0007)


@RestartOnRest(11405092)
def Event_11405092():
    """Event 11405092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11400080))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11400080))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11400080))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11400080))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11400080))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=BLIGHTTOWN))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11400080))
    if not OR_6:
        return RESTART
    EnableFlag(11400080)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=BLIGHTTOWN))
    if not AND_7:
        return RESTART
    DisableFlag(11400080)
    EnableFlag(11405095)


@ContinueOnRest(11405390)
def Event_11405390():
    """Event 11405390"""
    AND_1.Add(FlagDisabled(CommonFlags.QuelaagDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1401990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11405391)
def Event_11405391():
    """Event 11405391"""
    AND_1.Add(FlagDisabled(CommonFlags.QuelaagDead))
    AND_1.Add(FlagEnabled(11405393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1402998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1401990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1402997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11405393)
def Event_11405393():
    """Event 11405393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.QuelaagDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1402996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5280_0000)


@RestartOnRest(11405392)
def Event_11405392():
    """Event 11405392"""
    if FlagEnabled(CommonFlags.QuelaagDead):
        DisableBackread(Characters.c5280_0000)
        Kill(Characters.c5280_0000)
        End()
    Event_11405396()
    Event_11405397()
    if FlagDisabled(11400000):
        DisableCharacter(Characters.c5280_0000)
    DisableAI(Characters.c5280_0000)
    AND_1.Add(FlagEnabled(11405393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1402996))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Intruder))
    if OR_1:
        return
    SkipLinesIfFlagEnabled(11, 11400000)
    DeleteVFX(VFX.QuelaagEntranceFog, erase_root_only=False)
    DeleteVFX(VFX.QuelaagExitFog, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(140000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(140000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    CreateVFX(VFX.QuelaagEntranceFog)
    CreateVFX(VFX.QuelaagExitFog)
    EnableCharacter(Characters.c5280_0000)
    EnableFlag(11400000)
    EnableAI(Characters.c5280_0000)
    EnableBossHealthBar(Characters.c5280_0000, name=5280)


@ContinueOnRest(11400001)
def Event_11400001():
    """Event 11400001"""
    MAIN.Await(CharacterDead(Characters.c5280_0000))
    
    EnableFlag(CommonFlags.QuelaagDead)
    KillBoss(game_area_param_id=1400800)
    DisableObject(Objects.o4950_0000)
    DeleteVFX(VFX.QuelaagEntranceFog)
    DisableObject(Objects.o4951_0000)
    DeleteVFX(VFX.QuelaagExitFog)
    DisableNetworkSync()
    Wait(3.0)
    DisableBackread(Characters.c5280_0000)


@ContinueOnRest(11405394)
def Event_11405394():
    """Event 11405394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.QuelaagDead))
    AND_1.Add(FlagEnabled(11405392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11405391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1402990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.QuelaagMusic)


@ContinueOnRest(11405395)
def Event_11405395():
    """Event 11405395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.QuelaagDead))
    AND_1.Add(FlagEnabled(11405394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.QuelaagMusic)


@EndOnRest(11405396)
def Event_11405396():
    """Event 11405396"""
    AND_1.Add(CharacterAlive(Characters.c5280_0000))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c5280_0000))
    
    CreateNPCPart(Characters.c5280_0000, npc_part_id=5281, part_index=NPCPartType.Part2, part_health=300)
    SetNPCPartEffects(Characters.c5280_0000, npc_part_id=5281, material_sfx_id=75, material_vfx_id=75)
    AND_2.Add(CharacterPartHealth(Characters.c5280_0000, npc_part_id=5281) <= 0)
    AND_3.Add(HealthRatio(Characters.c5280_0000) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    ForceAnimation(Characters.c5280_0000, 3011, wait_for_completion=True)
    Restart()


@EndOnRest(11405397)
def Event_11405397():
    """Event 11405397"""
    AND_1.Add(CharacterAlive(Characters.c5280_0000))
    SkipLinesIfConditionTrue(1, AND_1)
    End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c5280_0000))
    
    CreateNPCPart(Characters.c5280_0000, npc_part_id=5280, part_index=NPCPartType.Part1, part_health=1)
    SetNPCPartEffects(Characters.c5280_0000, npc_part_id=5280, material_sfx_id=60, material_vfx_id=60)
    AND_2.Add(CharacterPartHealth(Characters.c5280_0000, npc_part_id=5280) <= 0)
    AND_3.Add(HealthRatio(Characters.c5280_0000) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    ForceAnimation(Characters.c5280_0000, 2007, wait_for_completion=True)
    Restart()


@RestartOnRest(11400800)
def Event_11400800():
    """Event 11400800"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c5340_0000)
        DisableSoundEvent(sound_id=Sounds.FairLadyMusic)
        DisableMapCollision(collision=Collisions.h5810B0)
        DisableMapCollision(collision=Collisions.h5810B0_0000)
        End()
    
    MAIN.Await(CharacterDead(Characters.c5340_0000))
    
    EnableFlag(CommonFlags.FairLadyDead)
    DisableSoundEvent(sound_id=Sounds.FairLadyMusic)
    DisableMapCollision(collision=Collisions.h5810B0)
    DisableMapCollision(collision=Collisions.h5810B0_0000)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerCovenant(Covenant.ChaosServant))
    if not AND_1:
        return
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()


@ContinueOnRest(11405000)
def Event_11405000():
    """Event 11405000"""
    if ThisEventFlagEnabled():
        AddSpecialEffect(Characters.c5340_0000, 5401)
        End()
    
    MAIN.Await(HealthRatio(Characters.c5340_0000) != 1.0)
    
    AddSpecialEffect(Characters.c5340_0000, 5401)


@RestartOnRest(11400900)
def Event_11400900():
    """Event 11400900"""
    if FlagEnabled(11400902):
        DisableCharacter(Characters.c5240_0000)
        End()
    AND_1.Add(CharacterAlive(Characters.c5240_0000))
    SkipLinesIfConditionTrue(2, AND_1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    
    MAIN.Await(HealthRatio(Characters.c5240_0000) <= 0.0)
    
    EnableNetworkSync()
    EzstateAIRequest(Characters.c5240_0000, command_id=1200, command_slot=0)
    Restart()


@ContinueOnRest(11405100)
def Event_11405100(_, entity: int, region: Region | int, region_1: Region | int, region_2: Region | int):
    """Event 11405100"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_1))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(AND_1)
    
    EnableNetworkSync()
    Restart()


@ContinueOnRest(11405110)
def Event_11405110(
    _,
    entity: int,
    region: Region | int,
    region_1: Region | int,
    region_2: Region | int,
    region_3: Region | int,
    region_4: Region | int,
):
    """Event 11405110"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_3))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_4))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_1))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_2))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_3))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_4))
    
    MAIN.Await(AND_1)
    
    EnableNetworkSync()
    Restart()


@RestartOnRest(11405250)
def Event_11405250(_, character: Character | int):
    """Event 11405250"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(
        character,
        npc_part_id=2811,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(character, npc_part_id=2811, desired_scaling=0.0)
    SetNPCPartEffects(character, npc_part_id=2811, material_sfx_id=1, material_vfx_id=1)
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    SetNPCPartHealth(character, npc_part_id=2811, desired_health=0, overwrite_max=False)


@RestartOnRest(11405300)
def Event_11405300():
    """Event 11405300"""
    Event_11405301(0, character=1400500, part_index=1, npc_part_id=0, npc_part_id_1=3290, flag=3290)
    Event_11405310(0, character=1400500, flag=11405301, bit_index=0, bit_index_1=0)
    Event_11405310(1, character=1400500, flag=11405301, bit_index=2, bit_index_1=0)
    Event_11405320(
        0,
        character=1400500,
        flag=11405301,
        obj=Objects.o3910_0000,
        obj_1=Objects.o3910_0001,
        model_point=120,
        model_point_1=0,
    )
    Event_11405320(
        1,
        character=1400500,
        flag=11405301,
        obj=Objects.o3910_0002,
        obj_1=Objects.o3910_0003,
        model_point=126,
        model_point_1=0,
    )
    Event_11405330(
        0,
        character=1400500,
        flag=11405301,
        character_1=1400600,
        character_2=1400601,
        model_point=120,
        model_point_1=123,
    )
    Event_11405330(
        1,
        character=1400500,
        flag=11405301,
        character_1=1400602,
        character_2=1400603,
        model_point=126,
        model_point_1=129,
    )
    Event_11405301(1, character=1400500, part_index=2, npc_part_id=0, npc_part_id_1=3291, flag=3291)
    Event_11405310(2, character=1400500, flag=11405302, bit_index=5, bit_index_1=0)
    Event_11405320(
        2,
        character=1400500,
        flag=11405302,
        obj=Objects.o3910_0004,
        obj_1=Objects.o3910_0005,
        model_point=135,
        model_point_1=0,
    )
    Event_11405330(
        2,
        character=1400500,
        flag=11405302,
        character_1=1400604,
        character_2=1400605,
        model_point=135,
        model_point_1=137,
    )
    Event_11405330(
        3,
        character=1400500,
        flag=11405302,
        character_1=1400606,
        character_2=1400607,
        model_point=153,
        model_point_1=155,
    )
    Event_11405301(2, character=1400500, part_index=3, npc_part_id=0, npc_part_id_1=3292, flag=3292)
    Event_11405310(3, character=1400500, flag=11405303, bit_index=6, bit_index_1=0)
    Event_11405310(4, character=1400500, flag=11405303, bit_index=8, bit_index_1=0)
    Event_11405320(
        3,
        character=1400500,
        flag=11405303,
        obj=Objects.o3910_0006,
        obj_1=Objects.o3910_0007,
        model_point=138,
        model_point_1=0,
    )
    Event_11405320(
        4,
        character=1400500,
        flag=11405303,
        obj=Objects.o3910_0008,
        obj_1=Objects.o3910_0009,
        model_point=144,
        model_point_1=0,
    )
    Event_11405330(
        4,
        character=1400500,
        flag=11405303,
        character_1=1400608,
        character_2=1400609,
        model_point=138,
        model_point_1=141,
    )
    Event_11405330(
        5,
        character=1400500,
        flag=11405303,
        character_1=1400610,
        character_2=1400611,
        model_point=144,
        model_point_1=150,
    )
    Event_11405301(3, character=1400500, part_index=4, npc_part_id=0, npc_part_id_1=3293, flag=3293)
    Event_11405310(5, character=1400500, flag=11405304, bit_index=4, bit_index_1=0)
    Event_11405320(
        5,
        character=1400500,
        flag=11405304,
        obj=Objects.o3910_0010,
        obj_1=Objects.o3910_0011,
        model_point=132,
        model_point_1=0,
    )
    Event_11405330(
        6,
        character=1400500,
        flag=11405304,
        character_1=1400612,
        character_2=1400613,
        model_point=132,
        model_point_1=134,
    )
    Event_11405330(
        7,
        character=1400500,
        flag=11405304,
        character_1=1400614,
        character_2=1400615,
        model_point=150,
        model_point_1=152,
    )


@EndOnRest(11405301)
def Event_11405301(_, character: int, part_index: short, npc_part_id: short, npc_part_id_1: int, flag: Flag | int):
    """Event 11405301"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=100)
    AND_1.Add(CharacterPartHealth(character, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    DisableFlagRange((11405290, 11405291))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11405290, 11405291))
    AND_3.Add(FlagEnabled(11405290))
    AND_4.Add(FlagEnabled(11405291))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_4)
    EnableFlag(11405290)
    SkipLines(1)
    EnableFlag(11405291)
    EnableFlag(flag)
    if FlagEnabled(11405301):
        ForceAnimation(character, 8000)
    if FlagEnabled(11405302):
        ForceAnimation(character, 8010)


@EndOnRest(11405310)
def Event_11405310(_, character: Character | int, flag: Flag | int, bit_index: uchar, bit_index_1: uchar):
    """Event 11405310"""
    if FlagDisabled(flag):
        AND_1.Add(FlagEnabled(flag))
        AND_2.Add(CharacterDead(character))
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfFinishedConditionTrue(input_condition=AND_2)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)


@EndOnRest(11405320)
def Event_11405320(
    _,
    character: Character | int,
    flag: Flag | int,
    obj: Object | int,
    obj_1: Object | int,
    model_point: short,
    model_point_1: short,
):
    """Event 11405320"""
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


@EndOnRest(11405330)
def Event_11405330(
    _,
    character: int,
    flag: Flag | int,
    character_1: int,
    character_2: int,
    model_point: int,
    model_point_1: int,
):
    """Event 11405330"""
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


@RestartOnRest(11405350)
def Event_11405350(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    left: int,
):
    """Event 11405350"""
    SkipLinesIfValueEqual(1, left=left, right=0)
    SkipLinesIfFlagEnabled(1, 11400533)
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
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableCharacter(character_4)
    EnableCharacter(character_5)
    ForceAnimation(character_1, 7000)
    ForceAnimation(character_2, 7000)
    ForceAnimation(character_3, 7000)
    ForceAnimation(character_4, 7000)
    ForceAnimation(character_5, 7000)


@ContinueOnRest(11400100)
def Event_11400100(_, flag: Flag | int, region: Region | int, entity: int):
    """Event 11400100"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    EnableFlag(flag)
    DisableSpawner(entity=entity)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    DisableFlag(flag)
    EnableSpawner(entity=entity)
    Restart()


@RestartOnRest(11400850)
def Event_11400850(_, character: Character | int, item_lot: int):
    """Event 11400850"""
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


@ContinueOnRest(11400600)
def Event_11400600(_, obj: Object | int, obj_act_id: int):
    """Event 11400600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11400200)
def Event_11400200():
    """Event 11400200"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(Objects.o4560_0000, obj_act_id=-1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=11400201))
    
    TriggerMultiplayerEvent(event_id=10010)
    
    MAIN.Await(HealthRatio(PLAYER) > 0.0)
    
    DisableBackread(Characters.c5280_0000)
    DisableBackread(Characters.c5340_0000)
    WaitFrames(frames=1)
    if FlagDisabled(11010700):
        PlayCutscene(140010, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(140015, cutscene_flags=0, player_id=10000)
        EnableFlag(11500200)
    WaitFrames(frames=1)
    if FlagDisabled(CommonFlags.QuelaagDead):
        EnableBackread(Characters.c5280_0000)
    EnableBackread(Characters.c5340_0000)
    EnableFlag(11400200)
    AwardAchievement(achievement_id=30)
    AwardItemLot(9030, host_only=True)


@ContinueOnRest(11415170)
def Event_11415170():
    """Event 11415170"""
    MAIN.Await(MultiplayerEvent(event_id=10010))
    
    DisableNetworkSync()
    PlaySoundEffect(Objects.o4550_0000, 130300002, sound_type=SoundType.o_Object)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(Objects.o4550_0000, 130300002, sound_type=SoundType.o_Object)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(Objects.o4550_0000, 130300002, sound_type=SoundType.o_Object)
    Restart()


@ContinueOnRest(11400210)
def Event_11400210():
    """Event 11400210"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o4570_0000)
        End()
    
    MAIN.Await(ObjectDestroyed(Objects.o4570_0000))
    
    EnableFlag(11400210)


@ContinueOnRest(11400220)
def Event_11400220():
    """Event 11400220"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1402400))
    
    AddSpecialEffect(PLAYER, 4140)
    Restart()


@ContinueOnRest(11400230)
def Event_11400230():
    """Event 11400230"""
    DisableNetworkSync()
    if FlagEnabled(CommonFlags.BlighttownDoorOpened):
        EndOfAnimation(obj=m10_00_Objects.o1309, animation_id=1)
        End()
    AND_1.Add(Singleplayer())
    AND_1.Add(FlagDisabled(CommonFlags.BlighttownDoorOpened))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=m10_00_Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=m10_00_Objects.o1309)
    Restart()


@RestartOnRest(11405200)
def Event_11405200(_, character: Character | int, obj: int):
    """Event 11405200"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    RestoreObject(obj)
    DisableCharacterCollision(character)
    DisableGravity(character)
    Move(character, destination=obj, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(ObjectDestroyed(obj))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character)
    EnableCharacterCollision(character)
    EnableGravity(character)


@ContinueOnRest(11400510)
def Event_11400510(_, character: Character | int, flag: Flag | int):
    """Event 11400510"""
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


@ContinueOnRest(11400520)
def Event_11400520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11400501)
def Event_11400501(_, character: Character | int, flag: Flag | int):
    """Event 11400501"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1284))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1272))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400502)
def Event_11400502(_, character: Character | int, flag: Flag | int):
    """Event 11400502"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    OR_2.Add(FlagEnabled(1280))
    OR_2.Add(FlagEnabled(1281))
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400503)
def Event_11400503(_, character: Character | int, flag: Flag | int):
    """Event 11400503"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1286))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11400504)
def Event_11400504(_, character: Character | int, flag: Flag | int, character_1: Character | int):
    """Event 11400504"""
    AND_1.Add(FlagDisabled(1603))
    AND_1.Add(FlagEnabled(1601))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1763))
    AND_2.Add(FlagEnabled(1760))
    AND_2.Add(HealthRatio(character_1) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(character_1) > 0.0)
    AND_2.Add(Attacked(attacked_entity=character_1, attacker=PLAYER))
    AND_2.Add(ThisEventFlagDisabled())
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(1763))
    OR_2.Add(FlagEnabled(745))
    AND_3.Add(OR_2)
    AND_3.Add(ThisEventFlagDisabled())
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
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.Enemy)
    EnableCharacter(character_1)
    SetTeamTypeAndExitStandbyAnimation(character_1, team_type=TeamType.Enemy)
    if ThisEventFlagEnabled():
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_7.Add(OR_7)
    AND_7.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_7.Add(FlagDisabled(11402889))
    if not AND_7:
        return
    BetrayCurrentCovenant()
    EnableFlag(742)
    EnableFlag(746)
    SaveRequest()


@ContinueOnRest(11400530)
def Event_11400530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400530"""
    AND_1.Add(FlagDisabled(1253))
    AND_1.Add(FlagEnabled(1256))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)


@ContinueOnRest(11400531)
def Event_11400531(_, character: int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400531"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1280))
    AND_1.Add(FlagEnabled(11400593))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(11405001)
    SetNest(character, region=1402301)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.FightingAlly)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    AND_2.Add(CharacterInsideRegion(character, region=1402300))
    AND_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11405001)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.Ally)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@ContinueOnRest(11400532)
def Event_11400532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400532"""
    AND_1.Add(FlagDisabled(1282))
    AND_1.Add(FlagDisabled(1283))
    AND_1.Add(FlagDisabled(1287))
    AND_1.Add(FlagEnabled(1281))
    AND_1.Add(FlagEnabled(753))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@RestartOnRest(11400533)
def Event_11400533():
    """Event 11400533"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3220_0000)
        DisableCharacter(Characters.c3220_0001)
        DisableCharacter(Characters.c3220_0002)
        DisableCharacter(Characters.c3220_0003)
        DisableCharacter(Characters.c3220_0004)
        End()
    
    MAIN.Await(CharacterDead(Characters.c3210_0000))
    
    End()


@ContinueOnRest(11400536)
def Event_11400536(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400536"""
    AND_1.Add(FlagDisabled(1294))
    AND_1.Add(FlagEnabled(1290))
    OR_1.Add(PlayerHasWeapon(1331000))
    OR_1.Add(PlayerHasWeapon(1331100))
    OR_1.Add(PlayerHasWeapon(1331200))
    OR_1.Add(PlayerHasWeapon(1331300))
    OR_1.Add(PlayerHasWeapon(1331400))
    OR_1.Add(PlayerHasWeapon(1331500))
    OR_1.Add(PlayerHasWeapon(1332000))
    OR_1.Add(PlayerHasWeapon(1332100))
    OR_1.Add(PlayerHasWeapon(1332200))
    OR_1.Add(PlayerHasWeapon(1332300))
    OR_1.Add(PlayerHasWeapon(1332400))
    OR_1.Add(PlayerHasWeapon(1332500))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11400537)
def Event_11400537(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400537"""
    AND_1.Add(FlagDisabled(1294))
    AND_1.Add(FlagEnabled(1293))
    AND_1.Add(FlagEnabled(11400595))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11400538)
def Event_11400538(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400538"""
    AND_1.Add(FlagDisabled(1294))
    AND_1.Add(FlagEnabled(1291))
    AND_1.Add(FlagEnabled(CommonFlags.BedOfChaosDead))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11400539)
def Event_11400539(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400539"""
    AND_1.Add(FlagEnabled(1290))
    AND_1.Add(FlagEnabled(CommonFlags.BedOfChaosDead))
    AND_2.Add(FlagDisabled(1294))
    AND_2.Add(FlagEnabled(1291))
    AND_2.Add(FlagDisabled(71400061))
    AND_2.Add(FlagEnabled(CommonFlags.BedOfChaosDead))
    AND_3.Add(FlagDisabled(1294))
    AND_3.Add(FlagEnabled(1292))
    AND_3.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11400551)
def Event_11400551(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400551"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1497))
    AND_1.Add(FlagEnabled(11020592))
    AND_1.Add(InsideMap(game_map=BLIGHTTOWN))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableFlag(814)


@ContinueOnRest(11400552)
def Event_11400552(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11400552"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1501))
    AND_1.Add(FlagEnabled(11400590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11400553)
def Event_11400553():
    """Event 11400553"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11400590))
    
    End()


@ContinueOnRest(11400554)
def Event_11400554(_, character: Character | int):
    """Event 11400554"""
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(ThisEventFlagEnabled())
    OR_1.Add(FlagEnabled(1501))
    
    MAIN.Await(OR_1)
    
    if ThisEventFlagDisabled():
        MAIN.Await(FlagDisabled(814))
    SetStandbyAnimationSettings(character, cancel_animation=7856)


@ContinueOnRest(11400560)
def Event_11400560(
    _,
    character: Character | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    character_1: Character | int,
):
    """Event 11400560"""
    AND_1.Add(Host())
    AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(FlagDisabled(1603))
    AND_1.Add(FlagEnabled(1600))
    AND_1.Add(FlagEnabled(11400582))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)
    EnableCharacter(character_1)
    DisableFlag(1766)
    EnableFlag(11405022)


@ContinueOnRest(11400566)
def Event_11400566(_, character: Character | int, character_1: Character | int):
    """Event 11400566"""
    SkipLinesIfHost(1)
    if FlagEnabled(11405022):
        return
    AND_1.Add(FlagEnabled(746))
    if not AND_1:
        return
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableFlag(1766)
    DisableFlag(11405022)


@ContinueOnRest(11400567)
def Event_11400567(_, character: Character | int, character_1: Character | int):
    """Event 11400567"""
    AND_1.Add(Host())
    AND_2.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(not AND_2)
    AND_1.Add(FlagDisabled(746))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableFlag(11405022)


@ContinueOnRest(CommonFlags.FairLadyDead)
def Event_140():
    """Event 140"""
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


@ContinueOnRest(11405030)
def Event_11405030():
    """Event 11405030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0010, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11405033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11405031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0010)
    if FlagEnabled(CommonFlags.QuelaagDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11400901))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0010))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0010,
        region=1402050,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


@ContinueOnRest(14005990)
def Event_14005990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 14005990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11405029)
def Event_11405029():
    """Event 11405029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0010, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11405033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11405031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0010)
    if FlagEnabled(CommonFlags.QuelaagDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11405031))
    AND_1.Add(FlagDisabled(11405033))
    AND_1.Add(FlagEnabled(11400901))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0010))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0010,
        region=1402050,
        summon_flag=11405031,
        dismissal_flag=11405033,
    )


@ContinueOnRest(11405032)
def Event_11405032():
    """Event 11405032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11405031))
    AND_1.Add(FlagEnabled(11405393))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0010, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0010)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0010, region=1402998))
    
    RotateToFaceEntity(Characters.c0000_0010, target_entity=1402997)
    ForceAnimation(Characters.c0000_0010, 7410)
    AICommand(Characters.c0000_0010, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0010)


@ContinueOnRest(11405035)
def Event_11405035():
    """Event 11405035"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11405036):
        return
    if FlagEnabled(CommonFlags.QuelaagDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11400901))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1402061))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=Characters.c0000_0007,
        region=1402060,
        summon_flag=11405036,
        dismissal_flag=11405037,
    )
    Wait(20.0)
    Restart()


@ContinueOnRest(11400901)
def Event_11400901():
    """Event 11400901"""
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(11405036))
    AND_1.Add(FlagDisabled(11405037))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(Characters.c0000_0007)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(Characters.c0000_0007))
    
    EnableFlag(11400901)


@ContinueOnRest(11405843)
def Event_11405843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11405843"""
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


@ContinueOnRest(11405846)
def Event_11405846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11405846"""
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
