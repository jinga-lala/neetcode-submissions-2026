# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # return_head = head
        def reverse_list(head):
            reverse_list = head
            prev_head = None
            while reverse_list is not None:
                if prev_head is None:
                    prev_head = reverse_list
                    reverse_list = reverse_list.next
                    prev_head.next=None #sealing the forward head
                    continue
                tmp = reverse_list.next
                reverse_list.next = prev_head
                prev_head = reverse_list
                reverse_list = tmp
            return prev_head

        end = reverse_list(head)
        end_copy = end
        prev_head = None
        for i in range(n-1):          
            prev_head = end
            end = end.next
        # you need to remove end
        if prev_head is not None:
            prev_head.next = end.next
        else:
            end_copy = end_copy.next
        
        new_head = reverse_list(end_copy)
        return new_head

            
