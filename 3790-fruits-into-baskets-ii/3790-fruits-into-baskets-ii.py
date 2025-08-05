class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        fr=0
        for i in range(len(fruits)):
            c=0
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    c+=1
                    baskets[j]=0
                    break
                
            if c==0:
                fr+=1
        return fr