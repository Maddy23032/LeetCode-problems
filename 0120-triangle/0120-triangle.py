class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        prev=[0 for _ in range(n)]
        for i in range(n):
            prev[i]=triangle[n-1][i]
        
        for i in range(n-2,-1,-1):
            cur=[0 for _ in range(n)]
            for j in range(i,-1,-1):
                d=triangle[i][j]+prev[j]
                dg=triangle[i][j]+prev[j+1]
                cur[j]=min(d,dg)
            prev=cur
        return prev[0]
#         n=len(triangle)
#         def uniqP(a,b,triangle,dp):
#             nonlocal n
#             if a==n-1:
#                 dp[a][b]=triangle[a][b]
#                 return dp[a][b]
#             if dp[a][b]!=-1:
#                 return dp[a][b]
#             d=triangle[a][b]+uniqP(a+1,b,triangle,dp)
#             dq=triangle[a][b]+uniqP(a+1,b+1,triangle,dp)
#             dp[a][b]=min(d,dq)
#             return dp[a][b]
        
#         dp=[[-1 for _ in range(n)] for _ in range(n)]
#         return uniqP(0,0,triangle,dp)

# def recursion(l,x,y,ans,memo):
#     if x>=len(l):
#         return 0
#     if (x,y) in memo:
#         return memo[(x,y)]
#     ans += l[x][y]+min(recursion(l,x+1,y,ans,memo),recursion(l,x+1,y+1,ans,memo))
#     memo[(x, y)] = ans
#     return ans
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         return recursion(triangle,0,0,0,{})
        