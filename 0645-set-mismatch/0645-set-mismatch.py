class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s1=sum(nums)
        s2=n*(n+1)//2
        val1=s1-s2
        s3=sum([i*i for i in nums])
        s2n=n*(n+1)*(2*n+1)//6
        val2=s3-s2n
        val2=val2//val1
        x=(val1+val2)//2
        y=val2-x

        return [x,y]