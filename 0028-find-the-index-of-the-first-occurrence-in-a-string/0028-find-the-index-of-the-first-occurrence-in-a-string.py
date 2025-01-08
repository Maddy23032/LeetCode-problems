class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps=[0]*len(needle)
        i,pl=1,0
        while i<len(needle):
            if needle[i]==needle[pl]:
                lps[i]=pl+1
                pl+=1
                i+=1
            elif pl==0:
                lps[i]=0
                i+=1
            else:
                pl=lps[pl-1]
        i,j=0,0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i,j=i+1,j+1
            else:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
            if j==len(needle):
                return i-len(needle)
        return -1