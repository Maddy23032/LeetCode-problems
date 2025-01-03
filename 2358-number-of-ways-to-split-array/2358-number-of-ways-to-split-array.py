class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        le,ri=0,sum(nums)
        c=0
        for i in range(len(nums)-1):
            le+=nums[i]
            ri-=nums[i]
            c+=1 if le>=ri else 0
        return c