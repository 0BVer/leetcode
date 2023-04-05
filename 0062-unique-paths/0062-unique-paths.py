import itertools
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        memo = [[0] * (m)] * (n)

        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[-1][-1]