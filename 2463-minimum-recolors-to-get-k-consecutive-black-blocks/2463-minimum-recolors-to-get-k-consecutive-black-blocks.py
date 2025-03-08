class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b,w=0,0
        for i in range(k):
            if blocks[i]=='B':
                b+=1
            elif blocks[i]=='W':
                w+=1
        if b>=k:
            return 0
        res=101
        res=min(res,w)
        for i in range(1,len(blocks)-k+1):
            if blocks[i-1]=='W':
                w-=1
            if blocks[i+k-1]=='W':
                w+=1
            if blocks[i-1]=='B':
                b-=1
            if blocks[i+k-1]=='B':
                b+=1
            res=min(res,w)
        return res