class Solution:
    def findMin(self, nums: List[int]) -> int:
        min1 = nums[0]
        if nums == sorted(nums):
            return min1 
        else:
            for i in range(len(nums)):
                if min1 > nums[i]:
                    min1 = nums[i]

            return min1        