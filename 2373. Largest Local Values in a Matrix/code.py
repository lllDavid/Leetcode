class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [[max(grid[i+a][j+b] for a in range(3) for b in range(3)) 
             for j in range(len(grid) - 2)] 
             for i in range(len(grid) - 2)]