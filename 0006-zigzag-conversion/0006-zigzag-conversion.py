class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = [[] for _ in range(numRows)]
        down = True
        col_index = 0

        if numRows == 1: return s

        for i in s:
            if down:
                grid[col_index].append(i)
                col_index += 1

                if col_index == numRows:
                    col_index -= 2
                    down = False

            else:
                grid[col_index].append(i)
                col_index -= 1

                if col_index == -1:
                    col_index += 2
                    down = True
        
        answer = ''
        for i in grid:
            for j in i:
                answer = answer + j
        return answer
