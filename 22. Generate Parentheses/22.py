class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(cur, l, r):
            if not l and not r:
                out.append(cur)
                return
            if r and r > l:
                gen(cur + ')', l, r - 1)
            if l:
                gen(cur + '(', l - 1, r)

        out = []
        gen('', n, n)
        return out


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(4))
