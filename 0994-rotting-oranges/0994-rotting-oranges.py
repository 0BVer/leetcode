from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mq = deque()
        nq = deque()
        lm = len(grid)
        ln = len(grid[0])
        count = 0
        visit = set()

        for i in range(lm):
            for j in range(ln):
                if grid[i][j] == 2:
                    mq.append(i)
                    nq.append(j)
                    visit.add((i, j))
                elif grid[i][j] == 1:
                    count += 1
        
        time = 0

        while mq and count > 0:
            time += 1
            l = len(mq)

            for _ in range(l):
                m = mq.popleft()
                n = nq.popleft()

                for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if -1 < m + y < lm and -1 < n + x < ln and (m + y, n + x) not in visit and grid[m + y][n + x] == 1:
                        mq.append(m + y)
                        nq.append(n + x)
                        visit.add((m + y, n + x))
                        count -= 1

        if count == 0: return time
        return -1