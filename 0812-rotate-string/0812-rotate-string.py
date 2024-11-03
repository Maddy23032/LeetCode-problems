class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False
        for i in range(len(s)):
            st=s[i:]+s[:i]
            if st==goal:return True
        return False    