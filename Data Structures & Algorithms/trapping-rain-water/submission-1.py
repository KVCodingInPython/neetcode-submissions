class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        
        max_left = [0] * n
        max_right = [0] * n
        
        # Build max_left prefix array
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
            
        # Build max_right suffix array
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
            
        # Calculate water at each position
        water_trapped = 0
        for i in range(n):
            water_trapped += min(max_left[i], max_right[i]) - height[i]
            
        return water_trapped
            

