class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        pref = []
        suff = []

        for i in range(len(nums)):
            pref.append(total)
            total *= nums[i]
        
        total = 1
        
        for i in range(len(nums) - 1, -1, -1):
            pref[i] *= total
            total *= nums[i]
        return pref
