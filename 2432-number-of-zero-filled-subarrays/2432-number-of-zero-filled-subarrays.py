class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res,cur=0,0

        for i in nums:
            if i==0:
                cur+=1
            else:
                res+=(cur*(cur+1))//2
                cur=0
        res+=cur*(cur+1)//2
        return res