class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds=[]
        def helper(ind,nl):
            if ind==len(nums):
                ds.append(nl[:])
                return
            
            nl.append(nums[ind])
            helper(ind+1,nl)

            nl.pop()
            helper(ind+1,nl)


        helper(0,[])
        return ds