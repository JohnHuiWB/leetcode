class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = True if x >= 0 else False
        r, x = 0, abs(x)
        while x:
            r = r * 10 + x % 10
            x //= 10
        if - (2 ** 31) <= r <= (2 ** 31 - 1) and \
                - (2 ** 31) <= x <= (2 ** 31 - 1):
            return r if f else -r
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(1534236469))
