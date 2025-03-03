class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,p,g=[],[],[]
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i==pivot:
                p.append(i)
            else:
                g.append(i)
        return l+p+g