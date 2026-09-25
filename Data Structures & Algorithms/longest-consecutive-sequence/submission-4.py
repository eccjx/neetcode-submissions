class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 1
        cur_len = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 1:
                cur_len += 1
                res = max(res, cur_len)
            elif diff == 0:
                continue
            else:
                res = max(res, cur_len)
                cur_len = 1
        res = min(res, len(nums))
        return res
