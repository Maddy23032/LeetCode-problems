class Solution:
    def maxScore(self, s: str) -> int:
        ma=float('-inf')
        o,z=0,0
        for i in range(len(s)-1):
            if s[i]=='0':
                z+=1
            else:o+=1
            ma=max(z-o,ma)
        if s[-1]=='1':o+=1
        return ma+o