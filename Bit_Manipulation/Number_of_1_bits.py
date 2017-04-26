# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        count = 0
        while n >= 2:
            if n%2 == 1:
                count += 1
            n = n/2
        if n == 1:
            count +=1
        return count