class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for i in range(len(nums)-k+1):
            l=[]
            for j in range(i,i+k):
                if j+1<i+k and nums[j+1]-nums[j]!=1:
                    l=[]
                    l.append(-1)
                    break
                l.append(nums[j])    
            if l[-1]==-1:res.append(-1)
            else:res.append(max(l))
        return res            