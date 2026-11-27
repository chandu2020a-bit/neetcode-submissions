class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for i in s :
            if i.isalpha() :
                new += [i.lower()]
            elif i.isdigit():
                new += [i]
        return new == new[::-1]
        