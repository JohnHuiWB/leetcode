class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_sum = sum(nums[:3])
        min_diff = abs(min_sum - target)
        last = len(nums) - 1
        for i, n in enumerate(nums[:-2]):
            l = i + 1
            r = last
            while l < r:
                tmp_sum = nums[l] + nums[r] + nums[i]
                tmp_diff = abs(tmp_sum - target)
                if tmp_diff < min_diff:
                    if tmp_diff == 0:
                        return tmp_sum
                    min_diff = tmp_diff
                    min_sum = tmp_sum
                if tmp_sum > target:
                    r -= 1
                else:
                    l += 1
        return min_sum


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0, 2, 1, -3], 1))
