class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node, par, vis, adj, tin, low, bridges):
            vis[node] = 1
            tin[node] = low[node] = self.timer
            self.timer += 1
            for i in adj[node]:
                if i == par:
                    continue
                if not vis[i]:
                    dfs(i, node, vis, adj, tin, low, bridges)
                    low[node] = min(low[node], low[i])
                    if low[i] > tin[node]:
                        bridges.append([node, i])
                else:
                    low[node] = min(low[node], tin[i])  

        self.timer = 0  
        adj = [[] for _ in range(n)]  
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []

        dfs(0, -1, vis, adj, tin, low, bridges)

        return bridges
