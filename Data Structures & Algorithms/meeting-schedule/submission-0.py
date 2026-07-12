"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        startVals = []
        endVals = []

        for val in intervals:
            startVals.append(val.start)
            endVals.append(val.end)

        startVals.sort() # 00 05 15
        endVals.sort()   # 10 20 30

        s = 0
        e = 0

        while s < len(startVals) and e < len(endVals):
            if startVals[s] < endVals[e]:
                if s > e:
                    return False
                s += 1
            else:
                e += 1

        return True
            