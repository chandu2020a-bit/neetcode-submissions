class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1 
        new = []
        while i<j:
            if numbers[i] + numbers[j] == target :
                print(numbers[i] + numbers[j], "equal")
                new += [i+1] + [j+1]
                break
            elif numbers[i]+ numbers[j] > target :
                print(numbers[i]+ numbers[j], "Greater")
                j -= 1

            elif numbers[i]+ numbers[j] < target :
                print(numbers[i]+ numbers[j], "lesser")
                i += 1 
        return new
        