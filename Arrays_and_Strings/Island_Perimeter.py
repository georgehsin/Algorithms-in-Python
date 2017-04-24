# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        for x in range (0, len(grid)):
            print x
            print grid[x]
            for i in range (0, len(grid[x])):
                if grid[x][i] == 1:
                    sum += 4
                    if x != 0: #Don't check top
                        if grid[x-1][i] == 1:
                            sum -= 1
                    if x != len(grid)-1: #Don't check bottom
                        if grid[x+1][i] == 1:
                            sum -= 1
                    if i != 0: #Don't check left
                        if grid[x][i-1] == 1:
                            sum -= 1
                    if i != len(grid[x])-1: #don't check right
                        if grid[x][i+1] == 1:
                            sum -= 1
        return sum
