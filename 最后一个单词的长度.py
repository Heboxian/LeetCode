class Solution:
    def lengthOfLastWord(self, s):
        a = s.split(" ")
        b = a.copy()
        b.reverse()
        
        if len(s)>0 and a[-1]=='':
            
            for i in b:
                if i!='':
                    return(len(i))
  
        return(len(a[-1]))
