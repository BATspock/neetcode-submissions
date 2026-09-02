class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = [0]*len(height), [0]*len(height)
        left_max, right_max = 0, 0
        for i in range(1, len(height)):
            left_max = max(left_max, height[i-1])
            left[i] = left_max

        for i in range(len(height)-2, -1, -1):
            right_max = max(right_max, height[i+1])
            right[i] = right_max


        area = 0
        for i in range(len(height)):
            if (min(left[i],right[i]) - height[i] > 0):
                area+= min(left[i],right[i]) - height[i]

        return area