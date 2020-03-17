class Solution(object):
    def twoSum_1(self, nums, target):
        """
        Brute Force
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    return [i, j + i + 1]

    def twoSum_2(self, nums, target):
        """
        Two-pass Hash Table
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            n = target - num
            if n in d and i is not d[n]:
                return [i, d[n]]

    def twoSum_3(self, nums, target):
        """
        One-pass Hash Table
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in d:
                return [i, d[n]]
            else:
                d[num] = i

    def twoSum_4(self, nums, target):
        """
        Clear code
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target - num]]
            else:
                d[num] = i


if __name__ == '__main__':
    s = Solution()
    i = [3, 2, 4]
    t = 6
    print(s.twoSum_3(i, t))