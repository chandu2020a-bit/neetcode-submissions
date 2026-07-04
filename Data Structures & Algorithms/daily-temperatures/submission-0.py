class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new = []
        flag = True
        for i in range(len(temperatures)):
            count1 = 0
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    new += [count1]
                    print(temperatures[i], count1)
                    count1 = 0
                    flag = False
                    break
                else:
                    count1 += 1
                flag = True
            if flag :
                new += [0] 
            print(temperatures[i], count1)
        return (new)