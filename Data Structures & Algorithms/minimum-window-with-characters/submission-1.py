class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Dictionary to keep a count of all the unique characters in t
        dict_t = Counter(t)
        
        # Number of unique characters in t that need to be present in the desired window
        required = len(dict_t)
        
        # Left and Right pointers
        left, right = 0, 0
        
        # Total unique characters in the current window that match the required count in t
        formed = 0
        
        # Dictionary to keep track of all the unique characters in the current window
        window_counts = {}
        
        # (window length, left pointer, right pointer)
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add one character from the right to the window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the frequency of the current character matches its frequency in t, 
            # increment the formed count
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Try to contract the window till the point where it ceases to be 'valid'
            while left <= right and formed == required:
                char = s[left]
                
                # Save the smallest window so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # The character at the position pointer by the 'left' pointer is being removed from the window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                # Move the left pointer forward to look for a new window
                left += 1    
            
            # Move the right pointer forward to look for a new window
            right += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]