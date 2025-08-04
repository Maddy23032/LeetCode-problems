class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        maxlen = 0
        l = 0
        
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            
            while len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            
            maxlen = max(maxlen, r - l + 1)
        
        return maxlen
