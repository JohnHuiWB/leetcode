class Solution(object):
    def isMatch(self, s, p):
        """
        Recursion
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        m = len(s) >= 1 and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:])) or (m and self.isMatch(s[1:], p))
        else:
            return m and self.isMatch(s[1:], p[1:])


    def isMatch2(self, s, p):
        """
        DP
        :type s: str
        :type p: str
        :rtype: bool
        """
        records = {}
        def dp(i, j):
            if (i, j) not in records:
                if j == len(p):
                    r = i == len(s)
                else:
                    m = i < len(s) and (s[i] == p[j] or p[j] == '.')
                    if j < (len(p) - 1) and p[j + 1] == '*':
                        r = dp(i, j + 2) or (m and dp(i + 1, j))
                    else:
                        r = m and dp(i + 1, j + 1)
                records[i, j] = r
            return records[i, j]
        return dp(0, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch2("aa", "a"))
    print(s.isMatch2("aa", "a*"))
    print(s.isMatch2("ab", ".*"))
    print(s.isMatch2("aab", "c*a*b"))
    print(s.isMatch2("mississippi", "mis*is*p*."))