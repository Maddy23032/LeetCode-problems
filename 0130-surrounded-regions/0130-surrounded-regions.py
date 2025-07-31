class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c,vis,board,dr,dc):
            nonlocal n,m
            vis[r][c]=1
            for i in range(4):
                nr,nc=r+dr[i],c+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and not vis[nr][nc] and board[nr][nc]=='O':
                    dfs(nr,nc,vis,board,dr,dc)
        n,m=len(board),len(board[0])
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]

        vis=[[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            if vis[0][i]==0 and board[0][i]=='O':
                dfs(0,i,vis,board,dr,dc)
            if vis[n-1][i]==0 and board[n-1][i]=='O':
                dfs(n-1,i,vis,board,dr,dc)
        
        for j in range(n):
            if vis[j][0]==0 and board[j][0]=='O':
                dfs(j,0,vis,board,dr,dc)
            if vis[j][m-1]==0 and board[j][m-1]=='O':
                dfs(j,m-1,vis,board,dr,dc)
            
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and board[i][j]=='O':
                    board[i][j]='X'
        return board