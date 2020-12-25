class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = []
        for srt1 in s:

            if( srt1 >= '0' and srt1 <= '9') or (srt1 >= 'a' and  srt1 <= 'z'):
                s1.append(srt1)
        
        if len(s1)%2==0:
            b = s1[len(s1)//2:]
            b.reverse()
            return b == s1[:len(s1)//2]

        else:
            b = s1[len(s1)//2+1:]
            b.reverse()
            return b == s1[:len(s1)//2]

