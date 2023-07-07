"""
Undead Asylum

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m18_01_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11810992()
    EnableTreasure(obj=1811660)
    EnableTreasure(obj=1811661)
    RegisterBonfire(bonfire_flag=11810992, obj=Objects.o0200_0000, reaction_distance=1.0)
    RegisterBonfire(bonfire_flag=11810984, obj=Objects.o0200_0001, reaction_distance=1.0)
    RegisterLadder(start_climbing_flag=11810010, stop_climbing_flag=11810011, obj=Objects.o8500_0000)
    DisableMapCollision(collision=Collisions.h0550B1_0000)
    DisableFlag(11810315)
    DisableFlag(11810112)
    DisableObjectActivation(Objects.o8540_0000, obj_act_id=-1)
    DisableObjectActivation(Objects.o8540_0001, obj_act_id=-1)
    DisableObjectActivation(Objects.o8540_0002, obj_act_id=-1)
    SkipLinesIfOutsideMap(4, game_map=UNDEAD_ASYLUM)
    SkipLinesIfFlagEnabled(3, 11810002)
    PlayCutscene(
        180101,
        cutscene_flags=CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=1812011,
        game_map=UNDEAD_ASYLUM,
    )
    EnableFlag(11810002)
    SetRespawnPoint(respawn_point=1812900)
    Event_11810090(0, obj=Objects.o8952_0000, vfx_id=VFX.CheckpointFog1, destination=1812600, destination_1=1812601)
    Event_11810000()
    Event_11810150()
    Event_11810211()
    Event_11810200(1, obj=Objects.o8520_0000, obj_1=Objects.o8520_0001, obj_2=Objects.o8521_0000)
    Event_11810310()
    Event_11810311()
    Event_11810312()
    Event_11810313()
    Event_11810120()
    Event_11810110()
    Event_11810111()
    Event_11810450()
    Event_11810320()
    Event_11810300()
    Event_11810850(0, character=Characters.c2792_0000, item_lot=27907000)
    Event_11810850(1, character=Characters.c2792_0001, item_lot=27907000)
    SkipLinesIfClient(44)
    Event_11810641(0, item_type=3, item=111, flag=11810601, flag_1=51810800)
    Event_11810641(1, item_type=3, item=270, flag=11810602, flag_1=51810810)
    Event_11810641(2, item_type=3, item=271, flag=11810603, flag_1=51810820)
    Event_11810641(3, item_type=3, item=272, flag=11810604, flag_1=51810830)
    Event_11810641(4, item_type=3, item=275, flag=11810605, flag_1=51810840)
    Event_11810641(5, item_type=3, item=293, flag=11810606, flag_1=51810850)
    Event_11810641(6, item_type=3, item=350, flag=11810607, flag_1=51810860)
    Event_11810641(7, item_type=3, item=500, flag=11810607, flag_1=51810860)
    Event_11810641(8, item_type=3, item=370, flag=11810608, flag_1=51810870)
    Event_11810641(9, item_type=3, item=375, flag=11810609, flag_1=51810880)
    Event_11810641(10, item_type=3, item=376, flag=11810610, flag_1=51810890)
    Event_11810641(11, item_type=3, item=380, flag=11810611, flag_1=51810900)
    Event_11810641(12, item_type=3, item=385, flag=11810612, flag_1=51810910)
    Event_11810641(13, item_type=3, item=501, flag=11810613, flag_1=51810920)
    Event_11810641(14, item_type=0, item=1330000, flag=11810614, flag_1=51810930)
    Event_11810641(15, item_type=0, item=1332000, flag=11810615, flag_1=51810940)
    Event_11810641(16, item_type=0, item=1396000, flag=11810616, flag_1=51810950)
    Event_11810641(17, item_type=1, item=190000, flag=11810617, flag_1=51810960)
    Event_11810641(18, item_type=1, item=290000, flag=11810618, flag_1=51810970)
    Event_11810641(19, item_type=1, item=560000, flag=11810619, flag_1=51810980)
    Event_11810641(20, item_type=2, item=130, flag=11810620, flag_1=51810990)
    Event_11810641(21, item_type=3, item=711, flag=11810621, flag_1=51811000)
    Event_11810600()
    Event_11815110(0, flag=11810601, item_lot=3000, flag_1=51810800)
    Event_11815110(1, flag=11810602, item_lot=3010, flag_1=51810810)
    Event_11815110(2, flag=11810603, item_lot=3020, flag_1=51810820)
    Event_11815110(3, flag=11810604, item_lot=3030, flag_1=51810830)
    Event_11815110(4, flag=11810605, item_lot=3040, flag_1=51810840)
    Event_11815110(5, flag=11810606, item_lot=3050, flag_1=51810850)
    Event_11815110(6, flag=11810607, item_lot=3060, flag_1=51810860)
    Event_11815110(7, flag=11810608, item_lot=3070, flag_1=51810870)
    Event_11815110(8, flag=11810609, item_lot=3080, flag_1=51810880)
    Event_11815110(9, flag=11810610, item_lot=3090, flag_1=51810890)
    Event_11815110(10, flag=11810611, item_lot=3100, flag_1=51810900)
    Event_11815110(11, flag=11810612, item_lot=3110, flag_1=51810910)
    Event_11815110(12, flag=11810613, item_lot=3120, flag_1=51810920)
    Event_11815110(13, flag=11810614, item_lot=3130, flag_1=51810930)
    Event_11815110(14, flag=11810615, item_lot=3140, flag_1=51810940)
    Event_11815110(15, flag=11810616, item_lot=3150, flag_1=51810950)
    Event_11815110(16, flag=11810617, item_lot=3160, flag_1=51810960)
    Event_11815110(17, flag=11810618, item_lot=3170, flag_1=51810970)
    Event_11815110(18, flag=11810619, item_lot=3180, flag_1=51810980)
    Event_11815110(19, flag=11810620, item_lot=3190, flag_1=51810990)
    Event_11815110(20, flag=11810621, item_lot=3200, flag_1=51811000)
    Event_11810100(0, obj_act_id=11810100, obj=Objects.o8540_0000, text=10010869)
    Event_11810100(1, obj_act_id=11810101, obj=Objects.o8540_0001, text=10010869)
    Event_11810100(2, obj_act_id=11810102, obj=Objects.o8540_0002, text=10010869)
    Event_11810100(3, obj_act_id=11810103, obj=Objects.o8540_0003, text=10010869)
    Event_11810100(4, obj_act_id=11810104, obj=Objects.o8540_0004, text=10010875)
    Event_11810100(5, obj_act_id=11810105, obj=Objects.o8540_0005, text=0)
    Event_11810100(6, obj_act_id=11810106, obj=Objects.o8540_06, text=10010871)
    Event_11815150()
    Event_11810400(
        0,
        class_type=0,
        obj=Objects.o0500_0033,
        obj_1=Objects.o0500_0023,
        obj_2=Objects.o0500_0023,
        state=0,
        state_1=0,
        state_2=0,
        state_3=0,
    )
    Event_11810400(
        1,
        class_type=1,
        obj=Objects.o0500_0034,
        obj_1=Objects.o0500_0024,
        obj_2=1811661,
        state=0,
        state_1=0,
        state_2=0,
        state_3=1,
    )
    Event_11810400(
        2,
        class_type=2,
        obj=Objects.o0500_0035,
        obj_1=Objects.o0500_0025,
        obj_2=Objects.o0500_0025,
        state=0,
        state_1=0,
        state_2=0,
        state_3=0,
    )
    Event_11810400(
        3,
        class_type=3,
        obj=Objects.o0500_0036,
        obj_1=Objects.o0500_0026,
        obj_2=1811660,
        state=1,
        state_1=0,
        state_2=0,
        state_3=0,
    )
    Event_11810400(
        4,
        class_type=4,
        obj=Objects.o0500_0037,
        obj_1=Objects.o0500_0027,
        obj_2=Objects.o0500_0027,
        state=0,
        state_1=0,
        state_2=0,
        state_3=0,
    )
    Event_11810400(
        5,
        class_type=5,
        obj=Objects.o0500_0038,
        obj_1=Objects.o0500_0028,
        obj_2=Objects.o0500_0043,
        state=0,
        state_1=0,
        state_2=1,
        state_3=0,
    )
    Event_11810400(
        6,
        class_type=6,
        obj=Objects.o0500_0039,
        obj_1=Objects.o0500_0029,
        obj_2=Objects.o0500_0044,
        state=1,
        state_1=0,
        state_2=0,
        state_3=0,
    )
    Event_11810400(
        7,
        class_type=7,
        obj=Objects.o0500_0040,
        obj_1=Objects.o0500_0030,
        obj_2=Objects.o0500_0045,
        state=0,
        state_1=1,
        state_2=0,
        state_3=0,
    )
    Event_11810400(
        8,
        class_type=8,
        obj=Objects.o0500_0041,
        obj_1=Objects.o0500_0031,
        obj_2=Objects.o0500_0046,
        state=0,
        state_1=0,
        state_2=0,
        state_3=1,
    )
    Event_11810400(
        9,
        class_type=9,
        obj=Objects.o0500_0042,
        obj_1=Objects.o0500_0032,
        obj_2=Objects.o0500_0032,
        state=0,
        state_1=0,
        state_2=0,
        state_3=0,
    )
    DisableSoundEvent(sound_id=Sounds.AsylumDemonMusic)
    if FlagDisabled(11810312):
        DisableFlag(11810310)
        DisableFlag(11810314)
    if FlagEnabled(61810105):
        DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)
    if FlagEnabled(CommonFlags.AsylumDemonDead):
        Event_11815392()
        DisableObject(Objects.o8950_0000)
        DeleteVFX(VFX.AsylumTopEntranceFog, erase_root_only=False)
        EndOfAnimation(obj=Objects.o8542_0000, animation_id=1)
        EndOfAnimation(obj=Objects.o8541_0001, animation_id=1)
        DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)
    else:
        Event_11815390()
        Event_11815393()
        Event_11815392()
        Event_11810001()
        Event_11815394()
        Event_11815395()
    DisableObject(Objects.o8953_0000)
    DeleteVFX(VFX.StrayDemonLadderFog, erase_root_only=False)
    DisableSoundEvent(sound_id=Sounds.StrayDemonMusic)
    if FlagDisabled(CommonFlags.TutorialComplete):
        return
    if FlagEnabled(11810900):
        Event_11815382()
    else:
        Event_11815382()
        Event_11810900()
        Event_11815384()
        Event_11815385()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    SkipLinesIfClient(11)
    SkipLinesIfFlagEnabled(10, 705)
    AND_1.Add(NewGameCycleGreaterThanOrEqual(completion_count=1))
    SkipLinesIfConditionFalse(8, AND_1)
    EnableFlag(705)
    EnableFlag(50000082)
    SetRespawnPoint(respawn_point=1812900)
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    Event_11810050()
    Event_11810350()
    Event_11810220()
    HumanityRegistration(Characters.c0000_0002, event_flag=8326)
    if FlagDisabled(1061):
        DisableCharacter(Characters.c0000_0003)
    SetTeamType(Characters.c0000_0003, TeamType.HostileAlly)
    Event_11810520(0, character=Characters.c0000_0002, first_flag=1060, last_flag=1074, flag=1073)
    Event_11810530(0, character=Characters.c0000_0002)
    Event_11810531(0, character=Characters.c0000_0003, first_flag=1060, last_flag=1074, flag=1061)
    Event_11810532(0, character=Characters.c0000_0003, first_flag=1060, last_flag=1074, flag=1062)
    Event_11815010()


@ContinueOnRest(11810992)
def Event_11810992():
    """Event 11810992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c2230_0000, 7100)
    AddSpecialEffect(Characters.c2792_0000, 7100)
    AddSpecialEffect(Characters.c2792_0001, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c2230_0000, 7100)
    RemoveSpecialEffect(Characters.c2792_0000, 7100)
    RemoveSpecialEffect(Characters.c2792_0001, 7100)
    Restart()


@ContinueOnRest(11810090)
def Event_11810090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11810090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
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


@RestartOnRest(11815090)
def Event_11815090():
    """Event 11815090"""
    DisableCharacter(1810900)
    
    MAIN.Await(FlagEnabled(CommonFlags.TutorialComplete))
    
    OR_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    OR_1.Add(FlagEnabled(11815090))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11815090)
    EnableCharacter(1810900)
    
    MAIN.Await(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    
    Kill(1810900)


@ContinueOnRest(11815390)
def Event_11815390():
    """Event 11815390"""
    AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1812998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=1811990,
    ))
    
    MAIN.Await(AND_1)
    
    Move(Characters.c2232_0000, destination=1812301, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(PLAYER, target_entity=1812997)
    ForceAnimation(PLAYER, 7410)
    DisableSoapstoneMessage(1813210)
    ForceAnimation(Objects.o8542_0000, 3)
    if FlagEnabled(11810112):
        ForceAnimation(Objects.o8541_0001, 3)
    Restart()


@ContinueOnRest(11815393)
def Event_11815393():
    """Event 11815393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
        OR_1.Add(CharacterInsideRegion(PLAYER, region=1812996))
        OR_1.Add(CharacterInsideRegion(PLAYER, region=1812350))
        AND_1.Add(OR_1)
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2232_0000)


@RestartOnRest(11815392)
def Event_11815392():
    """Event 11815392"""
    if FlagEnabled(CommonFlags.AsylumDemonDead):
        DisableCharacter(Characters.c2232_0000)
        Kill(Characters.c2232_0000)
        End()
    AND_1.Add(FlagDisabled(11810310))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1812996))
    AND_2.Add(FlagEnabled(11810310))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1812990))
    AND_3.Add(FlagEnabled(11815393))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.c2232_0000)


@ContinueOnRest(11810001)
def Event_11810001():
    """Event 11810001"""
    MAIN.Await(HealthRatio(Characters.c2232_0000) <= 0.0)
    
    PlaySoundEffect(Characters.c2232_0000, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.c2232_0000))
    
    EnableFlag(CommonFlags.AsylumDemonDead)
    KillBoss(game_area_param_id=1810800)
    DisableObject(Objects.o8950_0000)
    DeleteVFX(VFX.AsylumTopEntranceFog)
    ForceAnimation(Objects.o8541_0001, 1)
    if FlagEnabled(11810312):
        ForceAnimation(Objects.o8542_0000, 1)
    DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)


@ContinueOnRest(11815394)
def Event_11815394():
    """Event 11815394"""
    DisableNetworkSync()
    
    MAIN.Await(FlagDisabled(11815396))
    
    AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(FlagEnabled(11810310))
    AND_1.Add(FlagEnabled(11815392))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1812990))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1812350))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(11815396)
    EnableSoundEvent(sound_id=Sounds.AsylumDemonMusic)
    EnableBossHealthBar(Characters.c2232_0000, name=2232)
    Restart()


@ContinueOnRest(11815395)
def Event_11815395():
    """Event 11815395"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11815396))
    
    AND_1.Add(FlagDisabled(11815390))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1812990))
    AND_2.Add(CharacterDead(Characters.c2232_0000))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11815396)
    DisableSoundEvent(sound_id=Sounds.AsylumDemonMusic)
    DisableBossHealthBar(Characters.c2232_0000, name=2232)
    Restart()


@RestartOnRest(11810310)
def Event_11810310():
    """Event 11810310"""
    if FlagEnabled(11810314):
        return
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(CommonFlags.AsylumDemonDead):
        return
    DisableObject(Objects.o8950_0000)
    DeleteVFX(VFX.AsylumTopEntranceFog, erase_root_only=False)
    DisableHealthBar(Characters.c2232_0000)
    DisableAI(Characters.c2232_0000)
    SetStandbyAnimationSettings(Characters.c2232_0000, standby_animation=9000)
    Move(Characters.c2232_0000, destination=1812305, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1812996))
    
    EnableFlag(11810314)
    AddSpecialEffect(Characters.c2232_0000, 4160)
    SetStandbyAnimationSettings(Characters.c2232_0000)
    ForceAnimation(Characters.c2232_0000, 9060, wait_for_completion=True)
    RemoveSpecialEffect(Characters.c2232_0000, 4160)
    SetNest(Characters.c2232_0000, region=1812300)
    EnableObject(Objects.o8950_0000)
    CreateVFX(VFX.AsylumTopEntranceFog)


@ContinueOnRest(11810311)
def Event_11810311():
    """Event 11810311"""
    AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(FlagDisabled(11815390))
    AND_1.Add(FlagDisabled(11810315))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1812996))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11810315)
    DisableFlag(11810112)
    ForceAnimation(Objects.o8541_0001, 3)
    ForceAnimation(Objects.o8542_0000, 1, wait_for_completion=True)


@ContinueOnRest(11810312)
def Event_11810312():
    """Event 11810312"""
    AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(FlagEnabled(11810315))
    AND_1.Add(PlayerStandingOnCollision(Collisions.h0006B1))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11810315)
    EnableFlag(11810312)
    DisableObjectActivation(Objects.o8541_0001, obj_act_id=-1)
    SetRespawnPoint(respawn_point=1812961)
    SaveRequest()
    EnableMapCollision(collision=Collisions.h0550B1_0000)
    ForceAnimation(Objects.o8542_0000, 3, wait_for_completion=True)
    DisableMapCollision(collision=Collisions.h0550B1_0000)


@ContinueOnRest(11810313)
def Event_11810313():
    """Event 11810313"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(FlagEnabled(11810312))
    AND_1.Add(FlagEnabled(61810105))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o8541_0001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160, anchor_entity=Objects.o8541_0001, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11815380)
def Event_11815380():
    """Event 11815380"""
    AND_1.Add(FlagDisabled(11810900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1812898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=0,
    ))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, target_entity=1812897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(Characters.c2230_0000)
    Restart()


@RestartOnRest(11815382)
def Event_11815382():
    """Event 11815382"""
    if FlagEnabled(11810900):
        DisableCharacter(Characters.c2230_0000)
        Kill(Characters.c2230_0000)
        RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=Objects.o8501_0000)
        End()
    DisableAI(Characters.c2230_0000)
    EnableInvincibility(Characters.c2230_0000)
    DisableHealthBar(Characters.c2230_0000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1812896))
    
    EnableAI(Characters.c2230_0000)
    DisableInvincibility(Characters.c2230_0000)
    EnableBossHealthBar(Characters.c2230_0000, name=2231)
    EnableObject(Objects.o8953_0000)
    CreateVFX(VFX.StrayDemonLadderFog)


@ContinueOnRest(11810900)
def Event_11810900():
    """Event 11810900"""
    MAIN.Await(CharacterDead(Characters.c2230_0000))
    
    KillBoss(game_area_param_id=1810810)
    DisableObject(Objects.o8953_0000)
    DeleteVFX(VFX.StrayDemonLadderFog)
    RegisterLadder(start_climbing_flag=11810012, stop_climbing_flag=11810013, obj=Objects.o8501_0000)


@ContinueOnRest(11815384)
def Event_11815384():
    """Event 11815384"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(FlagEnabled(11815382))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1812890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.StrayDemonMusic)


@ContinueOnRest(11815385)
def Event_11815385():
    """Event 11815385"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11815384))
    AND_1.Add(FlagEnabled(11810900))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.StrayDemonMusic)


@ContinueOnRest(CommonFlags.TutorialComplete)
def Event_11810000():
    """Event 11810000"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1812000))
    
    DisableBackread(Characters.c2232_0000)
    IssuePrefetchRequest(request_id=0)
    WaitFrames(frames=1)
    PlayCutscene(180125, cutscene_flags=0, player_id=10000)
    PlayCutscene(100225, cutscene_flags=0, player_id=10000, move_to_region=1022100, game_map=FIRELINK_SHRINE)
    WaitFrames(frames=1)
    if FlagDisabled(CommonFlags.AsylumDemonDead):
        EnableBackread(Characters.c2232_0000)
    EnableFlag(CommonFlags.TutorialComplete)
    SetRespawnPoint(respawn_point=1022960)
    SaveRequest()
    AwardAchievement(achievement_id=28)


@ContinueOnRest(11810150)
def Event_11810150():
    """Event 11810150"""
    if FlagDisabled(CommonFlags.TutorialComplete):
        DisableObject(Objects.o8550)
    
        MAIN.Await(FlagEnabled(CommonFlags.TutorialComplete))
    
        EnableObject(Objects.o8550)
    
    MAIN.Await(ActionButton(
        prompt_text=10010506,
        anchor_entity=1812001,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    SkipLinesIfMultiplayer(6)
    SetStandbyAnimationSettings(PLAYER)
    PlayCutscene(180126, cutscene_flags=0, player_id=10000, move_to_region=1022121, game_map=FIRELINK_SHRINE)
    PlayCutscene(100226, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=28)
    Restart()
    AND_1.Add(ActionButton(
        prompt_text=10010507,
        anchor_entity=1812001,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(CharacterOutsideRegion(PLAYER, region=1812001))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


@ContinueOnRest(11810100)
def Event_11810100(_, obj_act_id: Flag | int, obj: int, text: EventText | int):
    """Event 11810100"""
    if ThisEventSlotFlagEnabled():
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)
        End()
    SkipLinesIfClient(4)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    EnableFlag(obj_act_id)
    if ValueNotEqual(left=text, right=0):
        DisplayDialog(text=text, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(obj, obj_act_id=-1, relative_index=3)


@ContinueOnRest(11810120)
def Event_11810120():
    """Event 11810120"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1812020))
    AND_2.Add(FlagEnabled(11810105))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1812021))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@ContinueOnRest(11810110)
def Event_11810110():
    """Event 11810110"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(Objects.o8544_0000, obj_act_id=-1)
        EndOfAnimation(obj=Objects.o8544_0000, animation_id=1)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=11810110))
    
    EnableFlag(11810110)
    if Client():
        return
    DisplayDialog(text=10010870, anchor_entity=Objects.o8544_0000, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(11810111)
def Event_11810111():
    """Event 11810111"""
    MAIN.Await(ObjectActivated(obj_act_id=11810111))
    
    EnableFlag(11810112)
    Restart()


@ContinueOnRest(11810211)
def Event_11810211():
    """Event 11810211"""
    if ThisEventFlagEnabled():
        DisableObject(Objects.o8530_0000)
        EndOfAnimation(obj=Objects.o8530_0001, animation_id=0)
        End()
    DisableObject(Objects.o8530_0001)
    DisableObject(Objects.o8531_0000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1812120))
    
    CreateHazard(
        obj_flag=11810212,
        obj=Objects.o8530_0000,
        model_point=1,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=2.5,
        repetition_time=0.0,
    )
    ForceAnimation(Objects.o8530_0000, 0, wait_for_completion=True)
    DisableObject(Objects.o8530_0000)
    EnableObject(Objects.o8530_0001)
    EndOfAnimation(obj=Objects.o8530_0001, animation_id=0)
    EnableObject(Objects.o8531_0000)


@ContinueOnRest(11810200)
def Event_11810200(_, obj: Object | int, obj_1: Object | int, obj_2: Object | int):
    """Event 11810200"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DisableObject(obj_1)
        DisableObject(obj_2)
        End()
    DisableObject(obj_1)
    
    MAIN.Await(ObjectDestroyed(obj))
    
    DisableObject(obj)
    EnableObject(obj_1)
    DestroyObject(obj_1)
    DisableObject(obj_2)


@ContinueOnRest(11810400)
def Event_11810400(
    _,
    class_type: uchar,
    obj: Object | int,
    obj_1: Object | int,
    obj_2: Object | int,
    state: uchar,
    state_1: uchar,
    state_2: uchar,
    state_3: uchar,
):
    """Event 11810400"""
    AND_1.Add(PlayerClass(class_type))
    if not AND_1:
        return
    DisableSoapstoneMessage(1813200)
    DisableSoapstoneMessage(1813201)
    DisableSoapstoneMessage(1813202)
    DisableSoapstoneMessage(1813203)
    DisableSoapstoneMessage(1813204)
    DisableTreasure(obj=Objects.o0500_0033)
    DisableTreasure(obj=Objects.o0500_0023)
    DisableTreasure(obj=Objects.o0500_0034)
    DisableTreasure(obj=Objects.o0500_0024)
    DisableTreasure(obj=Objects.o0500_0035)
    DisableTreasure(obj=Objects.o0500_0025)
    DisableTreasure(obj=Objects.o0500_0036)
    DisableTreasure(obj=Objects.o0500_0026)
    DisableTreasure(obj=Objects.o0500_0037)
    DisableTreasure(obj=Objects.o0500_0027)
    DisableTreasure(obj=Objects.o0500_0038)
    DisableTreasure(obj=Objects.o0500_0028)
    DisableTreasure(obj=Objects.o0500_0043)
    DisableTreasure(obj=Objects.o0500_0039)
    DisableTreasure(obj=Objects.o0500_0029)
    DisableTreasure(obj=Objects.o0500_0044)
    DisableTreasure(obj=Objects.o0500_0040)
    DisableTreasure(obj=Objects.o0500_0030)
    DisableTreasure(obj=Objects.o0500_0045)
    DisableTreasure(obj=Objects.o0500_0041)
    DisableTreasure(obj=Objects.o0500_0031)
    DisableTreasure(obj=Objects.o0500_0046)
    DisableTreasure(obj=Objects.o0500_0042)
    DisableTreasure(obj=Objects.o0500_0032)
    DisableTreasure(obj=1811660)
    DisableTreasure(obj=1811661)
    DisableObject(Objects.o0500_0033)
    DisableObject(Objects.o0500_0023)
    DisableObject(Objects.o0500_0034)
    DisableObject(Objects.o0500_0024)
    DisableObject(Objects.o0500_0035)
    DisableObject(Objects.o0500_0025)
    DisableObject(Objects.o0500_0036)
    DisableObject(Objects.o0500_0026)
    DisableObject(Objects.o0500_0037)
    DisableObject(Objects.o0500_0027)
    DisableObject(Objects.o0500_0038)
    DisableObject(Objects.o0500_0028)
    DisableObject(Objects.o0500_0043)
    DisableObject(Objects.o0500_0039)
    DisableObject(Objects.o0500_0029)
    DisableObject(Objects.o0500_0044)
    DisableObject(Objects.o0500_0040)
    DisableObject(Objects.o0500_0030)
    DisableObject(Objects.o0500_0045)
    DisableObject(Objects.o0500_0041)
    DisableObject(Objects.o0500_0031)
    DisableObject(Objects.o0500_0046)
    DisableObject(Objects.o0500_0042)
    DisableObject(Objects.o0500_0032)
    DisableObject(1811660)
    DisableObject(1811661)
    SetSoapstoneMessageState(1813200, state)
    SetSoapstoneMessageState(1813201, state_1)
    SetSoapstoneMessageState(1813202, state_2)
    SetSoapstoneMessageState(1813203, state_2)
    SetSoapstoneMessageState(1813204, state_3)
    EnableObject(obj)
    EnableObject(obj_1)
    EnableObject(obj_2)
    EnableTreasure(obj=obj)
    EnableTreasure(obj=obj_1)
    EnableTreasure(obj=obj_2)


@ContinueOnRest(11810450)
def Event_11810450():
    """Event 11810450"""
    if ThisEventFlagEnabled():
        return
    DisableSoapstoneMessage(1813220)
    DisableSoapstoneMessage(1813221)
    OR_1.Add(FlagEnabled(11810590))
    OR_1.Add(FlagEnabled(50000082))
    
    MAIN.Await(OR_1)
    
    EnableSoapstoneMessage(1813220)
    EnableSoapstoneMessage(1813221)


@ContinueOnRest(11810220)
def Event_11810220():
    """Event 11810220"""
    if ThisEventFlagEnabled():
        DisableFlag(11810220)
        RestoreObject(Objects.o8510_0000)
        RestoreObject(Objects.o8510_0001)
        RestoreObject(Objects.o8511_0000)
    DisableObject(Objects.o8510_0001)
    AND_1.Add(FlagEnabled(CommonFlags.TutorialComplete))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1812400))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11810220)
    DisableObject(Objects.o8510_0000)
    EnableObject(Objects.o8510_0001)
    DestroyObject(Objects.o8510_0001)
    DisableObject(Objects.o8511_0000)
    PlaySoundEffect(Objects.o8510_0000, 851000000, sound_type=SoundType.o_Object)
    CreateTemporaryVFX(vfx_id=180100, anchor_entity=Objects.o8510_0000, anchor_type=CoordEntityType.Object)


@ContinueOnRest(11810320)
def Event_11810320():
    """Event 11810320"""
    if FlagEnabled(CommonFlags.TutorialComplete):
        return
    EnableInvincibility(Characters.c2230_0000)
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2230_0000))
    
    AICommand(Characters.c2230_0000, command_id=10, command_slot=0)
    
    MAIN.Await(FlagEnabled(CommonFlags.TutorialComplete))
    
    DisableInvincibility(Characters.c2230_0000)
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2230_0000))
    
    AICommand(Characters.c2230_0000, command_id=-1, command_slot=0)


@ContinueOnRest(11810300)
def Event_11810300():
    """Event 11810300"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(CommonFlags.AsylumDemonDead):
        return
    if FlagDisabled(11810301):
        EnableFlag(50000081)
        EnableFlag(50001661)
        EnableFlag(11810301)
    AND_1.Add(FlagDisabled(CommonFlags.AsylumDemonDead))
    AND_1.Add(FlagDisabled(11810090))
    AND_1.Add(HealthRatio(Characters.c2232_0000) <= 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlag(50000081)
    DisableFlag(50001661)
    EnableFlag(50001660)


@RestartOnRest(11810850)
def Event_11810850(_, character: Character | int, item_lot: int):
    """Event 11810850"""
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


@RestartOnRest(11810350)
def Event_11810350():
    """Event 11810350"""
    if FlagDisabled(CommonFlags.TutorialComplete):
        DisableObject(Objects.o0500_0008)
        DisableCharacter(Characters.c2792_0000)
        DisableCharacter(Characters.c2500_0012)
        DisableCharacter(Characters.c2500_0013)
        DisableCharacter(Characters.c2500_0014)
        DisableCharacter(Characters.c2500_0015)
        DisableCharacter(Characters.c2500_0016)
        DisableCharacter(Characters.c2500_0017)
        DisableCharacter(Characters.c2500_0018)
        DisableCharacter(Characters.c2500_0019)
        DisableCharacter(Characters.c2500_0020)
        DisableCharacter(Characters.c2500_0021)
        DisableCharacter(Characters.c2550_0001)
        DisableCharacter(Characters.c2550_0002)
        DisableCharacter(Characters.c2792_0001)
    
        MAIN.Await(FlagEnabled(CommonFlags.TutorialComplete))
    
        DisableFlag(11810211)
        EnableCharacter(Characters.c2792_0000)
        EnableCharacter(Characters.c2500_0012)
        EnableCharacter(Characters.c2500_0013)
        EnableCharacter(Characters.c2500_0014)
        EnableCharacter(Characters.c2500_0015)
        EnableCharacter(Characters.c2500_0016)
        EnableCharacter(Characters.c2500_0017)
        EnableCharacter(Characters.c2500_0018)
        EnableCharacter(Characters.c2500_0019)
        EnableCharacter(Characters.c2500_0020)
        EnableCharacter(Characters.c2500_0021)
        EnableCharacter(Characters.c2550_0001)
        EnableCharacter(Characters.c2550_0002)
        EnableCharacter(Characters.c2792_0001)
        EnableObject(Objects.o0500_0008)
    EnableTreasure(obj=Objects.o0500_0008)
    DisableObject(Objects.o0500_0000)
    DisableCharacter(Characters.c2500_0000)
    DisableCharacter(Characters.c2500_0001)
    DisableCharacter(Characters.c2500_0002)
    DisableCharacter(Characters.c2500_0003)
    DisableCharacter(Characters.c2500_0005)
    DisableCharacter(Characters.c2500_0006)
    DisableCharacter(Characters.c2500_0007)
    DisableCharacter(Characters.c2500_0009)
    DisableCharacter(Characters.c2500_0010)
    DisableCharacter(Characters.c2500_0011)
    DisableCharacter(Characters.c2550_0000)


@ContinueOnRest(11810600)
def Event_11810600():
    """Event 11810600"""
    AND_1.Add(FlagEnabled(11815200))
    AND_2.Add(FlagEnabled(11815201))
    AND_3.Add(FlagEnabled(11815202))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(5, input_condition=AND_1)
    EnableFlag(11815100)
    DisableFlag(11815101)
    DisableFlag(11815102)
    DisableFlagRange((11815200, 11815202))
    Restart()
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_3)
    DisableFlag(11815100)
    DisableFlag(11815101)
    EnableFlag(11815102)
    DisableFlag(71810093)
    DisableFlagRange((11815200, 11815202))
    Restart()
    DisableFlag(11815100)
    EnableFlag(11815101)
    DisableFlag(11815102)
    DisableFlag(71810092)
    DisableFlagRange((11815200, 11815202))
    Restart()


@ContinueOnRest(11810641)
def Event_11810641(_, item_type: int, item: BaseItemParam | int, flag: Flag | int, flag_1: Flag | int):
    """Event 11810641"""
    MAIN.Await(AnyItemDroppedInRegion(region=1812200))
    
    AND_2.Add(ItemDropped(item=item, item_type=item_type))
    SkipLinesIfConditionTrue(2, AND_2)
    EnableFlag(11815201)
    Restart()
    if FlagDisabled(flag_1):
        EnableFlag(11815200)
        SetNextSnugglyTrade(flag=flag)
        Restart()
    EnableFlag(11815202)
    Restart()


@ContinueOnRest(11815110)
def Event_11815110(_, flag: Flag | int, item_lot: ItemLotParam | int, flag_1: Flag | int):
    """Event 11815110"""
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    WaitFrames(frames=1)
    SnugglyItemDrop(item_lot=item_lot, region=1812201, flag=flag, collision=Collisions.h0052B1)


@ContinueOnRest(11815150)
def Event_11815150():
    """Event 11815150"""
    MAIN.Await(TimeElapsed(seconds=1.0))
    
    EnableFlag(11815151)


@ContinueOnRest(11810050)
def Event_11810050():
    """Event 11810050"""
    AND_1.Add(PlayerCovenant(Covenant.DarkmoonBlade))
    if not AND_1:
        return
    EnableFlag(71510036)
    EnableFlag(71510037)


@ContinueOnRest(11810510)
def Event_11810510(_, character: Character | int, flag: Flag | int):
    """Event 11810510"""
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


@ContinueOnRest(11810520)
def Event_11810520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11810520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11810530)
def Event_11810530(_, character: Character | int):
    """Event 11810530"""
    AND_1.Add(FlagEnabled(1060))
    OR_2.Add(FlagEnabled(11810590))
    OR_2.Add(FlagEnabled(11810591))
    OR_2.Add(FlagEnabled(11810592))
    AND_1.Add(OR_2)
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1812121))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=1812990))
    AND_1.Add(OR_3)
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    Kill(character, award_souls=True)


@ContinueOnRest(11810531)
def Event_11810531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11810531"""
    AND_1.Add(FlagEnabled(1073))
    AND_1.Add(FlagEnabled(CommonFlags.TutorialComplete))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11810532)
def Event_11810532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11810532"""
    if ThisEventFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    AND_1.Add(FlagEnabled(1061))
    AND_1.Add(HealthRatio(character) <= 0.0)
    AND_1.Add(InsideMap(game_map=UNDEAD_ASYLUM))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@RestartOnRest(11815010)
def Event_11815010():
    """Event 11815010"""
    if ThisEventFlagEnabled():
        return
    AddSpecialEffect(Characters.c0000_0002, 5492)
    DisableHealthBar(Characters.c0000_0002)
    WaitFrames(frames=5)
    EnableHealthBar(Characters.c0000_0002)
