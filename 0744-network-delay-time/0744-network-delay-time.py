from collections import deque
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        
        q = deque()
        q.append((0, k)) 
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while q:
            time, node = q.popleft()
            for nei, weight in adj[node]:
                if time + weight < dist[nei]:
                    dist[nei] = time + weight
                    q.append((dist[nei], nei))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1
