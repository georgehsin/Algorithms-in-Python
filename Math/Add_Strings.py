# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))