# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(bin(num))
        newnum = ''
        for x in range(2, len(num)):
            if num[x] == '1':
                newnum += '0'
            else:
                newnum += '1'
        return int(newnum, base=2)