class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        hm=dict()
        for i in items:
            if i[0] not in hm:
                hm[i[0]]=i[1]
            else:
                v=max(hm[i[0]],i[1])
                hm[i[0]]=v
        li=[]         
        for j in queries:
            m=0
            for i in hm.items():
                if i[0]<=j:
                    m=max(m,i[1])
                else:break    
            li.append(m)
        return li                