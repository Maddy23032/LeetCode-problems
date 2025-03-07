class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isp=[True for _ in range(right+1)]
        isp[0],isp[1]=False,False
        p=2
        while p*p<=right:
            if isp[p]==True:
                for i in range(p*p,right+1,p):
                    isp[i]=False
            p+=1
        pr=[]
        for i in range(left,right+1):
            if isp[i]:
                pr.append(i)
        # print(pr)
        res=[-1,-1]
        v=float('inf')
        for i in range(1,len(pr)):
            if pr[i]-pr[i-1]<v:
                v=pr[i]-pr[i-1]
                res=[pr[i-1],pr[i]]
        return res