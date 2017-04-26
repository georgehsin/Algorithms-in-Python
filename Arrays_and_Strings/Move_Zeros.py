class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for x in range (0, len(nums)):
            if nums[x] == 0:
                count += 1
            else:
                nums[x], nums[x-count] = nums[x-count], nums[x]