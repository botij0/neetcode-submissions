class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            
            value_to_move = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value_to_move)
        
        l_small = len(self.small)
        l_large = len(self.large)
        
        if l_small > l_large + 1:
            value_to_move = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value_to_move)

        if l_large > l_small + 1:
            value_to_move = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * value_to_move)
        


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return ((-1 * self.small[0]) + self.large[0]) / 2
        