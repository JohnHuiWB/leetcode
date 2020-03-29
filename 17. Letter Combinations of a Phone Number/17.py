class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        r = ['']
        for d in digits:
            tmp = []
            for l in r:
                tmp.extend([l + c for c in phone[d]])
            r = tmp
        return r

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def track(left, d):
            if not d:
                r.append(left)
            else:
                for c in phone[d[0]]:
                    track(left + c, d[1:])
        r = []
        if digits:
            track('', digits)
        return r

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
    print(s.letterCombinations2('23'))
