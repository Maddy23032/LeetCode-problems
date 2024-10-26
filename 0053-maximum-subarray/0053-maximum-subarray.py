class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cs,ms=0,float('-inf')
        for i in range(len(nums)):
            cs+=nums[i]
            ms=max(cs,ms)
            if cs<0:cs=0
        return ms    