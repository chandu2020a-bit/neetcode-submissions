class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            # Check if the lowest bit is 1
            count += n & 1
            # Shift right by 1 bit to process the next position
            n = n >> 1
        return count
        