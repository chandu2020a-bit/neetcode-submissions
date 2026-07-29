class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow = n
        fast = get_next(n)
        
        # Move pointers until they meet or fast reaches 1
        while fast != 1 and slow != fast:
            slow = get_next(slow)          # Moves 1 step
            fast = get_next(get_next(fast))  # Moves 2 steps
            
        return fast == 1