class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr) - 1
        for i in range(l):
            m = max(arr[i+1:])
            arr[i] = m
        arr[l]=-1
        return arr