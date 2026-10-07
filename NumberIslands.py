"""
LeetCode - Number of Islands

Time complexity: O(mn)where m is the number of rows and n is the number of columns and each node is visited at most once. 

Space complexity: O(mn) is worst case if the entire grid is one island and the DFS stack is full.

A brute force approach would repeatedly search connected land, but not mark previously visited cells. The optimized approach is a DFS approach where each visited cell is marked as 0 so each cell is processed at most once. 
"""

class Solution(object):
    def numIslands(self, grid):
        islands  = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col):
            grid[row][col] = "0"

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1"):
                    dfs(new_row, new_col)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)


        return islands



        
if __name__ == "__main__":
    sol = Solution()

    assert sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1

    assert sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
) == 3

    print("Passed")