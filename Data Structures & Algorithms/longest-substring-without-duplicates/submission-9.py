class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0 
        max_leng = 0 

        for index, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1 
            
            seen[char] = index 
            max_leng = max(max_leng, index- start+1)
        return max_leng