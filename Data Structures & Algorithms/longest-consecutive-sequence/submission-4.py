class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0): return 0
        nums.sort()
        res = 0
        cur = nums[0]
        streak = 1

        for i in range(1, len(nums), 1):
            if cur + 1 == nums[i]:
                cur = nums[i]
                streak += 1
            elif cur == nums[i]:
                continue
            elif cur + 1 < nums[i]:
                cur = nums[i]
                res = max(res, streak)
                streak = 1
        res = max(res, streak)
        return res


        