# Time:  O(nlogn)
# Space: O(logn) for stack call
#
# Sort a linked list in O(n log n) time using constant space complexity.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
            
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param head, a ListNode
    # @return a ListNode 
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)
        
        return self.mergeTwoLists(sorted_l1, sorted_l2)
           
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        
        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next
                
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
            
        return dummy.next

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next= ListNode(2)
    print Solution().sortList(head)


"""

링크드리스트를 소트하라는 문제인데 엔로그엔으로 풀어라

Can I think for a second?

엔로그엔 타임으로 풀으라는 것은, 퀵이나 머지소트를 하라는 것인데, 
링크드리스트이니까 인덱스를 사용할 수 없고, 머지소트를 사용해야 할 것 같다.

중간의 포인트를 구하는 것은 투포인터스(패스트와 슬로우 포인터스)를 사용하면 될 것 같고,
머지함수를 하나 정의하고, 전체를 재귀하면 될 것 같은데
리커젼을 사용하면 리커젼은 오로그엔 만큼 일어나고, 스택은 그만큼 사용하게 된다.

Does it look like a good strategy?

"""
