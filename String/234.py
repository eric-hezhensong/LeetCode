# coding: utf-8


class Solution(object):
    """
    Palindrome Linked List
    """

    @staticmethod
    def is_palindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val_list = Solution.convert_to_list(head)

        i, j = 0, len(val_list) - 1
        while i < j:
            if val_list[i] != val_list[j]:
                return False
            i += 1
            j -= 1

        return True

    @staticmethod
    def convert_to_list(head):
        result = list()

        if head is None:
            return result

        while head is not None:
            result.append(head.val)
            head = head.next

        return result


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node1.next = node2

    solution = Solution()
    print solution.is_palindrome(node1)
