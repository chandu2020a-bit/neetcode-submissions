class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for i in strs:
            str1 += str(len(i)) + "#" + i 
        print(str1)
        return str1
        

    def decode(self, s: str) -> List[str]:
        
            new_l = []
            
            i = 0
            while i < len(s):
                j = i 
                while s[j] != "#":
                    j += 1 
                length = int(s[i:j])
                j += 1 
                new_l += [s[j:j + length]]
                i = j+length
                
            return (new_l)
