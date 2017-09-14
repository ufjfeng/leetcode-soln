"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above
updated description carefully.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, j in enumerate(nums):
            index[j] = i

        for i, j in enumerate(nums):
            if target - j in index and index[target - j] != i:
                return sorted([i, index[target - j]])

a = Solution()
print(a.twoSum([2, 7, 11, 15], 9) == [0, 1])
print(a.twoSum([3, 2, 4], 6) == [1, 2])
print(a.twoSum([0, 4, 3, 0], 0) == [0, 3])
