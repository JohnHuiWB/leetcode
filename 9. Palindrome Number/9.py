class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x is not 0 and x % 10 is 0):
            return False
        r = 0
        while x > r:
            r = r * 10 + x % 10
            x //= 10
        return x == r or x == r // 10

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return x == int(str(x)[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
