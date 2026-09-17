class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in zip(position, speed):
            t = (target - p) / s
            time.append((p,t))
        
        time.sort()

        groups = []
        while time:
            current = time.pop()
            if groups and current[1] <= groups[-1][1]:
                continue
            
            groups.append(current)

        return len(groups)