# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums)-1]:
             return len(nums)
        elif target < nums[0]:
            return 0
        for x in range (0, len(nums)):
            if nums[x] == target:
                return x
            elif nums[x] > target:
                return x
       