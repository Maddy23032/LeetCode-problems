class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        lis=defaultdict(list)
        for i in flights:
            lis[i[0]].append([i[1],i[2]])
        prices=[float('inf') for _ in range(n)]
        prices[src]=0
        q=deque()
        q.append([0,src,0])
        while q:
            curr=q.popleft()
            print(curr)
            cost=curr[0]
            city=curr[1]
            stops=curr[2]

            if stops>k:continue

            for nei in lis[city]:
                neicity=nei[0]
                newcost=nei[1]+cost
                if newcost<prices[neicity]:
                    prices[neicity]=newcost
                    q.append([prices[neicity],neicity,stops+1])
            
        return -1 if prices[dst]==float('inf') else prices[dst]