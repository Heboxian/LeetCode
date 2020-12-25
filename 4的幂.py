class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return false;
        n1=log(n)/log(4)
        return n1*log(4)==log(n);
        
