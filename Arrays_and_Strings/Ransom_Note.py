# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for x in magazine:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        for y in ransomNote:
            if y in dict:
                dict[y]-=1
                if dict[y] < 0:
                    return False
            else:
                return False
        return True
                