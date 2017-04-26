# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

class Solution(object):
# Using Hash Table
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for x in s:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        for x in t:
            if x not in dict:
                return False
            else:
                dict[x] -= 1
            if dict[x] <0:
                return False
        for value in dict.values():
            if value != 0:
                return False
        return True
        
        # return sorted(s) == sorted(t)