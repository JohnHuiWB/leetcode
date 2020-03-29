class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ks = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        vs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        r = ''
        for k, v in zip(ks, vs):
            if num >= k:
                r += v * (num // k)
                num %= k
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))
    print(s.intToRoman(4))
    print(s.intToRoman(9))
    print(s.intToRoman(58))
    print(s.intToRoman(1994))
