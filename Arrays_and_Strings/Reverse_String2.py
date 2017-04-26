# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        i = 0
        while i < len(s):
            s[i:i+k] = self.reverse(s[i:i+k])
            i+=2*k
        return ''.join(s)
            
    def reverse(self, strList):
        for x in range(len(strList)/2):
        	strList[x], strList[len(strList)-1-x] = strList[len(strList)-1-x], strList[x] 
        return ''.join(strList)