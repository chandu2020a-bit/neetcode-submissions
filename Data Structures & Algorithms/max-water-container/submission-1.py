class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_prod = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            # Calculate current width and height
            width = right - left
            current_height = min(heights[left], heights[right])
            
            # Update maximum area
            current_area = current_height * width
            if current_area > max_prod:
                max_prod = current_area
                
            # Move the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_prod