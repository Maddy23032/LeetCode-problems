# class Solution:
#     def findScore(self, nums: List[int]) -> int:
#         score=0
#         while len(nums)!=0:
#             mi,ind=float('inf'),0
#             for i in range(0,len(nums)):
#                 if nums[i]<mi:
#                     mi=nums[i]
#                     ind=i
#             score+=nums[ind]        
#             if ind-1>=0 and ind+1<len(nums):
#                 nums.remove(nums[:ind-1]
#                 nums[ind+2:]
#             elif ind-1>=0 and ind+1==len(nums):
#                 nums1=nums[:ind-1]
#                 nums2=nums[ind+1:]
#             elif ind+1<len(nums) and ind-1==0:
#                 nums1=nums[:ind]
#                 nums2=nums[ind+2:]
#             nums=nums1+nums2   
#         return score 
class Solution:
    def findScore(self, nums):
        ans = 0
        marked = [False] * len(nums)

        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))

        while heap:
            number, index = heapq.heappop(heap)
            if not marked[index]:
                ans += number
                marked[index] = True
                # mark adjacent elements if they exist
                if index - 1 >= 0:
                    marked[index - 1] = True
                if index + 1 < len(nums):
                    marked[index + 1] = True

        return ans               