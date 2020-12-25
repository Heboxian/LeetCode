class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        gi = 0
        si = 0

        while si<len(s) and gi<len(g):
            if g[gi]<=s[si]:
                gi = gi+1
                si = si+1
            else:
                 si = si+1

        return gi
