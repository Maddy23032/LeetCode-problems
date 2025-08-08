class Solution:
    def myAtoi(self, s: str) -> int:
        def getint(s,i,res,sign):
            if i>=len(s) or not s[i].isdigit():
                return sign*int(res)
            
            res=res*10+int(s[i])
            if sign*res>=2**31-1:
                return 2**31-1
            if sign*res<=-2**31:
                return -2**31

            return getint(s,i+1,res,sign)
        s=s.strip()
        if not s:
            return 0
        
        sign=1
        i=0

        if s[0] in '+-':
            sign=-1 if s[0]=='-' else 1
            i+=1
        
        while i<len(s) and s[i]=='0':
            i+=1

        return getint(s,i,0,sign)