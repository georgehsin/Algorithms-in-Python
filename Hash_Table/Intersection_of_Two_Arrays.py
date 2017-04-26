# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

# Note:
# Each element in the result must be unique.
# The result can be in any order.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # if len(nums1) <= len(nums2):
        #     one = nums1
        #     two = nums2
        # else:
        #     one = nums2
        #     two = nums1
        # dict = {}
        # arr = []
        # for x in one:
        #     if x not in dict:
        #         dict[x] = 1
        # for y in range(0, len(two)):
        #     if two[y] in dict:
        #         dict[two[y]]-=1
        #         if dict[two[y]]==0:
        #             arr.append(two[y])
        # return arr

#using python methods: shorter code, less memory, however, a bit slower on average
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1&nums2)
        
        