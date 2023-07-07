

REGISTER_GOAL(GOAL_HaikaiDemon230000_Battle, "HaikaiDemon230000Battle")

local Att3000_Dist_min = 0
local Att3000_Dist_max = 3.8
local Att3002_Dist_min = 0
local Att3002_Dist_max = 4
local Att3003_Dist_min = 0
local Att3003_Dist_max = 8
local Att3005_Dist_min = 0
local Att3005_Dist_max = 7.5
local Att3006_Dist_min = -1.3
local Att3006_Dist_max = 0
local Att3007_Dist_min = 6.5
local Att3007_Dist_max = 8.7
local Att3008_Dist_min = 11.8
local Att3008_Dist_max = 13.5
local Att3009_Dist_min = 5.5
local Att3009_Dist_max = 25

REGISTER_GOAL_NO_UPDATE(GOAL_HaikaiDemon230000_Battle, 1)

function HaikaiDemon230000Battle_Activate(ai, goal)
	
   local role = ai:GetTeamOrder(ORDER_TYPE_Role)
   local myThinkId = ai:GetNpcThinkParamID()
   local targetDist = ai:GetDist(TARGET_ENE_0)
   local hprate = ai:GetHpRate(TARGET_SELF)
   local fate = ai:GetRandam_Int(1, 100)
   local fate2 = ai:GetRandam_Int(1, 100)
   local fate3 = ai:GetRandam_Int(1, 100)
   local GetWellSpace_Odds = 0
   local Act01Per = 0
   local Act02Per = 0
   local Act03Per = 0
   local Act04Per = 0
   local Act05Per = 0
   local Act06Per = 0
   local Act07Per = 0
   local CanStep = 1
   local LJump = 1
   
    if targetDist <= 0.8 then
        Act04Per = 85
        Act05Per = 15
    elseif targetDist >= 12.3 then
        Act01Per = 5
        Act02Per = 10
        Act04Per = 75
        Act06Per = 10
    elseif targetDist >= 7 then
        Act02Per = 40
        Act03Per = 5
        Act04Per = 40
        Act06Per = 15
    elseif targetDist >= 4 then
        Act01Per = 55
        Act02Per = 25
        Act03Per = 20
    elseif targetDist >= 2.2 then
        Act01Per = 70
        Act03Per = 20
        Act05Per = 10
    else
        Act01Per = 55
        Act03Per = 15
        Act05Per = 30
    end
	
	local fateAct = ai:GetRandam_Int(1, Act01Per + Act02Per + Act03Per + Act04Per + Act05Per + Act06Per + Act07Per)
	
	if fateAct <= Act01Per then
		goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, Att3000_Dist_max, TARGET_SELF, false, -1)
		if fate <= 10 then
			goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 70)
		elseif fate <= 50 then
			goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 70)
			goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
		else
			goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 70)
			goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
			goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
		end
		GetWellSpace_Odds = 100
	elseif fateAct <= Act01Per + Act02Per then
        goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, Att3003_Dist_max, TARGET_SELF, false, -1)
        if fate <= 10 then
			goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 70)
        elseif fate <= 50 then
            goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 70)
            goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
        else
            goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 70)
            goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
            goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
        end
        GetWellSpace_Odds = 100
    elseif fateAct <= Act01Per + Act02Per + Act03Per then
        goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, Att3006_Dist_max, TARGET_SELF, false, -1)
        goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
        GetWellSpace_Odds = 100
    elseif fateAct <= Act01Per + Act02Per + Act03Per + Act04Per then
        if Att3008_Dist_min <= targetDist and fate <= 40 and LJump == 1 then
            goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, Att3008_Dist_max, TARGET_SELF, false, -1)
            goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
            GetWellSpace_Odds = 100
        else
            goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, Att3007_Dist_max, TARGET_SELF, false, -1)
            goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3007, TARGET_ENE_0, DIST_Middle, 0)
            GetWellSpace_Odds = 100
        end
    elseif fateAct <= Act01Per + Act02Per + Act03Per + Act04Per + Act05Per then
        goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0)
        GetWellSpace_Odds = 0
	elseif fateAct <= Act01Per + Act02Per + Act03Per + Act04Per + Act05Per + Act06Per then
        goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
        if myThinkId == 230003 then
            goal:AddSubGoal(GOAL_COMMON_SidewayMove, 10, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(15, 30), true, true, -1)
        end
        GetWellSpace_Odds = 0
    elseif myThinkId == 230003 then
        ai:SetEventMoveTarget(1012798)
        goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, POINT_EVENT, 1, TARGET_ENE_0, True, -1)
    else
        goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, POINT_INITIAL, 1, TARGET_ENE_0, True, -1)
    end

    local fateGWS = ai:GetRandam_Int(1, 100)

    if fateGWS <= GetWellSpace_Odds and CanStep == 1 then
        local Odds_Guard = 0
        local Odds_NoAct = 70
        local Odds_BackAndSide = 0
        local Odds_Back = 0
        local Odds_BitWait = 0
        local Odds_Backstep = 30
        GetWellSpace_Act(ai, goal, Odds_Guard, Odds_NoAct, Odds_BackAndSide, Odds_Back, Odds_BitWait, Odds_Backstep)
    end
	
end

function HaikaiDemon230000Battle_Update(ai, goal) 

	return GOAL_RESULT_Continue

end

function HaikaiDemon230000Battle_Terminate(ai, goal)
end

HaikaiDemon230000Battle_Interupt = function(ai, goal)

   local fate = ai:GetRandam_Int(1, 100)
   local fate2 = ai:GetRandam_Int(1, 100)
   local fate3 = ai:GetRandam_Int(1, 100)
   local targetDist = ai:GetDist(TARGET_ENE_0)
   local distDamagedStep = 3
   local oddsDamagedStep = 15
   local bkStepPer = 100
   local leftStepPer = 0
   local rightStepPer = 0
   local safetyDist = 6

   if Damaged_Step(ai, goal, distDamagedStep, oddsDamagedStep, bkStepPer, leftStepPer, rightStepPer, safetyDist) then
      return true
   end

   local distGuardBreak_Attack = 4.3
   local oddsGuardBreak_Attack = 60
   local AttID = 3000

   if GuardBreak_Attack(ai, goal, distGuardBreak_Attack, oddsGuardBreak_Attack, AttID) then
      return true
   end

   local distUseItem_Act = 9.5
   local oddsUseItem_Act = 15

   if UseItem_Act(ai, goal, distUseItem_Act, oddsUseItem_Act) then
      if targetDist >= 4.4 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end

   local oddsResponse = 20
   local bkStepPer = 100
   local leftStepPer = 0
   local rightStepPer = 0
   local safetyDist = 6

   if RebByOpGuard_Step(ai, goal, oddsResponse, bkStepPer, leftStepPer, rightStepPer, safetyDist) then
      return true
   end

   return false

end
