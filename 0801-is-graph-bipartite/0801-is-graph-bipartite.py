class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(st,col,color,graph):
            # q=deque([st])
            # color[st]=0
            # while q:
            #     node=q.popleft()
            #     for i in graph[node]:
            #         if color[i]==-1:
            #             color[i]=0 if color[node]==1 else 1
            #             q.append(i)
            #         elif color[node]==color[i]:
            #             return False
            # return True
            color[st]=col
            for i in graph[st]:
                if color[i]==-1:
                    if (not dfs(i,0 if col==1 else 1,color,graph)):
                        return False
                elif color[i]==col:return False
            return True
        n=len(graph)
        color=[-1 for _ in range(n)]
        for i in range(n):
            if color[i]==-1:
                if dfs(i,0,color,graph)==False:
                    return False
        return True