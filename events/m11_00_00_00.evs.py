"""
Painted World

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m11_00_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11100992()
    Event_11100998()
    Event_11100999()
    RegisterBonfire(bonfire_flag=11100992, obj=Objects.o0200_0000)
    RegisterLadder(start_climbing_flag=11100010, stop_climbing_flag=11100011, obj=Objects.o1510_0000)
    RegisterLadder(start_climbing_flag=11100014, stop_climbing_flag=11100015, obj=Objects.o1512_0000)
    RegisterLadder(start_climbing_flag=11100016, stop_climbing_flag=11100017, obj=Objects.o1513_0000)
    SkipLinesIfClient(1)
    DisableFlag(11100410)
    if FlagDisabled(11100810):
        DisableTreasure(obj=Objects.o0500_0015)
        DisableObject(Objects.o0500_0015)
    if FlagEnabled(11100810):
        EnableTreasure(obj=Objects.o0500_0015)
    Event_11100860(0, character=Characters.c0000_vel1, left=0, item_lot=0)
    Event_11100860(1, character=Characters.c2300_ttn1, left=0, item_lot=0)
    Event_11100860(2, character=Characters.c4180_prs1, left=0, item_lot=0)
    Event_11100090(1, obj=Objects.o1603_0000, vfx_id=VFX.CheckpointFog2, destination=1102602, destination_1=1102603)
    Event_11105070()
    Event_11105071()
    Event_11105072()
    Event_11105399()
    Event_11100030()
    Event_11100031()
    Event_11100136()
    Event_11100135()
    Event_11100120(0, obj_act_id=11100120, text=10010868, anchor_entity=Objects.o1580_0000)
    Event_11100710()
    Event_11100200()
    Event_11100600(0, obj=Objects.o0110_0000, obj_act_id=11100650)
    Event_11105150(0, character=Characters.c2500_0011)
    Event_11105150(1, character=Characters.c2500_0012)
    Event_11105150(2, character=Characters.c2500_0013)
    Event_11105160(0, character=Characters.c2500_0014, region=1102006)
    Event_11105160(1, character=Characters.c2500_0015, region=1102001)
    Event_11105170(0, character=Characters.c2500_0016, region=1102202, seconds=0.20000000298023224)
    Event_11105170(1, character=Characters.c2500_0017, region=1102202, seconds=0.0)
    Event_11105170(2, character=Characters.c2500_0018, region=1102202, seconds=0.4000000059604645)
    Event_11105170(3, character=Characters.c2500_0019, region=1102202, seconds=0.6000000238418579)
    Event_11105170(4, character=Characters.c2500_0020, region=1102007, seconds=0.30000001192092896)
    Event_11105170(5, character=Characters.c2500_0021, region=1102007, seconds=0.0)
    Event_11106299()
    Event_11106200(0, obj=Objects.o0150_00, other_entity=Objects.o0150_00, animation_id=12, left=-1)
    Event_11106200(1, obj=Objects.o0150_01, other_entity=Objects.o0150_01, animation_id=13, left=11006200)
    Event_11106200(2, obj=Objects.o0150_02, other_entity=Objects.o0150_00, animation_id=12, left=11006200)
    Event_11106200(3, obj=Objects.o0150_03, other_entity=Objects.o0150_03, animation_id=13, left=11006200)
    Event_11106200(4, obj=Objects.o0150_04, other_entity=Objects.o0150_05, animation_id=12, left=11006205)
    Event_11106200(5, obj=Objects.o0150_05, other_entity=Objects.o0150_05, animation_id=13, left=-1)
    Event_11106200(6, obj=Objects.o0150_06, other_entity=Objects.o0150_05, animation_id=12, left=11006205)
    Event_11106200(7, obj=Objects.o0150_07, other_entity=Objects.o0150_07, animation_id=13, left=-1)
    Event_11106200(8, obj=Objects.o0150_08, other_entity=Objects.o0150_08, animation_id=13, left=-1)
    Event_11106200(9, obj=Objects.o0150_09, other_entity=Objects.o0150_09, animation_id=12, left=-1)
    Event_11106200(13, obj=Objects.o0150_13, other_entity=Objects.o0150_13, animation_id=13, left=-1)
    Event_11106200(14, obj=Objects.o0150_14, other_entity=Objects.o0150_14, animation_id=12, left=-1)
    Event_11106200(18, obj=Objects.o0150_18, other_entity=Objects.o0150_18, animation_id=12, left=-1)
    Event_11106200(19, obj=Objects.o0150_19, other_entity=Objects.o0150_19, animation_id=13, left=-1)
    Event_11106200(24, obj=Objects.o0150_24, other_entity=Objects.o0150_24, animation_id=12, left=-1)
    Event_11106200(27, obj=Objects.o0150_27, other_entity=Objects.o0150_27, animation_id=12, left=-1)
    Event_11106200(28, obj=Objects.o0150_40, other_entity=Objects.o0150_40, animation_id=13, left=-1)
    Event_11106200(29, obj=Objects.o0150_41, other_entity=Objects.o0150_41, animation_id=12, left=-1)
    Event_11106200(30, obj=Objects.o0150_42, other_entity=Objects.o0150_42, animation_id=12, left=-1)
    Event_11106200(31, obj=Objects.o0150_43, other_entity=Objects.o0150_43, animation_id=13, left=-1)
    Event_11106200(32, obj=Objects.o0150_44, other_entity=Objects.o0150_44, animation_id=12, left=-1)
    Event_11106200(33, obj=Objects.o0150_45, other_entity=Objects.o0150_45, animation_id=12, left=-1)
    Event_11100070(0, obj=Objects.o1570_0000, obj_1=Objects.o0500_0100, animation_id=120, animation_id_1=121)
    Event_11100070(1, obj=Objects.o1571_0000, obj_1=Objects.o0500_0101, animation_id=125, animation_id_1=126)
    if FlagEnabled(11100400):
        DisableCharacter(Characters.c3420_0000)
    Event_11105370()
    Event_11100100(0, obj=Objects.o1560_0000, vfx_id=VFX.FireVFX05)
    Event_11100100(1, obj=Objects.o1560_0001, vfx_id=VFX.FireVFX06)
    Event_11100400()
    Event_11105371()
    DisableSoundEvent(sound_id=Sounds.CrossbreedPriscillaMusic)
    DisableObject(Objects.o1601_0000)
    DeleteVFX(VFX.BossExitFog, erase_root_only=False)
    if FlagEnabled(CommonFlags.CrossbreedPriscillaDead):
        Event_11105392()
        DisableObject(Objects.o1600_0000)
        DeleteVFX(VFX.BossEntranceFog, erase_root_only=False)
    else:
        Event_11105390()
        Event_11105391()
        Event_11105393()
        Event_11105392()
        Event_11100000()
        Event_11105394()
        Event_11105395()
        Event_11105396()
        Event_11105397()
        Event_11105398()
    Event_11105843(
        0,
        flag=CommonFlags.CrossbreedPriscillaDead,
        line_intersects=1101990,
        anchor_entity=1102998,
        target_entity=1102997,
    )
    Event_11105846(0, flag=CommonFlags.CrossbreedPriscillaDead, obj=Objects.o1600_0000, vfx_id=VFX.BossEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_11100420()
    HumanityRegistration(Characters.c0000_0005, event_flag=8964)
    Event_11105030()
    Event_11100810()
    Event_11105010()
    if FlagDisabled(1691):
        SetTeamType(Characters.c2730_0000, TeamType.Ally)
    Event_11100530(0, character=Characters.c2730_0000, first_flag=1690, last_flag=1693, flag=1691)
    Event_11100531(0, character=Characters.c2730_0000, first_flag=1690, last_flag=1693, flag=1692)
    HumanityRegistration(Characters.c0000_0003, event_flag=8470)
    HumanityRegistration(Characters.c0000_0004, event_flag=8900)
    DisableCharacter(Characters.c0000_0003)
    DisableCharacter(Characters.c0000_0004)
    Event_11100040()
    Event_11100532(
        0,
        character=Characters.c0000_0003,
        first_flag=1600,
        last_flag=1619,
        flag=1606,
        flag_1=1607,
        character_1=Characters.c0000_0004,
    )
    Event_11100533(0, character=Characters.c0000_0003, first_flag=1600, last_flag=1619, flag=1608)
    Event_11100534(0, character=Characters.c0000_0003, first_flag=1600, last_flag=1619, flag=1609)
    Event_11100535(0, character=Characters.c0000_0003, first_flag=1600, last_flag=1619, flag=1608, flag_1=1609)
    Event_11100300()


@ContinueOnRest(11100992)
def Event_11100992():
    """Event 11100992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c2730_0000, 7100)
    AddSpecialEffect(Characters.c0000_0005, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c2730_0000, 7100)
    RemoveSpecialEffect(Characters.c0000_0005, 7100)
    Restart()


@ContinueOnRest(11100998)
def Event_11100998():
    """Event 11100998"""
    if FlagDisabled(11102998):
        AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Objects.o1540_0000, radius=5.0))
        AND_1.Add(PlayerHasGood(116))
        AND_1.Add(FlagDisabled(1606))
        AND_1.Add(FlagDisabled(1607))
    
        MAIN.Await(AND_1)
    
        DisplayStatus(10010690)
        EnableFlag(11102998)
    AND_2.Add(OutsideMap(game_map=PAINTED_WORLD))
    DisableFlag(11102998)


@ContinueOnRest(11100999)
def Event_11100999():
    """Event 11100999"""
    AND_1.Add(FlagEnabled(11102999))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    AwardItemLot(63160, host_only=True)
    Wait(2.0)
    AwardItemLot(6310, host_only=True)
    Wait(2.0)
    AwardItemLot(6420, host_only=True)


@RestartOnRest(11100860)
def Event_11100860(_, character: Character | int, left: int, item_lot: int):
    """Event 11100860"""
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


@ContinueOnRest(11100090)
def Event_11100090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11100090"""
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


@RestartOnRest(11105070)
def Event_11105070():
    """Event 11105070"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2840_0011)
        DisableCharacter(Characters.c2840_0012)
        DisableCharacter(Characters.c2840_0013)
        DisableCharacter(Characters.c2840_0014)
        DisableCharacter(Characters.c2840_0015)
        DisableCharacter(Characters.c2840_0016)
        DisableCharacter(Characters.c2840_0017)
        DisableCharacter(Characters.c2930_0009)
        DisableCharacter(Characters.c2930_0010)
        DisableCharacter(Characters.c2930_0011)
        DisableCharacter(Characters.c2930_0012)
        DisableCharacter(Characters.c2930_0013)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(11105071)
def Event_11105071():
    """Event 11105071"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2840_0011)
    Kill(Characters.c2840_0012)
    Kill(Characters.c2840_0013)
    Kill(Characters.c2840_0014)
    Kill(Characters.c2840_0015)
    Kill(Characters.c2840_0016)
    Kill(Characters.c2840_0017)
    Kill(Characters.c2930_0009)
    Kill(Characters.c2930_0010)
    Kill(Characters.c2930_0011)
    Kill(Characters.c2930_0012)
    Kill(Characters.c2930_0013)


@RestartOnRest(11105072)
def Event_11105072():
    """Event 11105072"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=PAINTED_WORLD))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11100050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=PAINTED_WORLD))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11100050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=PAINTED_WORLD))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11100050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=PAINTED_WORLD))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11100050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=PAINTED_WORLD))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11100050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=PAINTED_WORLD))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11100050))
    if not OR_6:
        return RESTART
    EnableFlag(11100050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=PAINTED_WORLD))
    if not AND_7:
        return RESTART
    DisableFlag(11100050)
    EnableFlag(11105075)


@ContinueOnRest(11105390)
def Event_11105390():
    """Event 11105390"""
    AND_1.Add(FlagDisabled(CommonFlags.CrossbreedPriscillaDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1102998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1101990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1102997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11105391)
def Event_11105391():
    """Event 11105391"""
    AND_1.Add(FlagDisabled(CommonFlags.CrossbreedPriscillaDead))
    AND_1.Add(FlagEnabled(11105393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1102998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1101990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1102997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11105393)
def Event_11105393():
    """Event 11105393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.CrossbreedPriscillaDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1102996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c2730_0000)
    EnableFlag(11105393)
    
    MAIN.Await(FlagEnabled(CommonFlags.CrossbreedPriscillaDead))
    
    End()


@RestartOnRest(11105392)
def Event_11105392():
    """Event 11105392"""
    if FlagEnabled(CommonFlags.CrossbreedPriscillaDead):
        DisableCharacter(Characters.c2730_0000)
        DisableCharacter(Characters.c2731_0000)
        Kill(Characters.c2730_0000)
        Kill(Characters.c2731_0000)
        DisableBackread(Characters.c2730_0000)
        DisableBackread(Characters.c2731_0000)
        End()
    if FlagEnabled(1691):
        SetTeamType(Characters.c2730_0000, TeamType.Ally)
    DisableAI(Characters.c2730_0000)
    DisableHealthBar(Characters.c2730_0000)
    AND_1.Add(CharacterAlive(Characters.c2730_0000))
    AND_1.Add(FlagEnabled(11105393))
    AND_1.Add(Attacked(attacked_entity=Characters.c2730_0000, attacker=PLAYER))
    AND_2.Add(FlagEnabled(11105393))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1102100))
    AND_2.Add(FlagEnabled(1691))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.c2730_0000)
    SetTeamType(Characters.c2730_0000, TeamType.Boss)
    EnableBossHealthBar(Characters.c2730_0000, name=2730)
    EnableFlag(11105392)
    
    MAIN.Await(FlagEnabled(CommonFlags.CrossbreedPriscillaDead))
    
    End()


@ContinueOnRest(11100000)
def Event_11100000():
    """Event 11100000"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(Characters.c2730_0000))
    
    EnableFlag(CommonFlags.CrossbreedPriscillaDead)
    KillBoss(game_area_param_id=1100160)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=40)
    Kill(Characters.c2731_0000)
    DisableBackread(Characters.c2731_0000)
    DisableObject(Objects.o1600_0000)
    DeleteVFX(VFX.BossEntranceFog)


@ContinueOnRest(11105394)
def Event_11105394():
    """Event 11105394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.CrossbreedPriscillaDead))
    AND_1.Add(FlagEnabled(11105390))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1102996))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11105391))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.CrossbreedPriscillaMusic)
    EnableFlag(11105394)
    
    MAIN.Await(FlagEnabled(CommonFlags.CrossbreedPriscillaDead))
    
    End()


@ContinueOnRest(11105395)
def Event_11105395():
    """Event 11105395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.CrossbreedPriscillaDead))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1102100))
    AND_2.Add(FlagEnabled(11105380))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableSoundEvent(sound_id=Sounds.CrossbreedPriscillaMusic)
    EnableFlag(11105395)
    
    MAIN.Await(FlagEnabled(CommonFlags.CrossbreedPriscillaDead))
    
    End()


@RestartOnRest(11105396)
def Event_11105396():
    """Event 11105396"""
    DisableCharacter(Characters.c2731_0000)
    if FlagEnabled(CommonFlags.CrossbreedPriscillaDead):
        return
    if ThisEventFlagEnabled():
        SetDisplayMask(Characters.c2730_0000, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(Characters.c2730_0000, bit_index=1, switch_type=OnOffChange.Off)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(Characters.c2730_0000))
    
    CreateNPCPart(Characters.c2730_0000, npc_part_id=2730, part_index=NPCPartType.Part1, part_health=158)
    AND_1.Add(HealthRatio(Characters.c2730_0000) > 0.0)
    AND_1.Add(CharacterPartHealth(Characters.c2730_0000, npc_part_id=2730) <= 0)
    AND_1.Add(FlagDisabled(11105381))
    AND_1.Add(Attacked(attacked_entity=Characters.c2730_0000, attacker=PLAYER))
    AND_2.Add(HealthRatio(Characters.c2730_0000) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(Characters.c2730_0000)
    ForceAnimation(Characters.c2730_0000, 8000)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c2730_0000, tae_event_id=400))
    
    EnableCharacter(Characters.c2731_0000)
    SetDisplayMask(Characters.c2730_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c2730_0000, bit_index=1, switch_type=OnOffChange.Off)
    Move(
        Characters.c2731_0000,
        destination=Characters.c2730_0000,
        destination_type=CoordEntityType.Character,
        model_point=40,
        copy_draw_parent=Characters.c2730_0000,
    )
    ForceAnimation(Characters.c2731_0000, 8100)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    SkipLinesIfConditionFalse(1, OR_7)
    AwardItemLot(27310000, host_only=True)
    EnableFlag(11105396)
    
    MAIN.Await(FlagEnabled(CommonFlags.CrossbreedPriscillaDead))
    
    End()


@RestartOnRest(11105397)
def Event_11105397():
    """Event 11105397"""
    MAIN.Await(CharacterHasTAEEvent(Characters.c2730_0000, tae_event_id=600))
    
    DisableHealthBar(Characters.c2730_0000)
    DisableBossHealthBar(Characters.c2730_0000, name=2730)
    EnableFlag(11105381)
    DisableFlagRange((11105110, 11105119))
    SkipLinesIfClient(44)
    SetNetworkUpdateAuthority(Characters.c2730_0000, authority_level=UpdateAuthority.Forced)
    EnableRandomFlagInRange(flag_range=(11105110, 11105119))
    SkipLinesIfFlagDisabled(3, 11105110)
    AND_1.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102810))
    SkipLinesIfConditionTrue(2, AND_1)
    Move(Characters.c2730_0000, destination=1102810, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105111)
    AND_2.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102811))
    SkipLinesIfConditionTrue(2, AND_2)
    Move(Characters.c2730_0000, destination=1102811, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105112)
    AND_3.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102812))
    SkipLinesIfConditionTrue(2, AND_3)
    Move(Characters.c2730_0000, destination=1102812, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105113)
    AND_4.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102813))
    SkipLinesIfConditionTrue(2, AND_4)
    Move(Characters.c2730_0000, destination=1102813, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105114)
    AND_5.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102814))
    SkipLinesIfConditionTrue(2, AND_5)
    Move(Characters.c2730_0000, destination=1102814, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105115)
    AND_6.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102815))
    SkipLinesIfConditionTrue(2, AND_6)
    Move(Characters.c2730_0000, destination=1102815, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105116)
    AND_7.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102816))
    SkipLinesIfConditionTrue(2, AND_7)
    Move(Characters.c2730_0000, destination=1102816, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105117)
    OR_1.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102817))
    SkipLinesIfConditionTrue(2, OR_1)
    Move(Characters.c2730_0000, destination=1102817, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105118)
    OR_2.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102818))
    SkipLinesIfConditionTrue(2, OR_2)
    Move(Characters.c2730_0000, destination=1102818, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(3, 11105119)
    OR_3.Add(CharacterInsideRegion(Characters.c2730_0000, region=1102819))
    SkipLinesIfConditionTrue(2, OR_3)
    Move(Characters.c2730_0000, destination=1102819, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(Characters.c2730_0000, destination=1102810, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(Characters.c2730_0000, tae_event_id=600))
    
    Restart()


@RestartOnRest(11105398)
def Event_11105398():
    """Event 11105398"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c2730_0000, tae_event_id=700))
    
    EnableHealthBar(Characters.c2730_0000)
    EnableBossHealthBar(Characters.c2730_0000, name=2730)
    DisableFlag(11105381)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(Characters.c2730_0000, tae_event_id=700))
    
    Restart()


@ContinueOnRest(11105399)
def Event_11105399():
    """Event 11105399"""
    if Client():
        return
    DisableNetworkSync()
    
    MAIN.Await(InsideMap(game_map=ANOR_LONDO))
    
    MAIN.Await(InsideMap(game_map=PAINTED_WORLD))
    
    RestartEvent(event_id=11105390)
    RestartEvent(event_id=11105391)
    RestartEvent(event_id=11105392)
    RestartEvent(event_id=11105393)
    RestartEvent(event_id=11105394)
    RestartEvent(event_id=11105395)
    RestartEvent(event_id=11105396)
    RestartEvent(event_id=11105397)
    RestartEvent(event_id=11105398)
    DisableFlagRange((11105390, 11105399))
    Restart()


@RestartOnRest(11105150)
def Event_11105150(_, character: int):
    """Event 11105150"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableCharacterCollision(character)
    DisableAI(character)
    DisableGravity(character)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    EnableAI(character)


@RestartOnRest(11105160)
def Event_11105160(_, character: Character | int, region: Region | int):
    """Event 11105160"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableCharacterCollision(character)
    DisableAI(character)
    DisableGravity(character)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    EnableAI(character)


@RestartOnRest(11105170)
def Event_11105170(_, character: Character | int, region: Region | int, seconds: float):
    """Event 11105170"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableCharacterCollision(character)
    DisableAI(character)
    DisableGravity(character)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    Wait(seconds)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    EnableAI(character)


@RestartOnRest(11106200)
def Event_11106200(_, obj: int, other_entity: int, animation_id: int, left: Flag | int):
    """Event 11106200"""
    DisableNetworkSync()
    if ValueNotEqual(left=left, right=-1):
        OR_1.Add(FlagEnabled(left))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=7.0))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@RestartOnRest(11106299)
def Event_11106299():
    """Event 11106299"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1102000))
    
    Event_11106298(-1, obj=Objects.o0150_28, animation_id=13)
    Event_11106298(-1, obj=Objects.o0150_29, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_30, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_31, animation_id=13)
    Event_11106298(-1, obj=Objects.o0150_32, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_33, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_34, animation_id=13)
    Event_11106298(-1, obj=Objects.o0150_35, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_36, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_37, animation_id=13)
    Event_11106298(-1, obj=Objects.o0150_38, animation_id=12)
    Event_11106298(-1, obj=Objects.o0150_39, animation_id=12)


@EndOnRest(11106298)
def Event_11106298(_, obj: int, animation_id: int):
    """Event 11106298"""
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@ContinueOnRest(11100070)
def Event_11100070(_, obj: Object | int, obj_1: int, animation_id: int, animation_id_1: int):
    """Event 11100070"""
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


@RestartOnRest(11105370)
def Event_11105370():
    """Event 11105370"""
    if FlagEnabled(11100410):
        SetStandbyAnimationSettings(Characters.c3420_0000)
        End()
    AND_3.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_3)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1102070))
    AND_2.Add(not AND_3)
    AND_2.Add(Attacked(attacked_entity=Characters.c3420_0000, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableFlag(11100410)
    SetStandbyAnimationSettings(Characters.c3420_0000)
    ForceAnimation(Characters.c3420_0000, 9060)
    PlaySoundEffect(1102080, 110003420, sound_type=SoundType.a_Ambient)


@RestartOnRest(11105371)
def Event_11105371():
    """Event 11105371"""
    DisableCharacter(Characters.c3422_0000)
    if ThisEventFlagEnabled():
        MAIN.Await(CharacterBackreadEnabled(Characters.c3420_0000))
    
        SetDisplayMask(Characters.c3420_0000, bit_index=0, switch_type=OnOffChange.On)
        SetDisplayMask(Characters.c3420_0000, bit_index=1, switch_type=OnOffChange.On)
        End()
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c3420_0000, tae_event_id=400))
    
    SetDisplayMask(Characters.c3420_0000, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.c3420_0000, bit_index=1, switch_type=OnOffChange.On)
    Move(
        Characters.c3422_0000,
        destination=Characters.c3420_0000,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=Characters.c3420_0000,
    )
    EnableCharacter(Characters.c3422_0000)
    ForceAnimation(Characters.c3422_0000, 8100, wait_for_completion=True)
    DisableCharacter(Characters.c3422_0000)


@ContinueOnRest(11100100)
def Event_11100100(_, obj: int, vfx_id: VFXEvent | int):
    """Event 11100100"""
    if ThisEventSlotFlagEnabled():
        DestroyObject(obj)
        ForceAnimation(obj, 0)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    
    MAIN.Await(ObjectDestroyed(obj))
    
    DeleteVFX(vfx_id)


@RestartOnRest(11100400)
def Event_11100400():
    """Event 11100400"""
    EnableImmortality(Characters.c3421_0000)
    EnableInvincibility(Characters.c3421_0000)
    DisableHealthBar(Characters.c3421_0000)
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c3420_0000)
        End()
    SetBackreadStateAlternate(Characters.c3420_0000, True)
    DisableGravity(Characters.c3420_0000)
    
    MAIN.Await(CharacterDead(Characters.c3420_0000))
    
    EnableFlag(11100400)


@ContinueOnRest(11100030)
def Event_11100030():
    """Event 11100030"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=Objects.o1500_0000, animation_id=2)
        DisableNavmeshType(navmesh_id=Navigation.CrowDemonActivityPointB, navmesh_type=NavmeshType.Solid)
        End()
    EnableNavmeshType(navmesh_id=Navigation.CrowDemonActivityPointB, navmesh_type=NavmeshType.Solid)
    AND_1.Add(FlagDisabled(11100700))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1500_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1102090, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o1500_0000, 1, wait_for_completion=True)
    DisableNavmeshType(navmesh_id=Navigation.CrowDemonActivityPointB, navmesh_type=NavmeshType.Solid)


@ContinueOnRest(11100031)
def Event_11100031():
    """Event 11100031"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11100030))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1500_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=Objects.o1500_0000, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11100120)
def Event_11100120(_, obj_act_id: int, text: EventText | int, anchor_entity: int):
    """Event 11100120"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    if Client():
        return
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@ContinueOnRest(11100135)
def Event_11100135():
    """Event 11100135"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=Objects.o1540_0000, animation_id=1)
        EndOfAnimation(obj=Objects.o1520_0000, animation_id=1)
        DisableNavmeshType(navmesh_id=Navigation.Navmesh_EventNavmesh02, navmesh_type=NavmeshType.Solid)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010503,
        anchor_entity=Objects.o1550_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    DisableObject(Objects.o0150_07)
    DisableObject(Objects.o0150_08)
    DisableObject(Objects.o0150_09)
    Move(
        PLAYER,
        destination=Objects.o1550_0000,
        destination_type=CoordEntityType.Object,
        model_point=191,
        short_move=True,
    )
    ForceAnimation(PLAYER, 8010)
    ForceAnimation(Objects.o1550_0000, 1, wait_for_completion=True)
    SkipLinesIfSingleplayer(2)
    PlayCutscene(110000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(1)
    PlayCutscene(110000, cutscene_flags=0, player_id=10000)
    ForceAnimation(Objects.o1540_0000, 1)
    ForceAnimation(Objects.o1520_0000, 1)
    DisableNavmeshType(navmesh_id=Navigation.Navmesh_EventNavmesh02, navmesh_type=NavmeshType.Solid)


@ContinueOnRest(11100136)
def Event_11100136():
    """Event 11100136"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11100135))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1520_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160, anchor_entity=Objects.o1520_0000, button_type=ButtonType.Yes_or_No)
    Restart()


@RestartOnRest(11100420)
def Event_11100420():
    """Event 11100420"""
    if ThisEventFlagEnabled():
        Move(Characters.c2570_0000, destination=1102201, destination_type=CoordEntityType.Region, short_move=True)
        SetNest(Characters.c2570_0000, region=1102201)
        End()
    DisableAI(Characters.c2570_0000)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1102200))
    OR_1.Add(Attacked(attacked_entity=Characters.c2570_0000, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c2500_0016, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c2500_0017, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c2500_0018, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=Characters.c2500_0019, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(Characters.c2570_0000, 500)
    EnableAI(Characters.c2570_0000)
    SetNest(Characters.c2570_0000, region=1102201)


@ContinueOnRest(11100710)
def Event_11100710():
    """Event 11100710"""
    DisableFlag(11105380)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1691))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1102500))
    
    MAIN.Await(AND_1)
    
    EnableImmortality(Characters.c2730_0000)
    if Client():
        return
    DisableImmortality(Characters.c2730_0000)
    EnableFlag(11105380)
    if FlagDisabled(CommonFlags.CrossbreedPriscillaDead):
        MAIN.Await(FlagEnabled(11105395))
    if FlagEnabled(CommonFlags.DarkAnorLondo):
        SetMapDrawParamSlot(map_area_id=15, draw_param_slot=2)
    PlayCutscene(110035, cutscene_flags=0, player_id=10000, move_to_region=1512500, game_map=ANOR_LONDO)
    WaitFrames(frames=1)
    if ThisEventFlagDisabled():
        AwardItemLot(9030, host_only=True)
    SetRespawnPoint(respawn_point=1512960)
    SaveRequest()
    Restart()


@RestartOnRest(11105010)
def Event_11105010():
    """Event 11105010"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterAlive(Characters.c2830_0000))
    AND_1.Add(CharacterAlive(Characters.c2830_0001))
    AND_1.Add(CharacterAlive(Characters.c2830_0002))
    AND_1.Add(CharacterAlive(Characters.c2830_0003))
    AND_1.Add(CharacterAlive(Characters.c2830_0004))
    AND_1.Add(CharacterAlive(Characters.c2830_0005))
    AND_1.Add(CharacterAlive(Characters.c2830_0006))
    AND_1.Add(CharacterAlive(Characters.c2830_0007))
    AND_1.Add(CharacterAlive(Characters.c2830_0008))
    AND_1.Add(CharacterAlive(Characters.c2830_0009))
    AND_1.Add(CharacterAlive(Characters.c2830_0010))
    AND_1.Add(CharacterAlive(Characters.c2830_0011))
    AND_1.Add(CharacterAlive(Characters.c2830_0012))
    AND_1.Add(CharacterAlive(Characters.c2830_0013))
    if not AND_1:
        return
    DisableCharacterCollision(Characters.c2830_0000)
    DisableCharacterCollision(Characters.c2830_0001)
    DisableCharacterCollision(Characters.c2830_0002)
    DisableCharacterCollision(Characters.c2830_0003)
    DisableCharacterCollision(Characters.c2830_0004)
    DisableCharacterCollision(Characters.c2830_0005)
    DisableCharacterCollision(Characters.c2830_0006)
    DisableCharacterCollision(Characters.c2830_0007)
    DisableCharacterCollision(Characters.c2830_0008)
    DisableCharacterCollision(Characters.c2830_0009)
    DisableCharacterCollision(Characters.c2830_0010)
    DisableCharacterCollision(Characters.c2830_0011)
    DisableCharacterCollision(Characters.c2830_0012)
    DisableCharacterCollision(Characters.c2830_0013)
    DisableAnimations(Characters.c2830_0000)
    DisableAnimations(Characters.c2830_0001)
    DisableAnimations(Characters.c2830_0002)
    DisableAnimations(Characters.c2830_0003)
    DisableAnimations(Characters.c2830_0004)
    DisableAnimations(Characters.c2830_0005)
    DisableAnimations(Characters.c2830_0006)
    DisableAnimations(Characters.c2830_0007)
    DisableAnimations(Characters.c2830_0008)
    DisableAnimations(Characters.c2830_0009)
    DisableAnimations(Characters.c2830_0010)
    DisableAnimations(Characters.c2830_0011)
    DisableAnimations(Characters.c2830_0012)
    DisableAnimations(Characters.c2830_0013)
    DisableGravity(Characters.c2830_0000)
    DisableGravity(Characters.c2830_0001)
    DisableGravity(Characters.c2830_0002)
    DisableGravity(Characters.c2830_0003)
    DisableGravity(Characters.c2830_0004)
    DisableGravity(Characters.c2830_0005)
    DisableGravity(Characters.c2830_0006)
    DisableGravity(Characters.c2830_0007)
    DisableGravity(Characters.c2830_0008)
    DisableGravity(Characters.c2830_0009)
    DisableGravity(Characters.c2830_0010)
    DisableGravity(Characters.c2830_0011)
    DisableGravity(Characters.c2830_0012)
    DisableGravity(Characters.c2830_0013)
    DisableAI(Characters.c2830_0000)
    DisableAI(Characters.c2830_0001)
    DisableAI(Characters.c2830_0002)
    DisableAI(Characters.c2830_0003)
    DisableAI(Characters.c2830_0004)
    DisableAI(Characters.c2830_0005)
    DisableAI(Characters.c2830_0006)
    DisableAI(Characters.c2830_0007)
    DisableAI(Characters.c2830_0008)
    DisableAI(Characters.c2830_0009)
    DisableAI(Characters.c2830_0010)
    DisableAI(Characters.c2830_0011)
    DisableAI(Characters.c2830_0012)
    DisableAI(Characters.c2830_0013)
    SetStandbyAnimationSettings(Characters.c2830_0000, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0001, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0002, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0003, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0004, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0005, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0006, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0007, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0008, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0009, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0010, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0011, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0012, standby_animation=9000)
    SetStandbyAnimationSettings(Characters.c2830_0013, standby_animation=9000)
    Move(Characters.c2830_0000, destination=1102830, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0001, destination=1102831, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0002, destination=1102832, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0003, destination=1102833, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0004, destination=1102834, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0005, destination=1102835, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0006, destination=1102836, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0007, destination=1102837, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0008, destination=1102838, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0009, destination=1102839, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0010, destination=1102840, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0011, destination=1102841, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0012, destination=1102842, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.c2830_0013, destination=1102843, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1102300))
    
    EnableAI(Characters.c2830_0000)
    EnableAI(Characters.c2830_0001)
    EnableAI(Characters.c2830_0002)
    EnableAI(Characters.c2830_0003)
    EnableAI(Characters.c2830_0004)
    EnableAI(Characters.c2830_0005)
    EnableAI(Characters.c2830_0006)
    EnableAI(Characters.c2830_0007)
    EnableAI(Characters.c2830_0008)
    EnableAI(Characters.c2830_0009)
    EnableAI(Characters.c2830_0010)
    EnableAI(Characters.c2830_0011)
    EnableAI(Characters.c2830_0012)
    EnableAI(Characters.c2830_0013)
    SetStandbyAnimationSettings(Characters.c2830_0000)
    SetStandbyAnimationSettings(Characters.c2830_0001)
    SetStandbyAnimationSettings(Characters.c2830_0002)
    SetStandbyAnimationSettings(Characters.c2830_0003)
    SetStandbyAnimationSettings(Characters.c2830_0004)
    SetStandbyAnimationSettings(Characters.c2830_0005)
    SetStandbyAnimationSettings(Characters.c2830_0006)
    SetStandbyAnimationSettings(Characters.c2830_0007)
    SetStandbyAnimationSettings(Characters.c2830_0008)
    SetStandbyAnimationSettings(Characters.c2830_0009)
    SetStandbyAnimationSettings(Characters.c2830_0010)
    SetStandbyAnimationSettings(Characters.c2830_0011)
    SetStandbyAnimationSettings(Characters.c2830_0012)
    SetStandbyAnimationSettings(Characters.c2830_0013)
    EnableGravity(Characters.c2830_0000)
    EnableGravity(Characters.c2830_0001)
    EnableGravity(Characters.c2830_0002)
    EnableGravity(Characters.c2830_0003)
    EnableGravity(Characters.c2830_0004)
    EnableGravity(Characters.c2830_0005)
    EnableGravity(Characters.c2830_0006)
    EnableGravity(Characters.c2830_0007)
    EnableGravity(Characters.c2830_0008)
    EnableGravity(Characters.c2830_0009)
    EnableGravity(Characters.c2830_0010)
    EnableGravity(Characters.c2830_0011)
    EnableGravity(Characters.c2830_0012)
    EnableGravity(Characters.c2830_0013)
    EnableAnimations(Characters.c2830_0000)
    EnableAnimations(Characters.c2830_0001)
    EnableAnimations(Characters.c2830_0002)
    EnableAnimations(Characters.c2830_0003)
    EnableAnimations(Characters.c2830_0004)
    EnableAnimations(Characters.c2830_0005)
    EnableAnimations(Characters.c2830_0006)
    EnableAnimations(Characters.c2830_0007)
    EnableAnimations(Characters.c2830_0008)
    EnableAnimations(Characters.c2830_0009)
    EnableAnimations(Characters.c2830_0010)
    EnableAnimations(Characters.c2830_0011)
    EnableAnimations(Characters.c2830_0012)
    EnableAnimations(Characters.c2830_0013)
    EnableCharacterCollision(Characters.c2830_0000)
    EnableCharacterCollision(Characters.c2830_0001)
    EnableCharacterCollision(Characters.c2830_0002)
    EnableCharacterCollision(Characters.c2830_0003)
    EnableCharacterCollision(Characters.c2830_0004)
    EnableCharacterCollision(Characters.c2830_0005)
    EnableCharacterCollision(Characters.c2830_0006)
    EnableCharacterCollision(Characters.c2830_0007)
    EnableCharacterCollision(Characters.c2830_0008)
    EnableCharacterCollision(Characters.c2830_0009)
    EnableCharacterCollision(Characters.c2830_0010)
    EnableCharacterCollision(Characters.c2830_0011)
    EnableCharacterCollision(Characters.c2830_0012)
    EnableCharacterCollision(Characters.c2830_0013)


@RestartOnRest(11100200)
def Event_11100200():
    """Event 11100200"""
    Event_11105190(
        0,
        character=Characters.c2310_0000,
        animation_id=3010,
        animation_id_1=3011,
        flag=11105230,
        flag_1=11105232,
    )
    Event_11105190(
        1,
        character=Characters.c2310_0001,
        animation_id=3012,
        animation_id_1=3013,
        flag=11105234,
        flag_1=11105236,
    )
    Event_11105195(0, character=Characters.c2310_0002, flag=11105240)
    Event_11105195(1, character=Characters.c2310_0003, flag=11105244)
    Event_11105200(
        0,
        flag=11105190,
        flag_1=11105210,
        event_slot=0,
        event_id=11105250,
        flag_2=11105230,
        flag_3=11105231,
        flag_4=11105232,
        flag_5=11105233,
    )
    Event_11105200(
        1,
        flag=11105191,
        flag_1=11105211,
        event_slot=1,
        event_id=11105260,
        flag_2=11105234,
        flag_3=11105235,
        flag_4=11105236,
        flag_5=11105237,
    )
    Event_11105200(
        2,
        flag=11105195,
        flag_1=11105212,
        event_slot=2,
        event_id=11105270,
        flag_2=11105238,
        flag_3=11105239,
        flag_4=11105240,
        flag_5=11105241,
    )
    Event_11105200(
        3,
        flag=11105196,
        flag_1=11105213,
        event_slot=3,
        event_id=11105280,
        flag_2=11105242,
        flag_3=11105243,
        flag_4=11105244,
        flag_5=11105245,
    )
    Event_11105220(0, character=Characters.c2310_0000, flag=11105210, seconds=10.0, event_id=11105250)
    Event_11105220(1, character=Characters.c2310_0001, flag=11105211, seconds=10.0, event_id=11105260)
    Event_11105220(2, character=Characters.c2310_0002, flag=11105212, seconds=10.0, event_id=11105270)
    Event_11105220(3, character=Characters.c2310_0003, flag=11105213, seconds=10.0, event_id=11105280)
    Event_11105250(
        0,
        flag=11105210,
        character=Characters.c2310_0000,
        command_id=1,
        region=1102040,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105232,
    )
    Event_11105250(
        1,
        flag=11105210,
        character=Characters.c2310_0000,
        command_id=2,
        region=1102020,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105230,
    )
    Event_11105250(
        2,
        flag=11105210,
        character=Characters.c2310_0000,
        command_id=3,
        region=1102030,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105231,
    )
    Event_11105250(
        3,
        flag=11105210,
        character=Characters.c2310_0000,
        command_id=4,
        region=1102020,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105230,
    )
    Event_11105250(
        4,
        flag=11105210,
        character=Characters.c2310_0000,
        command_id=5,
        region=1102050,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105233,
    )
    Event_11105250(
        5,
        flag=11105210,
        character=Characters.c2310_0000,
        command_id=6,
        region=1102040,
        first_flag=11105230,
        last_flag=11105233,
        flag_1=11105232,
    )
    Event_11105260(
        0,
        flag=11105211,
        character=Characters.c2310_0001,
        command_id=1,
        region=1102040,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105236,
    )
    Event_11105260(
        1,
        flag=11105211,
        character=Characters.c2310_0001,
        command_id=2,
        region=1102020,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105234,
    )
    Event_11105260(
        2,
        flag=11105211,
        character=Characters.c2310_0001,
        command_id=3,
        region=1102030,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105235,
    )
    Event_11105260(
        3,
        flag=11105211,
        character=Characters.c2310_0001,
        command_id=4,
        region=1102020,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105234,
    )
    Event_11105260(
        4,
        flag=11105211,
        character=Characters.c2310_0001,
        command_id=5,
        region=1102050,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105237,
    )
    Event_11105260(
        5,
        flag=11105211,
        character=Characters.c2310_0001,
        command_id=6,
        region=1102040,
        first_flag=11105234,
        last_flag=11105237,
        flag_1=11105236,
    )
    Event_11105270(
        0,
        flag=11105212,
        character=Characters.c2310_0002,
        command_id=1,
        region=1102040,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105240,
    )
    Event_11105270(
        1,
        flag=11105212,
        character=Characters.c2310_0002,
        command_id=2,
        region=1102020,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105238,
    )
    Event_11105270(
        2,
        flag=11105212,
        character=Characters.c2310_0002,
        command_id=3,
        region=1102030,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105239,
    )
    Event_11105270(
        3,
        flag=11105212,
        character=Characters.c2310_0002,
        command_id=4,
        region=1102020,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105238,
    )
    Event_11105270(
        4,
        flag=11105212,
        character=Characters.c2310_0002,
        command_id=5,
        region=1102050,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105241,
    )
    Event_11105270(
        5,
        flag=11105212,
        character=Characters.c2310_0002,
        command_id=6,
        region=1102040,
        first_flag=11105238,
        last_flag=11105241,
        flag_1=11105240,
    )
    Event_11105280(
        0,
        flag=11105213,
        character=Characters.c2310_0003,
        command_id=1,
        region=1102040,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105244,
    )
    Event_11105280(
        1,
        flag=11105213,
        character=Characters.c2310_0003,
        command_id=2,
        region=1102020,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105242,
    )
    Event_11105280(
        2,
        flag=11105213,
        character=Characters.c2310_0003,
        command_id=3,
        region=1102030,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105243,
    )
    Event_11105280(
        3,
        flag=11105213,
        character=Characters.c2310_0003,
        command_id=4,
        region=1102020,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105242,
    )
    Event_11105280(
        4,
        flag=11105213,
        character=Characters.c2310_0003,
        command_id=5,
        region=1102050,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105245,
    )
    Event_11105280(
        5,
        flag=11105213,
        character=Characters.c2310_0003,
        command_id=6,
        region=1102040,
        first_flag=11105242,
        last_flag=11105245,
        flag_1=11105244,
    )


@EndOnRest(11105190)
def Event_11105190(_, character: int, animation_id: int, animation_id_1: int, flag: Flag | int, flag_1: Flag | int):
    """Event 11105190"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableCharacterCollision(character)
    DisableGravity(character)
    AddSpecialEffect(character, 4160)
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(51100260))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202021))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1102040))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableCharacterCollision(character)
    EnableGravity(character)
    SetStandbyAnimationSettings(character)
    SkipLinesIfFinishedConditionFalse(5, input_condition=AND_1)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    RemoveSpecialEffect(character, 4160)
    SetNest(character, region=1102020)
    EnableFlag(flag)
    Restart()
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    RemoveSpecialEffect(character, 4160)
    SetNest(character, region=1102040)
    EnableFlag(flag_1)
    Restart()


@EndOnRest(11105195)
def Event_11105195(_, character: int, flag: Flag | int):
    """Event 11105195"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(flag)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1102050))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 3006)


@EndOnRest(11105200)
def Event_11105200(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    event_slot: int,
    event_id: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 11105200"""
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1102020))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=1102030))
    AND_3.Add(FlagDisabled(flag_4))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=1102040))
    AND_4.Add(FlagDisabled(flag_5))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=1102050))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag_1)
    RestartEvent(event_id=11105220, event_slot=event_slot)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    if FlagEnabled(flag_3):
        RestartEvent(event_id=event_id, event_slot=3)
    if FlagEnabled(flag_4):
        RestartEvent(event_id=event_id, event_slot=1)
    if FlagEnabled(flag_5):
        RestartEvent(event_id=event_id, event_slot=5)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    if FlagEnabled(flag_2):
        RestartEvent(event_id=event_id, event_slot=2)
    if FlagEnabled(flag_4):
        RestartEvent(event_id=event_id, event_slot=1)
    if FlagEnabled(flag_5):
        RestartEvent(event_id=event_id, event_slot=5)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_3)
    if FlagEnabled(flag_2):
        RestartEvent(event_id=event_id)
    if FlagEnabled(flag_3):
        RestartEvent(event_id=event_id, event_slot=3)
    if FlagEnabled(flag_5):
        RestartEvent(event_id=event_id, event_slot=5)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_4)
    if FlagEnabled(flag_2):
        RestartEvent(event_id=event_id)
    if FlagEnabled(flag_3):
        RestartEvent(event_id=event_id, event_slot=3)
    if FlagEnabled(flag_4):
        RestartEvent(event_id=event_id, event_slot=4)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()


@EndOnRest(11105220)
def Event_11105220(_, character: Character | int, flag: Flag | int, seconds: float, event_id: int):
    """Event 11105220"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(seconds)
    if FlagDisabled(flag):
        return RESTART
    DisableFlag(flag)
    RestartEvent(event_id=event_id)
    RestartEvent(event_id=event_id, event_slot=1)
    RestartEvent(event_id=event_id, event_slot=2)
    RestartEvent(event_id=event_id, event_slot=3)
    RestartEvent(event_id=event_id, event_slot=4)
    RestartEvent(event_id=event_id, event_slot=5)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@EndOnRest(11105250)
def Event_11105250(
    _,
    flag: Flag | int,
    character: int,
    command_id: int,
    region: Region | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
):
    """Event 11105250"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterDead(character))
    
        End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@EndOnRest(11105260)
def Event_11105260(
    _,
    flag: Flag | int,
    character: int,
    command_id: int,
    region: Region | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
):
    """Event 11105260"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterDead(character))
    
        End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@EndOnRest(11105270)
def Event_11105270(
    _,
    flag: Flag | int,
    character: int,
    command_id: int,
    region: Region | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
):
    """Event 11105270"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterDead(character))
    
        End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@EndOnRest(11105280)
def Event_11105280(
    _,
    flag: Flag | int,
    character: int,
    command_id: int,
    region: Region | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
):
    """Event 11105280"""
    if FlagDisabled(flag):
        MAIN.Await(CharacterDead(character))
    
        End()
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    SetNest(character, region=region)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@ContinueOnRest(11100600)
def Event_11100600(_, obj: Object | int, obj_act_id: int):
    """Event 11100600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11100510)
def Event_11100510(_, character: Character | int, flag: Flag | int):
    """Event 11100510"""
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


@ContinueOnRest(11100520)
def Event_11100520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11100520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11100530)
def Event_11100530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11100530"""
    AND_1.Add(FlagEnabled(1690))
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(HealthRatio(character) > 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11100531)
def Event_11100531(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11100531"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11100040)
def Event_11100040():
    """Event 11100040"""
    DisableNetworkSync()
    Wait(1.0)
    if FlagEnabled(11100700):
        return
    RegisterLadder(start_climbing_flag=11100012, stop_climbing_flag=11100013, obj=Objects.o1511_0000)


@ContinueOnRest(11100532)
def Event_11100532(
    _,
    character: Character | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    flag_1: Flag | int,
    character_1: Character | int,
):
    """Event 11100532"""
    DisableMapPiece(map_piece_id=MapPieces.m2230B0)
    DisableMapCollision(collision=Collisions.h0148B0_0000)
    DisableObject(Objects.o1604_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(11100700))
    
    DisableFlagRange((first_flag, last_flag))
    if FlagEnabled(8111):
        EnableFlag(flag)
    else:
        EnableFlag(flag_1)
    EnableMapPiece(map_piece_id=MapPieces.m2230B0)
    EnableMapCollision(collision=Collisions.h0148B0_0000)
    DisableObject(Objects.o1511_0000)
    EnableObject(Objects.o1604_0000)
    CreateVFX(VFX.MultiplayerFog1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    SetTeamType(character_1, TeamType.WhitePhantom)
    DisableCharacter(Characters.c2830_0000)
    DisableCharacter(Characters.c2830_0001)
    DisableCharacter(Characters.c2830_0002)
    DisableCharacter(Characters.c2830_0003)
    DisableCharacter(Characters.c2830_0004)
    DisableCharacter(Characters.c2830_0005)
    DisableCharacter(Characters.c2830_0006)
    DisableCharacter(Characters.c2830_0007)
    DisableCharacter(Characters.c2830_0008)
    DisableCharacter(Characters.c2830_0009)
    DisableCharacter(Characters.c2830_0010)
    DisableCharacter(Characters.c2830_0011)
    DisableCharacter(Characters.c2830_0012)
    DisableCharacter(Characters.c2830_0013)
    DisableCharacter(Characters.c2500_0022)
    DisableCharacter(Characters.c2500_0023)
    DisableCharacter(Characters.c2500_0024)
    DisableCharacter(Characters.c2500_0025)
    DisableCharacter(Characters.c2500_0026)
    DisableCharacter(Characters.c2500_hlw2)
    DisableCharacter(Characters.c2500_hlw3)
    DisableCharacter(Characters.c0000_vel1)


@ContinueOnRest(11100533)
def Event_11100533(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11100533"""
    AND_1.Add(FlagEnabled(1606))
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(8110)


@ContinueOnRest(11100534)
def Event_11100534(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11100534"""
    AND_1.Add(FlagEnabled(1607))
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(8110)


@ContinueOnRest(11100535)
def Event_11100535(
    _,
    character: Character | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    flag_1: Flag | int,
):
    """Event 11100535"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagDisabled(11100700))
    AND_1.Add(FlagEnabled(8110))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11102999)
    RemoveGoodFromPlayer(item=116)
    EnableFlag(11100300)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    if FlagEnabled(8111):
        EnableFlag(flag)
    else:
        EnableFlag(flag_1)
    DisableFlagRange((1760, 1769))
    EnableFlag(1764)


@ContinueOnRest(11100300)
def Event_11100300():
    """Event 11100300"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(ThisEventFlagEnabled())
    
    if FlagEnabled(11400400):
        AwardItemLot(2800, host_only=False)
    if FlagEnabled(11400401):
        AwardItemLot(2810, host_only=False)
    if FlagEnabled(11400402):
        AwardItemLot(2820, host_only=False)


@ContinueOnRest(11105030)
def Event_11105030():
    """Event 11105030"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(11105031):
        return
    if FlagEnabled(CommonFlags.CrossbreedPriscillaDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(11100810))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1102011))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=Characters.c0000_0005,
        region=1102010,
        summon_flag=11105031,
        dismissal_flag=11105032,
    )
    Wait(20.0)
    Restart()


@ContinueOnRest(11100810)
def Event_11100810():
    """Event 11100810"""
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(11105031))
    AND_1.Add(FlagDisabled(11105032))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(Characters.c0000_0005)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(Characters.c0000_0005))
    
    EnableFlag(11100810)


@ContinueOnRest(11105843)
def Event_11105843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11105843"""
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


@ContinueOnRest(11105846)
def Event_11105846(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11105846"""
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
