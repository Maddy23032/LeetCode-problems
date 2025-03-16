class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l,r=1,ranks[0]*cars*cars
        res=-1
        while l<=r:
            m=(l+r)//2
            c=0
            for i in ranks:
                c+=int(sqrt(m/i))
            if c>=cars:
                res=m
                r=m-1
            else:
                l=m+1
        return res 