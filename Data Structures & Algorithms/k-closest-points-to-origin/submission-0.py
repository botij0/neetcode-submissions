from collections import defaultdict


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        r = []
        index = defaultdict(list)
        for i,p in enumerate(points):           
            x,y = p
            d = math.sqrt(math.pow(x,2) + math.pow(y,2))
            r.append(d)
            index[d].append(p)

        r.sort(reverse=True)
        aux = []
        while len(r)>0 and k>0:
            d = r.pop()
            d_points = index[d]
            print(d_points)

            while len(d_points)>0:
                aux.append(d_points.pop())
                k-=1
        
        return aux