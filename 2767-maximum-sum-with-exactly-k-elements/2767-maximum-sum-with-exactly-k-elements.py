class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=0
        nums.sort()
        for i in range(k):
            s+=nums[-1]
            nums[-1]+=1
        return s    