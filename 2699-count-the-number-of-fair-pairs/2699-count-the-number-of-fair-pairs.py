class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        # 0 1 4 4 5 7
        def bs(a,b,t):
            while a<=b:
                m=(a+b)//2
                if nums[m]>=t:
                    b=m-1
                else:
                    a=m+1
            return b            
        c=0
        for i in range(len(nums)):
            l=lower-nums[i]
            u=upper-nums[i]
            c+=(bs(i+1,len(nums)-1,u+1)-bs(i+1,len(nums)-1,l))        
        return c    