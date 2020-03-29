class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def get_pairs(l, r, third):
            while l < r:
                sum_result = nums[l] + nums[r] + third
                if sum_result < 0:
                    l += 1
                elif sum_result > 0:
                    r -= 1
                else:
                    pairs.append([third, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        nums = sorted(nums)
        pairs = []
        last = len(nums) - 1
        for i, n in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            get_pairs(i + 1, last, n)
        return pairs


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([-2, -1, 0, 1, 2]))
    print(s.threeSum([0, 0, 0, 0]))
    print(s.threeSum([1, 4, 3, 2]))
    print(s.threeSum([-1, -4, -3, -2]))
