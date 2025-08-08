class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(base,exp):
            if exp==0:
                return 1
            elif exp%2==0:
                return func(base*base,exp//2)
            else:
                return base*func(base*base,(exp-1)//2)
        
        f=func(x,abs(n))
        return float(f) if n>=0 else 1/f