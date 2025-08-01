class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        indeg=[0 for _ in range(n)]
        adj=[[] for _ in range(n)]

        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                indeg[i]+=1
        q=deque()
        for i in range(n):
            if not indeg[i]:
                q.append(i)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for i in adj[node]:
                indeg[i]-=1
                if not indeg[i]:
                    q.append(i)
        
        return sorted(res)
        
        # for i in range(n):
        #     outdeg[i]=len(graph[i])
        
        # q=deque()
        # for i in range(n):
        #     if not outdeg[i]:
        #         q.append(i)
        # print(outdeg)
        # return []