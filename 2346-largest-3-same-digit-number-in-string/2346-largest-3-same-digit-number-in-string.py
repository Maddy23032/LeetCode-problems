class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxd='\0'
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                maxd=max(maxd,num[i])
        
        return '' if maxd=='\0' else maxd*3