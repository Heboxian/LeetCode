class Solution(object):
    def arrangeCoins(self, n):
 
        c = 0
        while n > c:
            c = c + 1
            n = n - c
        return c
