# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsum = nums[0]
        sum = nums[0]
        for x in range(1, len(nums)):
            sum += nums[x]
            if nums[x] >= sum :
                sum = nums[x]
            if sum>maxsum:
                maxsum = sum
        return maxsum
        
                