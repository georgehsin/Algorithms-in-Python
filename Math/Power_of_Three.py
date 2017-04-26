# Given an integer, write a function to determine if it is a power of three.

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 0
        value = 0
        while value < n:
            if 3**x == n:
                return True
            else:
                value = 3 ** x
                x += 1
        return False
        
#Need to optimize