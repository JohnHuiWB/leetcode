class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        elif s == '':
            return 0

        length = 0
        sub = []
        for c in s:
            if c in sub:
                sub = sub[sub.index(c)+1:]
            sub.append(c)
            length = max(length, len(sub))
        return length

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        length = start = 0
        for i, c in enumerate(s):
            if c in dicts:
                sums = dicts[c] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > length:
                length = num
            dicts[c] = i
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring1('pwwkew'))
