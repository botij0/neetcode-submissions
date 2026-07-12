"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        r = []
        for n in intervals:
            (s, e) = n.start, n.end
            r.append((s,e))

        r.sort()

        for i in range(1, len(r)):
            curr = r[i-1]
            n = r[i]
            if n[0] < curr[1]:
                return False

        return True