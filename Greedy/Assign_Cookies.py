class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        x = len(s)-1
        y = len(g)-1
        output = 0
        while x >= 0 and y >=0:
            if g[y] <= s[x]:
                output += 1
                x -= 1
                y -= 1
            else:
                y -= 1
        return output