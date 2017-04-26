# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for x in range(0, len(s)):
            if s[x] in dict:
                dict[s[x]] = 'null' 
            else:
                dict[s[x]] = x
        min = len(s)+1
        for value in dict.values():
            if value != 'null':
                if value < min:
                    min = value
        if min == len(s)+1:
            return -1
        else:
            return min

