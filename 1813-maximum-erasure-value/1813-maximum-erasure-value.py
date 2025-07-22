class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxscore = 0
        su = 0
        hm = {}
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] in hm and hm[nums[j]] >= i:
                i = hm[nums[j]] + 1  
                su = sum(nums[i:j+1]) 
            else:
                su += nums[j]
                maxscore = max(maxscore, su)
            hm[nums[j]] = j
            j += 1

        return maxscore