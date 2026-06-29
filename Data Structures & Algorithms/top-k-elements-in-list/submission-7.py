class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_1 = dict()
        for i in nums :
            if i in dict_1 :
                dict_1[i] += 1 
            else:
                dict_1[i] = 1
        print(dict_1)
        sorted_dict = sorted(dict_1.keys(), key=lambda x:dict_1[x], reverse=True)
        return sorted_dict[:k]