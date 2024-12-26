class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l=defaultdict(int)
        l[0]=1
        for i in range(len(nums)):
            nl=defaultdict(int)
            for j,k in l.items():
                nl[j+nums[i]]+=k
                nl[j-nums[i]]+=k
            l=nl
        return l[target]