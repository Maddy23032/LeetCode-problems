class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[0]*len(boxes)
        b,m=0,0
        for i in range(len(boxes)):
            l[i]=b+m
            m+=b
            b+=int(boxes[i])
        b,m=0,0
        for i in reversed(range(len(boxes))):
            l[i]+=b+m
            m+=b
            b+=int(boxes[i])
        return l
