# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_ll_from_list(ll: List) -> ListNode:
    head = ListNode(ll[0])
    temp = head
    for i in range(1, len(ll)):
        temp.next = ListNode(ll[i])
        temp = temp.next
    return head

class Solution:
    def create_list(self, head: Optional[ListNode]) -> List:
        if not head:
            return []
        list_ = []
        while head:
            list_.append(head.val)
            head = head.next

        return list_

    def pairSum(self, head: Optional[ListNode]) -> int:
        head_copy = self.create_list(head)
        rev_head = list(reversed(head_copy))
        total_nodes = len(head_copy)

        ans = 0

        i, iterator = 1, 0

        while i <= total_nodes // 2:
            i += 1
            ans = max(
                ans, (
                        head_copy[iterator] + rev_head[iterator]
                )
            )
            iterator += 1

        return ans


list_ = [5,4,2,1]

head = create_ll_from_list(list_)

sol_obj = Solution()
print(sol_obj.pairSum(head))