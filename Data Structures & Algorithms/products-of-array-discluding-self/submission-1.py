class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math 
        
        new_l = []
        for i in range(len(nums)):
            prod = 1 
            j = 0 
            while j < len(nums):
                if i == j :
                    j += 1
                    continue 
                else:
                    prod *= nums[j]
                    #print(prod)
                    j += 1 
            #print("final prod", prod)
            new_l += [prod]
        return new_l 
        