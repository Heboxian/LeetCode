class Solution:
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)
        c = a+b
        result = '{0:b}'.format(c)
        return result
