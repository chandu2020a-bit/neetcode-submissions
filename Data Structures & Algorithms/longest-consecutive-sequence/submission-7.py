class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        new = []
        set_nums = sorted(list(set_nums))
        if len(set_nums) == 0 :
            return 0 
        else:
            first = set_nums[0]
        longest = 0 
        j = 0 
        i = 0 
        while i < (len(set_nums)):
            if (first + j ) in set_nums :
                longest += 1 
                print(longest)
                j += 1 
            else:
                #print(longest)
                new += [longest]
                first = set_nums[i]
                i = i-1
                longest = 0
                j = 0
            i += 1 
        new += [longest]
        print(new) 
        #print(new)
        print(set_nums)
        if len(new) == 0 :
            return longest
        else:        
            return max(new) 
        