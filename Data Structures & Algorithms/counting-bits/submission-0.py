class Solution:
    def countBits(self, n: int) -> List[int]:
        si = []
        for j in range(n+1):
            count = 0
            i = j
            while i > 0:
                # Check if the lowest bit is 1
                count += i & 1
                # Shift right by 1 bit to process the next position
                i = i >> 1
            si += [count]
        return si