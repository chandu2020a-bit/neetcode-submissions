class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_1 = dict()
        for i in strs:
            key = "".join(sorted(i))
            if key not in dict_1:
                dict_1[key] = [i]
            else:
                dict_1[key].append(i)
        return list(dict_1.values())

        