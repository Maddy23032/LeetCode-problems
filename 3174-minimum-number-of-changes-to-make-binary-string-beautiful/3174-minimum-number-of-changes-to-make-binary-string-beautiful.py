class Solution:
    def minChanges(self, s: str) -> int:
        c,k=0,0
        for i in range(len(s)//2):
            f=0
            for j in range(0,2):
                if s[k+j]=='1' and j==0:
                    f=1
                elif f and s[k+j]=='0':c+=1
                elif f==0 and s[k+j]=='1':c+=1
            k+=2
        return c            