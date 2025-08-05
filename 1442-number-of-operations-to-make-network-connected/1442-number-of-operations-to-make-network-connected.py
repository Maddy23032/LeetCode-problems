class DisjointSet:
    def __init__(self, n: int):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.size=[1]*n
    
    def findParent(self,node:int) -> int:
        if self.parent[node]!=node:
            self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]

    def find(self, u: int, v: int) -> bool:
        return self.findParent(u)==self.findParent(v)

    def unionByRank(self, u: int, v: int) -> None:
        pu=self.findParent(u)
        pv=self.findParent(v)

        if pu==pv:return
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

    def unionBySize(self, u: int, v: int) -> None:
        pu=self.findParent(u)
        pv=self.findParent(v)
        if pu==pv:
            return
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
    

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dis=DisjointSet(n)
        ce=0
        for u,v in connections:
            if dis.find(u,v):
                ce+=1
            else:
                dis.unionBySize(u,v)
        
        c=0
        for i in range(n):
            if dis.parent[i]==i:
                c+=1

        if c-1<=ce:return c-1
        return -1