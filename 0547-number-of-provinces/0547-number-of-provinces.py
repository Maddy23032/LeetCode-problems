from typing import List

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dis = DisjointSet(n)

        for i in range(n):
            for j in range(i+1, n):  # check only upper triangle
                if isConnected[i][j] == 1:
                    dis.unionBySize(i, j)

        provinces = set()
        for i in range(n):
            provinces.add(dis.findParent(i))  # collect unique parents
        
        return len(provinces)
