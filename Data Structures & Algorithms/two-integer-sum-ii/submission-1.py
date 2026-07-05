class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1

        while p1 < p2:
            current = numbers[p1] + numbers[p2]

            if current == target:
                return [p1 + 1, p2 + 1]

            if current > target:
                p2 -= 1
            else:
                p1 += 1
        