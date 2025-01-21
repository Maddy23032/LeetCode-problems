class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1,l2=len(str1),len(str2)
        dl=[[0]*(l2+1) for _ in range(l1+1)]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if str1[i-1]==str2[j-1]:
                    dl[i][j]=1+dl[i-1][j-1]
                else:
                    dl[i][j]=max(dl[i-1][j],dl[i][j-1])
        a,b=l1,l2
        res=[]
        while a>0 and b>0:
            if str1[a-1]==str2[b-1]:
                res.append(str1[a-1])
                a-=1
                b-=1
            elif dl[a-1][b]>dl[a][b-1]:
                res.append(str1[a-1])
                a-=1
            else:
                res.append(str2[b-1])
                b-=1
        while a>0:
            res.append(str1[a-1])
            a-=1
        while b>0:
            res.append(str2[b-1])
            b-=1
        return ''.join(res[::-1])
