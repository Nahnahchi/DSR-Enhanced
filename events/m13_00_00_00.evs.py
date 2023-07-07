"""
Catacombs

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m13_00_00_00_enums import *
from ..enums.common_enums import CommonFlags
from ..enums.m13_01_00_00_enums import Objects as m13_01_Objects


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11300997()
    Event_11300998()
    Event_11302098(0, character=Characters.c0000_drk1)
    RegisterBonfire(bonfire_flag=11300992, obj=Objects.o0200_0000)
    RegisterBonfire(bonfire_flag=11300984, obj=Objects.o0200_0001)
    RegisterBonfire(bonfire_flag=11300976, obj=Objects.o0200_0003)
    RegisterLadder(start_climbing_flag=11300010, stop_climbing_flag=11300011, obj=Objects.o3040_0000)
    RegisterLadder(start_climbing_flag=11300012, stop_climbing_flag=11300013, obj=Objects.o3041_0000)
    RegisterLadder(start_climbing_flag=11300014, stop_climbing_flag=11300015, obj=Objects.o3042_0000)
    if FlagEnabled(CommonFlags.PinwheelDead):
        RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=Objects.o3043_0000)
    RegisterLadder(start_climbing_flag=11300018, stop_climbing_flag=11300019, obj=Objects.o3044_0000)
    RegisterLadder(start_climbing_flag=11300020, stop_climbing_flag=11300021, obj=Objects.o3045_0000)
    RegisterLadder(start_climbing_flag=11300022, stop_climbing_flag=11300023, obj=Objects.o3046_0000)
    RegisterLadder(start_climbing_flag=11300024, stop_climbing_flag=11300025, obj=Objects.o3046_0001)
    RegisterLadder(start_climbing_flag=11300026, stop_climbing_flag=11300027, obj=Objects.o3047_0000)
    RegisterLadder(start_climbing_flag=11300028, stop_climbing_flag=11300029, obj=Objects.o3048_0000)
    SkipLinesIfClient(3)
    DisableFlag(11300000)
    DisableObject(Objects.o3951_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    Event_11300090(0, obj=Objects.o3952_0000, vfx_id=VFX.CheckpointFog1, destination=1302650, destination_1=1302651)
    Event_11305065()
    Event_11305066()
    Event_11305067()
    Event_11300800()
    Event_11300300()
    Event_11300350()
    Event_11300900(
        0,
        obj_act_id=11300900,
        obj=Objects.o3011_0000,
        obj_1=Objects.o3020_0000,
        navmesh_id=Navigation.InvaderSpawn00,
    )
    Event_11300900(
        1,
        obj_act_id=11300901,
        obj=Objects.o3011_0003,
        obj_1=Objects.o3021_0000,
        navmesh_id=Navigation.Navmesh_MiddleGate,
    )
    Event_11305032(0, obj_act_id=11300902, obj_act_id_1=11300903, flag=11305035, flag_1=11305036)
    Event_11305030(
        0,
        flag=11300402,
        flag_1=11305035,
        flag_2=11305036,
        obj=Objects.o3011_0001,
        obj_1=Objects.o3000_0000,
        navmesh_id=Navigation.Navmesh_BridgeA,
    )
    Event_11305032(1, obj_act_id=11300904, obj_act_id_1=11300905, flag=11305037, flag_1=11305038)
    Event_11305030(
        1,
        flag=11300403,
        flag_1=11305037,
        flag_2=11305038,
        obj=Objects.o3011_0002,
        obj_1=Objects.o3001_0000,
        navmesh_id=Navigation.Navmesh_BridgeB,
    )
    Event_11305000()
    Event_11305001()
    Event_11305002()
    Event_11305003()
    Event_11305004()
    Event_11305009()
    Event_11300420(0, character=10000)
    Event_11300420(1, character=10001)
    Event_11300420(2, character=10002)
    Event_11300420(3, character=10003)
    Event_11300420(4, character=10004)
    Event_11300420(5, character=10005)
    Event_11300420(6, character=10006)
    Event_11300420(7, character=10007)
    Event_11300420(8, character=10008)
    Event_11300420(9, character=10009)
    Event_11300420(10, character=10010)
    Event_11300420(11, character=10011)
    Event_11300420(12, character=10012)
    Event_11300420(13, character=10013)
    Event_11300420(14, character=10014)
    Event_11300420(15, character=10015)
    Event_11300420(16, character=10016)
    Event_11300420(17, character=10017)
    Event_11300210()
    Event_11305060()
    Event_11300200()
    Event_11305045()
    Event_11300100(0, flag=11300100, region=1302100, obj=Objects.o3030_0000, sound_id=303000000)
    Event_11300100(1, flag=11300101, region=1302101, obj=Objects.o3031_0000, sound_id=303100000)
    Event_11300100(2, flag=11300102, region=1302102, obj=Objects.o3032_0000, sound_id=303200000)
    Event_11300100(3, flag=11300103, region=1302103, obj=Objects.o3033_0000, sound_id=303300000)
    Event_11300100(4, flag=11300104, region=1302104, obj=Objects.o3034_0000, sound_id=303400000)
    Event_11300100(5, flag=11300105, region=1302105, obj=Objects.o3035_0000, sound_id=303500000)
    Event_11300150()
    Event_11300160()
    Event_11300700(0, obj=Objects.o3321_0000, obj_flag=11300750)
    Event_11300700(1, obj=Objects.o3321_0001, obj_flag=11300751)
    Event_11300700(2, obj=Objects.o3321_0002, obj_flag=11300752)
    Event_11300700(3, obj=Objects.o3321_0003, obj_flag=11300753)
    Event_11300700(4, obj=Objects.o3321_0004, obj_flag=11300754)
    Event_11300700(5, obj=Objects.o3321_0005, obj_flag=11300755)
    Event_11300700(6, obj=Objects.o3321_0006, obj_flag=11300756)
    Event_11300700(7, obj=Objects.o3321_0007, obj_flag=11300757)
    Event_11300700(8, obj=Objects.o3321_0008, obj_flag=11300758)
    Event_11300700(9, obj=Objects.o3321_0009, obj_flag=11300759)
    Event_11300700(10, obj=Objects.o3321_0010, obj_flag=11300760)
    Event_11300700(12, obj=Objects.o3321_0011, obj_flag=11300762)
    Event_11300700(13, obj=Objects.o3321_1004, obj_flag=11300763)
    Event_11300700(14, obj=Objects.o3321_1005, obj_flag=11300764)
    Event_11300700(15, obj=Objects.o3321_1006, obj_flag=11300765)
    Event_11300700(16, obj=Objects.o3321_1007, obj_flag=11300766)
    Event_11300700(17, obj=Objects.o3321_1008, obj_flag=11300767)
    Event_11300700(18, obj=Objects.o3321_1009, obj_flag=11300768)
    Event_11300700(19, obj=Objects.o3321_1010, obj_flag=11300769)
    Event_11300880()
    DisableSoundEvent(sound_id=Sounds.PinwheelMusic)
    if FlagEnabled(CommonFlags.PinwheelDead):
        DisableObject(Objects.o3954_0000)
        DeleteVFX(VFX.PinwheelEntranceFog, erase_root_only=False)
        Event_11305392()
    else:
        Event_11305390()
        Event_11305391()
        Event_11305393()
        Event_11305392()
        Event_11300001()
        Event_11305394()
        Event_11305395()
        Event_11300882()
        Event_11305396()
        Event_11305397()
        Event_11305398()
        Event_11305250()
        Event_11305350(
            0,
            flag=11305251,
            flag_1=11305252,
            character=Characters.c3320_0001,
            character_1=Characters.c3320_0002,
            destination=1302600,
            destination_1=1302612,
            flag_2=11305300,
        )
        Event_11305350(
            1,
            flag=11305253,
            flag_1=11305254,
            character=Characters.c3320_0003,
            character_1=Characters.c3320_0004,
            destination=1302601,
            destination_1=1302611,
            flag_2=11305301,
        )
        Event_11305350(
            2,
            flag=11305255,
            flag_1=11305256,
            character=Characters.c3320_0005,
            character_1=Characters.c3320_0006,
            destination=1302602,
            destination_1=1302610,
            flag_2=11305302,
        )
        Event_11305350(
            3,
            flag=11305257,
            flag_1=11305258,
            character=Characters.c3320_0007,
            character_1=Characters.c3320_0008,
            destination=1302603,
            destination_1=1302609,
            flag_2=11305303,
        )
        Event_11305350(
            4,
            flag=11305259,
            flag_1=11305260,
            character=Characters.c3320_0009,
            character_1=Characters.c3320_0010,
            destination=1302604,
            destination_1=1302608,
            flag_2=11305304,
        )
        Event_11305350(
            5,
            flag=11305261,
            flag_1=11305262,
            character=Characters.c3320_0011,
            character_1=Characters.c3320_0012,
            destination=1302605,
            destination_1=1302607,
            flag_2=11305305,
        )
        Event_11305350(
            6,
            flag=11305263,
            flag_1=11305264,
            character=Characters.c3320_0013,
            character_1=Characters.c3320_0014,
            destination=1302606,
            destination_1=1302606,
            flag_2=11305306,
        )
        Event_11305370(0, character=Characters.c3320_0001, flag=11305251)
        Event_11305370(1, character=Characters.c3320_0002, flag=11305252)
        Event_11305370(2, character=Characters.c3320_0003, flag=11305253)
        Event_11305370(3, character=Characters.c3320_0004, flag=11305254)
        Event_11305370(4, character=Characters.c3320_0005, flag=11305255)
        Event_11305370(5, character=Characters.c3320_0006, flag=11305256)
        Event_11305370(6, character=Characters.c3320_0007, flag=11305257)
        Event_11305370(7, character=Characters.c3320_0008, flag=11305258)
        Event_11305370(8, character=Characters.c3320_0009, flag=11305259)
        Event_11305370(9, character=Characters.c3320_0010, flag=11305260)
        Event_11305370(10, character=Characters.c3320_0011, flag=11305261)
        Event_11305370(11, character=Characters.c3320_0012, flag=11305262)
        Event_11305370(12, character=Characters.c3320_0013, flag=11305263)
    Event_11305370(13, character=Characters.c3320_0014, flag=11305264)
    Event_11300850(0, character=Characters.c2650_0000, item_lot=0)
    Event_11300850(1, character=Characters.c2650_0001, item_lot=0)
    Event_11300850(2, character=Characters.c2650_0002, item_lot=0)
    Event_11300850(3, character=Characters.c2650_0003, item_lot=0)
    Event_11300850(4, character=Characters.c2650_0004, item_lot=0)
    Event_11300850(5, character=Characters.c2650_0005, item_lot=0)
    Event_11300850(6, character=Characters.c3300_0000, item_lot=33003000)
    Event_11300850(7, character=Characters.c3300_0001, item_lot=33003000)
    Event_11300850(8, character=1300300, item_lot=0)
    Event_11300850(9, character=Characters.c2794_0000, item_lot=27902000)
    Event_11300850(10, character=Characters.c0000_drk1, item_lot=61840000)
    Event_11300850(11, character=Characters.c0000_ano1, item_lot=0)
    Event_11305846(0, flag=CommonFlags.PinwheelDead, obj=Objects.o3954_0000, vfx_id=VFX.PinwheelEntranceFog)
    Event_11305843(
        0,
        flag=CommonFlags.PinwheelDead,
        line_intersects=1301990,
        anchor_entity=1302998,
        target_entity=1302997,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0004, event_flag=8948)
    Event_11305025()
    Event_11305029()
    Event_11305027()
    Event_11305990(0, flag=11305026, summoned_character=Characters.c0000_0004)
    Event_11300510(0, character=Characters.c2920_0000, flag=1341)
    Event_11300520(0, character=Characters.c2920_0000, first_flag=1340, last_flag=1343, flag=CommonFlags.VamosDead)
    Event_11305061(0, character=Characters.c2920_0000)
    HumanityRegistration(Characters.c0000_0002, event_flag=8478)
    SkipLinesIfFlagEnabled(2, 1627)
    SkipLinesIfFlagRangeAnyEnabled(1, (1620, 1621))
    DisableCharacter(Characters.c0000_0002)
    Event_11300510(1, character=Characters.c0000_0002, flag=1627)
    Event_11300531(0, character=Characters.c0000_0002, flag=1628)
    Event_11300530(0, character=Characters.c0000_0002, first_flag=1620, last_flag=1631, flag=1621)
    Event_11300533(0, character=Characters.c0000_0002, first_flag=1620, last_flag=1631, flag=1623)
    Event_11300592()
    Event_11300593()


@ContinueOnRest(11302098)
def Event_11302098(_, character: Character | int):
    """Event 11302098"""
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_1)
    
    DisableAI(character)
    EnableInvincibility(character)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 2180))
    
    MAIN.Await(AND_2)
    
    EnableAI(character)
    DisableInvincibility(character)
    Restart()


@ContinueOnRest(11300998)
def Event_11300998():
    """Event 11300998"""
    SkipLinesIfFlagDisabled(3, 11012998)
    SkipLinesIfFlagEnabled(2, 11010868)
    SkipLinesIfFlagEnabled(1, 11510869)
    SkipLinesIfFlagDisabled(2, 11302998)
    DisableCharacter(Characters.c0000_ano1)
    End()
    OR_1.Add(FlagEnabled(11307900))
    OR_1.Add(FlagEnabled(11307910))
    OR_1.Add(FlagEnabled(11307920))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11302998)


@ContinueOnRest(11300997)
def Event_11300997():
    """Event 11300997"""
    if FlagDisabled(11012997):
        AND_1.Add(Attacked(attacked_entity=Characters.c0000_ano1, attacker=PLAYER))
        AND_1.Add(HealthRatio(Characters.c0000_ano1) <= 0.75)
    
        MAIN.Await(AND_1)
    
        EnableFlag(11012997)
        EnableFlag(744)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_ano1, team_type=TeamType.HostileAlly)


@ContinueOnRest(11300090)
def Event_11300090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11300090"""
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


@RestartOnRest(11305065)
def Event_11305065():
    """Event 11305065"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2900_0034)
        DisableCharacter(Characters.c2900_0040)
        DisableCharacter(Characters.c2900_0041)
        DisableCharacter(Characters.c2900_0054)
        DisableCharacter(Characters.c2900_0055)
        DisableCharacter(Characters.c2900_0056)
        DisableCharacter(Characters.c2900_0057)
        DisableCharacter(Characters.c2900_0058)
        DisableCharacter(Characters.c2930_0007)
        DisableCharacter(Characters.c2930_0008)
        DisableCharacter(Characters.c2930_0009)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11305066)
def Event_11305066():
    """Event 11305066"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2900_0034)
    Kill(Characters.c2900_0040)
    Kill(Characters.c2900_0041)
    Kill(Characters.c2900_0054)
    Kill(Characters.c2900_0055)
    Kill(Characters.c2900_0056)
    Kill(Characters.c2900_0057)
    Kill(Characters.c2900_0058)
    Kill(Characters.c2930_0007)
    Kill(Characters.c2930_0008)
    Kill(Characters.c2930_0009)


@RestartOnRest(11305067)
def Event_11305067():
    """Event 11305067"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=CATACOMBS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11300050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=CATACOMBS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11300050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=CATACOMBS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11300050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=CATACOMBS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11300050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=CATACOMBS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11300050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=CATACOMBS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11300050))
    if not OR_6:
        return RESTART
    EnableFlag(11300050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=CATACOMBS))
    if not AND_7:
        return RESTART
    DisableFlag(11300050)
    EnableFlag(11305069)


@ContinueOnRest(11305390)
def Event_11305390():
    """Event 11305390"""
    AND_1.Add(FlagDisabled(CommonFlags.PinwheelDead))
    AND_1.Add(CharacterAlive(Characters.c3320_0000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1302998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1301990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11305391)
def Event_11305391():
    """Event 11305391"""
    AND_1.Add(FlagDisabled(CommonFlags.PinwheelDead))
    AND_1.Add(FlagEnabled(11305393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1302998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1301990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11305393)
def Event_11305393():
    """Event 11305393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.PinwheelDead))
        AND_1.Add(FlagEnabled(11305390))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1302996))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c3320_0000)


@RestartOnRest(11305392)
def Event_11305392():
    """Event 11305392"""
    if FlagEnabled(CommonFlags.PinwheelDead):
        DisableCharacter(Characters.c3320_0000)
        Kill(Characters.c3320_0000)
        End()
    if FlagDisabled(11300000):
        DisableCharacter(Characters.c3320_0000)
    DisableAI(Characters.c3320_0000)
    AND_1.Add(FlagDisabled(CommonFlags.PinwheelDead))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(8, 11300000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(130000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(Characters.c3320_0000)
    EnableFlag(11300000)
    EnableFlag(11300005)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c3320_0000, authority_level=UpdateAuthority.Forced)
    EnableAI(Characters.c3320_0000)
    EnableBossHealthBar(Characters.c3320_0000, name=3320)


@ContinueOnRest(11300001)
def Event_11300001():
    """Event 11300001"""
    MAIN.Await(HealthRatio(Characters.c3320_0000) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(Characters.c3320_0000, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.c3320_0000))
    
    EnableFlag(CommonFlags.PinwheelDead)
    KillBoss(game_area_param_id=1300800)
    DisableObject(Objects.o3954_0000)
    DeleteVFX(VFX.PinwheelEntranceFog)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=Objects.o3043_0000)
    Event_11300880()


@ContinueOnRest(11305394)
def Event_11305394():
    """Event 11305394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.PinwheelDead))
    AND_1.Add(FlagEnabled(11305392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11305391))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.PinwheelMusic)


@ContinueOnRest(11305395)
def Event_11305395():
    """Event 11305395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.PinwheelDead))
    AND_1.Add(FlagEnabled(11305394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.PinwheelMusic)


@ContinueOnRest(11305396)
def Event_11305396():
    """Event 11305396"""
    MAIN.Await(CharacterHasTAEEvent(Characters.c3320_0000, tae_event_id=600))
    
    DisableCharacter(Characters.c3320_0000)
    DisableFlagRange((11305320, 11305326))
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(Characters.c3320_0000, authority_level=UpdateAuthority.Forced)
    EnableRandomFlagInRange(flag_range=(11305320, 11305326))
    EnableFlag(11305329)
    OR_1.Add(FlagDisabled(11305329))
    OR_1.Add(TimeElapsed(seconds=5.0))
    
    MAIN.Await(OR_1)
    
    Wait(3.0)
    EnableCharacter(Characters.c3320_0000)
    if FlagEnabled(11305320):
        Move(Characters.c3320_0000, destination=1302600, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305321):
        Move(Characters.c3320_0000, destination=1302602, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305322):
        Move(Characters.c3320_0000, destination=1302604, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305323):
        Move(Characters.c3320_0000, destination=1302605, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305324):
        Move(Characters.c3320_0000, destination=1302606, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305325):
        Move(Characters.c3320_0000, destination=1302608, destination_type=CoordEntityType.Region, short_move=True)
    if FlagEnabled(11305326):
        Move(Characters.c3320_0000, destination=1302612, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=1)
    EnableCharacter(Characters.c3320_0000)
    ForceAnimation(Characters.c3320_0000, 7000, wait_for_completion=True)
    Restart()


@ContinueOnRest(11300882)
def Event_11300882():
    """Event 11300882"""
    AND_1.Add(FlagEnabled(11305329))
    AND_2.Add(FlagEnabled(11305329))
    AND_3.Add(FlagEnabled(11305329))
    AND_4.Add(FlagEnabled(11305329))
    AND_5.Add(FlagEnabled(11305329))
    AND_6.Add(FlagEnabled(11305329))
    AND_7.Add(FlagEnabled(11305329))
    AND_1.Add(FlagEnabled(11305320))
    AND_2.Add(FlagEnabled(11305321))
    AND_3.Add(FlagEnabled(11305322))
    AND_4.Add(FlagEnabled(11305323))
    AND_5.Add(FlagEnabled(11305324))
    AND_6.Add(FlagEnabled(11305325))
    AND_7.Add(FlagEnabled(11305326))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    EnableFlag(11305320)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_2)
    EnableFlag(11305321)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_3)
    EnableFlag(11305322)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_4)
    EnableFlag(11305323)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_5)
    EnableFlag(11305324)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_6)
    EnableFlag(11305325)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_7)
    EnableFlag(11305326)
    DisableFlag(11305329)
    Restart()


@ContinueOnRest(11305397)
def Event_11305397():
    """Event 11305397"""
    if Client():
        return
    if FlagDisabled(11305310):
        AND_1.Add(FlagDisabled(11305399))
        AND_1.Add(CharacterHasTAEEvent(Characters.c3320_0000, tae_event_id=700))
    
        MAIN.Await(AND_1)
    
        EnableFlag(11305310)
    DisableFlagRange((11305300, 11305306))
    EnableRandomFlagInRange(flag_range=(11305300, 11305306))
    SkipLinesIfFlagDisabled(2, 11305300)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305251, 11305252))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305301)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305253, 11305254))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305302)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305255, 11305256))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305303)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305257, 11305258))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305304)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305259, 11305260))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305305)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305261, 11305262))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305306)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305263, 11305264))
    DisableFlag(11305310)
    if FlagEnabled(11305310):
        return RESTART
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(Characters.c3320_0000, tae_event_id=700))
    
    Restart()


@ContinueOnRest(11305398)
def Event_11305398():
    """Event 11305398"""
    MAIN.Await(HealthRatio(Characters.c3320_0000) <= 0.30000001192092896)
    
    EnableFlag(11305399)
    AICommand(Characters.c3320_0000, command_id=1, command_slot=1)
    ReplanAI(Characters.c3320_0000)
    Event_11305330(0, character=Characters.c3320_0001, flag=11305251)
    Event_11305330(1, character=Characters.c3320_0002, flag=11305252)
    Event_11305330(2, character=Characters.c3320_0003, flag=11305253)
    Event_11305330(3, character=Characters.c3320_0004, flag=11305254)
    Event_11305330(4, character=Characters.c3320_0005, flag=11305255)
    Event_11305330(5, character=Characters.c3320_0006, flag=11305256)
    Event_11305330(6, character=Characters.c3320_0007, flag=11305257)
    Event_11305330(7, character=Characters.c3320_0008, flag=11305258)
    Event_11305330(8, character=Characters.c3320_0009, flag=11305259)
    Event_11305330(9, character=Characters.c3320_0010, flag=11305260)
    Event_11305330(10, character=Characters.c3320_0011, flag=11305261)
    Event_11305330(11, character=Characters.c3320_0012, flag=11305262)
    Event_11305330(12, character=Characters.c3320_0013, flag=11305263)
    Event_11305330(13, character=Characters.c3320_0014, flag=11305264)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(11305251, 11305264)))
    
    AICommand(Characters.c3320_0000, command_id=2, command_slot=1)
    ReplanAI(Characters.c3320_0000)
    AND_1.Add(FlagEnabled(11305399))
    AND_1.Add(CharacterHasTAEEvent(Characters.c3320_0000, tae_event_id=700))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c3320_0000, command_id=1, command_slot=1)
    ReplanAI(Characters.c3320_0000)
    Event_11305350(
        10,
        flag=11305251,
        flag_1=11305252,
        character=Characters.c3320_0001,
        character_1=Characters.c3320_0002,
        destination=1302602,
        destination_1=1302603,
        flag_2=11305300,
    )
    Event_11305350(
        11,
        flag=11305253,
        flag_1=11305254,
        character=Characters.c3320_0003,
        character_1=Characters.c3320_0004,
        destination=1302604,
        destination_1=1302605,
        flag_2=11305301,
    )
    Event_11305350(
        12,
        flag=11305255,
        flag_1=11305256,
        character=Characters.c3320_0005,
        character_1=Characters.c3320_0006,
        destination=1302607,
        destination_1=1302608,
        flag_2=11305302,
    )
    Event_11305350(
        13,
        flag=11305257,
        flag_1=11305258,
        character=Characters.c3320_0007,
        character_1=Characters.c3320_0008,
        destination=1302609,
        destination_1=1302612,
        flag_2=11305303,
    )


@ContinueOnRest(11305330)
def Event_11305330(_, character: Character | int, flag: Flag | int):
    """Event 11305330"""
    AICommand(character, command_id=1, command_slot=1)
    ReplanAI(character)
    
    MAIN.Await(FlagDisabled(flag))
    
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)


@ContinueOnRest(11305350)
def Event_11305350(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    character: int,
    character_1: int,
    destination: int,
    destination_1: int,
    flag_2: Flag | int,
):
    """Event 11305350"""
    if FlagDisabled(11305399):
        AND_1.Add(Host())
        AND_1.Add(FlagDisabled(11305310))
        AND_1.Add(FlagEnabled(flag_2))
    
        MAIN.Await(AND_1)
    
        WaitForNetworkApproval(max_seconds=3.0)
    DisableFlag(flag_2)
    AddSpecialEffect(character, 5450)
    AddSpecialEffect(character_1, 5450)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    EnableCharacter(character_1)
    ReplanAI(character)
    ReplanAI(character_1)
    ForceAnimation(character, 7000)
    ForceAnimation(character_1, 7000)
    EnableFlag(flag)
    EnableFlag(flag_1)
    if FlagEnabled(11305399):
        return
    RestartEvent(event_id=11305250)
    Restart()


@ContinueOnRest(11305370)
def Event_11305370(_, character: Character | int, flag: Flag | int):
    """Event 11305370"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=710))
    AND_2.Add(HealthRatio(Characters.c3320_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_1)
    AICommand(character, command_id=1, command_slot=1)
    ReplanAI(character)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=710))
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ResetAnimation(character, disable_interpolation=True)
    DisableCharacter(character)
    DisableFlag(flag)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    RestartEvent(event_id=11305250)
    if FlagDisabled(flag):
        return RESTART


@ContinueOnRest(11305250)
def Event_11305250():
    """Event 11305250"""
    MAIN.Await(FlagEnabled(11305392))
    
    AIEvent(Characters.c3320_0000, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0001, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0002, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0003, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0004, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0005, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0006, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0007, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0008, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0009, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0010, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0011, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0012, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0013, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(Characters.c3320_0014, command_id=0, command_slot=0, first_event_flag=11305251, last_event_flag=11305264)
    ReplanAI(Characters.c3320_0000)
    ReplanAI(Characters.c3320_0001)
    ReplanAI(Characters.c3320_0002)
    ReplanAI(Characters.c3320_0003)
    ReplanAI(Characters.c3320_0004)
    ReplanAI(Characters.c3320_0005)
    ReplanAI(Characters.c3320_0006)
    ReplanAI(Characters.c3320_0007)
    ReplanAI(Characters.c3320_0008)
    ReplanAI(Characters.c3320_0009)
    ReplanAI(Characters.c3320_0010)
    ReplanAI(Characters.c3320_0011)
    ReplanAI(Characters.c3320_0012)
    ReplanAI(Characters.c3320_0013)
    ReplanAI(Characters.c3320_0014)
    
    MAIN.Await(CharacterDead(Characters.c3320_0000))
    
    End()


@RestartOnRest(11300880)
def Event_11300880():
    """Event 11300880"""
    DisableHealthBar(Characters.c3320_0001)
    DisableHealthBar(Characters.c3320_0002)
    DisableHealthBar(Characters.c3320_0003)
    DisableHealthBar(Characters.c3320_0004)
    DisableHealthBar(Characters.c3320_0005)
    DisableHealthBar(Characters.c3320_0006)
    DisableHealthBar(Characters.c3320_0007)
    DisableHealthBar(Characters.c3320_0008)
    DisableHealthBar(Characters.c3320_0009)
    DisableHealthBar(Characters.c3320_0010)
    DisableHealthBar(Characters.c3320_0011)
    DisableHealthBar(Characters.c3320_0012)
    DisableHealthBar(Characters.c3320_0013)
    DisableHealthBar(Characters.c3320_0014)
    DisableCharacter(Characters.c3320_0001)
    DisableCharacter(Characters.c3320_0002)
    DisableCharacter(Characters.c3320_0003)
    DisableCharacter(Characters.c3320_0004)
    DisableCharacter(Characters.c3320_0005)
    DisableCharacter(Characters.c3320_0006)
    DisableCharacter(Characters.c3320_0007)
    DisableCharacter(Characters.c3320_0008)
    DisableCharacter(Characters.c3320_0009)
    DisableCharacter(Characters.c3320_0010)
    DisableCharacter(Characters.c3320_0011)
    DisableCharacter(Characters.c3320_0012)
    DisableCharacter(Characters.c3320_0013)
    DisableCharacter(Characters.c3320_0014)
    if FlagDisabled(CommonFlags.PinwheelDead):
        EnableImmortality(Characters.c3320_0001)
        EnableImmortality(Characters.c3320_0002)
        EnableImmortality(Characters.c3320_0003)
        EnableImmortality(Characters.c3320_0004)
        EnableImmortality(Characters.c3320_0005)
        EnableImmortality(Characters.c3320_0006)
        EnableImmortality(Characters.c3320_0007)
        EnableImmortality(Characters.c3320_0008)
        EnableImmortality(Characters.c3320_0009)
        EnableImmortality(Characters.c3320_0010)
        EnableImmortality(Characters.c3320_0011)
        EnableImmortality(Characters.c3320_0012)
        EnableImmortality(Characters.c3320_0013)
        EnableImmortality(Characters.c3320_0014)
    if FlagDisabled(CommonFlags.PinwheelDead):
        return
    Kill(Characters.c3320_0001)
    Kill(Characters.c3320_0002)
    Kill(Characters.c3320_0003)
    Kill(Characters.c3320_0004)
    Kill(Characters.c3320_0005)
    Kill(Characters.c3320_0006)
    Kill(Characters.c3320_0007)
    Kill(Characters.c3320_0008)
    Kill(Characters.c3320_0009)
    Kill(Characters.c3320_0010)
    Kill(Characters.c3320_0011)
    Kill(Characters.c3320_0012)
    Kill(Characters.c3320_0013)
    Kill(Characters.c3320_0014)


@ContinueOnRest(11300700)
def Event_11300700(_, obj: int, obj_flag: Flag | int):
    """Event 11300700"""
    MAIN.Await(EntityWithinDistance(entity=obj, other_entity=PLAYER, radius=1.5))
    
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=102,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(obj, 0, wait_for_completion=True)
    Restart()


@ContinueOnRest(11300300)
def Event_11300300():
    """Event 11300300"""
    MAIN.Await(FlagDisabled(11300402))
    
    CreateHazard(
        obj_flag=11300301,
        obj=Objects.o3000_0000,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300302,
        obj=Objects.o3000_0000,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300303,
        obj=Objects.o3000_0000,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300304,
        obj=Objects.o3000_0000,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300305,
        obj=Objects.o3000_0000,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300306,
        obj=Objects.o3000_0000,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300307,
        obj=Objects.o3000_0000,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300308,
        obj=Objects.o3000_0000,
        model_point=15,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    
    MAIN.Await(FlagEnabled(11300402))
    
    RemoveObjectFlag(obj_flag=11300301)
    RemoveObjectFlag(obj_flag=11300302)
    RemoveObjectFlag(obj_flag=11300303)
    RemoveObjectFlag(obj_flag=11300304)
    RemoveObjectFlag(obj_flag=11300305)
    RemoveObjectFlag(obj_flag=11300306)
    RemoveObjectFlag(obj_flag=11300307)
    RemoveObjectFlag(obj_flag=11300308)
    Restart()


@ContinueOnRest(11300350)
def Event_11300350():
    """Event 11300350"""
    MAIN.Await(FlagDisabled(11300403))
    
    CreateHazard(
        obj_flag=11300351,
        obj=Objects.o3001_0000,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300352,
        obj=Objects.o3001_0000,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300353,
        obj=Objects.o3001_0000,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300354,
        obj=Objects.o3001_0000,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300355,
        obj=Objects.o3001_0000,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300356,
        obj=Objects.o3001_0000,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300357,
        obj=Objects.o3001_0000,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300358,
        obj=Objects.o3001_0000,
        model_point=33,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300359,
        obj=Objects.o3001_0000,
        model_point=35,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300360,
        obj=Objects.o3001_0000,
        model_point=37,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300361,
        obj=Objects.o3001_0000,
        model_point=39,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    
    MAIN.Await(FlagEnabled(11300403))
    
    RemoveObjectFlag(obj_flag=11300351)
    RemoveObjectFlag(obj_flag=11300352)
    RemoveObjectFlag(obj_flag=11300353)
    RemoveObjectFlag(obj_flag=11300354)
    RemoveObjectFlag(obj_flag=11300355)
    RemoveObjectFlag(obj_flag=11300356)
    RemoveObjectFlag(obj_flag=11300357)
    RemoveObjectFlag(obj_flag=11300358)
    RemoveObjectFlag(obj_flag=11300359)
    RemoveObjectFlag(obj_flag=11300360)
    RemoveObjectFlag(obj_flag=11300361)
    Restart()


@ContinueOnRest(11300900)
def Event_11300900(_, obj_act_id: int, obj: Object | int, obj_1: int, navmesh_id: NavigationEvent | int):
    """Event 11300900"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj_1, animation_id=2)
        EndOfAnimation(obj=obj, animation_id=2)
        DisableObjectActivation(obj, obj_act_id=-1)
        End()
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    ForceAnimation(obj_1, 1)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)


@ContinueOnRest(11305030)
def Event_11305030(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    obj: Object | int,
    obj_1: int,
    navmesh_id: NavigationEvent | int,
):
    """Event 11305030"""
    if FlagEnabled(flag):
        DisableObjectActivation(obj, obj_act_id=3011)
        EndOfAnimation(obj=obj_1, animation_id=0)
        EndOfAnimation(obj=obj, animation_id=2)
    else:
        DisableObjectActivation(obj, obj_act_id=3012)
        EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfFinishedConditionTrue(6, input_condition=AND_2)
    EnableFlag(flag)
    ForceAnimation(obj_1, 3)
    WaitFrames(frames=140)
    EnableObjectActivation(obj, obj_act_id=3012)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    Restart()
    DisableFlag(flag)
    ForceAnimation(obj_1, 1)
    WaitFrames(frames=140)
    EnableObjectActivation(obj, obj_act_id=3011)
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    Restart()


@ContinueOnRest(11305032)
def Event_11305032(_, obj_act_id: int, obj_act_id_1: int, flag: Flag | int, flag_1: Flag | int):
    """Event 11305032"""
    AND_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_2.Add(ObjectActivated(obj_act_id=obj_act_id_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    EnableFlag(flag)
    Restart()
    EnableFlag(flag_1)
    Restart()


@ContinueOnRest(11305000)
def Event_11305000():
    """Event 11305000"""
    DisableNetworkSync()
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=CATACOMBS))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302700))
    AND_1.Add(FlagDisabled(11310000))
    AND_1.Add(PlayerHasGood(109))
    
    MAIN.Await(AND_1)
    
    Wait(30.0)
    if Multiplayer():
        return RESTART
    AND_6.Add(CharacterInsideRegion(PLAYER, region=1302700))
    if not AND_6:
        return RESTART
    AND_7.Add(HealthRatio(PLAYER) <= 0.0)
    if AND_7:
        return RESTART
    EnableFlag(11310050)
    PlayCutscene(130020, cutscene_flags=0, player_id=10000, move_to_region=1312110, game_map=TOMB_OF_THE_GIANTS)
    PlayCutscene(130120, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableObjectActivation(m13_01_Objects.o3060_0000, obj_act_id=-1)
    SetStandbyAnimationSettings(PLAYER)
    Restart()


@RestartOnRest(11305001)
def Event_11305001():
    """Event 11305001"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302700))
    AND_1.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11305006)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=3060)
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=3061)
    RestartEvent(event_id=11305002)
    RestartEvent(event_id=11305009)
    Restart()


@RestartOnRest(11305002)
def Event_11305002():
    """Event 11305002"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11305006))
    
    DisableFlag(11305006)
    Wait(5.0)
    EnableFlag(11305008)
    Restart()


@ContinueOnRest(11305003)
def Event_11305003():
    """Event 11305003"""
    MAIN.Await(FlagEnabled(11305008))
    
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=3060)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=3061)
    DisableFlag(11305006)
    DisableFlag(11305008)
    RestartEvent(event_id=11305000)
    RestartEvent(event_id=11305001)
    RestartEvent(event_id=11305002)
    Restart()


@RestartOnRest(11305004)
def Event_11305004():
    """Event 11305004"""
    AND_1.Add(CharacterTargeting(targeting_character=1300300, targeted_character=PLAYER))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4130))
    
    MAIN.Await(AND_1)
    
    ClearTargetList(1300300)
    ReplanAI(1300300)
    Restart()


@ContinueOnRest(11305009)
def Event_11305009():
    """Event 11305009"""
    AND_1.Add(AllPlayersOutsideRegion(region=1302700))
    AND_1.Add(EntityWithinDistance(entity=Objects.o3060_0000, other_entity=PLAYER, radius=10.0))
    AND_1.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(AND_1)
    
    EnableObjectActivation(Objects.o3060_0000, obj_act_id=3060)
    DisableObjectActivation(Objects.o3060_0000, obj_act_id=3061)
    Restart()


@ContinueOnRest(11300420)
def Event_11300420(_, character: int):
    """Event 11300420"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=Objects.o3060_0000, other_entity=character, radius=10.0))
    AND_1.Add(CharacterInsideRegion(character, region=1302700))
    
    MAIN.Await(AND_1)
    
    SetStandbyAnimationSettings(character, standby_animation=7151, death_animation=6082)
    AND_2.Add(EntityWithinDistance(entity=Objects.o3060_0000, other_entity=character, radius=10.0))
    AND_2.Add(CharacterOutsideRegion(character, region=1302700))
    
    MAIN.Await(AND_2)
    
    SetStandbyAnimationSettings(character)
    Restart()


@ContinueOnRest(11300100)
def Event_11300100(_, flag: Flag | int, region: Region | int, obj: int, sound_id: int):
    """Event 11300100"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=130000, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, sound_id, sound_type=SoundType.o_Object)


@ContinueOnRest(11300150)
def Event_11300150():
    """Event 11300150"""
    if ThisEventFlagEnabled():
        PostDestruction(Objects.o3036_0000)
        End()
    DisableAI(Characters.c2910_0001)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1302020))
    
    EnableAI(Characters.c2910_0001)
    DestroyObject(Objects.o3036_0000)
    PlaySoundEffect(Objects.o3036_0000, 303600000, sound_type=SoundType.a_Ambient)


@ContinueOnRest(11300160)
def Event_11300160():
    """Event 11300160"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o3661_0000)
        End()
    
    MAIN.Await(ObjectDestroyed(Objects.o3661_0000))
    
    EnableFlag(11300160)


@ContinueOnRest(11300200)
def Event_11300200():
    """Event 11300200"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o3350_0000, animation_id=0)
        End()
    
    MAIN.Await(FlagEnabled(CommonFlags.PinwheelDead))
    
    ForceAnimation(Objects.o3350_0000, 0)


@ContinueOnRest(11300210)
def Event_11300210():
    """Event 11300210"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o3871_0000)
        DisableObject(Objects.o3872_0000)
        End()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302030))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfMultiplayer(3)
    PlayCutscene(130010, cutscene_flags=0, player_id=10000, move_to_region=1302030, game_map=CATACOMBS)
    WaitFrames(frames=1)
    SkipLines(5)
    if FlagEnabled(11305060):
        PlayCutscene(
            130010,
            cutscene_flags=CutsceneFlags.Unskippable,
            player_id=10000,
            move_to_region=1302030,
            game_map=CATACOMBS,
        )
    else:
        PlayCutscene(130010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(Objects.o3871_0000)
    DisableObject(Objects.o3872_0000)


@ContinueOnRest(11305060)
def Event_11305060():
    """Event 11305060"""
    if FlagEnabled(11300210):
        return
    DisableNetworkSync()
    DisableFlag(11305060)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1302030))
    
    EnableFlag(11305060)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1302030))
    
    Restart()


@RestartOnRest(11300800)
def Event_11300800():
    """Event 11300800"""
    EnableFlag(11305200)
    EnableFlag(11305040)
    Event_11305050(1, flag=11305040, character=Characters.c2650_0000, region=1302202, radius=10.0)
    Event_11305050(2, flag=11305051, character=Characters.c2650_0000, region=1302203, radius=10.0)
    Event_11305050(3, flag=11305052, character=Characters.c2650_0000, region=1302204, radius=10.0)
    Event_11305050(4, flag=11305053, character=Characters.c2650_0000, region=1302205, radius=10.0)
    Event_11300801(0, character=Characters.c2650_0000)
    Event_11300801(1, character=Characters.c2650_0001)
    Event_11300801(2, character=Characters.c2650_0002)
    Event_11300801(3, character=Characters.c2650_0003)
    Event_11300801(4, character=Characters.c2650_0004)
    Event_11300801(5, character=Characters.c2650_0005)
    Event_11305100(0, character=Characters.c2650_0000, character_1=Characters.c2900_0002)
    Event_11305100(1, character=Characters.c2650_0000, character_1=Characters.c2900_0003)
    Event_11305100(2, character=Characters.c2650_0000, character_1=Characters.c2900_0004)
    Event_11305100(3, character=Characters.c2650_0000, character_1=Characters.c2900_0005)
    Event_11305100(4, character=Characters.c2650_0000, character_1=Characters.c2900_0006)
    Event_11305100(5, character=Characters.c2650_0000, character_1=Characters.c2900_0007)
    Event_11305100(6, character=Characters.c2650_0000, character_1=Characters.c2900_0008)
    Event_11305100(7, character=Characters.c2650_0000, character_1=Characters.c2900_0009)
    Event_11305100(8, character=Characters.c2650_0000, character_1=Characters.c2900_0010)
    Event_11305100(9, character=Characters.c2650_0000, character_1=Characters.c2900_0011)
    Event_11305100(10, character=Characters.c2650_0000, character_1=Characters.c2900_0012)
    Event_11305100(11, character=Characters.c2650_0000, character_1=Characters.c2900_0013)
    Event_11305100(12, character=Characters.c2650_0000, character_1=Characters.c2900_0014)
    Event_11305100(13, character=Characters.c2650_0000, character_1=Characters.c2900_0015)
    Event_11305100(14, character=Characters.c2650_0001, character_1=Characters.c2900_0022)
    Event_11305100(15, character=Characters.c2650_0001, character_1=Characters.c2900_0023)
    Event_11305100(16, character=Characters.c2650_0001, character_1=Characters.c2900_0024)
    Event_11305100(17, character=Characters.c2650_0001, character_1=Characters.c2900_0025)
    Event_11305100(18, character=Characters.c2650_0001, character_1=Characters.c2900_0026)
    Event_11305100(19, character=Characters.c2650_0001, character_1=Characters.c2900_0021)
    Event_11305100(20, character=Characters.c2650_0001, character_1=Characters.c2900_0044)
    Event_11305100(21, character=Characters.c2650_0001, character_1=Characters.c2900_0020)
    Event_11305100(22, character=Characters.c2650_0002, character_1=Characters.c2900_0027)
    Event_11305100(23, character=Characters.c2650_0002, character_1=Characters.c2900_0028)
    Event_11305100(24, character=Characters.c2650_0002, character_1=Characters.c2900_0029)
    Event_11305100(25, character=Characters.c2650_0002, character_1=Characters.c2900_0030)
    Event_11305100(26, character=Characters.c2650_0002, character_1=Characters.c2900_0031)
    Event_11305100(27, character=Characters.c2650_0002, character_1=Characters.c2900_0032)
    Event_11305100(28, character=Characters.c2650_0002, character_1=Characters.c2900_0033)
    Event_11305100(29, character=Characters.c2650_0003, character_1=Characters.c2900_0016)
    Event_11305100(30, character=Characters.c2650_0003, character_1=Characters.c2900_0017)
    Event_11305100(31, character=Characters.c2650_0003, character_1=Characters.c2900_0018)
    Event_11305100(32, character=Characters.c2650_0003, character_1=Characters.c2900_0019)
    Event_11305100(33, character=Characters.c2650_0003, character_1=Characters.c2900_0052)
    Event_11305100(34, character=Characters.c2650_0003, character_1=Characters.c2900_0053)
    Event_11305100(35, character=Characters.c2650_0004, character_1=Characters.c2900_0048)
    Event_11305100(36, character=Characters.c2650_0004, character_1=Characters.c2900_0049)
    Event_11305100(37, character=Characters.c2650_0004, character_1=Characters.c2900_0047)
    Event_11305100(38, character=Characters.c2650_0004, character_1=Characters.c2900_0045)
    Event_11305100(39, character=Characters.c2650_0004, character_1=Characters.c2900_0046)
    Event_11305100(40, character=Characters.c2650_0004, character_1=Characters.c2900_0000)
    Event_11305100(41, character=Characters.c2650_0004, character_1=Characters.c2900_0001)
    Event_11305100(44, character=Characters.c2650_0005, character_1=Characters.c2900_0035)
    Event_11305100(45, character=Characters.c2650_0005, character_1=Characters.c2900_0036)
    Event_11305100(46, character=Characters.c2650_0005, character_1=Characters.c2900_0037)
    Event_11305100(47, character=Characters.c2650_0005, character_1=Characters.c2900_0038)
    Event_11305100(48, character=Characters.c2650_0005, character_1=Characters.c2900_0039)
    Event_11305100(49, character=Characters.c2650_0005, character_1=Characters.c2900_0042)
    Event_11305100(50, character=Characters.c2650_0005, character_1=Characters.c2900_0043)
    Event_11305070(0, character=Characters.c2900_0008, radius=5.0)
    Event_11305070(1, character=Characters.c2900_0010, radius=5.0)
    Event_11305070(2, character=Characters.c2900_0011, radius=5.0)
    Event_11305070(3, character=Characters.c2900_0014, radius=5.0)
    Event_11305070(4, character=Characters.c2900_0022, radius=5.0)
    Event_11305070(5, character=Characters.c2900_0023, radius=5.0)
    Event_11305070(6, character=Characters.c2900_0024, radius=5.0)
    Event_11305070(7, character=Characters.c2900_0025, radius=5.0)
    Event_11305070(8, character=Characters.c2900_0026, radius=5.0)
    Event_11305070(9, character=Characters.c2900_0033, radius=5.0)
    Event_11305070(10, character=Characters.c2900_0048, radius=5.0)
    Event_11305070(11, character=Characters.c2900_0049, radius=5.0)
    Event_11305070(12, character=Characters.c2900_0000, radius=5.0)
    Event_11305070(13, character=Characters.c2900_0001, radius=5.0)
    Event_11305070(16, character=Characters.c2900_0018, radius=5.0)
    Event_11305070(17, character=Characters.c2900_0019, radius=5.0)
    Event_11305070(18, character=Characters.c2900_0020, radius=5.0)
    Event_11305210(0, character=Characters.c3501_0006)
    Event_11305210(1, character=Characters.c3501_0007)
    Event_11305210(2, character=Characters.c3501_0008)
    Event_11305210(3, character=Characters.c3501_0009)
    Event_11305210(4, character=Characters.c3501_0010)
    Event_11305210(5, character=Characters.c3501_0011)
    Event_11305210(6, character=Characters.c3501_0012)
    Event_11305210(7, character=Characters.c3501_0013)
    Event_11305210(8, character=Characters.c3501_0014)
    Event_11305210(9, character=Characters.c3501_0015)
    Event_11305210(10, character=Characters.c3501_0016)
    Event_11305210(13, character=Characters.c3501_0019)


@EndOnRest(11305050)
def Event_11305050(_, flag: Flag | int, character: int, region: Region | int, radius: float):
    """Event 11305050"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(11300801)
def Event_11300801(_, character: Character | int):
    """Event 11300801"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@EndOnRest(11305070)
def Event_11305070(_, character: int, radius: float):
    """Event 11305070"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    SetStandbyAnimationSettings(character, cancel_animation=9061)


@EndOnRest(11305100)
def Event_11305100(_, character: Character | int, character_1: Character | int):
    """Event 11305100"""
    if ThisEventSlotFlagEnabled():
        RemoveSpecialEffect(character_1, 5451)
        End()
    EnableImmortality(character_1)
    
    MAIN.Await(CharacterDead(character))
    
    RemoveSpecialEffect(character_1, 5451)
    DisableImmortality(character_1)


@EndOnRest(11305210)
def Event_11305210(_, character: Character | int):
    """Event 11305210"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=400))
    DisableCharacter(character)


@RestartOnRest(11305045)
def Event_11305045():
    """Event 11305045"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1300300)
    SetStandbyAnimationSettings(1300300, standby_animation=9000)
    OR_1.Add(EntityWithinDistance(entity=1300300, other_entity=PLAYER, radius=5.0))
    OR_1.Add(Attacked(attacked_entity=1300300, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(1300300)
    EnableAI(1300300)


@RestartOnRest(11300850)
def Event_11300850(_, character: Character | int, item_lot: int):
    """Event 11300850"""
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


@ContinueOnRest(11300510)
def Event_11300510(_, character: Character | int, flag: Flag | int):
    """Event 11300510"""
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


@ContinueOnRest(11300520)
def Event_11300520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11300520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11300530)
def Event_11300530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11300530"""
    AND_1.Add(FlagDisabled(1622))
    AND_1.Add(FlagDisabled(1625))
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(FlagEnabled(11300593))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11300531)
def Event_11300531(_, character: Character | int, flag: Flag | int):
    """Event 11300531"""
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(1621))
    AND_2.Add(HealthRatio(character) <= 0.0)
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(1627)
    EnableFlag(flag)
    EndIfFinishedConditionFalse(input_condition=AND_3)
    DropMandatoryTreasure(character)


@ContinueOnRest(11300533)
def Event_11300533(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11300533"""
    AND_1.Add(FlagDisabled(1627))
    AND_1.Add(FlagDisabled(1628))
    OR_7.Add(FlagEnabled(1620))
    OR_7.Add(FlagEnabled(1621))
    AND_1.Add(OR_7)
    AND_2.Add(AND_1)
    AND_2.Add(FlagEnabled(CommonFlags.PinwheelDead))
    AND_3.Add(AND_1)
    AND_3.Add(FlagEnabled(1173))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11305025)
def Event_11305025():
    """Event 11305025"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0004, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11305028)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11305026))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0004)
    if FlagEnabled(CommonFlags.PinwheelDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0004))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0004,
        region=1302050,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    
    MAIN.Await(FlagEnabled(11305026))
    
    SetNest(Characters.c0000_0004, region=1302051)


@ContinueOnRest(11305990)
def Event_11305990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 11305990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11305029)
def Event_11305029():
    """Event 11305029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0004, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11305028)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11305026))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0004)
    if FlagEnabled(CommonFlags.PinwheelDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11305026))
    AND_1.Add(FlagDisabled(11305028))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0004))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0004,
        region=1302050,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    
    MAIN.Await(FlagEnabled(11305026))
    
    SetNest(Characters.c0000_0004, region=1302051)


@ContinueOnRest(11305027)
def Event_11305027():
    """Event 11305027"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11305026))
    AND_1.Add(FlagEnabled(11305393))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0004, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0004)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0004, region=1302998))
    
    RotateToFaceEntity(Characters.c0000_0004, target_entity=1302997)
    ForceAnimation(Characters.c0000_0004, 7410)
    AICommand(Characters.c0000_0004, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0004)


@RestartOnRest(11305061)
def Event_11305061(_, character: Character | int):
    """Event 11305061"""
    if ThisEventFlagEnabled():
        return
    DisableCharacterCollision(character)
    DisableGravity(character)
    WaitFrames(frames=10)
    EnableCharacterCollision(character)
    EnableGravity(character)


@ContinueOnRest(11300592)
def Event_11300592():
    """Event 11300592"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(FlagDisabled(11300403))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11300592)
    ActivateObject(Objects.o3011_0002, obj_act_id=3011, relative_index=-1)


@ContinueOnRest(11300593)
def Event_11300593():
    """Event 11300593"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(1620))
    AND_1.Add(FlagEnabled(11300592))
    AND_1.Add(FlagEnabled(11300403))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1302001))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11300593)
    ActivateObject(Objects.o3011_0002, obj_act_id=3012, relative_index=-1)


@ContinueOnRest(11305843)
def Event_11305843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11305843"""
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


@ContinueOnRest(11305846)
def Event_11305846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11305846"""
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
