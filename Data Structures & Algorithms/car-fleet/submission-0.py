class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = 0 
        current = 0.0
        for po, sp in cars :
            time = (target-po)/sp
            if time > current :
                fleets += 1 
                current = time 
        return fleets