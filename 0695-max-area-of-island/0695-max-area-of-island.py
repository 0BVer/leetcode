class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        way = [1, 0], [-1, 0], [0, 1], [0, -1]
        m, n = len(grid), len(grid[0])
        big = 0
        
        def dfs(y, x, count):
            if grid[y][x] == 1:
                grid[y][x] = 2
                count += 1
                for i, j in way:
                    if 0 <= y + i < m and 0 <= x + j < n:
                        count = dfs(y + i, x + j, count)
            return count

        for y, x in ((y, x) for x in range(n) for y in range(m) if grid[y][x] == 1):
            big = max(big, dfs(y, x, 0))
        return big