class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):return False
        hm=defaultdict(int)
        for i in s:
            hm[i]+=1
        oc=0
        for j in hm.values():
            oc+=j%2
        return oc<=k