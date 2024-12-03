class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        st=""
        v,i=0,0
        while i<len(s) and v<len(spaces):
            if i<spaces[v]:
                st+=s[i]
                i+=1
            else:
                st+=" "
                v+=1
        if i<len(s):
            st+=''.join(s[i:])            
        return st            