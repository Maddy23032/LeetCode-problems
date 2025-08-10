class Solution:

    def houseRob(self,arr,n):
        prev=arr[0]
        prev2=0
        for i in range(1,n):
            take=arr[i]
            if i>1:
                take+=prev2
            nottake=prev
            curi=max(take,nottake)
            prev2=prev
            prev=curi
        return prev
    def rob(self, nums: List[int]) -> int:
        arr1,arr2=[],[]
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(n):
            if i!=0:
                arr1.append(nums[i])

            if i!=n-1:
                arr2.append(nums[i])
            
        return max(self.houseRob(arr1,n-1),self.houseRob(arr2,n-1))