"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # if intervals is sorted by start times we can start at the 2nd interval
        # if the start interval is less than the previous end time it's overlapping
        # so return false, otherwise continue executing the loop

        # return true if make it to the end
        intervals.sort(key=lambda x: x.start)

        prevEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < prevEnd:
                return False
            else:
                prevEnd = intervals[i].end
        
        return True