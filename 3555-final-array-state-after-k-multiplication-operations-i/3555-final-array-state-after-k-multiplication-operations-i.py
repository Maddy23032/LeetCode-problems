class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        r=nums[:]
        mh=[(n,i) for i,n in enumerate(nums)]
        heapq.heapify(mh)
        for _ in range(k):
            n,i=heapq.heappop(mh)
            r[i]*=multiplier
            heapq.heappush(mh,(r[i],i))
        return r    