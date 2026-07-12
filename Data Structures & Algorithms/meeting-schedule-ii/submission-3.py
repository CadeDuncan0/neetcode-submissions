"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = []
        endTimes = []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort() # 00 05 15
        endTimes.sort()   # 10 20 40

        print(startTimes)
        print(endTimes)

        l = 0
        r = 0
        rooms = 0
        minRooms = 0

        while l < len(startTimes):
            if startTimes[l] < endTimes[r]:
                l += 1
                rooms += 1
            else:
                r += 1
                minRooms = max(minRooms, rooms)
                rooms -= 1
            
        return max(rooms, minRooms)