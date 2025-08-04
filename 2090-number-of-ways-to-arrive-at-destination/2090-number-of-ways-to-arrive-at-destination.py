class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v,t in roads:
            adj[u].append([v,t])
            adj[v].append([u,t])
        dist=[float('inf') for _ in range(n)]
        dist[0]=0
        ways=[0 for _ in range(n)]
        ways[0]=1
        pq=[(0,0)]
        mod=10**9+7
        while pq:
            dis,node=heapq.heappop(pq)
            for i in adj[node]:
                adjnode=i[0]
                edw=i[1]

                if dis+edw<dist[adjnode]:
                    dist[adjnode]=dis+edw
                    heapq.heappush(pq,(dis+edw,adjnode))
                    ways[adjnode]=ways[node]
                elif dis+edw==dist[adjnode]:
                    ways[adjnode]=(ways[node]+ways[adjnode])%mod
        return ways[n-1]%mod