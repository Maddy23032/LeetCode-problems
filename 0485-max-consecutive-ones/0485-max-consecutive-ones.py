class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mi,res=0,0
        for i in nums:
            if i==1:
                mi+=1
            else:
                res=max(res,mi)  
                mi=0
        res=max(res,mi)        
        return res          