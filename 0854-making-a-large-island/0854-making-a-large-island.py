class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def findParent(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u: int, v: int) -> None:
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
            return
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dis=DisjointSet(n*n)
        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    continue
                dr=[-1,0,1,0]
                dc=[0,-1,0,1]
                for ind in range(4):
                    nr=r+dr[ind]
                    nc=c+dc[ind]
                    if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc]==1:
                        nodeno=r*n+c
                        adjnodeno=nr*n+nc
                        dis.unionBySize(nodeno,adjnodeno)
        print(dis.parent)
        
        mx=0
        for r in range(n):
            for c in range(n):
                comp=set()
                if grid[r][c]==1:
                    continue
                dr=[-1,0,1,0]
                dc=[0,-1,0,1]
                for ind in range(4):
                    nr=r+dr[ind]
                    nc=c+dc[ind]
                    if nr>=0 and nr<n and nc>=0 and nc<n and grid[nr][nc]==1:
                        comp.add(dis.findParent(nr*n+nc))

                st=0
                for i in comp:
                    st+=dis.size[i]

                mx=max(mx,st+1)

        for i in range(n*n):
            mx=max(mx,dis.size[dis.findParent(i)])
        return mx