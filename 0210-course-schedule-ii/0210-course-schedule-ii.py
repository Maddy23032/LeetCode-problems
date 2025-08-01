class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg=[0 for _ in range(numCourses)]
        res=[]
        adj=[[] for _ in range(numCourses)]

        for course,prereq in prerequisites:
            adj[prereq].append(course)
            indeg[course]+=1
        
        q=deque()
        l=0
        for i in range(numCourses):
            if not indeg[i]:
                q.append(i)

        while q:
            node=q.popleft()
            res.append(node)
            l+=1
            for i in adj[node]:
                indeg[i]-=1
                if not indeg[i]:
                    q.append(i)
        
        return res if l==numCourses else []