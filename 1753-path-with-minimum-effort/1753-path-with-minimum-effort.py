class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n,m=len(heights),len(heights[0])
        pq=[(0,0,0)]
        dist=[[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0]=0
        dr=[-1,0,1,0]
        dc=[0,-1,0,1]

        while pq:
            diff,r,c=heapq.heappop(pq)
            
            if r==n-1 and c==m-1:
                return diff

            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m:
                    neweff=max(abs(heights[r][c]-heights[nr][nc]),diff)
                    if neweff<dist[nr][nc]:
                        dist[nr][nc]=neweff
                        heapq.heappush(pq,(neweff,nr,nc))
        return 0