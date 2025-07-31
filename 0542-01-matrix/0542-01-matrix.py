class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m=len(mat),len(mat[0])
        dist=[[0 for _ in range(m)] for _ in range(n)]
        vis=[[0 for _ in range(m)] for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    vis[i][j]=1
                    q.append([[i,j],0])
                else:vis[i][j]=0
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]

        while q:
            (r,c),st=q.popleft()
            dist[r][c]=st
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and not vis[nr][nc]:
                    vis[nr][nc]=1
                    q.append([[nr,nc],st+1])
        return dist