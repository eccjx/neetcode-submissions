class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #For each index, we need the product of all elements before it and all elements after it.
        pref = defaultdict(int)
        post = defaultdict(int)
        output_pref = 1
        output_post = 1
        for i in range(len(nums)):
            if i == 0:
                pref[i] = 1
            else:
                pref[i] = output_pref
            output_pref *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                post[i] = 1
            else:
                post[i] = output_post
            output_post *= nums[i]
        res = []
        for i in range(len(nums)):
            product = pref[i] * post[i]
            res.append(product)
        return res
        