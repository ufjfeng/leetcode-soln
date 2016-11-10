"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        soln = []
        self.dfs(nums, [], soln)
        return soln

    def dfs(self, nums, curr, soln):
        if nums is None or nums == []:
            soln.append(curr)
            return
        for i, num in enumerate(nums):
            self.dfs(nums[:i] + nums[i + 1:], curr + [num], soln)

a = Solution()
print(a.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
