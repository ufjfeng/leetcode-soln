"""
There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain color
is different. You have to paint all the houses such that no two adjacent houses
have the same color.

The cost of painting each house with a certain color is represented by a n x 3
cost matrix. For example, costs[0][0] is the cost of painting house 0 with color
red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.

Note:
    All costs are positive integers.
"""
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs is None or costs == []:
            return 0
        houses = len(costs)
        soln = [[0, 0, 0] for i in range(houses)]
        soln[0] = costs[0]
        for i in range(1, houses):
            soln[i][0] = min(soln[i - 1][1], soln[i - 1][2]) + costs[i][0]
            soln[i][1] = min(soln[i - 1][0], soln[i - 1][2]) + costs[i][1]
            soln[i][2] = min(soln[i - 1][0], soln[i - 1][1]) + costs[i][2]
        return min(soln[-1])

a = Solution()
a.minCost([[20,18,4],[9,9,10]])
