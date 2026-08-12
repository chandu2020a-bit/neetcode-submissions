class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new = set()
        for i in nums :
            if i not in new :
                new.add(i)
            elif i in new :
                new.remove(i)
        return list(new)[0]
        