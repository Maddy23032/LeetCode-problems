class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def isp(st):
            if len(st)<len(searchWord):return False
            for j in range(len(searchWord)):
                if st[j]!=searchWord[j]:
                    return False
            return True        
        sentence=sentence.split()
        v=float('inf')
        for i in range(len(sentence)):
            if isp(sentence[i]):
                v=min(v,i)
        return -1 if v==float('inf') else v+1        