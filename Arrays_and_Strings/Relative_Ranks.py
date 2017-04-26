# # Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dict ={}
        list =[]
        for x in range (len(nums)):
            dict[nums[x]] = x
            list.append(x)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if i < 3:
                list[dict[nums[i]]] = medals[i]
            else:
                list[dict[nums[i]]] = str(i+1)
        return list