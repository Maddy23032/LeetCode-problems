class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        vis=[[0 for _ in range(m)] for _ in range(n)]
        q=deque()

        for i in range(n):
             for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]==1:
                        vis[i][j]=1
                        q.append([i,j])
        
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        while q:
            r,c=q.popleft()
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc]==0 and grid[nr][nc]==1:
                    q.append([nr,nc])
                    vis[nr][nc]=1
        c=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and vis[i][j]==0:
                    c+=1
        return c
