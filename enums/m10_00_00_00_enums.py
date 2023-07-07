from soulstruct.darksouls1ptde.game_types import *

from soulstruct.darksouls1r.game_types import *


class Characters(Character):
    Domnhall = 6260
    SolaireSummon = 6541
    KnightKirkInvader = 6562

    GapingDragon = 1000800


class Flags(Flag):
    GapingDragonIntroCutsceneDone = 11000000
    GapingDragonDefeated = 11000001
    GravelordInvasionTrigger = 11000050
    CheckpointFog1Entered = 11000090
    ShortcutDoorOpened = 11000100
    ShortcutDoorWrongSide = 11000101
    OpenBlighttownDoor = 11000110
    BlighttownDoorLocked = 11000111
    ShowDoorUnlockedMessage = 11000120
    BasiliskRunningDone = 11000200
    AggroNPC = 11000510
    BreakLaurentiusFromPot = 11000530
    LaurentiusMovesOn = 11000531
    DomnhallMovesOn = 11000532
    DomnhallKilled = 11000533
    LaurentiusInvincibleInPot = 11000534
    LaurentiusFreedFromPot = 11000580
    OpenChest = 11000600
    GiantRatDead = 11000800
    KirkInvaderKilled = 11000810
    NoRespawn = 11000850
    Bonfire1BaseFlag = 11000992
    TinyRatsScurry = 11005000
    PlaceGoldSolaireSummonSign = 11005029
    PlaceSolaireSummonSign = 11005030
    SolaireSummoned = 11005032
    PlaceLautrecSummonSign = 11005033
    LautrecEntersGapingDragonFog = 11005034
    LautrecSummoned = 11005035
    PlaceGoldLautrecSummonSign = 11005036
    SolaireDismissed = 11005037
    LautrecDismissed = 11005038
    KirkInvaded = 11005040
    KirkRetreated = 11005041
    ChoppingButcherAggro = 11005050
    ChoppingButcherMeatVFX = 11005060
    ButcherDropAmbush = 11005070
    EnableGravelordPhantoms = 11005080
    DefeatGravelordInvader = 11005081
    GravelordInvasionTimer = 11005082
    CeilingSlimeAmbush = 11005100
    RatAmbushFromBox = 11005150
    RegionAITrigger = 11005200
    BuffLautrecSummon = 11005333
    HostEnteredGapingDragonFog = 11005390
    ClientEnteredGapingDragonFog = 11005391
    GapingDragonBattleActive = 11005392
    GapingDragonBattleNotified = 11005393
    GapingDragonMusicStarted = 11005394
    GapingDragonMusicStopped = 11005395
    GapingDragonTailCut = 11005396
    GapingDragonUnknownBodyPart = 11005397
    GapingDragonHeadHit = 11005398
    EraseSummonSign = 11005990


class RegionVolumes(RegionVolume):
    GapingDragonArena = 1002999


class Objects(Object):
    """`Object` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Object.auto_generate(ID_RANGES, count, 1000000)

    o0100_0000 = 1001900
    o0100_0001 = 1001901
    o0100_0002 = 1001902
    o0100_0003 = 1001903
    o0100_0004 = 1001904
    o0100_0005 = 1001905
    o0100_0006 = 1001906
    o0100_0007 = 1001907
    o0110_0000 = 1001650
    o0200_0000 = 1001960
    o1002_01 = 1001400
    o1155 = 1001250
    o1205 = 1001140
    o1309 = 1001200
    o1315_0000 = 1001315
    o1319_0000 = 1001319
    o1322_0002 = 1001100
    o1322_0005 = 1001101
    o1322_0006 = 1001102
    o1340_0000 = 1001000
    o1340_0001 = 1001001
    o1340_0002 = 1001002
    o1400_0000 = 1001990
    o1401_0000 = 1001994
    o1402_0000 = 1001996
    o1420_0000 = 1001700


class Characters(Character):
    """`Character` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Character.auto_generate(ID_RANGES, count, 1000000)

    c0000_0002 = 6130
    c0000_0004 = 6260
    c0000_0005 = 6541
    c0000_0006 = 6562
    c0000_0007 = 6591
    c0000_ano1 = 62884
    c1000_0000 = 1000960
    c1201_0000 = 1000150
    c1201_0001 = 1000151
    c1201_0002 = 1000152
    c1201_0018 = 1000906
    c1201_0019 = 1000907
    c1201_0020 = 1000908
    c1201_0021 = 1000909
    c1201_0022 = 1000910
    c1201_0023 = 1000911
    c1201_0024 = 1000912
    c1201_0025 = 1000913
    c1202_0000 = 1000500
    c2370_0000 = 1000300
    c2370_chn1 = 1000301
    c2500_0003 = 1000120
    c2500_0004 = 1000121
    c2500_0005 = 1000122
    c2500_0006 = 1000123
    c2500_0007 = 1000124
    c2500_0008 = 1000125
    c2500_0009 = 1000126
    c2500_0012 = 1000900
    c2500_0013 = 1000901
    c2500_0014 = 1000902
    c2500_0015 = 1000903
    c2500_0016 = 1000904
    c2660_0000 = 1000099
    c2660_0001 = 1000090
    c2660_0002 = 1000905
    c3200_0000 = 1000100
    c3200_0001 = 1000101
    c3200_0002 = 1000102
    c3200_0003 = 1000103
    c3200_0004 = 1000104
    c3200_0005 = 1000105
    c3200_0006 = 1000106
    c3200_0007 = 1000107
    c3200_slm1 = 1000999
    c3200_slm2 = 1000998
    c3200_slm3 = 1000997
    c3200_slm4 = 1000996
    c3200_slm5 = 1000995
    c3270_0000 = 1000200
    c3270_0006 = 1000210
    c3340_0000 = 1000111
    c3340_0001 = 1000112
    c3340_0002 = 1000110
    c3340_0003 = 1000113
    c3490_0000 = 1003900
    c3490_0001 = 1003910
    c3491_0000 = 1003901
    c3491_0001 = 1003911
    c3491_0002 = 1003902
    c3491_0003 = 1003912
    c5260_0000 = 1000800
    c5261_0000 = 1000801


class PlayerStarts(PlayerStart):
    """`PlayerStart` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return PlayerStart.auto_generate(ID_RANGES, count, 1000000)

    c0000_0001 = 1000999


class Collisions(Collision):
    """`Collision` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return Collision.auto_generate(ID_RANGES, count, 1000000)

    h0053B0_0001 = 1003000


class Sounds(SoundEvent):
    """`SoundEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SoundEvent.auto_generate(ID_RANGES, count, 1000000)

    GapingDragonMusic = 1003800


class VFX(VFXEvent):
    """`VFXEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return VFXEvent.auto_generate(ID_RANGES, count, 1000000)

    BossEntranceFog = 1001991
    CheckpointFog1 = 1001701
    MultiplayerFog1 = 1001995
    MultiplayerFog2 = 1001997


class SpawnPoints(SpawnPointEvent):
    """`SpawnPointEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return SpawnPointEvent.auto_generate(ID_RANGES, count, 1000000)

    SpawnPoint0 = 1002960
    SpawnPoint1 = 1002961
    SpawnPointAtBoss = 1002950


class Navigation(NavigationEvent):
    """`NavigationEvent` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return NavigationEvent.auto_generate(ID_RANGES, count, 1000000)

    InvaderSpawn00 = 1004000
    InvaderSpawn01 = 1004001
    Navmesh_Door02 = 1004002


class Points(RegionPoint):
    """`RegionPoint` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionPoint.auto_generate(ID_RANGES, count, 1000000)

    KirkInvaderSpawn = 1002001
    LautrecSummonSign = 1002002
    SolaireSummonSign = 1002000


class Boxes(RegionBox):
    """`RegionBox` entity IDs for MSB and EVS use."""

    # noinspection PyMethodParameters
    def _generate_next_value_(name, _, count, __):
        return RegionBox.auto_generate(ID_RANGES, count, 1000000)

    BasiliskMovementTrigger1 = 1002010
    BasiliskMovementTrigger2 = 1002011
    ButcherAmbushTrigger = 1002200
    CheckpointFog1BackSide = 1002601
    CheckpointFog1FrontSide = 1002600
    DepthsSlideCollision = 1003100
    GapingDragonCombatStart = 1002996
    GapingDragonCutsceneTrigger = 1002999
    GapingDragonFogPrompt = 1002998
    GapingDragonFogRotationTarget = 1002997
    GapingDragonMusic = 1002990
    GiantRatArena = 1002704
    GiantRatNest = 1002703
    GiantRatTurnsBack0 = 1002700
    GiantRatTurnsBack1 = 1002701
    GiantRatTurnsBack2 = 1002702
    HierarchyA = 1002020
    HierarchyB = 1002021
    HierarchyC = 1002022
    InvaderSpawn00 = 1004000
    InvaderSpawn01 = 1004001
    InvaderSpawn10 = 1004010
    InvaderSpawn11 = 1004011
    KirkInvaderTrigger = 1002005
    Slime0AmbushTrigger = 1002100
    Slime1AmbushTrigger = 1002101
    Slime2_3AmbushTrigger = 1002102
    Slime4_5_6AmbushTrigger = 1002103
    Slime7AmbushTrigger = 1002107
    SlimesProhibited = 1002800
    UnusedDepthsMapNameDisplay = 1022703
