class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg=[0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)  # edge: prereq -> course
            indeg[course] += 1

        q=deque()
        cnt=0
        for i in range(numCourses):
            if not indeg[i]:
                q.append(i)

        while q:
            node=q.popleft()
            cnt+=1

            for i in adj[node]:
                indeg[i]-=1
                if not indeg[i]:
                    q.append(i)
        
        return cnt==numCourses