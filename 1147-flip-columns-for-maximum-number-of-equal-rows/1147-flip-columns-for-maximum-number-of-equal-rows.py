class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hm=defaultdict(int)
        for i in matrix:
            rk=tuple(i)
            if i[0]:
                rk=tuple([0 if j else 1 for j in i])
            hm[rk]+=1
        return max(hm.values())        