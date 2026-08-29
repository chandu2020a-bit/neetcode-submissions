class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Shift the result left to make room for the next bit
            result <<= 1
            # Extract the lowest bit of n and add it to result
            result |= (n & 1)
            # Shift n right to process the next bit
            n >>= 1
        return result