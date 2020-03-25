class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i, num = 0, 0
        flag = True
        for c in str:
            if c == ' ':
                i += 1
            else:
                if c == '-':
                    flag = False
                    i += 1
                elif c == '+':
                    i += 1
                break

        if len(str) == i:
            return 0

        for c in str[i:]:
            if '0' <= c <= '9':
                num = num * 10 + int(c)
            else:
                break

        if -2147483648 <= num <= 2147483647:
            return num if flag else -num
        else:
            return 2147483647 if flag else -2147483648


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
