"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from m10_00_00_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(11000992)
    RunEvent(11000993)
    RunEvent(11000994)
    RunEvent(11000999)
    RegisterBonfire(11000992, objH01960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, objH01140)
    RegisterStatueH01900, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01901, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01902, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01903, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01904, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01905, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01906, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatueH01907, game_map=DEPTHS, statue_type=StatueType.Stone)
    SkipLinesIfClient(5)
    DisableFlag(11000000)
    DisableObjectH01994)
    DeleteFX(1001995, erase_root_only=False)
    DisableObjectH01996)
    DeleteFX(1001997, erase_root_only=False)
    SkipLinesIfFlagOff(1, 11000100)
    EndOfAnimationH01319, 0)
    RunEvent(11000090, slot=0, args=H01700, 1001701, 1002600, 1002601))
    RunEvent(11005080)
    RunEvent(11005081)
    RunEvent(11005082)
    RunEvent(11000100)
    RunEvent(11000101)
    RunEvent(11000120, slot=0, args=(11000120, 10010877,H01315, 10010883, 2018))
    RunEvent(11000200)
    RunEvent(11000800)
    RunEvent(11005050)
    RunEvent(11005060)
    RunEvent(11005070)
    RunEvent(11000110)
    RunEvent(11000111)
    RunEvent(11000600, slot=0, args=H01650, 11000600))
    DisableSoundEvent(1003800)
    SkipLinesIfFlagOff(4, 2)
    RunEvent(11005392)
    DisableObjectH01990)
    DeleteFX(1001991, erase_root_only=False)
    SkipLines(10)
    RunEvent(11005390)
    RunEvent(11005391)
    RunEvent(11005393)
    RunEvent(11005392)
    RunEvent(11000001)
    RunEvent(11005394)
    RunEvent(11005395)
    RunEvent(11005396)
    RunEvent(11005397)
    RunEvent(11005398)
    RunEvent(11005000, slot=0, args=H01000,H01000, 1))
    RunEvent(11005000, slot=1, args=H01001,H01001, 1))
    RunEvent(11005000, slot=2, args=H01002,H01002, 3))
    RunEvent(11005200, slot=0, args=H00120, 1002020))
    RunEvent(11005200, slot=1, args=H00121, 1002020))
    RunEvent(11005200, slot=2, args=H00122, 1002020))
    RunEvent(11005200, slot=3, args=H00123, 1002020))
    RunEvent(11005200, slot=4, args=H00124, 1002020))
    RunEvent(11005200, slot=5, args=H00125, 1002020))
    RunEvent(11005200, slot=6, args=H00110, 1002021))
    RunEvent(11005200, slot=7, args=H00111, 1002021))
    RunEvent(11005200, slot=8, args=H00112, 1002022))
    RunEvent(11005200, slot=9, args=H00113, 1002022))
    RunEvent(11005200, slot=10, args=H00126, 1002022))
    RunEvent(11005100, slot=0, args=(1002100,H00100, 0.0), arg_types='iif')
    RunEvent(11005100, slot=1, args=(1002101,H00101, 0.0), arg_types='iif')
    RunEvent(11005100, slot=2, args=(1002102,H00102, 0.0), arg_types='iif')
    RunEvent(11005100, slot=3, args=(1002102,H00103, 0.6000000238418579), arg_types='iif')
    RunEvent(11005100, slot=4, args=(1002103,H00104, 0.0), arg_types='iif')
    RunEvent(11005100, slot=5, args=(1002103,H00105, 0.20000000298023224), arg_types='iif')
    RunEvent(11005100, slot=6, args=(1002103,H00106, 0.8999999761581421), arg_types='iif')
    RunEvent(11005100, slot=7, args=(1002107,H00107, 0.0), arg_types='iif')
    RunEvent(11005150, slot=0, args=H00150,H01100, 11009000, 11009010))
    RunEvent(11005150, slot=1, args=H00151,H01101, 11009001, 11009011))
    RunEvent(11005150, slot=2, args=H00152,H01102, 11009002, 11009012))
    RunEvent(11000850, slot=0, args=H00110,))
    RunEvent(11000850, slot=1, args=H00099,))
    RunEvent(11000850, slot=2, args=H00090,))
    RunEvent(11000850, slot=3, args=H00300,))
    RunEvent(11000850, slot=4, args=H00301,))
    RunEvent(11000850, slot=5, args=r884,))
    RunEvent(11005843, slot=0, args=(2,H01990, 1002998, 1002997))
    RunEvent(11005844, slot=0, args=(2,H01990, 1001991))


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistrationu41, 8310)
    HumanityRegistrationu91, 8462)
    HumanityRegistrationu62, 8956)
    RunEvent(11005030)
    RunEvent(11005029)
    RunEvent(11005031)
    RunEvent(11005033)
    RunEvent(11005036)
    RunEvent(11005034)
    RunEvent(11005039)
    RunEvent(11000810)
    RunEvent(11005333)
    RunEvent(11005990, slot=0, args=(11005032,u41))
    RunEvent(11005990, slot=1, args=(11005035,u91))
    HumanityRegistrationq30, 8390)
    SkipLinesIfClient(1)
    DisableFlag(11000580)
    SkipLinesIfFlagOn(3, 11000580)
    SkipLinesIfFlagOn(2, 1250)
    SkipLinesIfFlagOn(1, 1253)
    DisableCharacterq30)
    SkipLinesIfFlagOff(2, 1250)
    DisableGravityq30)
    DisableCharacterCollisionq30)
    RunEvent(11000530, slot=0, args=q30, 1250, 1255, 1251))
    RunEvent(11000531, slot=0, args=q30,))
    RunEvent(11000510, slot=0, args=q30, 1253))
    RunEvent(11000520, slot=0, args=q30, 1250, 1255, 1254))
    RunEvent(11000534, slot=0, args=q30,))
    HumanityRegistrationr60, 8430)
    SkipLinesIfFlagOn(2, 1434)
    SkipLinesIfFlagOn(1, 1430)
    DisableCharacterr60)
    RunEvent(11000532, slot=0, args=r60, 1430, 1459, 1431))
    RunEvent(11000510, slot=1, args=r60, 1434))
    RunEvent(11000533, slot=0, args=r60, 1435))


def WT_BossBuff():
    """ 11000992: Dark World Tendency boss buff """
    IfFlagOn(1, 11027997)    
    IfConditionTrue(0, 1)
    AddSpecialEffectH00800, 7100)
    AddSpecialEffectu62, 7100)
    IfFlagOff(2, 11027997)    
    IfConditionTrue(0, 2)
    CancelSpecialEffectH00800, 7100)
    CancelSpecialEffectu62, 7100)
    Restart()


def Anon_Despawn():
    """ 11000993: Despawn the Anonymous """
    IfFlagOff(-1, 11412993)
    IfFlagOn(-1, 11410858)
    IfConditionTrue(0, -1)
    DisableCharacterr884)
    End()


def Anon_Aggro():
    """ 11000994: Make the Anonymous hostile """
    SkipLinesIfFlagOn(5, 11012997)
    IfAttacked(1,r884, attacking_character=10000)
    IfHealthLessThanOrEqual(1,r884, 0.75)
    IfConditionTrue(0, 1)
    EnableFlag(11012997)
    EnableFlag(744)
    SetTeamTypeAndExitStandbyAnimationr884, TeamType.HostileAlly)


@RestartOnRest
def Event11000999():
    """ 11000999: Event 11000999 """
    DisableHealthBarH00999)
    EnableInvincibilityH00999)
    DisableHealthBarH00998)
    EnableInvincibilityH00998)
    DisableHealthBarH00997)
    EnableInvincibilityH00997)
    DisableHealthBarH00996)
    EnableInvincibilityH00996)
    DisableHealthBarH00995)
    EnableInvincibilityH00995)
    IfFlagOn(1, 2)
    IfConditionTrue(0, 1)
    EnableHealthBarH00999)
    DisableInvincibilityH00999)
    EnableHealthBarH00998)
    DisableInvincibilityH00998)
    EnableHealthBarH00997)
    DisableInvincibilityH00997)
    EnableHealthBarH00996)
    DisableInvincibilityH00996)
    EnableHealthBarH00995)
    DisableInvincibilityH00995)
    

def Event11000090(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000090: Event 11000090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=arg_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def WT_SpawnPhantoms():
    """ 11005080: Spawn Red Phantom enemies """
    EndIfThisEventOn()
    SkipLinesIfFlagOn(14, 11007999)
    DisableCharacterH00900)
    DisableCharacterH00901)
    DisableCharacterH00902)
    DisableCharacterH00903)
    DisableCharacterH00904)
    DisableCharacterH00905)
    DisableCharacterH00906)
    DisableCharacterH00907)
    DisableCharacterH00908)
    DisableCharacterH00909)
    DisableCharacterH00910)
    DisableCharacterH00911)
    DisableCharacterH00912)
    DisableCharacterH00913)
    #IfFlagOn(0, 11000050)
    #EndIfFlagOn(735)
    #EnableFlag(5000)
    IfFlagOn(-1, 744)
    IfFlagOn(-1, 742)
    IfFlagOff(1, 11007999)
    IfConditionTrue(1, -1)
    EndIfConditionFalse(1)
    EnableFlag(11007999)
    EnableCharacterH00900)
    EnableCharacterH00901)
    EnableCharacterH00902)
    EnableCharacterH00903)
    EnableCharacterH00904)
    EnableCharacterH00905)
    EnableCharacterH00906)
    EnableCharacterH00907)
    EnableCharacterH00908)
    EnableCharacterH00909)
    EnableCharacterH00910)
    EnableCharacterH00911)
    EnableCharacterH00912)
    EnableCharacterH00913)


@RestartOnRest
def WT_KillPhantoms():
    """ 11005081: Kill Red Phantom enemies """
    #IfFlagOn(-1, 11005085)
    #IfFlagOn(-1, 735)
    #IfConditionTrue(0, input_condition=-1)
    #SkipLinesIfFlagOff(1, 735)
    #DisableFlag(735) 
    #DisableFlag(11000050)
    #DisableFlag(11005085)
    #EnableFlag(5001)
    IfFlagOff(1, 744)
    IfFlagOff(1, 742)
    IfFlagOn(1, 11007999)
    IfConditionTrue(0, 1)
    DisableFlag(11007999)
    KillH00900, award_souls=False)
    KillH00901, award_souls=False)
    KillH00902, award_souls=False)
    KillH00903, award_souls=False)
    KillH00904, award_souls=False)
    KillH00905, award_souls=False)
    KillH00906, award_souls=False)
    KillH00907, award_souls=False)
    KillH00908, award_souls=False)
    KillH00909, award_souls=False)
    KillH00910, award_souls=False)
    KillH00911, award_souls=False)
    KillH00912, award_souls=False)
    KillH00913, award_souls=False)


@RestartOnRest
def Event11005082():
    """ 11005082: Event 11005082 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=DEPTHS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11000050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=DEPTHS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11000050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=DEPTHS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11000050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=DEPTHS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11000050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=DEPTHS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11000050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=DEPTHS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11000050)
    RestartIfConditionFalse(-6)
    EnableFlag(11000050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=DEPTHS)
    RestartIfConditionFalse(7)
    DisableFlag(11000050)
    EnableFlag(11005085)


def Event11005390():
    """ 11005390: Event 11005390 """
    IfFlagOff(1, 2)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1002998, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersectsH01990, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11005391():
    """ 11005391: Event 11005391 """
    IfFlagOff(1, 2)
    IfFlagOn(1, 11005393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1002998, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersectsH01990, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1002997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11005393():
    """ 11005393: Event 11005393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 2)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffsH00800)


@RestartOnRest
def Event11005392():
    """ 11005392: Event 11005392 """
    SkipLinesIfFlagOff(5, 2)
    DisableCharacterH00800)
    DisableCharacterH00801)
    KillH00800, award_souls=False)
    KillH00801, award_souls=False)
    End()
    SkipLinesIfFlagOn(1, 11000000)
    DisableCharacterH00800)
    DisableAIH00800)
    IfFlagOn(1, 11005393)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(7, 11000000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(100000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(100000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacterH00800)
    EnableFlag(11000000)
    EnableAIH00800)
    EnableBossHealthBarH00800, name=5260, slot=0)


def Event11000001():
    """ 11000001: Event 11000001 """
    IfCharacterDead(0,H00800)
    EnableFlag(2)
    KillH00801, award_souls=False)
    KillBossH00800)
    DisableObjectH01990)
    DeleteFX(1001991, erase_root_only=True)


def Event11005394():
    """ 11005394: Event 11005394 """
    DisableNetworkSync()
    IfFlagOff(1, 2)
    IfFlagOn(1, 11005392)
    IfCharacterInsideRegion(1, PLAYER, region=1002999)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1003800)


def Event11005395():
    """ 11005395: Event 11005395 """
    DisableNetworkSync()
    IfFlagOn(1, 2)
    IfFlagOn(1, 11005394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1003800)


@RestartOnRest
def Event11005396():
    """ 11005396: Event 11005396 """
    DisableCharacterH00801)
    EndIfThisEventOn()
    IfFlagOn(0, 11005390)
    CreateNPCPartH00800, npc_part_id=5260, part_index=NPCPartType.Part1, part_health=300, damage_correction=1.0, 
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(0,H00800, npc_part_id=5260, value=0)
    EzstateAIRequestH00800, command_id=1001, slot=0)
    IfHasTAEEvent(0,H00800, tae_event_id=400)
    EnableCharacterH00801)
    MoveH00801, destinationH00800, destination_type=CoordEntityType.Character, model_point=100, 
         copy_draw_parentH00800)
    ForceAnimationH00801, 8100)
    SetDisplayMaskH00800, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMaskH00800, bit_index=1, switch_type=OnOffChange.Off)
    AICommandH00800, command_id=20, slot=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52610000, host_only=True)


@RestartOnRest
def Event11005397():
    """ 11005397: Event 11005397 """
    IfFlagOn(1, 11005390)
    IfCharacterBackreadEnabled(1,H00800)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPartH00800, npc_part_id=5261, part_index=NPCPartType.Part2, part_health=100, damage_correction=0.0, 
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffectsH00800, npc_part_id=5261, material_special_effect_id=60, material_fx_id=60)


@RestartOnRest
def Event11005398():
    """ 11005398: Event 11005398 """
    IfFlagOn(0, 11005390)
    CreateNPCPartH00800, npc_part_id=5262, part_index=NPCPartType.Part3, part_health=1, damage_correction=1.0, 
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(0,H00800, npc_part_id=5262, value=0)
    AICommandH00800, command_id=1, slot=0)
    DisableNetworkSync()
    Wait(1.0)
    EnableNetworkSync()
    SkipLinesIfFlagOn(2, 11005396)
    AICommandH00800, command_id=0, slot=0)
    SkipLines(1)
    AICommandH00800, command_id=20, slot=0)
    Restart()


def Event11005000(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11005000: Event 11005000 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_4_7)
    End()
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=3.0)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    DisableObject(arg_4_7)


def Event11000100():
    """ 11000100: Event 11000100 """
    IfFlagOff(1, 11000100)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entityH01319, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=101, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destinationH01319, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimationH01319, 0)


def Event11000101():
    """ 11000101: Event 11000101 """
    DisableNetworkSync()
    IfFlagOff(1, 11000100)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entityH01319, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010161, anchor_entityH01319, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11000110():
    """ 11000110: Event 11000110 """
    SkipLinesIfFlagOn(1, 590)
    SkipLinesIfThisEventOff(2)
    EndOfAnimationH01200, 1)
    End()
    IfPlayerHasGood(1, 2007, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entityH01200, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11000111)
    Move(PLAYER, destinationH01200, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimationH01200, 1)
    EndIfClient()
    DisplayDialog(10010866, anchor_entityH01200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.NoButton)
    EnableFlag(590)


def Event11000111():
    """ 11000111: Event 11000111 """
    DisableNetworkSync()
    IfFlagOn(-1, 11000110)
    IfPlayerDoesNotHaveGood(1, 2007, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entityH01200, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=True)
    IfClient(2)
    IfDialogPromptActivated(2, prompt_text=10010400, anchor_entityH01200, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=100, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(11000110)
    DisplayDialog(10010163, anchor_entityH01200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11000120(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11000120: Event 11000120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(arg_12_15, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)
    SkipLines(1)
    DisplayDialog(arg_4_7, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)


@RestartOnRest
def Event11000200():
    """ 11000200: Event 11000200 """
    EndIfThisEventOn()
    DisableAIH00200)
    IfFlagOff(1, 11000200)
    IfEntityWithinDistance(1,H00200, PLAYER, radius=9.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimationH00200, 500, wait_for_completion=True)
    ForceAnimationH00200, 500, wait_for_completion=True)
    ForceAnimationH00200, 500, wait_for_completion=True)
    ForceAnimationH00200, 500, wait_for_completion=True)
    ForceAnimationH00200, 500, wait_for_completion=True)
    ForceAnimationH00200, 500, wait_for_completion=True)
    ForceAnimationH00200, 500, wait_for_completion=True)
    EnableAIH00200)


@RestartOnRest
def Event11000800():
    """ 11000800: Event 11000800 """
    SkipLinesIfThisEventOff(2)
    DisableCharacterH00500)
    End()
    IfCharacterDead(0,H00500)
    EnableFlag(11000800)


@RestartOnRest
def Event11005050():
    """ 11005050: Event 11005050 """
    IfEntityWithinDistance(-1, PLAYER,H00099, radius=7.0)
    IfAttacked(-1,H00099, attacking_character=PLAYER)
    IfObjectDestroyed(-1,H01400)
    IfHasAIStatus(-1,H00110, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettingsH00099, cancel_animation=9060)


def Event11005060():
    """ 11005060: Event 11005060 """
    EndIfThisEventOn()
    CreateObjectFX(100013, objH01400, model_point=10)
    IfObjectDestroyed(0,H01400)
    DeleteObjectFXH01400, erase_root=True)


@RestartOnRest
def Event11005070():
    """ 11005070: Event 11005070 """
    IfCharacterDead(7,H00090)
    SkipLinesIfConditionFalse(2, 7)
    DisableCharacterH00090)
    End()
    EndIfThisEventOn()
    DisableAIH00090)
    IfCharacterInsideRegion(1, PLAYER, region=1002200)
    IfAttacked(2,H00090, attacking_character=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    ForceAnimationH00090, 500)
    EnableAIH00090)


@RestartOnRest
def Event11005100(arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11005100: Event 11005100 """
    SkipLinesIfThisEventSlotOn(6)
    DisableGravity(arg_4_7)
    DisableCharacterCollision(arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfAttacked(-1, arg_4_7, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_8_11)
    EnableGravity(arg_4_7)
    EnableCharacterCollision(arg_4_7)
    ResetStandbyAnimationSettings(arg_4_7)


@RestartOnRest
def Event11005200(arg_0_3: int, arg_4_7: int):
    """ 11005200: Event 11005200 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11005150(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11005150: Event 11005150 """
    IfCharacterDead(4, arg_0_3)
    SkipLinesIfConditionTrue(2, 4)
    DisableFlag(arg_8_11)
    DisableFlag(arg_12_15)
    IfCharacterAlive(5, arg_0_3)
    SkipLinesIfConditionTrue(1, 5)
    SkipLinesIfFlagOn(1, arg_8_11)
    SkipLinesIfThisEventSlotOff(9)
    IfCharacterDead(3, arg_0_3)
    IfHost(3)
    SkipLinesIfConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    EnableFlag(arg_12_15)
    SkipLinesIfFlagOff(1, arg_12_15)
    DisableCharacter(arg_0_3)
    PostDestruction(arg_4_7, slot=1)
    End()
    RestoreObject(arg_4_7)
    DisableCharacter(arg_0_3)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=3.0)
    IfObjectDestroyed(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(6, 1)
    DestroyObject(arg_4_7, slot=1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=132200000)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3002)
    EnableFlag(arg_8_11)
    End()
    EnableCharacter(arg_0_3)
    EnableFlag(arg_8_11)


@RestartOnRest
def Event11000850(arg_0_3: int):
    """ 11000850: Event 11000850 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11000600(arg_0_3: int, arg_4_7: int):
    """ 11000600: Event 11000600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11000510(arg_0_3: int, arg_4_7: int):
    """ 11000510: Event 11000510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11000520(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000520: Event 11000520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11000530(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000530: Event 11000530 """
    SkipLinesIfFlagOn(9, 11000580)
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1250)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfObjectDestroyed(-1,H01250)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfObjectDestroyed(1,H01250)
    DestroyObjectH01250, slot=1)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7821)
    EnableFlag(11000580)


def Event11000531(arg_0_3: int):
    """ 11000531: Event 11000531 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1252)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11000532(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11000532: Event 11000532 """
    IfFlagOff(1, 1434)
    IfFlagOff(1, 1435)
    IfFlagOn(1, 1430)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11000533(arg_0_3: int, arg_4_7: int):
    """ 11000533: Event 11000533 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlag(1434)
    EnableFlag(arg_4_7)


def Event11000534(arg_0_3: int):
    """ 11000534: Event 11000534 """
    IfFlagOn(1, 1250)
    IfFlagOff(1, 1253)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(arg_0_3)
    IfObjectDestroyed(0,H01250)
    DisableNetworkSync()
    Wait(2.0)
    DisableInvincibility(arg_0_3)


def Event11005030():
    """ 11005030: Event 11005030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthorityu41, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005037)
    IfClient(2)
    IfFlagOn(2, 11005032)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacteru41)
    EndIfFlagOn(2)
    IfMultiplayerCount(condition=1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11005032)
    IfFlagOff(1, 11005037)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1,u41)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign,u41, region=1002000, summon_flag=11005032, dismissal_flag=11005037)


def Event11005029():
    """ 11005029: Event 11005029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthorityu41, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005037)
    IfClient(2)
    IfFlagOn(2, 11005032)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacteru41)
    EndIfFlagOn(2)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11005032)
    IfFlagOff(1, 11005037)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1,u41)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign,u41, region=1002000, summon_flag=11005032, dismissal_flag=11005037)


def Event11005031():
    """ 11005031: Event 11005031 """
    EndIfThisEventOn()
    IfFlagOn(1, 11005032)
    IfFlagOn(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommandu41, command_id=10, slot=0)
    ReplanAIu41)
    IfCharacterInsideRegion(0,u41, region=1002998)
    RotateToFaceEntityu41, 1002997)
    ForceAnimationu41, 7410)
    AICommandu41, command_id=-1, slot=0)
    ReplanAIu41)


def Event11005033():
    """ 11005033: Event 11005033 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthorityu91, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005038)
    IfClient(2)
    IfFlagOn(2, 11005035)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacteru91)
    EndIfFlagOn(2)
    IfMultiplayerCount(condition=1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 11020607)
    IfFlagOff(1, 11005035)
    IfFlagOff(1, 11005038)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1,u91)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign,u91, region=1002002, summon_flag=11005035, dismissal_flag=11005038)


def Event11005333():
    """ 11005333: Event 11005333 """
    IfFlagOn(0, 11005035)
    AddSpecialEffectu91, 5450)


def Event11005990(arg_0_3: int, arg_4_7: int):
    """ 11005990: Event 11005990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11005036():
    """ 11005036: Event 11005036 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthorityu91, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11005038)
    IfClient(2)
    IfFlagOn(2, 11005035)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacteru91)
    EndIfFlagOn(2)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11005035)
    IfFlagOff(1, 11005038)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1,u91)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign,u91, region=1002002, summon_flag=11005035, dismissal_flag=11005038)


def Event11005034():
    """ 11005034: Event 11005034 """
    EndIfThisEventOn()
    IfFlagOn(1, 11005035)
    IfFlagOn(1, 11005393)
    IfConditionTrue(0, input_condition=1)
    AICommandu91, command_id=10, slot=0)
    ReplanAIu91)
    IfCharacterInsideRegion(0,u91, region=1002998)
    RotateToFaceEntityu91, 1002997)
    ForceAnimationu91, 7410)
    AICommandu91, command_id=-1, slot=0)
    ReplanAIu91)


def Event11005039():
    """ 11005039: Event 11005039 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11005040)
    EndIfFlagOn(2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11000810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1002005)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign,u62, region=1002001, summon_flag=11005040, dismissal_flag=11005041)
    Wait(20.0)
    Restart()


def Event11000810():
    """ 11000810: Event 11000810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11005040)
    IfFlagOff(1, 11005041)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacteru62)
    EndIfThisEventOn()
    IfCharacterDead(0,u62)
    EnableFlag(11000810)


def Event11005843(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11005843: Event 11005843 """
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOn(1, arg_0_3)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=arg_4_7, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


def Event11005844(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11005844: Event 11005844 """
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateFX(arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteFX(arg_8_11, erase_root_only=True)
    Restart()
