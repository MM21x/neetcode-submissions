class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0 
        best_streak = 0
        for num in nums:
            if num == 1:
                current_streak = current_streak + 1 #or += 1
                if current_streak > best_streak:
                    best_streak = current_streak
        
            elif num == 0:
                current_streak = 0
            #elif can be else here
        return  best_streak