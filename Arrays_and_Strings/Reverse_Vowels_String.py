# Write a function that takes a string as input and reverse only the vowels of a string.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        vowelfront = 0
        vowelback = 0
        x=0
        y=len(s)-1
        s = list(s)
        while x < y:
            if s[x] not in vowel:
                x+=1
            if s[y] not in vowel:
                y-=1
            if s[x] in vowel and s[y] in vowel:
                s[x], s[y] = s[y], s[x]
                x+=1
                y-=1
        return ''.join(s)