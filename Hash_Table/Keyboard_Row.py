# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict = {}
        results = []
        for x in 'qwertyuiop':
            dict[x] = 0
        for x in 'asdfghjkl':
            dict[x] = 1
        for x in 'zxcvbnm':
            dict[x] = 2
        print dict
        for i in range (len(words)):
            samerow = True
            row = dict[words[i][0].lower()]
            for j in words[i]:
                if dict[j.lower()] != row:
                    samerow = False
                    break
            if samerow == True:
                results.append(words[i])
        return results
                