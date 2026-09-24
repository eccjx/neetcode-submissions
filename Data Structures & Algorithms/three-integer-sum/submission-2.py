class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                
                cur_total = nums[i] + nums[l] + nums[r]
                if cur_total == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif cur_total < 0:
                    l += 1
                else:
                    r -= 1
        return res
            