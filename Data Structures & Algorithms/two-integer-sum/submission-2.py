class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}
        for i in range(len(nums)):
            
            res = target - nums[i]
            if res in res_dict:
                return [res_dict[res], i]
            else:
                res_dict[nums[i]] = i