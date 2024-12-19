class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        r,d=0,0
        for i in range(len(arr)):
            d+=arr[i]-i
            if d==0:
                r+=1
        return r        