class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sym = ["+", "-", "*", "/"]
        new = []
        if len(tokens) == 1 :
            return int(tokens[-1])
        else:
            for i in tokens :
                if i not in sym:
                    new.append(i)
                else:
                    if i == "+":
                        ele1 = new.pop()
                        ele2 = new.pop()
                        ans = int(ele2) + int(ele1)
                        new.append(ans)
                    elif i == "-":
                        ele1 = new.pop()
                        ele2 = new.pop()
                        ans = int(ele2) - int(ele1)
                        new.append(ans)
                    elif i == "*":
                        ele1 = new.pop()
                        ele2 = new.pop()
                        ans = int(ele2) * int(ele1)
                        new.append(ans)
                    elif i == "/":
                        ele1 = new.pop()
                        ele2 = new.pop()
                        ans = int(ele2) / int(ele1)
                        new.append(ans)
            return int(new[-1])