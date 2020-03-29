class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ks = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        vs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i, r = 0, 0
        for k, v in zip(ks, vs):
            while s[i:].startswith(k):
                r += v
                i += len(k)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))
