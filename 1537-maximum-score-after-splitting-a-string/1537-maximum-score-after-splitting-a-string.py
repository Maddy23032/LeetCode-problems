class Solution:
    def maxScore(self, s: str) -> int:
        ma=float('-inf')
        for i in range(len(s)-1):
            ls=s[:i+1]
            rs=s[i+1:]
            ma=max(ma,ls.count('0')+rs.count('1'))
        return ma