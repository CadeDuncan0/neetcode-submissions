class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # water MUST be top, bottom, left, right

        # if index out of range, assume it's a water spot

        def dfs(row, col):
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
                return
            if grid[row][col] == '0':
                return

            grid[row][col] = '0'
            dfs(row - 1, col) # up
            dfs(row, col - 1) # left
            dfs(row + 1, col) # down
            dfs(row, col + 1) # right

        islandCount = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islandCount += 1
                    # run dfs from here to all adjacent 1's
                    dfs(row, col)

        return islandCount