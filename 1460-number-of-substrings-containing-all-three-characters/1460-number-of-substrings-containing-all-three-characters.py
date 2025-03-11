class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        hm=defaultdict(int)
        n=len(s)
        c=0
        for r in range(n):
            hm[s[r]]+=1
            while len(hm)==3:
                c+=n-r
                hm[s[l]]-=1
                if hm[s[l]]==0:
                    hm.pop(s[l])
                l+=1
        return c