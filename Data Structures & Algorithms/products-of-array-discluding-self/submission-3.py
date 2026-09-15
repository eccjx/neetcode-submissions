class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        product = 1
        
        for i in range(len(nums)):
            pref.append(product)
            product *= nums[i]
        
        suff = []
        suff_product = 1
        for i in range(len(nums)-1, -1, -1):
            pref[i] = pref[i] * (suff_product)
            suff_product *= nums[i]
        return pref