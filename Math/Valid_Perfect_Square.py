# Given a positive integer num, write a function which returns True if num is a perfect square else False.

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrt = 0
        x = 0
        while sqrt < num:
            x += 1
            sqrt = x ** 2
            if sqrt == num:
                return True
        return False