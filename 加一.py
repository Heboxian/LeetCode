class Solution:
    def plusOne(self, digits):
        digits.reverse()
        digits_len = len(digits)
        num = 0
        for index,i in enumerate(digits):
            num = num + i*pow(10,index)
        num = num + 1
        a = str(num)
        result = []
        for i in a:
            result.append(int(i))
        
        while(len(result))<digits_len:
            result.insert(0,0)
        return result
