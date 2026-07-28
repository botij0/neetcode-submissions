class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]
            elif end < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
                
        result.append(newInterval)
        return result
    
    def mine(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]

        for interval in intervals:
            if interval[0] <= start <= interval[1]:
                start = interval[0]
                end = max(interval[1], end)
            
            if interval[0] <= end <= interval[1]:
                end = interval[1]
            
        
        r = []
        inserted = False

        for interval in intervals:
            if inserted:
                r.append(interval)
                continue

            if interval[1] < start:
                r.append(interval)
            elif interval[0] > end:
                r.append([start, end])
                r.append(interval)
                inserted = True

        if not inserted:
            r.append([start, end])

        return r

