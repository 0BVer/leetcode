class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[0 for _ in g] for g in grid]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if x == 0 and y == 0:   memo[y][x] = grid[0][0]
                elif x == 0:            memo[y][x] = memo[y - 1][x] + grid[y][x]
                elif y == 0:            memo[y][x] = memo[y][x - 1] + grid[y][x]
                else:
                    down = memo[y - 1][x] + grid[y][x]
                    right = memo[y][x - 1] + grid[y][x]

                    if right > down:    memo[y][x] = down
                    else:               memo[y][x] = right
        return memo[-1][-1]