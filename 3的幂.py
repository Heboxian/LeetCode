class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return 1
        while(n>1):
            n=n/3
            if n==1:
                return 1
        
        return 0
