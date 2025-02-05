class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        tab=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            tab[i][0]=i
        for i in range(n+1):
            tab[0][i]=i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    tab[i][j]=tab[i-1][j-1]
                else:
                    tab[i][j]=1+min(tab[i-1][j],tab[i][j-1])
        return tab[-1][-1]