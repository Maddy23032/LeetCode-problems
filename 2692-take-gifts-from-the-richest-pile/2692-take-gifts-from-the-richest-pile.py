import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            a=gifts[0]
            ind=0
            for j in range(1,len(gifts)):
                if gifts[j]>=a:
                    ind=j
                    a=gifts[j]
            gifts[ind]=math.floor(gifts[ind]**(1/2))
        s=0
        for i in gifts:
            s+=i
        return s        