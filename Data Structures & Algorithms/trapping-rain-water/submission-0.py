class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = [0] * len(height)
        l_max = 0
        r_max = 0
        for i in range(len(height)):
            leftMax.append(l_max)
            l_max = max(l_max, height[i])
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = r_max
            r_max = max(r_max, height[i])

        res = 0
        for i in range(len(height)):
            min_height = min(leftMax[i], rightMax[i])
            if height[i] < min_height:
                res += (min_height - height[i])

        return res

