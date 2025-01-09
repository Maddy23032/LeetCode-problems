class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # c=0
        # for i in words:
        #     if i.startswith(pref):
        #         c+=1
        # return c
        return sum(i.startswith(pref) for i in words)