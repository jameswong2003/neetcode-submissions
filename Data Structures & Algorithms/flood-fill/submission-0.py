class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        def dfs(r, c, color, original_color):
            ROWS, COLS = len(image), len(image[0])

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or image[r][c] != original_color:
                return

            image[r][c] = color
            dfs(r + 1, c, color, original_color)
            dfs(r - 1, c, color, original_color)
            dfs(r, c + 1, color, original_color)
            dfs(r, c - 1, color, original_color)
        
        dfs(sr, sc, color, image[sr][sc])
        return image
