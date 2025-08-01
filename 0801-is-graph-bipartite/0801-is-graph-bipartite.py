class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def check(st,color,n,graph):
            q=deque([st])
            color[st]=0
            while q:
                node=q.popleft()
                for i in graph[node]:
                    if color[i]==-1:
                        color[i]=0 if color[node]==1 else 1
                        q.append(i)
                    elif color[node]==color[i]:
                        return False
            return True
        n=len(graph)
        color=[-1 for _ in range(n)]

        for i in range(n):
            if color[i]==-1:
                if check(i,color,n,graph)==False:
                    return False
        return True