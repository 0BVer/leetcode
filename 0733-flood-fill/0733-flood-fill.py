class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        l_y, l_x = len(image), len(image[0])
        target = image[sr][sc]
        way = [0, 1], [1, 0], [0, -1], [-1, 0]
        if target == color: return image
        def dfs(y: int, x: int):
            if image[y][x] != target: return
            image[y][x] = color
            
            for i, j in way:
                if 0 <= x + i < l_x and 0 <= y + j < l_y:
                    dfs(y + j, x + i)
            
        dfs(sr, sc)
        return image
