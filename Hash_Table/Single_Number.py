# Given an array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x]=1
            else:
                dict.pop(x)
        for key in dict.iterkeys():
            return key