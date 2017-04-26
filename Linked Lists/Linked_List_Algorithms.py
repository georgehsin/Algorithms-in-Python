# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next

#Reverse a Linked List
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        prev = head
        head = head.next
        prev.next = None
        while head:
            temp = prev
            prev = head
            head = head .next
            prev.next = temp
        return prev

#Delete Duplicates in a linked List
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headnode = head
        if head:
            while head.next != None:
                if head.val == head.next.val:
                    node = head.next
                    head.next = node.next
                else:
                    head = head.next
        return headnode

#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list = []
        while l1 and l2:
            if l1.val < l2.val:
                list.append(l1.val)
                l1 = l1.next
            else:
                list.append(l2.val)
                l2 = l2.next
        while l1:
            list.append(l1.val)
            l1 = l1.next
        while l2:
            list.append(l2.val)
            l2 = l2.next
        return list

#Convert a Sorted List to BST
#First function actually first converts the sorted linked list into an array, then we convert Array to BST
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        list = []
        if not head:
            return None
        double == head
        single == head
        mid = head
        while double != None:
            double = double.next.next
            mid = single
            single = single.next
        return self.sortedArrayToBST(list)

    #Helper Function (Converts a sorted list to a BST)
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root