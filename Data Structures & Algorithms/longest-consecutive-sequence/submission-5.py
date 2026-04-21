class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 0
        nums.sort()
        res = 0
        cur = nums[0]
        streak = 0
        i = 0
        
        while i < len(nums):
            if cur != nums[i]:
                cur = nums[i]
                streak = 0
    
            while i < len(nums) and nums[i] == cur:
                i += 1

            streak += 1
            cur += 1
            res = max(res, streak)
            
        return res


        