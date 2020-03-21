class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lines = [''] * numRows
        row, carry = 0, 1
        for c in s:
            if row == numRows - 1:
                carry = -1
            elif row == 0:
                carry = 1
            lines[row] += c
            row += carry
        rs = ''.join(lines)
        return rs


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
