LuaP		¶	hçõ}A@       @N:\FRPG\data\INTERROOT_x64\script\ai\out\common_logic_func.lua           z      ü      q        ¿     Í  Ë  Õ  Ó  Õ                    _COMMON_AddCautionAndFindGoal        _COMMON_AddBattleGoal        _COMMON_SetBattleActLogic        _COMMON_AddNonBattleGoal        _COMMON_EasySetup        COMMON_EasySetup3        COMMON_EzSetup                    !   "   #   $   %   &   .   .   1   1   2   2   2   2   2   2   2   5   5   8   8   8   9   9   ;   ;   ;   ;   ;   ;   ;   ;   ;   ;   @   @   @   @   @   @   A   D   D   F   F   F   G   G   I   I   I   I   I   I   I   I   I   I   N   N   N   N   N   N   O   R   R   T   T   T   W   W   X   X   X   X   X   X   X   [   [   \   \   \   \   \   \   \   \   \   \   `   `   `   `   `   `   `   `   `   b   d   d   g   g   h   h   h   h   h   p   p   p   p   r   s   t   u   v   w   w   w   w   w   w   w   w   w   w   z             ai        
       life_time               NPC_THINK_GOAL_ACTION__NONE       #       NPC_THINK_GOAL_ACTION__TURN_TO_TGT       #       NPC_THINK_GOAL_ACTION__WALK_TO_TGT       "       NPC_THINK_GOAL_ACTION__RUN_TO_TGT               NPC_THINK_GOAL_ACTION__SET_GOAL       $       NPC_THINK_GOAL_ACTION__LEAVE_TO_TGT       	       idAction              targetDist    (          targetDist .   @          targetDist F   d          idGoal i   m          life s             searchDist t             isExitWhenFindEnemy u             isRunWhenNonBattle v             arriveDistToBackHome w                           ğ?       @      @      @      @       GetReplanningGoalAction        AddTopGoal        GOAL_COMMON_Stay        TARGET_ENE_0        GetDist        GOAL_COMMON_MoveToSomewhere        AI_DIR_TYPE_CENTER       @       TARGET_SELF       *@       @       GOAL_COMMON_LeaveTarget       .@      ğ¿      4@       GetReplanningGoalID        HasTopSubgoal        GOAL_COMMON_NonBattleAct        POINT_INIT_POSE          A    Á   A @  Õ   K@ 	     E Y 	Ô  T A 	E 	V~ T K@ 
Å   E  A   Y
 K@ 
     E Y 
Ô U T A 	E 	V~ T K@ 
Å   E  A    Y
 K@ 
     E Y 
Ô Õ T A 	E 	W  K@ 
 A    E Y 
T W T K@ 
E A  E  E  Á Y
T	 K@ 
E   E     Á Y
Ô   ËC 	 	K@ 
   Y 
 D 	 	X	 Á 	Á 
      K@ Å           Y                C                                                                                                            ¢   ¢   ¢   ¢   £   £   £   ¦   ¦   ¦   ¦   ¦   ¨   ¨   ¨   ¨   ©   ©   ©   ¬   ¬   ¬   ¬   ¬   ¯   ¯   ¯   ²   ²   ²   ²   ü             ai     B          battleGoalId    B                 GetExcelParam (       AI_EXCEL_THINK_PARAM_TYPE__battleGoalID        IsChangeState        IsBattleState        TeamHelp_IsValidCall        AddTopGoal        GOAL_COMMON_TeamCallHelp       $@       TARGET_SELF        IsCautionState        ReqPlatoonState        PLATOON_STATE_Battle       ğ?      ğ¿       PLATOON_STATE_Caution        _COMMON_AddCautionAndFindGoal        PLATOON_STATE_Find     C   > E  ?   Ô K?   T ?   Ô Ë?  Á  YT Ë@      ?    Ë?  Á  YK?   Ô A Å YË?   A Y  Ë@   Ô A  YÅ    A Y A  YÅ    A Y              l                                                                         !  !  !  $  $  $  %  %  %  '  '  (  (  (  +  +  .  .  .  .  .  .  /  /  /  2  2  4  4  6  6  6  8  8  9  9  9  ?  ?  ?  ?  ?  ?  @  @  A  M  M  N  N  O  O  O  _  _  _  _  _  _  `  `  f  k  k  k  k  k  k  l  l  p  p  q            ai     k          funcBattle     k          funcNonBattle     k          maxBackhomeDist    k          backhomeDist    k          backhomeBattleDist 	   k          nonBattleActLife    k          behaviorTime              isFindTarget )   i   
       pointDist .   `          targetDist 1   `                 GetExcelParam +       AI_EXCEL_THINK_PARAM_TYPE__maxBackhomeDist (       AI_EXCEL_THINK_PARAM_TYPE__backhomeDist .       AI_EXCEL_THINK_PARAM_TYPE__backhomeBattleDist ,       AI_EXCEL_THINK_PARAM_TYPE__nonBattleActLife        TeamHelp_IsValidReply 8       AI_EXCEL_THINK_PARAM_TYPE__callHelp_ForgetTimeByArrival        AddTopGoal        GOAL_COMMON_TeamReplyHelp        IsForceBattleGoal        ClearForceBattleGoal        ReqPlatoonState        PLATOON_STATE_Battle        IsSearchTarget        TARGET_ENE_0        GetMovePointEffectRange        GetDist       ğ?      ğ¿    l   > E  >   > Å  >  Ë?  T >  	K@  
 Y    Ë@  Ô A Y KA  	Y  Y  ËA  	   KB  B 	 	    
       Y
 
 
   V Ô KA 
 Y
  
Y 
 
 
   
      Y
 
 
Ô     
Y 
 
 
   
        Y
 
 
Ô    	 
   Y                                                                ai               life               search_dist               isFoundTarget               runNonBattle               nonBattleBackhomeDist               isEnableForceBattleGoal                      TeamHelp_ValidateCall        TeamHelp_ValidateReply        AddTopGoal        GOAL_COMMON_NonBattleAct        POINT_INIT_POSE                > Y Ë> Y ? Å  	  
        A   Y                  ­  ­  ­  ¶  ·  ¸  ¸  ¹  ¹  ¹  ¹  ¶  ¼  ¼  ¼  ½  ½  ½  ½  ½  ½  ½  ½  ½  ½  ¿            ai               isRunNonBattle               nonBattleBackhomeDist               battleGoalId              bSet           	          GetExcelParam (       AI_EXCEL_THINK_PARAM_TYPE__battleGoalID        _COMMON_SetBattleActLogic        AddTopGoal        GOAL_COMMON_NonBattleAct       ğ?      ğ¿               POINT_INIT_POSE            ¸       ¸  ¸  ¸  ¸                ai           _COMMON_AddBattleGoal             Y            ¹   
   ¹  ¹  ¹  ¹  ¹  ¹  ¹  ¹  ¹  ¹            life     	          search_dist     	          isFoundTarget     	          isEnableForceBattleGoal     	             ai        isRunNonBattle        nonBattleBackhomeDist           _COMMON_AddNonBattleGoal     
               	 
 Y      > E       "      b               U T K?    	 
Á Á  Á Y           Ë       Ì  Ì  Ì  Ì  Ì  Í            ai                      _COMMON_EasySetup                       A  Y           Ó       Ô  Ô  Ô  Ô  Ô  Õ            ai                      _COMMON_EasySetup                       A  Y      "      b   G   ¢      â   Ç   "    b  G  ¢      