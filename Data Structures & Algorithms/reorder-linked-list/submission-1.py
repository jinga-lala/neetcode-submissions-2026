# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def printList(head):
            while head is not None:
                print(head.val, end=',')
                head = head.next
        
        def getlength(head):
            cnt = 0
            while head is not None:
                cnt +=1 
                head = head.next
            return cnt
        
        length  = getlength(head)
        import math


        first_list = None
        second_list = None

        first_head = head
        second_head = None
        i = 0
        prev_head = None
        while head is not None:
            # if i==0:
            #     first_head = head
            #     first_list = first_head
            #     head = head.next
            #     i+=1
            #     continue
            # elif i==1:
            #     second_head = head
            #     second_list = second_head
            #     head = head.next 
            #     i+=1
            #     continue
            # if i%2==0:
            #     first_list.next = head
            #     first_list = first_list.next
            # elif i%2==1:
            #     second_list.next = head
            #     second_list = second_list.next

            if i == math.ceil(length/2):
                prev_head.next = None
                second_head = head
                break
            prev_head = head
            head = head.next
            i+=1
        
        # important
        # first_list.next = None
        # second_list.next = None
            
        # # print("here")
        # printList(first_head)
        # print()
        # printList(second_head)
        # print()
        second_head_copy = second_head
        prev_head = None
        # reverse second list
        while second_head_copy is not None:
            if prev_head is None:
                prev_head = second_head_copy
                second_head_copy = second_head_copy.next
                prev_head.next = None
                continue
            tmp = second_head_copy.next
            second_head_copy.next = prev_head
            prev_head = second_head_copy
            second_head_copy = tmp
        # second
        second_head = prev_head
        printList(second_head)
        print()
        i = 0
        first_head_copy = first_head
        while first_head_copy is not None:
            tmp = first_head_copy.next
            first_head_copy.next = second_head
            if second_head is not None:
                tmp2 = second_head.next 
                second_head.next = tmp
                second_head = tmp2
            first_head_copy=tmp
        # return first_head

