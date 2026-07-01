class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new = []
        flag = False
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target :
                    new += [i+1] + [j+1]
                    flag = True
                    break
                if flag:
                    break
        return new 
        