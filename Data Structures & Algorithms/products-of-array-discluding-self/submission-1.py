class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
                continue
            total_product *= num
        res = []
        for num in nums:
            if num == 0:
                if zero_counter > 1:
                    res.append(0)
                    continue
                res.append(total_product)
            else:
                if zero_counter > 0:
                    res.append(0)
                else:

                    res.append(int(total_product / num))
        return res