class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def rp(p,sc):
            nonlocal s
            r=0
            st=[]
            for c in s:
                if c==p[1] and st and st[-1]==p[0]:
                    st.pop()
                    r+=sc
                else:
                    st.append(c)
            s="".join(st)
            return r
        r=0
        p="ab" if x>y else "ba"
        r+=rp(p,max(x,y))
        r+=rp(p[::-1],min(x,y))                    
        return r            