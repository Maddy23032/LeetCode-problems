class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        su=0
        for i in derived:
            su^=i
        return False if su else True