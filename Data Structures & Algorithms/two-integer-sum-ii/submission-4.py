class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1 
        while i<j:
            tot = numbers[i] + numbers[j]
            if tot == target :
                return [i+1, j+1]
            elif tot > target :
                j -= 1
            elif tot < target :
                i += 1       