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

# find the node at which the intersection of two singly linked lists begins
    def getIntersectionNode1(self, headA, headB): #original solution
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return 
        dict = {}
        while headA:
            dict[headA.val] = True
            print headA.val
            headA = headA.next
        while headB:
            if headB.val in dict:
                return headB
            headB = headB.next
        return 
    def getIntersectionNode2(self, headA, headB): #optimized solution O(n) time and O(1) memory
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return 
        pointerA, pointerB = headA, headB
        while pointerA is not pointerB:
            if not pointerA:
                pointerA = headB
            else:
                pointerA = pointerA.next
            if not pointerB:
                pointerB = headA
            else:
                pointerB = pointerB.next
        return pointerA
#you are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = str(int(num1) + int(num2))
        l1 = ListNode(num1[0])
        num2 = l1
        for x in range(1,len(num1)):
            l1.next = ListNode(num1[x])
            l1 = l1.next
        return num2