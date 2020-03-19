class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        current = timeSeries[0]
        total_time = duration

        for point in timeSeries[1:]:
            total_time += min(point - current, duration)
            current = point

        return total_time


if __name__ == '__main__':
    s = Solution()
    print(s.findPoisonedDuration([1, 4], 2))
    print(s.findPoisonedDuration([1, 2], 2))
    print(s.findPoisonedDuration([1], 3))