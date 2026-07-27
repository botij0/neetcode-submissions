class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # return self.bruteForce(gas, cost)
        return self.greedy(gas, cost)

    def greedy(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        L = len(gas)
        currentGas = 0

        for i in range(L):
            currentGas += gas[i]
            currentGas -= cost[i]

            if currentGas < 0:
                currentGas = 0
                start = i + 1
        
        return start

    def bruteForce(self, gas: List[int], cost: List[int]) -> int:
        startOptions = []
        m = 0
        L = len(gas)

        for i in range(L):
            aux = gas[i] - cost[i]
            if  aux >= 0:
                startOptions.append(i)
                m = aux
        

        for start in startOptions:
            visited = set()
            currentGas = gas[start]
            r = 0

            while start not in visited:
                visited.add(start)

                currentGas = currentGas - cost[start]
                if currentGas < 0:
                    r = -1
                    break
                
                start = (start + 1) % L
                currentGas += gas[start]
            
            if r == 0:
                return start
            
        return -1