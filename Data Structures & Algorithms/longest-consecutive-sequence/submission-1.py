class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            cnt = 1
            max_tmp = nums[i]
            for j in range(i+1, len(nums), 1):
                if nums[j] - max_tmp == 1 : 
                    cnt += 1
                    max_tmp = nums[j]
                elif nums[j] - max_tmp > 1:
                    break
            result = max(result, cnt)
        return result


        