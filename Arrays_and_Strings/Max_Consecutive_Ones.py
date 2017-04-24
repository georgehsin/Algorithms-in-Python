# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        count = 0
        for x in(nums):
            if x == 0:
                count = 0
            else:
                count += 1
            if count > max:
                max = count
        return max