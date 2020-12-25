class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h={}
        for string in ransomNote:
            if string not in h:
                h[string]=1
            else:
                h[string]+=1
        for key in h.keys():
            if h[key]>magazine.count(key):
                return False
        return True
