# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.aux(pairs, 0, len(pairs)-1)

    def aux(self, pairs: List[Pair], start: int, end: int):
        if end - start + 1 <= 1:
            return pairs
        
        middle = (start + end) // 2

        self.aux(pairs, start, middle)
        self.aux(pairs, middle + 1, end)

        self.merge(pairs, start, middle, end)

        return pairs


    def merge(self, array: List[Pair], start: int, middle: int, end: int):
        L = array[start : middle + 1]
        R = array[middle + 1 : end + 1]

        i = 0
        j = 0
        k = start

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            
            k += 1
        
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
