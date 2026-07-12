"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        r = []
        for n in intervals:
            (s, e) = n.start, n.end
            r.append((s,e))

        r.sort()
        print(r)
        curr = r[0]
        for i in range(1, len(r)):
            n = r[i]
            if n[0] < curr[1]:
                return False
            curr = n

        return True