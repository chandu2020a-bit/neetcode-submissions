class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores indices: (index)
        max_area = 0
        
        # Append a 0 at the end to flush out remaining elements in the stack
        heights.append(0)
        
        for i, h in enumerate(heights):
            # Maintain a monotonic increasing stack
            while stack and heights[stack[-1]] > h:
                # Pop the bar that serves as the height of the rectangle
                height_idx = stack.pop()
                height = heights[height_idx]
                
                # If stack is empty, it means 'height' was the smallest bar seen so far
                # Width spans from index 0 to i
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        # Restore the array modifications (good practice)
        heights.pop()
        
        return max_area