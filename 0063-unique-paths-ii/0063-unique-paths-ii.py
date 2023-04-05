class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        map = [[0 for _ in y] for y in obstacleGrid]
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                if obstacleGrid[y][x] == 0:
                    if x == 0 and y == 0:   map[y][x] = 1
                    elif y == 0:            map[y][x] = 0 + map[y][x - 1]
                    elif x == 0:            map[y][x] = map[y - 1][x] + 0
                    else:                   map[y][x] = map[y - 1][x] + map[y][x - 1]
        return map[-1][-1]
