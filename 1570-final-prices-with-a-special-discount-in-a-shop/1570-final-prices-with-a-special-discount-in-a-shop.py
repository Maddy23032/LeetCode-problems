class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        r=[i for i in prices]
        st=[]
        for i in range(len(prices)):
            while st and prices[st[-1]]>=prices[i]:
                j=st.pop()
                r[j]-=prices[i]
            st.append(i)    
        return r        