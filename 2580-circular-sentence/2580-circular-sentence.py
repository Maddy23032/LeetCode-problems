class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence=sentence.split()
        if len(sentence)==1:
            if sentence[0][0]==sentence[0][-1]:return True
            else:return False
        if sentence[0][0]!=sentence[-1][-1]:return False
        for i in range(1,len(sentence)):
            if sentence[i][0]!=sentence[i-1][-1]:return False
        return True        