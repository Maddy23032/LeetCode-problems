class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix=[[float('inf') for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            matrix[u][v]=w
            matrix[v][u]=w

        for i in range(n):
            matrix[i][i]=0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k]==float('inf') or matrix[k][j]==float('inf'):
                        continue
                    matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
        
        citymax=n
        cityno=-1
        for i in range(n):
            cities=0
            for j in range(n):
                if matrix[i][j]<=distanceThreshold:
                    cities+=1
            if cities<=citymax:
                citymax=cities
                cityno=i
        
        return cityno