class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque([[beginWord,1]])
        s=set(wordList)
        if beginWord in s:
            s.remove(beginWord)
        print(q)
        while q:
            st,steps=q.popleft()
            if st==endWord:return steps
            st=list(st)
            for i in range(len(st)):
                orig=st[i]
                for j in range(26):
                    st[i]=chr(j+97)
                    nst="".join(st)
                    if nst in s:
                        s.remove(nst)
                        q.append([nst,steps+1])
                st[i]=orig
            print(q)
        return 0