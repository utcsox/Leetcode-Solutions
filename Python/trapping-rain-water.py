class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left, max_right, l, r = [0] * len(height), [0] * len(height), 0, 0

        for i in range(len(height)):
            j = len(height) - 1 - i

            max_left[i] = l
            max_right[j] = r

            l = max(l, height[i])
            r = max(r, height[j])
            
        res = 0

        for i in range(len(height)):
            res += max(0, min(max_left[i], max_right[i]) - height[i])

        return res
