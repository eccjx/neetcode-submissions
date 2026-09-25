class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = [0] * len(height)

        l_max = 0
        for num in height:
            leftMax.append(l_max)
            l_max = max(l_max, num)
        
        r_max = 0
        for r in range(len(height)-1, -1, -1):
            rightMax[r] = r_max
            r_max = max(r_max, height[r])
        
        
        res = 0
        for i in range(len(height)):
            min_height_i = min(rightMax[i], leftMax[i])
            if height[i] >= min_height_i:
                continue
            else:
                res += min_height_i - height[i]
        return res