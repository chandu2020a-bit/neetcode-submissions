class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slo = 0
        fa = 0

        while True:
            slo = nums[slo]
            fa = nums[nums[fa]]
            if slo == fa :
                break
        
        slo = 0 
        while slo != fa :
            slo = nums[slo]
            fa = nums[fa]

        return slo