from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]
        
        q = deque([(0, 0, 1)]) 
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while q:
            r, c, dist = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
        
        return -1
