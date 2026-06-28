class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_l = []
        flag = False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target :
                    new_l += [i] 
                    new_l += [j]
                    flag = True
                    break
            if flag:
                break
        return (new_l)
        