class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # if len(word)==5 and k>0:
        #     return 0
        # n=len(word)
        # v={'a','e','i','o','u'}
        # a=e=i=o=u=0
        # c=0
        # for j in range(5+k):
        #     if word[j]=='a':a+=1
        #     elif word[j]=='e':e+=1
        #     elif word[j]=='i':i+=1
        #     elif word[j]=='o':o+=1
        #     elif word[j]=='u':u+=1
        #     else:c+=1
        # for j in range(1,n-5+1):
        #     if word[j-1]=='a':a-=1
        #     if word[j-1]=='e':e-=1
        #     if word[j-1]=='i':i-=1
        #     if word[j-1]=='o':o-=1
        #     if word[j-1]=='u':u-=1
        #     if word[j+5+]
        def atk(k):
            vow=defaultdict(int)
            c=0
            l=0
            res=0
            for i in range(len(word)):
                if word[i] in "aeiou":
                    vow[word[i]]+=1
                else:
                    c+=1
                while len(vow)==5 and c>=k:
                    res+=len(word)-i
                    if word[l] in "aeiou":
                        vow[word[l]]-=1
                    else:
                        c-=1
                    if vow[word[l]]==0:
                        vow.pop(word[l])
                    l+=1
            return res
        return atk(k)-atk(k+1)