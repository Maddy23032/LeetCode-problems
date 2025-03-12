class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def ff(nums,n):
            l,r=0,n-1
            ind=n
            while l<=r:
                m=(l+r)//2
                if nums[m]<0:
                    l=m+1
                else:
                    r=m-1
                    ind=m
            return ind
        def sf(nums,n):
            l,r=0,n-1
            ind=n
            while l<=r:
                m=(l+r)//2
                if nums[m]<=0:
                    l=m+1
                else:
                    r=m-1
                    ind=m
            return ind
        n=len(nums)
        return max(n-sf(nums,n),ff(nums,n))