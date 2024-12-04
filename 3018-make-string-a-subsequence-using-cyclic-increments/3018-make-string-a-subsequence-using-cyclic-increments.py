class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s2p,s1p=0,0
        while s1p<len(str1) and s2p<len(str2):
            if s2p<len(str2) and str1[s1p]==str2[s2p] or ord(str1[s1p])+1==ord(str2[s2p]) or ord(str1[s1p])-25==ord(str2[s2p]):
                s1p+=1
                s2p+=1
            else:
                s1p+=1
        return s2p==len(str2)            