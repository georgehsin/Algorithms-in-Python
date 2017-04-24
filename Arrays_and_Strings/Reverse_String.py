class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1] # Extended Slices (python method)

    def reverseString2(self, s):
    	'''  - runs too slow
    	for i in range(len(s)-1,-1,-1):
    		newstring += s[i]
    	return newstring
    	'''
    	return ''.join([s[i] for i in range(len(s)-1,-1,-1)])

new = Solution()
print new.reverseString2('hello')