class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        L = 0
        R = len(arr)-1
        result = []

        while L <= R:
            mid = (L + R)//2

            if arr[mid] == mid:
                result.append(mid)
                R = mid -1
            elif arr[mid] > mid:
                R = mid - 1
            else: 
                L = mid + 1
        
        return -1 if not result else result [-1]
