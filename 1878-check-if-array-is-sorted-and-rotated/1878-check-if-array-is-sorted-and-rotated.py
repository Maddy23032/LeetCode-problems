class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<=1:
            return True
        ic=0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                ic+=1
        if nums[0]<nums[n-1]:
            ic+=1
        return ic<=1