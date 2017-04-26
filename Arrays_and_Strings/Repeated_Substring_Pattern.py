# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str 
        :rtype: bool
        """
        for x in range(len(str)/2):
            multiple = len(str)/(x+1)
            sub = str[:x+1]
            if sub*multiple == str:
                return True
        return False