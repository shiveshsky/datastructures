class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return f"[{self.start, self.end}]"


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        new_arr = []
        new_arr.append(intervals[0])
        for i in range(1, len(intervals)):
            if new_arr[-1].start <= intervals[i].start <= new_arr[-1].end:
                new_arr[-1].end = max(intervals[i].end, new_arr[-1].end)
            else:
                new_arr.append(intervals[i])
        return new_arr





print(Solution().merge([Interval(2,100),Interval(100,100)]))