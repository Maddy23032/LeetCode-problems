class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(st):
            vis[st]=1
            for i in range(len(isConnected[st])):
                if not vis[i] and isConnected[st][i]:
                    dfs(i)
        vis=[0]*len(isConnected)
        number=0
        for i in range(len(isConnected)):
            if not vis[i]:
                number+=1
                dfs(i)
        return number