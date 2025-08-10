class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev2=0
        prev=nums[0]
        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=prev2
            nottake=prev
            curi=max(take,nottake)
            prev2=prev
            prev=curi
        return prev
