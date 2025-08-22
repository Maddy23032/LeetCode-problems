class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lis=[]
        intervals.sort()
        for i in range(len(intervals)):
            if lis==[] or lis[-1][1]<intervals[i][0]:
                lis.append(intervals[i])
            else:
                lis[-1][1]=max(lis[-1][1],intervals[i][1])
        return lis