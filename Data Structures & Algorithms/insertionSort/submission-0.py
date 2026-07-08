# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        n = len(pairs)
        
        # Handle the edge case of an empty input list
        if n == 0:
            return res

        # Outer loop iterates through each element to be inserted
        for i in range(n):
            j = i
            # Move the element backwards into its correct sorted position
            # Use strict inequality '>' to maintain stability (stable sort)
            while j > 0 and pairs[j - 1].key > pairs[j].key:
                # Swap elements
                pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                j -= 1
            
            # Create a shallow copy of the current state of the array
            res.append(list(pairs))
            
        return res