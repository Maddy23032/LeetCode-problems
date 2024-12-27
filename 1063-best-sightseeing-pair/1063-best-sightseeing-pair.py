class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxsc=0
        cm=values[0]-1
        for i in range(1,len(values)):
            maxsc=max(maxsc,values[i]+cm)
            cm=max(cm-1,values[i]-1)
        return maxsc