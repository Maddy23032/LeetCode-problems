class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for i in flights:
            adj[i[0]].append([i[1],i[2]])
        q=deque([[0,src,0]])
        dist=[float('inf') for _ in range(n)]
        dist[src]=0

        while q:
            stops,node,cost=q.popleft()
            if stops>k:
                continue
            for i in adj[node]:
                adjnode=i[0]
                edw=i[1]
                if cost+edw<dist[adjnode] and stops<=k:
                    dist[adjnode]=cost+edw
                    q.append([stops+1,adjnode,cost+edw])
        return -1 if dist[dst]==float('inf') else dist[dst]