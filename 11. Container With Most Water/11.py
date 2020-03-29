class Solution(object):
    def maxArea(self, height):
        """
        简单的理解:
        左端为L,右端为R,则体积为Math.min(A[L],A[R])*(r-l)
        如果 L < R,向右移动L, 因为此时容器的高度是L,
        R-L即宽度减小,体积必然减小,所以可以忽略所有其他的当L为左端边界的情况.
        R的移动同理.
        :type height: List[int]
        :rtype: int
        """
        r, i, j = 0, 0, len(height) - 1
        while i < j:
            hi, hj = height[i], height[j]
            if hi < hj:
                r = max(r, (j - i) * hi)
                i += 1
            else:
                r = max(r, (j - i) * hj)
                j -= 1
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
