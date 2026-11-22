class Solution:
    def isValid(self, s: str) -> bool:
        new = []
        if len(s)%2 != 0 :
            return False
        else:
            for i in s :
                if i == "(" or i == "[" or i == "{" :
                    new.append(i)
                elif i == ")" or i == "]" or i == "}" :
                    if not new :
                        return False
                    top = new[-1]
                    if (i == ")" and top != "(") or (i == "]" and top != "[") or (i == "}" and top != "{") :
                        return False
                    new.pop()
            return not new