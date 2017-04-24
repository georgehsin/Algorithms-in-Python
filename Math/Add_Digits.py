# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit. 

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = num
        while len(str(num))>1:
            sum = 0
            for x in str(num):
                sum += int(x)
            num = sum
        return sum