class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        r=[-1]*len(queries)
        g=defaultdict(list)
        for i,q in enumerate(queries):
            l,ri=sorted(q)
            if l==ri or heights[ri]>heights[l]:
                r[i]=ri
            else:
                m=max(heights[l],heights[ri])
                g[ri].append((m,i))
        mh=[]
        for i,h in enumerate(heights):
            for qh,qi in g[i]:
                heapq.heappush(mh,(qh,qi))
            while mh and h>mh[0][0]:
                a,b=heapq.heappop(mh)
                r[b]=i
        return r