class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def bfs(r, c, grid):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            bfs(r + 1, c, grid)
            bfs(r - 1, c, grid)
            bfs(r, c + 1, grid)
            bfs(r, c - 1, grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j, grid)
        return count