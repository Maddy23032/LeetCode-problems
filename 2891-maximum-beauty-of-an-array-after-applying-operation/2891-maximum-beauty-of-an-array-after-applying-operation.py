class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        c,l=0,0
        for i in range(len(nums)):
            while nums[i]-nums[l]>2*k:
                l+=1
            c=max(c,i-l+1)
        return c        