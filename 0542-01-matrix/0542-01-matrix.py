from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dq = deque()

        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    dq.append((y, x))
                else:
                    mat[y][x] = float('inf')

        while dq:
            count = len(dq)

            for yx in range(count):
                y, x = dq.popleft()

                for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
                    
                    if -1 < y + i < m and -1 < x + j < n and mat[y + i][x + j] == float('inf'):
                        mat[y + i][x + j] = mat[y][x] + 1
                        dq.append((y + i, x + j))
        
        return mat