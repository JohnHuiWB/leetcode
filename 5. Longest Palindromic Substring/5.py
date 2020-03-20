class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 1:
            return s
        elif length == 0:
            return ''

        length1, length2 = 1, 2
        center = {
            1: [[x, x] for x in range(length)],
            2: [[x - 1, x] for x in range(1, length) if s[x - 1] == s[x]]
        }

        def expand(tmp_len):
            while tmp_len < length:
                f = False
                center[tmp_len + 2] = []
                for l, r in center[tmp_len]:
                    if l > 0 and r < length - 1 and s[l - 1] == s[r + 1]:
                        center[tmp_len + 2].append([l - 1, r + 1])
                        f = True
                tmp_len += 2 if f else 0
                if not f:
                    break
            return tmp_len

        """
        Expand Around Center, begin from 1 char and 2 char
        eg. for 'abba'
        {
            1: [[0, 0], [1, 1], [2, 2], [3, 3]],
            2: [[0, 1], [1, 2], [2, 3]],
            4: [[0, 3]]
        }
        """
        length1 = expand(length1)
        if not center[2]:
            length2 = length1
        else:
            length2 = expand(length2)

        l, r = center[max(length1, length2)][0]
        return s[l:r + 1]

    def longestPalindrome2(self, s):
        def expand(s, l, r):
            while (l>=0) and (r<len(s)) and (s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        if s==None or len(s)<1: return ""
        start, end =0, 0
        for i in range(len(s)):
            len1=expand(s,i,i)
            len2=expand(s,i,i+1)
            maxl=max(len1,len2)
            if maxl>end-start:
                start= i-(maxl-1)//2
                end=i+maxl//2
        return s[start:end+1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome2("aaaa"))