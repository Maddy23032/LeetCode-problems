class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        fresh=0
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([[i,j],0])
                    vis[i][j]=2
                elif grid[i][j]==1:fresh+=1
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        tm,cnt=0,0
        while q:
            pos, t = q.popleft()
            r, c = pos
            tm=max(tm,t)
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc] == 0 and grid[nr][nc] == 1:
                    q.append([[nr,nc],t+1])
                    vis[nr][nc]=2
                    cnt+=1
        if cnt!=fresh:return -1
        return tm
