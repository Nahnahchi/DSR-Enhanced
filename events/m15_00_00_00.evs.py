"""
Sen's Fortress

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m15_00_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11500992()
    CreateProjectileOwner(entity=Characters.c2690_0000)
    SetNetworkUpdateRate(Characters.c2860_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RegisterBonfire(bonfire_flag=11500984, obj=Objects.o0200_0002)
    RegisterLadder(start_climbing_flag=11500010, stop_climbing_flag=11500011, obj=Objects.o5400_0000)
    RegisterLadder(start_climbing_flag=11500012, stop_climbing_flag=11500013, obj=Objects.o5401_0000)
    RegisterLadder(start_climbing_flag=11500014, stop_climbing_flag=11500015, obj=Objects.o5404_0000)
    RegisterLadder(start_climbing_flag=11500016, stop_climbing_flag=11500017, obj=Objects.o5403_0000)
    SkipLinesIfHost(2)
    EnableFlag(11505240)
    DisableFlag(11505360)
    SkipLinesIfClient(2)
    DisableObject(Objects.o5151_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableMapCollision(collision=Collisions.h0110B0_0000)
    DisableObject(Objects.o5010_0000)
    DisableObject(Objects.o5010_0001)
    DisableObject(Objects.o5010_0002)
    DisableObject(Objects.o5010_0003)
    DisableObject(Objects.o5010_0004)
    DisableObject(Objects.o5010_0005)
    DisableObject(Objects.o5010_0006)
    DisableObject(Objects.o5010_0007)
    if FlagDisabled(11500803):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=3)
    if FlagEnabled(11500806):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=0)
    if FlagEnabled(11500809):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=1)
    if FlagEnabled(11500812):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=2)
    DisableMapCollision(collision=Collisions.h0081B0_0000)
    DisableMapCollision(collision=Collisions.h0081B0_0001)
    DisableMapCollision(collision=Collisions.h0081B0_0002)
    if FlagEnabled(11500821):
        EnableObject(Objects.o5010_0001)
        EndOfAnimation(obj=Objects.o5010_0001, animation_id=5)
        EnableMapCollision(collision=Collisions.h0081B0_0000)
    if FlagEnabled(11500822):
        EnableObject(Objects.o5010_0002)
        EndOfAnimation(obj=Objects.o5010_0002, animation_id=6)
        EnableMapCollision(collision=Collisions.h0081B0_0001)
    if FlagEnabled(11500823):
        EnableObject(Objects.o5010_0003)
        EndOfAnimation(obj=Objects.o5010_0003, animation_id=7)
        EnableMapCollision(collision=Collisions.h0081B0_0002)
    SkipLinesIfFlagDisabled(21, 11500100)
    SkipLinesIfFlagEnabled(10, 11500101)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EndOfAnimation(obj=Objects.o5301_0000, animation_id=12)
    SkipLines(9)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.Wall)
    EndOfAnimation(obj=Objects.o5301_0000, animation_id=11)
    SkipLines(4)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Solid)
    Event_11500090(0, obj=Objects.o5152_0000, vfx_id=VFX.CheckpointFog1, destination=1502600, destination_1=1502601)
    Event_11500090(1, obj=Objects.o5153_0000, vfx_id=VFX.CheckpointFog2, destination=1502602, destination_1=1502603)
    Event_11505090()
    Event_11505091()
    Event_11505092()
    Event_11500201()
    Event_11505300()
    Event_11500840()
    Event_11500841(0, flag=11500803)
    Event_11500841(1, flag=11500806)
    Event_11500841(2, flag=11500809)
    Event_11500841(3, flag=11500812)
    Event_11500790()
    Event_11500791()
    Event_11500795()
    Event_11500796()
    Event_11500797()
    Event_11500798()
    Event_11500830()
    Event_11500831()
    Event_11500850()
    Event_11505255()
    Event_11500100()
    Event_11500102()
    Event_11500103()
    Event_11500106()
    Event_11500107()
    Event_11500110(0, obj=Objects.o5310_0002, obj_act_id=11500110)
    Event_11500110(1, obj=Objects.o5310_0003, obj_act_id=11500111)
    Event_11500110(2, obj=Objects.o5310_0004, obj_act_id=11500112)
    Event_11500110(3, obj=Objects.o5310_0006, obj_act_id=11500113)
    Event_11500110(5, obj=Objects.o5310_0012, obj_act_id=11500115)
    Event_11500110(6, obj=Objects.o5310_0017, obj_act_id=11500116)
    Event_11505050()
    Event_11505051()
    Event_11505055()
    Event_11505110()
    Event_11505101()
    Event_11505102()
    Event_11505111(0, left=11505111, region=1502700, command_id=1)
    Event_11505111(1, left=11505112, region=1502701, command_id=2)
    Event_11505111(2, left=11505113, region=1502702, command_id=3)
    Event_11505111(3, left=11505114, region=1502703, command_id=4)
    Event_11505111(4, left=11505115, region=1502704, command_id=5)
    Event_11505111(5, left=11505116, region=1502705, command_id=6)
    Event_11505111(6, left=11505117, region=1502710, command_id=-1)
    Event_11505060(0, character=Characters.c2860_0001)
    Event_11505060(1, character=Characters.c2860_0000)
    Event_11505060(2, character=Characters.c2860_0003)
    Event_11505070(0, character=Characters.c2860_0001)
    Event_11505070(1, character=Characters.c2860_0000)
    Event_11505070(2, character=Characters.c2860_0003)
    Event_11505080()
    Event_11500210()
    Event_11500835()
    DisableSoundEvent(sound_id=Sounds.IronGolemMusic)
    if FlagEnabled(CommonFlags.IronGolemDead):
        Event_11505392()
        DisableObject(Objects.o5150_0000)
        DeleteVFX(VFX.IronGolemEntranceFog, erase_root_only=False)
    else:
        Event_11505390()
        Event_11505391()
        Event_11505393()
        Event_11505392()
        Event_11500001()
        Event_11505394()
        Event_11505395()
        Event_11505350()
        Event_11505353()
    Event_11505010()
    Event_11505011()
    Event_11505012()
    Event_11505013()
    Event_11505014()
    Event_11500900()
    Event_11505015()
    Event_11505270(
        0,
        region=1502200,
        obj=Objects.o5500_0000,
        vfx_id=VFX.ArrowTriggerA,
        source_entity=Objects.o5510_0000,
        launch_angle_y=0,
        left=11505280,
    )
    Event_11505270(
        1,
        region=1502201,
        obj=Objects.o5501_0001,
        vfx_id=VFX.ArrowTriggerA,
        source_entity=Objects.o5510_0001,
        launch_angle_y=90,
        left=11505281,
    )
    Event_11505270(
        2,
        region=1502202,
        obj=Objects.o5501_0002,
        vfx_id=VFX.ArrowTriggerA,
        source_entity=Objects.o5510_0002,
        launch_angle_y=90,
        left=11505282,
    )
    Event_11505270(
        3,
        region=1502203,
        obj=Objects.o5501_0003,
        vfx_id=VFX.ArrowTriggerA,
        source_entity=Objects.o5510_0003,
        launch_angle_y=270,
        left=11505283,
    )
    Event_11505270(
        4,
        region=1502204,
        obj=Objects.o5501_0004,
        vfx_id=VFX.ArrowTriggerA,
        source_entity=Objects.o5510_0004,
        launch_angle_y=180,
        left=11505284,
    )
    Event_11505270(
        5,
        region=1502205,
        obj=Objects.o5501_0005,
        vfx_id=VFX.ArrowTriggerA,
        source_entity=Objects.o5510_0003,
        launch_angle_y=270,
        left=11505285,
    )
    Event_11505260()
    Event_11500860(0, character=Characters.c0000_0009)
    Event_11500860(1, character=Characters.c2300_0000)
    Event_11500860(2, character=Characters.c2300_0001)
    Event_11500860(3, character=Characters.c2300_0002)
    Event_11500860(4, character=Characters.c2300_0003)
    Event_11500860(5, character=Characters.c2860_0001)
    Event_11500860(7, character=Characters.c2860_0003)
    Event_11500600(0, obj=Objects.o0110_0000, obj_act_id=11500600)
    Event_11500600(2, obj=Objects.o0110_0002, obj_act_id=11500602)
    Event_11500600(4, obj=Objects.o0110_0004, obj_act_id=11500604)
    Event_11500600(9, obj=Objects.o0110_0009, obj_act_id=11500609)
    Event_11500600(10, obj=Objects.o0110_0010, obj_act_id=11500610)
    Event_11505843(
        0,
        flag=CommonFlags.IronGolemDead,
        line_intersects=1501990,
        anchor_entity=1502998,
        target_entity=1502997,
    )
    Event_11505846(0, flag=CommonFlags.IronGolemDead, obj=Objects.o5150_0000, vfx_id=VFX.IronGolemEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0009, event_flag=8980)
    HumanityRegistration(Characters.c0000_0007, event_flag=8924)
    Event_11505030()
    Event_11505029()
    Event_11505032()
    Event_11505990(0, flag=11505031, summoned_character=Characters.c0000_0007)
    HumanityRegistration(Characters.c0000_0004, event_flag=8334)
    SkipLinesIfFlagEnabled(3, 1090)
    SkipLinesIfFlagEnabled(2, 1091)
    SkipLinesIfFlagEnabled(1, 1096)
    DisableCharacter(Characters.c0000_0004)
    Event_11500510(0, character=Characters.c0000_0004, flag=1096)
    Event_11500520(0, character=Characters.c0000_0004, first_flag=1090, last_flag=1109, flag=1097)
    Event_11500530()
    Event_11500531(0, character=Characters.c0000_0004, first_flag=1090, last_flag=1109, flag=1091)
    Event_11500532(0, character=Characters.c0000_0004, first_flag=1090, last_flag=1109, flag=1092)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_0008, team_type=TeamType.HostileAlly)
    if FlagDisabled(1117):
        DisableCharacter(Characters.c0000_0008)
    Event_11500520(1, character=Characters.c0000_0008, first_flag=1110, last_flag=1119, flag=1115)
    Event_11500533(0, character=Characters.c0000_0008, first_flag=1110, last_flag=1119, flag=1117)
    HumanityRegistration(Characters.c0000_0006, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1514)
    SkipLinesIfFlagEnabled(2, 1513)
    SkipLinesIfFlagRangeAnyEnabled(1, (1493, 1511))
    SkipLines(1)
    DisableCharacter(Characters.c0000_0006)
    SkipLinesIfFlagEnabled(1, 11500200)
    SkipLines(1)
    Move(
        Characters.c0000_0006,
        destination=1502510,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0060B0_0000,
    )
    SkipLinesIfFlagRangeAnyEnabled(1, (1491, 1492))
    SkipLines(2)
    Kill(Characters.c2690_0006)
    Kill(Characters.c2690_0007)
    Event_11500510(2, character=Characters.c0000_0006, flag=1512)
    Event_11500520(2, character=Characters.c0000_0006, first_flag=1490, last_flag=1539, flag=1513)
    Event_11500534(0, character=Characters.c0000_0006, first_flag=1490, last_flag=1539, flag=1491)
    Event_11500535(0, character=Characters.c0000_0006, first_flag=1490, last_flag=1539, flag=1492)
    Event_11500536(0, character=Characters.c0000_0006, first_flag=1490, last_flag=1539, flag=1493)
    HumanityRegistration(Characters.c0000_0005, event_flag=8422)
    SkipLinesIfFlagRangeAnyEnabled(1, (1420, 1429))
    EnableFlag(1420)
    Event_11500510(3, character=Characters.c0000_0005, flag=1421)
    Event_11500520(3, character=Characters.c0000_0005, first_flag=1420, last_flag=1429, flag=1422)


@ContinueOnRest(11500992)
def Event_11500992():
    """Event 11500992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c2320_0000, 7100)
    AddSpecialEffect(Characters.c2860_0001, 7100)
    AddSpecialEffect(Characters.c2860_0000, 7100)
    AddSpecialEffect(Characters.c2860_0003, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c2320_0000, 7100)
    RemoveSpecialEffect(Characters.c2860_0001, 7100)
    RemoveSpecialEffect(Characters.c2860_0000, 7100)
    RemoveSpecialEffect(Characters.c2860_0003, 7100)
    Restart()


@ContinueOnRest(1000000000)
def Event_1000000000():
    """Event 1000000000"""
    DisableCharacter(Characters.c2690_0000)
    SetNetworkUpdateRate(Characters.c2860_0001, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(11500090)
def Event_11500090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11500090"""
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


@RestartOnRest(11505090)
def Event_11505090():
    """Event 11505090"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2690_0012)
        DisableCharacter(Characters.c2690_0013)
        DisableCharacter(Characters.c2690_0014)
        DisableCharacter(Characters.c2690_0015)
        DisableCharacter(Characters.c2690_0016)
        DisableCharacter(Characters.c2690_0017)
        DisableCharacter(Characters.c2690_0018)
        DisableCharacter(Characters.c2700_0008)
        DisableCharacter(Characters.c2700_0009)
        DisableCharacter(1500909)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11505091)
def Event_11505091():
    """Event 11505091"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2690_0012)
    Kill(Characters.c2690_0013)
    Kill(Characters.c2690_0014)
    Kill(Characters.c2690_0015)
    Kill(Characters.c2690_0016)
    Kill(Characters.c2690_0017)
    Kill(Characters.c2690_0018)
    Kill(Characters.c2700_0008)
    Kill(Characters.c2700_0009)
    Kill(1500909)


@RestartOnRest(11505092)
def Event_11505092():
    """Event 11505092"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11500050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11500050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11500050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11500050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11500050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=SENS_FORTRESS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11500050))
    if not OR_6:
        return RESTART
    EnableFlag(11500050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=SENS_FORTRESS))
    if not AND_7:
        return RESTART
    DisableFlag(11500050)
    EnableFlag(11505095)


@ContinueOnRest(11505300)
def Event_11505300():
    """Event 11505300"""
    CreateHazard(
        obj_flag=11505301,
        obj=Objects.o5000_0000,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505302,
        obj=Objects.o5000_0001,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505303,
        obj=Objects.o5000_0002,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505304,
        obj=Objects.o5000_0003,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505305,
        obj=Objects.o5000_0004,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505306,
        obj=Objects.o5000_0010,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505307,
        obj=Objects.o5000_0011,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505308,
        obj=Objects.o5000_0012,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505309,
        obj=Objects.o5000_0013,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505310,
        obj=Objects.o5000_0020,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505311,
        obj=Objects.o5000_0021,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505312,
        obj=Objects.o5000_0022,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505313,
        obj=Objects.o5000_0023,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505314,
        obj=Objects.o5000_0030,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505315,
        obj=Objects.o5000_0031,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505316,
        obj=Objects.o5000_0032,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505317,
        obj=Objects.o5000_0033,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        obj_flag=11505290,
        obj=Objects.o5300_0000,
        model_point=101,
        behavior_param_id=5060,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=0.5,
    )


@ContinueOnRest(11505390)
def Event_11505390():
    """Event 11505390"""
    AND_1.Add(FlagDisabled(CommonFlags.IronGolemDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1501990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11505391)
def Event_11505391():
    """Event 11505391"""
    AND_1.Add(FlagDisabled(CommonFlags.IronGolemDead))
    AND_1.Add(FlagEnabled(11505393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1501990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11505393)
def Event_11505393():
    """Event 11505393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.IronGolemDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1502996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2320_0000)


@RestartOnRest(11505392)
def Event_11505392():
    """Event 11505392"""
    if FlagEnabled(CommonFlags.IronGolemDead):
        DisableCharacter(Characters.c2320_0000)
        DropMandatoryTreasure(Characters.c2320_0000)
        DisableBackread(Characters.c2320_0000)
    
        MAIN.Await(CharacterBackreadEnabled(Characters.c2860_0001))
    
        AICommand(Characters.c2860_0001, command_id=10, command_slot=0)
        ReplanAI(Characters.c2860_0001)
        End()
    DisableAI(Characters.c2320_0000)
    SetStandbyAnimationSettings(Characters.c2320_0000, standby_animation=9000)
    Event_11505351()
    Event_11505352()
    AND_1.Add(FlagEnabled(11505393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502996))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.c2320_0000)
    SetStandbyAnimationSettings(Characters.c2320_0000, cancel_animation=9060)
    EnableBossHealthBar(Characters.c2320_0000, name=2320)


@ContinueOnRest(11500001)
def Event_11500001():
    """Event 11500001"""
    DeleteVFX(VFX.AnorLondoWarpRing, erase_root_only=False)
    
    MAIN.Await(CharacterDead(Characters.c2320_0000))
    
    EnableFlag(CommonFlags.IronGolemDead)
    KillBoss(game_area_param_id=1500800)
    DisableObject(Objects.o5150_0000)
    DeleteVFX(VFX.IronGolemEntranceFog)
    CreateVFX(VFX.AnorLondoWarpRing)
    AICommand(Characters.c2860_0001, command_id=10, command_slot=0)
    ReplanAI(Characters.c2860_0001)
    DisableFlag(11807020)
    DisableFlag(11807030)
    DisableFlag(11807040)
    DisableFlag(11807050)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(Characters.c2320_0000)
    DisableBackread(Characters.c2320_0000)


@ContinueOnRest(11505394)
def Event_11505394():
    """Event 11505394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.IronGolemDead))
    AND_1.Add(FlagEnabled(11505392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11505391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502996))
    AND_1.Add(CharacterAlive(Characters.c2320_0000))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.IronGolemMusic)


@ContinueOnRest(11505395)
def Event_11505395():
    """Event 11505395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.IronGolemDead))
    AND_1.Add(FlagEnabled(11505394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.IronGolemMusic)
    PlaySoundEffect(1502990, 150100002, sound_type=SoundType.a_Ambient)


@ContinueOnRest(11505350)
def Event_11505350():
    """Event 11505350"""
    if Client():
        return
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c2320_0000, tae_event_id=100))
    
    MAIN.Await(CharacterDead(Characters.c2320_0000))


@EndOnRest(11505351)
def Event_11505351():
    """Event 11505351"""
    if FlagEnabled(CommonFlags.IronGolemDead):
        return
    EnableNetworkSync()
    
    MAIN.Await(FlagDisabled(11505355))
    
    CreateNPCPart(Characters.c2320_0000, npc_part_id=2320, part_index=NPCPartType.Part2, part_health=200)
    SetNPCPartEffects(Characters.c2320_0000, npc_part_id=2320, material_sfx_id=56, material_vfx_id=56)
    
    MAIN.Await(CharacterPartHealth(Characters.c2320_0000, npc_part_id=2320) <= 0)
    
    EzstateAIRequest(Characters.c2320_0000, command_id=1300, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c2320_0000, tae_event_id=1204))
    
    EnableFlag(11505355)
    CreateNPCPart(Characters.c2320_0000, npc_part_id=2321, part_index=NPCPartType.Part2, part_health=100)
    SetNPCPartEffects(Characters.c2320_0000, npc_part_id=2321, material_sfx_id=56, material_vfx_id=56)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    DisableFlag(11505355)
    RestartEvent(event_id=11505352)
    SetNPCPartHealth(Characters.c2320_0000, npc_part_id=2321, desired_health=-1, overwrite_max=False)
    EzstateAIRequest(Characters.c2320_0000, command_id=1303, command_slot=0)
    Restart()


@EndOnRest(11505352)
def Event_11505352():
    """Event 11505352"""
    if FlagEnabled(CommonFlags.IronGolemDead):
        return
    EnableNetworkSync()
    
    MAIN.Await(FlagEnabled(11505355))
    
    AND_1.Add(FlagEnabled(11505355))
    AND_1.Add(CharacterPartHealth(Characters.c2320_0000, npc_part_id=2321) <= 0)
    
    MAIN.Await(AND_1)
    
    RestartEvent(event_id=11505351)
    EzstateAIRequest(Characters.c2320_0000, command_id=1301, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c2320_0000, tae_event_id=1203))
    
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    EzstateAIRequest(Characters.c2320_0000, command_id=1304, command_slot=0)
    DisableFlag(11505355)
    Restart()


@ContinueOnRest(11505353)
def Event_11505353():
    """Event 11505353"""
    AND_1.Add(CharacterHasTAEEvent(Characters.c2320_0000, tae_event_id=400))
    AND_2.Add(CharacterHasTAEEvent(Characters.c2320_0000, tae_event_id=300))
    AND_3.Add(HealthRatio(Characters.c2320_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_1)
    DisableMapCollision(collision=Collisions.h1100B0_0000)
    SkipLines(1)
    EnableMapCollision(collision=Collisions.h1100B0_0000)
    EndIfFinishedConditionTrue(input_condition=AND_3)
    AND_4.Add(CharacterDoesNotHaveTAEEvent(Characters.c2320_0000, tae_event_id=400))
    AND_4.Add(CharacterDoesNotHaveTAEEvent(Characters.c2320_0000, tae_event_id=300))
    
    MAIN.Await(AND_4)
    
    Restart()


@ContinueOnRest(11500201)
def Event_11500201():
    """Event 11500201"""
    if FlagEnabled(11500200):
        EndOfAnimation(obj=Objects.o5100_0000, animation_id=0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502050))
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1502050))
    
    Restart()


@ContinueOnRest(11500790)
def Event_11500790():
    """Event 11500790"""
    MAIN.Await(FlagEnabled(11500791))
    
    AND_1.Add(FlagDisabled(11505050))
    AND_1.Add(CharacterAlive(Characters.c2860_0000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11505052)
    Wait(5.0)
    EnableObject(Objects.o5010_0000)
    ForceAnimation(Objects.o5010_0000, 0)
    Wait(1.5)
    EnableMapCollision(collision=Collisions.h0110B0_0000)
    Wait(3.5)
    WaitForNetworkApproval(max_seconds=10.0)
    if FlagDisabled(11505210):
        EnableFlag(11505220)
        Restart()
    if FlagDisabled(11505211):
        EnableFlag(11505221)
        Restart()
    if FlagDisabled(11505212):
        EnableFlag(11505222)
        Restart()
    if FlagDisabled(11505213):
        EnableFlag(11505223)
    Restart()


@RestartOnRest(11500791)
def Event_11500791():
    """Event 11500791"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c2690_0004)
        End()
    DisableAI(Characters.c2690_0004)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502110))
    
    EnableFlag(11500791)
    EnableObject(Objects.o5010_0000)
    ForceAnimation(Characters.c2690_0004, 500, wait_for_completion=True)
    ForceAnimation(Characters.c2690_0004, 603, wait_for_completion=True)
    EnableAI(Characters.c2690_0004)
    CreateHazard(
        obj_flag=11505200,
        obj=Objects.o5010_0000,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(Objects.o5010_0000, 12, wait_for_completion=True)
    DisableObject(Objects.o5010_0000)


@ContinueOnRest(11500795)
def Event_11500795():
    """Event 11500795"""
    MAIN.Await(FlagEnabled(11505220))
    
    DisableFlag(11505220)
    EnableFlag(11505210)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0004)
    if FlagEnabled(11500812):
        Event_11500700(
            0,
            obj_flag=11505200,
            obj=Objects.o5010_0004,
            animation_id=1,
            life=2.5,
            entity=Objects.o5210_0002,
            flag=11505210,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(
            10,
            obj_flag=11505200,
            obj=Objects.o5010_0004,
            animation_id=2,
            life=7.5,
            entity=Objects.o5210_0003,
            flag=11505210,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(
            20,
            obj_flag=11505200,
            obj=Objects.o5010_0004,
            animation_id=3,
            life=7.5,
            entity=Objects.o5210_0000,
            flag=11505210,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(
            30,
            obj_flag=11505200,
            obj=Objects.o5010_0004,
            animation_id=4,
            life=12.5,
            entity=Objects.o5210_0001,
            flag=11505210,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505200,
            obj=Objects.o5010_0001,
            animation_id=5,
            collision=Collisions.h0081B0_0000,
            entity=Objects.o5210_0001,
            flag=11505210,
            flag_1=11500821,
            obj_1=Objects.o5010_0004,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505200,
            obj=Objects.o5010_0002,
            animation_id=6,
            collision=Collisions.h0081B0_0001,
            entity=Objects.o5210_0001,
            flag=11505210,
            flag_1=11500822,
            obj_1=Objects.o5010_0004,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505200,
            obj=Objects.o5010_0003,
            animation_id=7,
            collision=Collisions.h0081B0_0002,
            entity=Objects.o5210_0001,
            flag=11505210,
            flag_1=11500823,
            obj_1=Objects.o5010_0004,
        )
    
        MAIN.Await(FlagDisabled(11505210))
    
        Restart()
    Event_11500700(
        40,
        obj_flag=11505200,
        obj=Objects.o5010_0004,
        animation_id=8,
        life=18.5,
        entity=Objects.o5210_0001,
        flag=11505210,
    )
    
    MAIN.Await(FlagDisabled(11505210))
    
    Restart()


@ContinueOnRest(11500796)
def Event_11500796():
    """Event 11500796"""
    MAIN.Await(FlagEnabled(11505221))
    
    DisableFlag(11505221)
    EnableFlag(11505211)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0005)
    if FlagEnabled(11500812):
        Event_11500700(
            1,
            obj_flag=11505201,
            obj=Objects.o5010_0005,
            animation_id=1,
            life=2.5,
            entity=Objects.o5210_0002,
            flag=11505211,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(
            11,
            obj_flag=11505201,
            obj=Objects.o5010_0005,
            animation_id=2,
            life=7.5,
            entity=Objects.o5210_0003,
            flag=11505211,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(
            21,
            obj_flag=11505201,
            obj=Objects.o5010_0005,
            animation_id=3,
            life=7.5,
            entity=Objects.o5210_0000,
            flag=11505211,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(
            31,
            obj_flag=11505201,
            obj=Objects.o5010_0005,
            animation_id=4,
            life=12.5,
            entity=Objects.o5210_0001,
            flag=11505211,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505201,
            obj=Objects.o5010_0001,
            animation_id=5,
            collision=Collisions.h0081B0_0000,
            entity=Objects.o5210_0001,
            flag=11505211,
            flag_1=11500821,
            obj_1=Objects.o5010_0005,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505201,
            obj=Objects.o5010_0002,
            animation_id=6,
            collision=Collisions.h0081B0_0001,
            entity=Objects.o5210_0001,
            flag=11505211,
            flag_1=11500822,
            obj_1=Objects.o5010_0005,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505201,
            obj=Objects.o5010_0003,
            animation_id=7,
            collision=Collisions.h0081B0_0002,
            entity=Objects.o5210_0001,
            flag=11505211,
            flag_1=11500823,
            obj_1=Objects.o5010_0005,
        )
    
        MAIN.Await(FlagDisabled(11505211))
    
        Restart()
    Event_11500700(
        41,
        obj_flag=11505201,
        obj=Objects.o5010_0005,
        animation_id=8,
        life=18.5,
        entity=Objects.o5210_0001,
        flag=11505211,
    )
    
    MAIN.Await(FlagDisabled(11505211))
    
    Restart()


@ContinueOnRest(11500797)
def Event_11500797():
    """Event 11500797"""
    MAIN.Await(FlagEnabled(11505222))
    
    DisableFlag(11505222)
    EnableFlag(11505212)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0006)
    if FlagEnabled(11500812):
        Event_11500700(
            2,
            obj_flag=11505202,
            obj=Objects.o5010_0006,
            animation_id=1,
            life=2.5,
            entity=Objects.o5210_0002,
            flag=11505212,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(
            12,
            obj_flag=11505202,
            obj=Objects.o5010_0006,
            animation_id=2,
            life=7.5,
            entity=Objects.o5210_0003,
            flag=11505212,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(
            22,
            obj_flag=11505202,
            obj=Objects.o5010_0006,
            animation_id=3,
            life=7.5,
            entity=Objects.o5210_0000,
            flag=11505212,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(
            32,
            obj_flag=11505202,
            obj=Objects.o5010_0006,
            animation_id=4,
            life=12.5,
            entity=Objects.o5210_0001,
            flag=11505212,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505202,
            obj=Objects.o5010_0001,
            animation_id=5,
            collision=Collisions.h0081B0_0000,
            entity=Objects.o5210_0001,
            flag=11505212,
            flag_1=11500821,
            obj_1=Objects.o5010_0006,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505202,
            obj=Objects.o5010_0002,
            animation_id=6,
            collision=Collisions.h0081B0_0001,
            entity=Objects.o5210_0001,
            flag=11505212,
            flag_1=11500822,
            obj_1=Objects.o5010_0006,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505202,
            obj=Objects.o5010_0003,
            animation_id=7,
            collision=Collisions.h0081B0_0002,
            entity=Objects.o5210_0001,
            flag=11505212,
            flag_1=11500823,
            obj_1=Objects.o5010_0006,
        )
    
        MAIN.Await(FlagDisabled(11505212))
    
        Restart()
    Event_11500700(
        42,
        obj_flag=11505202,
        obj=Objects.o5010_0006,
        animation_id=8,
        life=18.5,
        entity=Objects.o5210_0001,
        flag=11505212,
    )
    
    MAIN.Await(FlagDisabled(11505212))
    
    Restart()


@ContinueOnRest(11500798)
def Event_11500798():
    """Event 11500798"""
    MAIN.Await(FlagEnabled(11505223))
    
    DisableFlag(11505223)
    EnableFlag(11505213)
    DisableObject(Objects.o5010_0000)
    EnableObject(Objects.o5010_0007)
    if FlagEnabled(11500812):
        Event_11500700(
            3,
            obj_flag=11505203,
            obj=Objects.o5010_0007,
            animation_id=1,
            life=2.5,
            entity=Objects.o5210_0002,
            flag=11505213,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500803):
        Event_11500700(
            13,
            obj_flag=11505203,
            obj=Objects.o5010_0007,
            animation_id=2,
            life=7.5,
            entity=Objects.o5210_0003,
            flag=11505213,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagEnabled(11500806):
        Event_11500700(
            23,
            obj_flag=11505203,
            obj=Objects.o5010_0007,
            animation_id=3,
            life=7.5,
            entity=Objects.o5210_0000,
            flag=11505213,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500830):
        Event_11500700(
            33,
            obj_flag=11505203,
            obj=Objects.o5010_0007,
            animation_id=4,
            life=12.5,
            entity=Objects.o5210_0001,
            flag=11505213,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500821):
        Event_11500750(
            0,
            obj_flag=11505203,
            obj=Objects.o5010_0001,
            animation_id=5,
            collision=Collisions.h0081B0_0000,
            entity=Objects.o5210_0001,
            flag=11505213,
            flag_1=11500821,
            obj_1=Objects.o5010_0007,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500822):
        Event_11500750(
            1,
            obj_flag=11505203,
            obj=Objects.o5010_0002,
            animation_id=6,
            collision=Collisions.h0081B0_0001,
            entity=Objects.o5210_0001,
            flag=11505213,
            flag_1=11500822,
            obj_1=Objects.o5010_0007,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    if FlagDisabled(11500823):
        Event_11500750(
            2,
            obj_flag=11505203,
            obj=Objects.o5010_0003,
            animation_id=7,
            collision=Collisions.h0081B0_0002,
            entity=Objects.o5210_0001,
            flag=11505213,
            flag_1=11500823,
            obj_1=Objects.o5010_0007,
        )
    
        MAIN.Await(FlagDisabled(11505213))
    
        Restart()
    Event_11500700(
        43,
        obj_flag=11505203,
        obj=Objects.o5010_0007,
        animation_id=8,
        life=18.5,
        entity=Objects.o5210_0001,
        flag=11505213,
    )
    
    MAIN.Await(FlagDisabled(11505213))
    
    Restart()


@ContinueOnRest(11500700)
def Event_11500700(_, obj_flag: Flag | int, obj: int, animation_id: int, life: float, entity: int, flag: Flag | int):
    """Event 11500700"""
    DisableMapCollision(collision=Collisions.h0110B0_0000)
    ForceAnimation(entity, 1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=life,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableFlag(flag)


@ContinueOnRest(11500750)
def Event_11500750(
    _,
    obj_flag: Flag | int,
    obj: int,
    animation_id: int,
    collision: Collision | int,
    entity: int,
    flag: Flag | int,
    flag_1: Flag | int,
    obj_1: Object | int,
):
    """Event 11500750"""
    DisableMapCollision(collision=Collisions.h0110B0_0000)
    EnableFlag(flag_1)
    EnableObject(obj)
    DisableObject(obj_1)
    ForceAnimation(entity, 1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=12.5,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    EnableMapCollision(collision=collision)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableFlag(flag)


@ContinueOnRest(11500830)
def Event_11500830():
    """Event 11500830"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1502810))
    
    EnableFlag(11500830)


@ContinueOnRest(11500831)
def Event_11500831():
    """Event 11500831"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11500751))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502811))
    AND_2.Add(FlagEnabled(11500752))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502812))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    Kill(PLAYER)


@ContinueOnRest(11500850)
def Event_11500850():
    """Event 11500850"""
    DisableFlag(11505250)
    AND_1.Add(FlagDisabled(11505250))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5200_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11505250))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=Objects.o5200_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    DisableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFinishedConditionFalse(23, input_condition=AND_1)
    Move(
        PLAYER,
        destination=Objects.o5200_0000,
        destination_type=CoordEntityType.Object,
        model_point=101,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8020)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
    if FlagEnabled(11500812):
        DisableFlag(11500812)
        DisableFlag(11500803)
        ForceAnimation(Objects.o5200_0000, 3, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500809):
        DisableFlag(11500809)
        EnableFlag(11500812)
        ForceAnimation(Objects.o5200_0000, 2, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500806):
        DisableFlag(11500806)
        EnableFlag(11500809)
        ForceAnimation(Objects.o5200_0000, 1, wait_for_completion=True)
        Restart()
    if FlagDisabled(11500803):
        EnableFlag(11500803)
        EnableFlag(11500806)
        ForceAnimation(Objects.o5200_0000, 0, wait_for_completion=True)
        Restart()
    RestartIfFinishedConditionFalse(input_condition=AND_2)
    Move(
        PLAYER,
        destination=Objects.o5200_0000,
        destination_type=CoordEntityType.Object,
        model_point=103,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8021)
    CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
    if FlagEnabled(11500812):
        DisableFlag(11500812)
        EnableFlag(11500809)
        ForceAnimation(Objects.o5200_0000, 5, wait_for_completion=True)
        Restart()
    if FlagDisabled(11500803):
        EnableFlag(11500803)
        EnableFlag(11500812)
        ForceAnimation(Objects.o5200_0000, 4, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500806):
        DisableFlag(11500806)
        DisableFlag(11500803)
        ForceAnimation(Objects.o5200_0000, 7, wait_for_completion=True)
        Restart()
    if FlagEnabled(11500809):
        DisableFlag(11500809)
        EnableFlag(11500806)
        ForceAnimation(Objects.o5200_0000, 6, wait_for_completion=True)
        Restart()
    EnableFlag(11500802)
    Restart()


@ContinueOnRest(11505255)
def Event_11505255():
    """Event 11505255"""
    AND_1.Add(FlagDisabled(11505250))
    AND_1.Add(FlagDisabled(11505251))
    AND_1.Add(FlagDisabled(11500809))
    AND_1.Add(TimeElapsed(seconds=2.0))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502800))
    AND_2.Add(FlagDisabled(11505250))
    AND_2.Add(FlagDisabled(11505252))
    AND_2.Add(FlagEnabled(11500803))
    AND_2.Add(TimeElapsed(seconds=2.0))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502801))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    SkipLinesIfFinishedConditionTrue(19, input_condition=AND_2)
    EnableFlag(11505251)
    DisableFlag(11505252)
    if FlagDisabled(11500803):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
        EnableFlag(11500803)
        EnableFlag(11500809)
        ForceAnimation(Objects.o5200_0000, 0, wait_for_completion=True)
        ForceAnimation(Objects.o5200_0000, 1, wait_for_completion=True)
    if FlagEnabled(11500806):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
        DisableFlag(11500806)
        EnableFlag(11500809)
        ForceAnimation(Objects.o5200_0000, 1, wait_for_completion=True)
    if FlagEnabled(11500812):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
        DisableFlag(11500812)
        EnableFlag(11500809)
        ForceAnimation(Objects.o5200_0000, 5, wait_for_completion=True)
    SkipLines(18)
    DisableFlag(11505251)
    EnableFlag(11505252)
    if FlagEnabled(11500809):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
        DisableFlag(11500809)
        DisableFlag(11500803)
        ForceAnimation(Objects.o5200_0000, 6, wait_for_completion=True)
        ForceAnimation(Objects.o5200_0000, 7, wait_for_completion=True)
    if FlagEnabled(11500806):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
        DisableFlag(11500806)
        DisableFlag(11500803)
        ForceAnimation(Objects.o5200_0000, 7, wait_for_completion=True)
    if FlagEnabled(11500812):
        CreateTemporaryVFX(vfx_id=150001, anchor_entity=Objects.o5200_0000, anchor_type=CoordEntityType.Object)
        DisableFlag(11500812)
        DisableFlag(11500803)
        ForceAnimation(Objects.o5200_0000, 3, wait_for_completion=True)
    DisableFlag(11505250)
    Restart()


@ContinueOnRest(11500840)
def Event_11500840():
    """Event 11500840"""
    MAIN.Await(FlagEnabled(11505240))
    
    EnableFlag(11505240)
    
    MAIN.Await(FlagDisabled(11505240))
    
    Restart()


@ContinueOnRest(11500841)
def Event_11500841(_, flag: Flag | int):
    """Event 11500841"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11505240))
    AND_1.Add(FlagDisabled(flag))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(11505240))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11505240)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    DisableFlag(flag)
    SkipLines(1)
    EnableFlag(flag)
    Restart()


@ContinueOnRest(11500835)
def Event_11500835():
    """Event 11500835"""
    if Host():
        return
    WaitFrames(frames=10)
    EnableFlag(11505360)
    AND_1.Add(FlagEnabled(11505250))
    AND_2.Add(FlagDisabled(11505250))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    Wait(3.0)
    if FlagDisabled(11500803):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=3)
    if FlagEnabled(11500806):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=0)
    if FlagEnabled(11500809):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=1)
    if FlagEnabled(11500812):
        EndOfAnimation(obj=Objects.o5200_0000, animation_id=2)


@ContinueOnRest(11500100)
def Event_11500100():
    """Event 11500100"""
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1502060))
    AND_2.Add(ThisEventFlagEnabled())
    AND_2.Add(FlagDisabled(11500101))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1502061))
    AND_3.Add(ThisEventFlagEnabled())
    AND_3.Add(FlagDisabled(11500101))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1502062))
    AND_4.Add(ThisEventFlagEnabled())
    AND_4.Add(FlagEnabled(11500101))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1502060))
    AND_5.Add(ThisEventFlagEnabled())
    AND_5.Add(FlagEnabled(11500101))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=1502063))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Solid)
    SkipLinesIfFinishedConditionFalse(16, input_condition=AND_1)
    EnableFlag(11500100)
    ForceAnimation(Objects.o5301_0000, 0, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.WallTouchingFloor)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1502062))
    
    Restart()
    SkipLinesIfFinishedConditionTrue(27, input_condition=AND_4)
    SkipLinesIfFinishedConditionTrue(26, input_condition=AND_5)
    EnableFlag(11500101)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.WallTouchingFloor)
    ForceAnimation(Objects.o5301_0000, 1, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.Wall)
    AND_6.Add(AllPlayersOutsideRegion(region=1502060))
    AND_6.Add(AllPlayersOutsideRegion(region=1502063))
    
    MAIN.Await(AND_6)
    
    Restart()
    DisableFlag(11500101)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Wall)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.WallTouchingFloor)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.Wall)
    ForceAnimation(Objects.o5301_0000, 2, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_0_1, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_1_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_0, navmesh_type=NavmeshType.WallTouchingFloor)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_2_1, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_0, navmesh_type=NavmeshType.Wall)
    EnableNavmeshType(navmesh_id=Navigation.Navmesh_CageElevator_3_1, navmesh_type=NavmeshType.WallTouchingFloor)
    AND_7.Add(AllPlayersOutsideRegion(region=1502061))
    AND_7.Add(AllPlayersOutsideRegion(region=1502062))
    
    MAIN.Await(AND_7)
    
    Restart()


@ContinueOnRest(11500102)
def Event_11500102():
    """Event 11500102"""
    SkipLinesIfThisEventFlagDisabled(4)
    SkipLinesIfFlagEnabled(1, 11500100)
    EndOfAnimation(obj=Objects.o5301_0000, animation_id=20)
    End()
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(PlayerHasGood(2003))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5301_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=Objects.o5301_0000,
        destination_type=CoordEntityType.Object,
        model_point=120,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(Objects.o5301_0000, 10)
    if Client():
        return
    DisplayDialog(text=10010862, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(11500103)
def Event_11500103():
    """Event 11500103"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11500102))
    AND_1.Add(PlayerDoesNotHaveGood(2003))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5301_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010163, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11500106)
def Event_11500106():
    """Event 11500106"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11500105))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5140_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=Objects.o5140_0000)
    Restart()


@ContinueOnRest(11500107)
def Event_11500107():
    """Event 11500107"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=Objects.o5140_0000, animation_id=0)
        End()
    AND_1.Add(FlagDisabled(11500105))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o5140_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11500105)
    Move(
        PLAYER,
        destination=Objects.o5140_0000,
        destination_type=CoordEntityType.Object,
        model_point=120,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7112)
    ForceAnimation(Objects.o5140_0000, 0)


@ContinueOnRest(11500110)
def Event_11500110(_, obj: int, obj_act_id: Flag | int):
    """Event 11500110"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if Client():
        return
    AND_1.Add(PlayerHasGood(2003))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=10010883, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=10010862, anchor_entity=obj, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(11505270)
def Event_11505270(
    _,
    region: Region | int,
    obj: int,
    vfx_id: VFXEvent | int,
    source_entity: int,
    launch_angle_y: int,
    left: Flag | int,
):
    """Event 11505270"""
    SkipLinesIfFlagDisabled(2, left)
    EndOfAnimation(obj=obj, animation_id=0)
    SkipLines(12)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(ObjectDamaged(obj, attacker=-1))
    
    MAIN.Await(OR_1)
    
    EnableFlag(left)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=obj, model_point=101, anchor_type=CoordEntityType.Object)
    DeleteVFX(vfx_id, erase_root_only=False)
    ForceAnimation(obj, 0, wait_for_completion=True)
    if ValueNotEqual(left=left, right=11505284):
        ShootProjectile(
            owner_entity=Characters.c2690_0000,
            source_entity=source_entity,
            model_point=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
        Wait(0.699999988079071)
        ShootProjectile(
            owner_entity=Characters.c2690_0000,
            source_entity=source_entity,
            model_point=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
        Wait(0.699999988079071)
        ShootProjectile(
            owner_entity=Characters.c2690_0000,
            source_entity=source_entity,
            model_point=101,
            behavior_id=5070,
            launch_angle_x=0,
            launch_angle_y=launch_angle_y,
            launch_angle_z=0,
        )
    
    MAIN.Await(EnabledFlagCount(FlagType.Absolute, flag_range=(11505280, 11505285)) >= 2)
    
    DisableFlag(left)
    ForceAnimation(obj, 1, wait_for_completion=True)
    Restart()


@ContinueOnRest(11505260)
def Event_11505260():
    """Event 11505260"""
    MAIN.Await(FlagEnabled(11505284))
    
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0004,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0005,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0006,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0007,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0004,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0005,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0006,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0007,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0004,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0005,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0006,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Objects.o5510_0007,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    
    MAIN.Await(FlagDisabled(11505284))
    
    Restart()


@RestartOnRest(11505050)
def Event_11505050():
    """Event 11505050"""
    if ThisEventFlagEnabled():
        return
    DisableAI(Characters.c2860_0000)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1502101))
    OR_1.Add(Attacked(attacked_entity=Characters.c2860_0000, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11505050)
    
    MAIN.Await(FlagDisabled(11505052))
    
    EnableAI(Characters.c2860_0000)


@RestartOnRest(11505051)
def Event_11505051():
    """Event 11505051"""
    AND_1.Add(FlagEnabled(11505050))
    AND_2.Add(FlagEnabled(11505052))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    Move(Characters.c2860_0000, destination=1502100, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(Characters.c2860_0000, 9001, wait_for_completion=True)
    DisableFlag(11505052)
    Restart()


@RestartOnRest(11505055)
def Event_11505055():
    """Event 11505055"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c2860_0001, authority_level=UpdateAuthority.Forced)
    AND_1.Add(ObjectDestroyed(Objects.o5560_0001))
    AND_1.Add(ObjectDestroyed(Objects.o5560_0002))
    AND_1.Add(ObjectDestroyed(Objects.o5560_0003))
    AND_1.Add(ObjectDestroyed(Objects.o5560_0004))
    AND_1.Add(ObjectDestroyed(Objects.o5560_0006))
    AND_1.Add(ObjectDestroyed(Objects.o5560_0007))
    AND_1.Add(ObjectDestroyed(Objects.o5560_0009))
    AND_1.Add(ObjectDestroyed(Objects.o5561_0000))
    AND_1.Add(ObjectDestroyed(Objects.o5561_0001))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c2860_0001, command_id=20, command_slot=1)
    ReplanAI(Characters.c2860_0001)


@ContinueOnRest(11505110)
def Event_11505110():
    """Event 11505110"""
    AND_1.Add(FlagEnabled(11505100))
    AND_2.Add(FlagEnabled(11505100))
    AND_3.Add(FlagEnabled(11505100))
    AND_4.Add(FlagEnabled(11505100))
    AND_5.Add(FlagEnabled(11505100))
    AND_6.Add(FlagEnabled(11505100))
    AND_7.Add(FlagEnabled(11505100))
    AND_1.Add(FlagEnabled(11505111))
    AND_2.Add(FlagEnabled(11505112))
    AND_3.Add(FlagEnabled(11505113))
    AND_4.Add(FlagEnabled(11505114))
    AND_5.Add(FlagEnabled(11505115))
    AND_6.Add(FlagEnabled(11505116))
    AND_7.Add(FlagRangeAllDisabled(flag_range=(11505111, 11505116)))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_6)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_5)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_4)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5303,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_3)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5302,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_2)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5301,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, input_condition=AND_1)
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    ShootProjectile(
        owner_entity=Characters.c2690_0000,
        source_entity=Characters.c2860_0001,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(Characters.c2860_0001, command_id=-1, command_slot=2)
    DisableFlag(11505105)
    RestartEvent(event_id=11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()


@ContinueOnRest(11505111)
def Event_11505111(_, left: Flag | int, region: Region | int, command_id: int):
    """Event 11505111"""
    AND_1.Add(FlagDisabled(11505100))
    AND_1.Add(FlagDisabled(11505105))
    AND_1.Add(TimeElapsed(seconds=2.0))
    AND_1.Add(FlagDisabled(left))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    if ValueLessThan(left=left, right=11505112):
        AND_1.Add(AllPlayersOutsideRegion(region=1502701))
    if ValueLessThan(left=left, right=11505113):
        AND_1.Add(AllPlayersOutsideRegion(region=1502702))
    if ValueLessThan(left=left, right=11505114):
        AND_1.Add(AllPlayersOutsideRegion(region=1502703))
    if ValueLessThan(left=left, right=11505115):
        AND_1.Add(AllPlayersOutsideRegion(region=1502704))
    if ValueLessThan(left=left, right=11505116):
        AND_1.Add(AllPlayersOutsideRegion(region=1502705))
    if ValueLessThan(left=left, right=11505117):
        AND_1.Add(AllPlayersOutsideRegion(region=1502710))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((11505111, 11505116))
    EnableFlag(left)
    AICommand(Characters.c2860_0001, command_id=command_id, command_slot=2)
    Restart()


@ContinueOnRest(11505101)
def Event_11505101():
    """Event 11505101"""
    MAIN.Await(FlagEnabled(11505105))
    
    EnableFlag(11505105)
    
    MAIN.Await(FlagDisabled(11505105))
    
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@ContinueOnRest(11505102)
def Event_11505102():
    """Event 11505102"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11505105))
    
    Wait(30.0)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@RestartOnRest(11505060)
def Event_11505060(_, character: Character | int):
    """Event 11505060"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=500))
    
    EzstateAIRequest(character, command_id=1500, command_slot=0)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(character, tae_event_id=500))
    
    Restart()


@RestartOnRest(11505070)
def Event_11505070(_, character: Character | int):
    """Event 11505070"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=1400))
    
    Wait(10.0)
    EzstateAIRequest(character, command_id=1501, command_slot=0)
    Restart()


@RestartOnRest(11505080)
def Event_11505080():
    """Event 11505080"""
    if ThisEventFlagEnabled():
        SetStandbyAnimationSettings(Characters.c2690_0005)
        End()
    OR_1.Add(Attacked(attacked_entity=Characters.c2690_0005, attacker=PLAYER))
    OR_1.Add(HealthRatio(Characters.c2690_0005) != 1.0)
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(Characters.c2690_0005)
    ForceAnimation(Characters.c2690_0005, 2000)


@RestartOnRest(11505010)
def Event_11505010():
    """Event 11505010"""
    AND_1.Add(CharacterAlive(Characters.c2780_0000))
    AND_1.Add(CharacterBackreadEnabled(Characters.c2780_0000))
    AND_1.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5421))
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Characters.c2780_0000,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=Characters.c2780_0000,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=Characters.c2780_0000,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(Characters.c2780_0000, command_id=10, command_slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(11505011)
def Event_11505011():
    """Event 11505011"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.c2780_0000, 5420))
    AND_1.Add(Attacked(attacked_entity=Characters.c2780_0000, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(Characters.c2780_0000, 3150)
    RemoveSpecialEffect(Characters.c2780_0000, 3151)
    AND_7.Add(CharacterBackreadDisabled(Characters.c2780_0000))
    if AND_7:
        return RESTART
    AND_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5421))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(Characters.c2780_0000, 3001, wait_for_completion=True)
    AND_3.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5422))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(Characters.c2780_0000, 3001, wait_for_completion=True)
    AND_4.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5423))
    SkipLinesIfConditionFalse(1, AND_4)
    ForceAnimation(Characters.c2780_0000, 3001, wait_for_completion=True)
    AND_5.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5424))
    SkipLinesIfConditionFalse(1, AND_5)
    ForceAnimation(Characters.c2780_0000, 3006, wait_for_completion=True)
    ReplanAI(Characters.c2780_0000)
    RemoveSpecialEffect(Characters.c2780_0000, 3150)
    RemoveSpecialEffect(Characters.c2780_0000, 3151)
    Restart()


@RestartOnRest(11505012)
def Event_11505012():
    """Event 11505012"""
    AND_1.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5421))
    AND_1.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 3150))
    AND_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5420))
    AND_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_2)
    AICommand(Characters.c2780_0000, command_id=200, command_slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(Characters.c2780_0000, command_id=210, command_slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5420))
    OR_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11505013)
def Event_11505013():
    """Event 11505013"""
    AND_1.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5422))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.c2780_0000, 3150))
    AND_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5423))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.c2780_0000, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(Characters.c2780_0000, 3150)
    RemoveSpecialEffect(Characters.c2780_0000, 3151)
    SkipLinesIfFinishedConditionTrue(5, input_condition=AND_2)
    AICommand(Characters.c2780_0000, command_id=201, command_slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(Characters.c2780_0000, command_id=211, command_slot=0)
    ReplanAI(Characters.c2780_0000)
    Wait(0.10000000149011612)
    AICommand(Characters.c2780_0000, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5420))
    OR_2.Add(CharacterHasSpecialEffect(Characters.c2780_0000, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11505014)
def Event_11505014():
    """Event 11505014"""
    AND_1.Add(Singleplayer())
    AND_1.Add(CharacterInsideRegion(Characters.c2780_0000, region=1502010))
    AND_1.Add(CharacterBackreadDisabled(Characters.c2780_0000))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c2780_0000, 5421)
    ClearTargetList(Characters.c2780_0000)
    ReplanAI(Characters.c2780_0000)
    Move(Characters.c2780_0000, destination=1502010, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2780_0000))
    
    Restart()


@RestartOnRest(11505015)
def Event_11505015():
    """Event 11505015"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(Characters.c2780_0000))
    if AND_1:
        return
    ResetAnimation(Characters.c2780_0000, disable_interpolation=True)
    ForceAnimation(Characters.c2780_0000, 0)
    ReplanAI(Characters.c2780_0000)


@RestartOnRest(11500900)
def Event_11500900():
    """Event 11500900"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(Characters.c2780_0000)
        End()
    
    MAIN.Await(CharacterDead(Characters.c2780_0000))
    
    End()


@ContinueOnRest(11500210)
def Event_11500210():
    """Event 11500210"""
    if Client():
        return
    
    MAIN.Await(InsideMap(game_map=SENS_FORTRESS))
    
    MAIN.Await(TimeElapsed(seconds=5.0))
    
    MAIN.Await(FlagEnabled(CommonFlags.IronGolemDead))
    
    MAIN.Await(ActionButton(
        prompt_text=10010120,
        anchor_entity=1502505,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    DisableBackread(Characters.c2570_0000)
    WaitFrames(frames=1)
    if FlagDisabled(CommonFlags.DarkAnorLondo):
        PlayCutscene(150000, cutscene_flags=0, player_id=10000, move_to_region=1502501, game_map=ANOR_LONDO)
    else:
        SetMapDrawParamSlot(map_area_id=15, draw_param_slot=2)
        PlayCutscene(150002, cutscene_flags=0, player_id=10000, move_to_region=1502501, game_map=ANOR_LONDO)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=33)
    Restart()


@RestartOnRest(11500860)
def Event_11500860(_, character: Character | int):
    """Event 11500860"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(11500600)
def Event_11500600(_, obj: Object | int, obj_act_id: int):
    """Event 11500600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11500510)
def Event_11500510(_, character: Character | int, flag: Flag | int):
    """Event 11500510"""
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


@ContinueOnRest(11500520)
def Event_11500520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11500530)
def Event_11500530():
    """Event 11500530"""
    if FlagDisabled(11500593):
        DisableObjectActivation(Objects.o5310_0004, obj_act_id=-1)
    
        MAIN.Await(FlagEnabled(11500593))
    
        EnableObjectActivation(Objects.o5310_0004, obj_act_id=-1)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(11500112))
    
    DisableFlag(71500021)


@ContinueOnRest(11500531)
def Event_11500531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500531"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1090))
    AND_1.Add(FlagEnabled(11500112))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11500532)
def Event_11500532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500532"""
    AND_1.Add(FlagDisabled(1096))
    AND_1.Add(FlagEnabled(1092))
    AND_1.Add(FlagEnabled(11500594))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11500533)
def Event_11500533(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500533"""
    AND_1.Add(FlagDisabled(1114))
    AND_1.Add(FlagEnabled(1113))
    AND_1.Add(FlagEnabled(723))
    AND_1.Add(InsideMap(game_map=SENS_FORTRESS))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11500534)
def Event_11500534(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500534"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1490))
    AND_1.Add(FlagEnabled(11500591))
    AND_1.Add(FlagEnabled(11500200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(
        character,
        destination=1502510,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0060B0_0000,
    )
    SetNest(character, region=1502510)
    Kill(Characters.c2690_0006)
    Kill(Characters.c2690_0007)


@ContinueOnRest(11500535)
def Event_11500535(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500535"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1490))
    AND_1.Add(FlagDisabled(11500591))
    AND_1.Add(FlagEnabled(11500200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(
        character,
        destination=1502510,
        destination_type=CoordEntityType.Region,
        set_draw_parent=Collisions.h0060B0_0000,
    )
    SetNest(character, region=1502510)
    Kill(Characters.c2690_0006)
    Kill(Characters.c2690_0007)


@ContinueOnRest(11500536)
def Event_11500536(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11500536"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1491))
    AND_1.Add(FlagEnabled(11500850))
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_2.Add(Host())
    AND_2.Add(FlagDisabled(1512))
    AND_2.Add(FlagEnabled(1492))
    AND_2.Add(FlagEnabled(11500592))
    AND_2.Add(FlagEnabled(11500850))
    AND_2.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(11505030)
def Event_11505030():
    """Event 11505030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11505033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11505031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0007)
    if FlagEnabled(CommonFlags.IronGolemDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0007))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0007, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0007,
        region=1502000,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


@ContinueOnRest(11505990)
def Event_11505990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 11505990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11505029)
def Event_11505029():
    """Event 11505029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11505033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11505031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0007)
    if FlagEnabled(CommonFlags.IronGolemDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11505031))
    AND_1.Add(FlagDisabled(11505033))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0007))
    AND_1.Add(EntityWithinDistance(entity=Characters.c0000_0007, other_entity=PLAYER, radius=10.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0007,
        region=1502000,
        summon_flag=11505031,
        dismissal_flag=11505033,
    )


@ContinueOnRest(11505032)
def Event_11505032():
    """Event 11505032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11505031))
    AND_1.Add(FlagEnabled(11505393))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0007, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0007)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0007, region=1502998))
    
    RotateToFaceEntity(Characters.c0000_0007, target_entity=1502997)
    ForceAnimation(Characters.c0000_0007, 7410)
    AICommand(Characters.c0000_0007, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0007)


@ContinueOnRest(11505843)
def Event_11505843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11505843"""
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


@ContinueOnRest(11505846)
def Event_11505846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11505846"""
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
