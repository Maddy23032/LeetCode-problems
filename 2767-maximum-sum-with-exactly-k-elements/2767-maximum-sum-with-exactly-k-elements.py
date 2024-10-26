class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=0
        nums.sort()
        for i in range(k):
            v=nums[-1]
            s+=v
            nums.append(v+1)
        return s    