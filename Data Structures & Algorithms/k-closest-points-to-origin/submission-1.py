from collections import defaultdict


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # My Version:
        # r = []
        # index = defaultdict(list)
        # for i,p in enumerate(points):           
        #     x,y = p
        #     d = math.sqrt(math.pow(x,2) + math.pow(y,2))
        #     r.append(d)
        #     index[d].append(p)

        # r.sort(reverse=True)
        # aux = []
        # while len(r)>0 and k>0:
        #     d = r.pop()
        #     d_points = index[d]
        #     print(d_points)

        #     while len(d_points)>0:
        #         aux.append(d_points.pop())
        #         k-=1
        
        # return aux

        heap=[]
        for i in points:
            heap.append([self.getDistance(i),i])
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

    def getDistance(self, point: List[int]) -> int :
        return (point[0]**2 + point[1]**2)**(1/2)