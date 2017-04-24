# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x
        y = y
        count = 0
        for i in range (31,-1,-1):
            j = 0
            k = 0
            if x/(2**i)  == 1: 
                x = x%(2**i)
                j = 1
            if y/(2**i) == 1:
                y = y%(2**i)
                k = 1
            if j != k:
                count += 1
        return count