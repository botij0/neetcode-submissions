class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = paths[0][0]

        aux = {}
        for src, dst in paths:
            aux[src] = dst

        while True:
            if source not in aux:
                return source
            
            source = aux[source]