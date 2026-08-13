class Solution:
    def countBits(self, n: int) -> List[int]:
        si = []
        for j in range(n+1):
            count = 0
            i = j
            while i > 0:
                count += i & 1
                i = i >> 1
            si += [count]
        return si