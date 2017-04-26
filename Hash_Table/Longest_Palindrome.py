# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        count = 0
        for x in s:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
                if dict [x] % 2 == 0:
                    count += 2
                    dict[x] = 0
        if count != len(s):
            return count +1 
        return count