"""
Depths

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *
from ..enums.m10_00_00_00_enums import *
from ..enums.common_enums import CommonFlags


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_11000992()
    Event_11000993()
    Event_11000994()
    Event_11000998()
    Event_11000999(0, chr=1000999)
    Event_11000999(1, chr=1000998)
    Event_11000999(2, chr=1000997)
    Event_11000999(3, chr=1000996)
    Event_11000999(4, chr=1000995)
    RegisterBonfire(bonfire_flag=Flags.Bonfire1BaseFlag, obj=Objects.o0200_0000)
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, obj=Objects.o1205)
    RegisterStatue(obj=Objects.o0100_0000, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0001, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0002, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0003, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0004, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0005, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0006, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(obj=Objects.o0100_0007, game_map=DEPTHS, statue_type=StatueType.Stone)
    SkipLinesIfClient(5)
    DisableFlag(Flags.GapingDragonIntroCutsceneDone)
    DisableObject(Objects.o1401_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    DisableObject(Objects.o1402_0000)
    DeleteVFX(VFX.MultiplayerFog2, erase_root_only=False)
    if FlagEnabled(Flags.ShortcutDoorOpened):
        EndOfAnimation(obj=Objects.o1319_0000, animation_id=0)
    Event_11000090(0, obj=Objects.o1420_0000, vfx_id=VFX.CheckpointFog1, destination=1002600, destination_1=1002601)
    Event_11005080()
    Event_11005081()
    Event_11005082()
    Event_11000100()
    Event_11000101()
    Event_11000120(0, obj_act_id=11000120, text=10010877, anchor_entity=Objects.o1315_0000, text_1=10010883, item=2018)
    Event_11000200()
    Event_11000800()
    Event_11005050()
    Event_11005060()
    Event_11005070()
    Event_11000110()
    Event_11000111()
    Event_11000600(0, obj=Objects.o0110_0000, obj_act_id=11000600)
    DisableSoundEvent(sound_id=Sounds.GapingDragonMusic)
    if FlagEnabled(CommonFlags.GapingDragonDead):
        Event_11005392()
        DisableObject(Objects.o1400_0000)
        DeleteVFX(VFX.BossEntranceFog, erase_root_only=False)
    else:
        Event_11005390()
        Event_11005391()
        Event_11005393()
        Event_11005392()
        Event_11000001()
        Event_11005394()
        Event_11005395()
        Event_11005396()
        Event_11005397()
        Event_11005398()
    Event_11005000(0, other_entity=Objects.o1340_0000, obj=Objects.o1340_0000, animation_id=1)
    Event_11005000(1, other_entity=Objects.o1340_0001, obj=Objects.o1340_0001, animation_id=1)
    Event_11005000(2, other_entity=Objects.o1340_0002, obj=Objects.o1340_0002, animation_id=3)
    Event_11005200(0, character=Characters.c2500_0003, region=1002020)
    Event_11005200(1, character=Characters.c2500_0004, region=1002020)
    Event_11005200(2, character=Characters.c2500_0005, region=1002020)
    Event_11005200(3, character=Characters.c2500_0006, region=1002020)
    Event_11005200(4, character=Characters.c2500_0007, region=1002020)
    Event_11005200(5, character=Characters.c2500_0008, region=1002020)
    Event_11005200(6, character=Characters.c3340_0002, region=1002021)
    Event_11005200(7, character=Characters.c3340_0000, region=1002021)
    Event_11005200(8, character=Characters.c3340_0001, region=1002022)
    Event_11005200(9, character=Characters.c3340_0003, region=1002022)
    Event_11005200(10, character=Characters.c2500_0009, region=1002022)
    Event_11005100(0, region=1002100, character=Characters.c3200_0000, seconds=0.0)
    Event_11005100(1, region=1002101, character=Characters.c3200_0001, seconds=0.0)
    Event_11005100(2, region=1002102, character=Characters.c3200_0002, seconds=0.0)
    Event_11005100(3, region=1002102, character=Characters.c3200_0003, seconds=0.6000000238418579)
    Event_11005100(4, region=1002103, character=Characters.c3200_0004, seconds=0.0)
    Event_11005100(5, region=1002103, character=Characters.c3200_0005, seconds=0.20000000298023224)
    Event_11005100(6, region=1002103, character=Characters.c3200_0006, seconds=0.8999999761581421)
    Event_11005100(7, region=1002107, character=Characters.c3200_0007, seconds=0.0)
    Event_11005150(0, character=Characters.c1201_0000, obj=Objects.o1322_0002, flag=11009000, flag_1=11009010)
    Event_11005150(1, character=Characters.c1201_0001, obj=Objects.o1322_0005, flag=11009001, flag_1=11009011)
    Event_11005150(2, character=Characters.c1201_0002, obj=Objects.o1322_0006, flag=11009002, flag_1=11009012)
    Event_11000850(0, character=Characters.c3340_0002)
    Event_11000850(1, character=Characters.c2660_0000)
    Event_11000850(2, character=Characters.c2660_0001)
    Event_11000850(3, character=Characters.c2370_0000)
    Event_11000850(4, character=Characters.c2370_chn1)
    Event_11000850(5, character=Characters.c0000_ano1)
    Event_11005843(
        0,
        flag=CommonFlags.GapingDragonDead,
        line_intersects=1001990,
        anchor_entity=1002998,
        target_entity=1002997,
    )
    Event_11005844(0, flag=CommonFlags.GapingDragonDead, obj=Objects.o1400_0000, vfx_id=VFX.BossEntranceFog)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(Characters.c0000_0005, event_flag=CommonFlags.SolaireHumanityFlag)
    HumanityRegistration(Characters.c0000_0007, event_flag=CommonFlags.LautrecHumanityFlag)
    HumanityRegistration(Characters.c0000_0006, event_flag=CommonFlags.KirkHumanityFlag)
    Event_11005030()
    Event_11005029()
    Event_11005031()
    Event_11005033()
    Event_11005036()
    Event_11005034()
    Event_11005039()
    Event_11000810()
    Event_11005333()
    Event_11005990(0, flag=Flags.SolaireSummoned, summoned_character=Characters.c0000_0005)
    Event_11005990(1, flag=Flags.LautrecSummoned, summoned_character=Characters.c0000_0007)
    HumanityRegistration(Characters.c0000_0002, event_flag=CommonFlags.LaurentiusHumanityFlag)
    SkipLinesIfClient(1)
    DisableFlag(Flags.LaurentiusFreedFromPot)
    SkipLinesIfFlagEnabled(3, Flags.LaurentiusFreedFromPot)
    SkipLinesIfFlagEnabled(2, 1250)
    SkipLinesIfFlagEnabled(1, 1253)
    DisableCharacter(Characters.c0000_0002)
    if FlagEnabled(1250):
        DisableGravity(Characters.c0000_0002)
        DisableCharacterCollision(Characters.c0000_0002)
    Event_11000530(0, character=Characters.c0000_0002, first_flag=1250, last_flag=1255, flag=1251)
    Event_11000531(0, character=Characters.c0000_0002)
    Event_11000510(0, character=Characters.c0000_0002, flag=1253)
    Event_11000520(0, character=Characters.c0000_0002, first_flag=1250, last_flag=1255, flag=1254)
    Event_11000534(0, character=Characters.c0000_0002)
    HumanityRegistration(Characters.c0000_0004, event_flag=CommonFlags.DomnhallHumanityFlag)
    SkipLinesIfFlagEnabled(2, 1434)
    SkipLinesIfFlagEnabled(1, 1430)
    DisableCharacter(Characters.c0000_0004)
    Event_11000532(0, character=Characters.c0000_0004, first_flag=1430, last_flag=1459, flag=1431)
    Event_11000510(1, character=Characters.c0000_0004, flag=1434)
    Event_11000533(0, character=Characters.c0000_0004, flag=1435)


@ContinueOnRest(Flags.Bonfire1BaseFlag)
def Event_11000992():
    """Event 11000992"""
    AND_1.Add(FlagEnabled(11027997))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.c5260_0000, 7100)
    AddSpecialEffect(Characters.c0000_0006, 7100)
    AND_2.Add(FlagDisabled(11027997))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(Characters.c5260_0000, 7100)
    RemoveSpecialEffect(Characters.c0000_0006, 7100)
    Restart()


@ContinueOnRest(11000993)
def Event_11000993():
    """Event 11000993"""
    OR_1.Add(FlagDisabled(11412993))
    OR_1.Add(FlagEnabled(11410858))
    
    MAIN.Await(OR_1)
    
    DisableCharacter(Characters.c0000_ano1)
    End()


@ContinueOnRest(11000994)
def Event_11000994():
    """Event 11000994"""
    if FlagDisabled(11012997):
        AND_1.Add(Attacked(attacked_entity=Characters.c0000_ano1, attacker=PLAYER))
        AND_1.Add(HealthRatio(Characters.c0000_ano1) <= 0.75)
    
        MAIN.Await(AND_1)
    
        EnableFlag(11012997)
        EnableFlag(744)
    SetTeamTypeAndExitStandbyAnimation(Characters.c0000_ano1, team_type=TeamType.HostileAlly)


@ContinueOnRest(11000998)
def Event_11000998():
    """Event 11000998"""
    DisableAI(Characters.c2370_chn1)
    OR_1.Add(EntityWithinDistance(entity=Characters.c2370_chn1, other_entity=PLAYER, radius=4.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c2370_chn1, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
    MAIN.Await(OR_1)
    
    EnableAI(Characters.c2370_chn1)


@RestartOnRest(11000999)
def Event_11000999(_, chr: int):
    """Event 11000999"""
    DisableAI(chr)
    AND_1.Add(EntityWithinDistance(entity=10000, other_entity=chr, radius=3.0))
    MAIN.Await(AND_1)    
    EnableAI(chr)


@ContinueOnRest(Flags.CheckpointFog1Entered)
def Event_11000090(_, obj: Object | int, vfx_id: VFXEvent | int, destination: int, destination_1: int):
    """Event 11000090"""
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


@RestartOnRest(Flags.EnableGravelordPhantoms)
def Event_11005080():
    """Event 11005080"""
    if FlagDisabled(11007999):
        DisableCharacter(Characters.c2500_0012)
        DisableCharacter(Characters.c2500_0013)
        DisableCharacter(Characters.c2500_0014)
        DisableCharacter(Characters.c2500_0015)
        DisableCharacter(Characters.c2500_0016)
        DisableCharacter(Characters.c2660_0002)
        DisableCharacter(Characters.c1201_0018)
        DisableCharacter(Characters.c1201_0019)
        DisableCharacter(Characters.c1201_0020)
        DisableCharacter(Characters.c1201_0021)
        DisableCharacter(Characters.c1201_0022)
        DisableCharacter(Characters.c1201_0023)
        DisableCharacter(Characters.c1201_0024)
        DisableCharacter(Characters.c1201_0025)
    OR_1.Add(FlagEnabled(742))
    AND_1.Add(FlagDisabled(11007999))
    AND_1.Add(OR_1)
    if not AND_1:
        return
    EnableFlag(11007999)


@RestartOnRest(Flags.DefeatGravelordInvader)
def Event_11005081():
    """Event 11005081"""
    AND_1.Add(FlagDisabled(742))
    AND_1.Add(FlagEnabled(11007999))
    
    MAIN.Await(AND_1)
    
    DisableFlag(11007999)
    Kill(Characters.c2500_0012)
    Kill(Characters.c2500_0013)
    Kill(Characters.c2500_0014)
    Kill(Characters.c2500_0015)
    Kill(Characters.c2500_0016)
    Kill(Characters.c2660_0002)
    Kill(Characters.c1201_0018)
    Kill(Characters.c1201_0019)
    Kill(Characters.c1201_0020)
    Kill(Characters.c1201_0021)
    Kill(Characters.c1201_0022)
    Kill(Characters.c1201_0023)
    Kill(Characters.c1201_0024)
    Kill(Characters.c1201_0025)


@RestartOnRest(Flags.GravelordInvasionTimer)
def Event_11005082():
    """Event 11005082"""
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=DEPTHS))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(Flags.GravelordInvasionTrigger))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=DEPTHS))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(Flags.GravelordInvasionTrigger))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=DEPTHS))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(Flags.GravelordInvasionTrigger))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=DEPTHS))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(Flags.GravelordInvasionTrigger))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=DEPTHS))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(Flags.GravelordInvasionTrigger))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=DEPTHS))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(Flags.GravelordInvasionTrigger))
    if not OR_6:
        return RESTART
    EnableFlag(Flags.GravelordInvasionTrigger)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=DEPTHS))
    if not AND_7:
        return RESTART
    DisableFlag(Flags.GravelordInvasionTrigger)
    EnableFlag(11005085)


@ContinueOnRest(Flags.HostEnteredGapingDragonFog)
def Event_11005390():
    """Event 11005390"""
    AND_1.Add(FlagDisabled(CommonFlags.GapingDragonDead))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1002998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1001990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(Flags.ClientEnteredGapingDragonFog)
def Event_11005391():
    """Event 11005391"""
    AND_1.Add(FlagDisabled(CommonFlags.GapingDragonDead))
    AND_1.Add(FlagEnabled(Flags.GapingDragonBattleNotified))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1002998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        boss_version=True,
        line_intersects=1001990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(Flags.GapingDragonBattleNotified)
def Event_11005393():
    """Event 11005393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(CommonFlags.GapingDragonDead))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5260_0000)


@RestartOnRest(Flags.GapingDragonBattleActive)
def Event_11005392():
    """Event 11005392"""
    if FlagEnabled(CommonFlags.GapingDragonDead):
        DisableCharacter(Characters.c5260_0000)
        DisableCharacter(Characters.c5261_0000)
        Kill(Characters.c5260_0000)
        Kill(Characters.c5261_0000)
        End()
    if FlagDisabled(Flags.GapingDragonIntroCutsceneDone):
        DisableCharacter(Characters.c5260_0000)
    DisableAI(Characters.c5260_0000)
    AND_1.Add(FlagEnabled(Flags.GapingDragonBattleNotified))
    AND_1.Add(Host())
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Intruder))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_1:
        return
    SkipLinesIfFlagEnabled(7, Flags.GapingDragonIntroCutsceneDone)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(100000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(Characters.c5260_0000)
    EnableFlag(Flags.GapingDragonIntroCutsceneDone)
    EnableAI(Characters.c5260_0000)
    EnableBossHealthBar(Characters.c5260_0000, name=5260)


@ContinueOnRest(Flags.GapingDragonDefeated)
def Event_11000001():
    """Event 11000001"""
    MAIN.Await(CharacterDead(Characters.c5260_0000))
    
    EnableFlag(CommonFlags.GapingDragonDead)
    Kill(Characters.c5261_0000)
    KillBoss(game_area_param_id=1000800)
    DisableObject(Objects.o1400_0000)
    DeleteVFX(VFX.BossEntranceFog)


@ContinueOnRest(Flags.GapingDragonMusicStarted)
def Event_11005394():
    """Event 11005394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(CommonFlags.GapingDragonDead))
    AND_1.Add(FlagEnabled(Flags.GapingDragonBattleActive))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1002999))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=Sounds.GapingDragonMusic)


@ContinueOnRest(Flags.GapingDragonMusicStopped)
def Event_11005395():
    """Event 11005395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(CommonFlags.GapingDragonDead))
    AND_1.Add(FlagEnabled(Flags.GapingDragonMusicStarted))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=Sounds.GapingDragonMusic)


@RestartOnRest(Flags.GapingDragonTailCut)
def Event_11005396():
    """Event 11005396"""
    DisableCharacter(Characters.c5261_0000)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(Flags.HostEnteredGapingDragonFog))
    
    CreateNPCPart(Characters.c5260_0000, npc_part_id=5260, part_index=NPCPartType.Part1, part_health=300)
    
    MAIN.Await(CharacterPartHealth(Characters.c5260_0000, npc_part_id=5260) <= 0)
    
    EzstateAIRequest(Characters.c5260_0000, command_id=1001, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(Characters.c5260_0000, tae_event_id=400))
    
    EnableCharacter(Characters.c5261_0000)
    Move(
        Characters.c5261_0000,
        destination=Characters.c5260_0000,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=Characters.c5260_0000,
    )
    ForceAnimation(Characters.c5261_0000, 8100)
    SetDisplayMask(Characters.c5260_0000, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Characters.c5260_0000, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Characters.c5260_0000, command_id=20, command_slot=0)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(52610000, host_only=True)


@RestartOnRest(Flags.GapingDragonUnknownBodyPart)
def Event_11005397():
    """Event 11005397"""
    AND_1.Add(FlagEnabled(Flags.HostEnteredGapingDragonFog))
    AND_1.Add(CharacterBackreadEnabled(Characters.c5260_0000))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(
        Characters.c5260_0000,
        npc_part_id=5261,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
    )
    SetNPCPartEffects(Characters.c5260_0000, npc_part_id=5261, material_sfx_id=60, material_vfx_id=60)


@RestartOnRest(Flags.GapingDragonHeadHit)
def Event_11005398():
    """Event 11005398"""
    MAIN.Await(FlagEnabled(Flags.HostEnteredGapingDragonFog))
    
    CreateNPCPart(Characters.c5260_0000, npc_part_id=5262, part_index=NPCPartType.Part3, part_health=1)
    
    MAIN.Await(CharacterPartHealth(Characters.c5260_0000, npc_part_id=5262) <= 0)
    
    AICommand(Characters.c5260_0000, command_id=1, command_slot=0)
    DisableNetworkSync()
    Wait(1.0)
    EnableNetworkSync()
    if FlagDisabled(Flags.GapingDragonTailCut):
        AICommand(Characters.c5260_0000, command_id=0, command_slot=0)
    else:
        AICommand(Characters.c5260_0000, command_id=20, command_slot=0)
    Restart()


@ContinueOnRest(Flags.TinyRatsScurry)
def Event_11005000(_, other_entity: int, obj: int, animation_id: int):
    """Event 11005000"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        End()
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=3.0))
    
    ForceAnimation(obj, animation_id, wait_for_completion=True)
    DisableObject(obj)


@ContinueOnRest(Flags.ShortcutDoorOpened)
def Event_11000100():
    """Event 11000100"""
    AND_1.Add(FlagDisabled(Flags.ShortcutDoorOpened))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1319_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=Objects.o1319_0000,
        destination_type=CoordEntityType.Object,
        model_point=121,
        short_move=True,
    )
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(Objects.o1319_0000, 0)


@ContinueOnRest(Flags.ShortcutDoorWrongSide)
def Event_11000101():
    """Event 11000101"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(Flags.ShortcutDoorOpened))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1319_0000,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=Objects.o1319_0000, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(Flags.OpenBlighttownDoor)
def Event_11000110():
    """Event 11000110"""
    SkipLinesIfFlagEnabled(1, CommonFlags.BlighttownDoorOpened)
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=Objects.o1309, animation_id=1)
    End()
    AND_1.Add(PlayerHasGood(2007))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(Flags.BlighttownDoorLocked)
    Move(PLAYER, destination=Objects.o1309, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(Objects.o1309, 1)
    if Client():
        return
    DisplayDialog(text=10010866, anchor_entity=Objects.o1309)
    EnableFlag(CommonFlags.BlighttownDoorOpened)


@ContinueOnRest(Flags.BlighttownDoorLocked)
def Event_11000111():
    """Event 11000111"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(Flags.OpenBlighttownDoor))
    AND_1.Add(PlayerDoesNotHaveGood(2007))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(Client())
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=Objects.o1309,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(Flags.OpenBlighttownDoor):
        return
    DisplayDialog(text=10010163, anchor_entity=Objects.o1309)
    Restart()


@ContinueOnRest(Flags.ShowDoorUnlockedMessage)
def Event_11000120(
    _,
    obj_act_id: int,
    text: EventText | int,
    anchor_entity: int,
    text_1: EventText | int,
    item: BaseItemParam | int,
):
    """Event 11000120"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    if Client():
        return
    AND_1.Add(PlayerHasGood(item))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayDialog(text=text_1, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)
    SkipLines(1)
    DisplayDialog(text=text, anchor_entity=anchor_entity, button_type=ButtonType.Yes_or_No)


@RestartOnRest(Flags.BasiliskRunningDone)
def Event_11000200():
    """Event 11000200"""
    if ThisEventFlagEnabled():
        return
    DisableAI(Characters.c3270_0000)
    AND_1.Add(FlagDisabled(Flags.BasiliskRunningDone))
    AND_1.Add(EntityWithinDistance(entity=Characters.c3270_0000, other_entity=PLAYER, radius=9.0))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    ForceAnimation(Characters.c3270_0000, 500, wait_for_completion=True)
    EnableAI(Characters.c3270_0000)


@RestartOnRest(Flags.GiantRatDead)
def Event_11000800():
    """Event 11000800"""
    if ThisEventFlagEnabled():
        DisableCharacter(Characters.c1202_0000)
        End()
    
    MAIN.Await(CharacterDead(Characters.c1202_0000))
    
    EnableFlag(Flags.GiantRatDead)


@RestartOnRest(Flags.ChoppingButcherAggro)
def Event_11005050():
    """Event 11005050"""
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.c2660_0000, radius=7.0))
    OR_1.Add(Attacked(attacked_entity=Characters.c2660_0000, attacker=PLAYER))
    OR_1.Add(ObjectDestroyed(Objects.o1002_01))
    OR_1.Add(HasAIStatus(Characters.c3340_0002, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(Characters.c2660_0000, cancel_animation=9060)


@ContinueOnRest(Flags.ChoppingButcherMeatVFX)
def Event_11005060():
    """Event 11005060"""
    if ThisEventFlagEnabled():
        return
    CreateObjectVFX(Objects.o1002_01, vfx_id=10, model_point=100013)
    
    MAIN.Await(ObjectDestroyed(Objects.o1002_01))
    
    DeleteObjectVFX(Objects.o1002_01)


@RestartOnRest(Flags.ButcherDropAmbush)
def Event_11005070():
    """Event 11005070"""
    AND_7.Add(CharacterDead(Characters.c2660_0001))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableCharacter(Characters.c2660_0001)
    End()
    if ThisEventFlagEnabled():
        return
    DisableAI(Characters.c2660_0001)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1002200))
    AND_2.Add(Attacked(attacked_entity=Characters.c2660_0001, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    ForceAnimation(Characters.c2660_0001, 500)
    EnableAI(Characters.c2660_0001)


@RestartOnRest(Flags.CeilingSlimeAmbush)
def Event_11005100(_, region: Region | int, character: Character | int, seconds: float):
    """Event 11005100"""
    if ThisEventSlotFlagDisabled():
        DisableGravity(character)
        DisableCharacterCollision(character)
        OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
        OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
        MAIN.Await(OR_1)
    
        Wait(seconds)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character)


@RestartOnRest(Flags.RegionAITrigger)
def Event_11005200(_, character: Character | int, region: Region | int):
    """Event 11005200"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)


@RestartOnRest(Flags.RatAmbushFromBox)
def Event_11005150(_, character: int, obj: int, flag: Flag | int, flag_1: Flag | int):
    """Event 11005150"""
    AND_4.Add(CharacterDead(character))
    SkipLinesIfConditionTrue(2, AND_4)
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_5.Add(CharacterAlive(character))
    SkipLinesIfConditionTrue(1, AND_5)
    SkipLinesIfFlagEnabled(1, flag)
    SkipLinesIfThisEventSlotFlagDisabled(9)
    AND_3.Add(CharacterDead(character))
    AND_3.Add(Host())
    SkipLinesIfConditionFalse(2, AND_3)
    DisableCharacter(character)
    EnableFlag(flag_1)
    if FlagEnabled(flag_1):
        DisableCharacter(character)
    PostDestruction(obj)
    End()
    RestoreObject(obj)
    DisableCharacter(character)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    AND_2.Add(ObjectDestroyed(obj))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    DestroyObject(obj)
    PlaySoundEffect(obj, 132200000, sound_type=SoundType.o_Object)
    EnableCharacter(character)
    ForceAnimation(character, 3002)
    EnableFlag(flag)
    End()
    EnableCharacter(character)
    EnableFlag(flag)


@RestartOnRest(Flags.NoRespawn)
def Event_11000850(_, character: Character | int):
    """Event 11000850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@ContinueOnRest(Flags.OpenChest)
def Event_11000600(_, obj: Object | int, obj_act_id: int):
    """Event 11000600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(Flags.AggroNPC)
def Event_11000510(_, character: Character | int, flag: Flag | int):
    """Event 11000510"""
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


@ContinueOnRest(11000520)
def Event_11000520(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11000520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(Flags.BreakLaurentiusFromPot)
def Event_11000530(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11000530"""
    if FlagDisabled(Flags.LaurentiusFreedFromPot):
        AND_1.Add(FlagDisabled(1253))
        AND_1.Add(FlagEnabled(1250))
        AND_1.Add(HealthRatio(character) > 0.0)
        OR_1.Add(ObjectDestroyed(Objects.o1155))
        OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
        AND_1.Add(OR_1)
    
        MAIN.Await(AND_1)
    
        DisableFlagRange((first_flag, last_flag))
        EnableFlag(flag)
    if ObjectNotDestroyed(Objects.o1155):
        DestroyObject(Objects.o1155)
    EnableGravity(character)
    EnableCharacterCollision(character)
    SetStandbyAnimationSettings(character, cancel_animation=7821)
    EnableFlag(Flags.LaurentiusFreedFromPot)


@ContinueOnRest(Flags.LaurentiusMovesOn)
def Event_11000531(_, character: Character | int):
    """Event 11000531"""
    AND_1.Add(FlagDisabled(1253))
    AND_1.Add(FlagEnabled(1252))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)


@ContinueOnRest(Flags.DomnhallMovesOn)
def Event_11000532(_, character: Character | int, first_flag: Flag | int, last_flag: Flag | int, flag: Flag | int):
    """Event 11000532"""
    AND_1.Add(FlagDisabled(1434))
    AND_1.Add(FlagDisabled(1435))
    AND_1.Add(FlagEnabled(1430))
    AND_1.Add(FlagEnabled(11010700))
    AND_1.Add(FlagEnabled(11400200))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)


@ContinueOnRest(Flags.DomnhallKilled)
def Event_11000533(_, character: Character | int, flag: Flag | int):
    """Event 11000533"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlag(1434)
    EnableFlag(flag)


@ContinueOnRest(Flags.LaurentiusInvincibleInPot)
def Event_11000534(_, character: Character | int):
    """Event 11000534"""
    AND_1.Add(FlagEnabled(1250))
    AND_1.Add(FlagDisabled(1253))
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(character)
    
    MAIN.Await(ObjectDestroyed(Objects.o1155))
    
    DisableNetworkSync()
    Wait(2.0)
    DisableInvincibility(character)


@ContinueOnRest(Flags.PlaceSolaireSummonSign)
def Event_11005030():
    """Event 11005030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0005, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, Flags.SolaireDismissed)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(Flags.SolaireSummoned))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0005)
    if FlagEnabled(CommonFlags.GapingDragonDead):
        return
    If_Unknown_3_24(AND_1, unk1=5, unk2=2)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(Flags.SolaireSummoned))
    AND_1.Add(FlagDisabled(Flags.SolaireDismissed))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0005))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0005,
        region=1002000,
        summon_flag=Flags.SolaireSummoned,
        dismissal_flag=Flags.SolaireDismissed,
    )


@ContinueOnRest(Flags.PlaceGoldSolaireSummonSign)
def Event_11005029():
    """Event 11005029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0005, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, Flags.SolaireDismissed)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(Flags.SolaireSummoned))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0005)
    if FlagEnabled(CommonFlags.GapingDragonDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(Flags.SolaireSummoned))
    AND_1.Add(FlagDisabled(Flags.SolaireDismissed))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0005))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0005,
        region=1002000,
        summon_flag=Flags.SolaireSummoned,
        dismissal_flag=Flags.SolaireDismissed,
    )


@ContinueOnRest(11005031)
def Event_11005031():
    """Event 11005031"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(Flags.SolaireSummoned))
    AND_1.Add(FlagEnabled(Flags.GapingDragonBattleNotified))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0005, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0005)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0005, region=1002998))
    
    RotateToFaceEntity(Characters.c0000_0005, target_entity=1002997)
    ForceAnimation(Characters.c0000_0005, 7410)
    AICommand(Characters.c0000_0005, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0005)


@ContinueOnRest(Flags.PlaceLautrecSummonSign)
def Event_11005033():
    """Event 11005033"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, Flags.LautrecDismissed)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(Flags.LautrecSummoned))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0007)
    if FlagEnabled(CommonFlags.GapingDragonDead):
        return
    If_Unknown_3_24(AND_1, unk1=5, unk2=2)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(11020607))
    AND_1.Add(FlagDisabled(Flags.LautrecSummoned))
    AND_1.Add(FlagDisabled(Flags.LautrecDismissed))
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0007))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0007,
        region=1002002,
        summon_flag=Flags.LautrecSummoned,
        dismissal_flag=Flags.LautrecDismissed,
    )


@ContinueOnRest(Flags.BuffLautrecSummon)
def Event_11005333():
    """Event 11005333"""
    MAIN.Await(FlagEnabled(Flags.LautrecSummoned))
    
    AddSpecialEffect(Characters.c0000_0007, 5450)


@ContinueOnRest(Flags.EraseSummonSign)
def Event_11005990(_, flag: Flag | int, summoned_character: Character | int):
    """Event 11005990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(Flags.PlaceGoldLautrecSummonSign)
def Event_11005036():
    """Event 11005036"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0007, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, Flags.LautrecDismissed)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(Flags.LautrecSummoned))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(Characters.c0000_0007)
    if FlagEnabled(CommonFlags.GapingDragonDead):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(Flags.LautrecSummoned))
    AND_1.Add(FlagDisabled(Flags.LautrecDismissed))
    AND_1.Add(FlagEnabled(11020607))
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1574))
    AND_1.Add(CharacterBackreadEnabled(Characters.c0000_0007))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=Characters.c0000_0007,
        region=1002002,
        summon_flag=Flags.LautrecSummoned,
        dismissal_flag=Flags.LautrecDismissed,
    )


@ContinueOnRest(Flags.LautrecEntersGapingDragonFog)
def Event_11005034():
    """Event 11005034"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(Flags.LautrecSummoned))
    AND_1.Add(FlagEnabled(Flags.GapingDragonBattleNotified))
    
    MAIN.Await(AND_1)
    
    AICommand(Characters.c0000_0007, command_id=10, command_slot=0)
    ReplanAI(Characters.c0000_0007)
    
    MAIN.Await(CharacterInsideRegion(Characters.c0000_0007, region=1002998))
    
    RotateToFaceEntity(Characters.c0000_0007, target_entity=1002997)
    ForceAnimation(Characters.c0000_0007, 7410)
    AICommand(Characters.c0000_0007, command_id=-1, command_slot=0)
    ReplanAI(Characters.c0000_0007)


@ContinueOnRest(11005039)
def Event_11005039():
    """Event 11005039"""
    DisableNetworkSync()
    if Client():
        return
    if FlagEnabled(Flags.KirkInvaded):
        return
    if FlagEnabled(CommonFlags.GapingDragonDead):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(Flags.KirkInvaderKilled))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1002005))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlackEyeSign,
        character=Characters.c0000_0006,
        region=1002001,
        summon_flag=Flags.KirkInvaded,
        dismissal_flag=Flags.KirkRetreated,
    )
    Wait(20.0)
    Restart()


@ContinueOnRest(Flags.KirkInvaderKilled)
def Event_11000810():
    """Event 11000810"""
    SkipLinesIfHost(3)
    AND_1.Add(FlagEnabled(Flags.KirkInvaded))
    AND_1.Add(FlagDisabled(Flags.KirkRetreated))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(Characters.c0000_0006)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(Characters.c0000_0006))
    
    EnableFlag(Flags.KirkInvaderKilled)


@ContinueOnRest(11005843)
def Event_11005843(_, flag: Flag | int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11005843"""
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


@ContinueOnRest(11005844)
def Event_11005844(_, flag: Flag | int, obj: Object | int, vfx_id: VFXEvent | int):
    """Event 11005844"""
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
