# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # none /  1->2->3->4->5->Null
        #  p     h,c n
        # 우선, prev, next 변수가 추가적으로 새로 쓰인다.
        # node.next와 next는 다른 것
        # 아이디어
        # 인덱스 2번째 위치에 값을 먼저 할당 후에, 역순 링크를 생각한다.
        
        # None 이라는 스칼라 타입 선언. scalar type 종류 : int, float, None(값없음), bool(True, False)
        cursor, prev = head, None
        
        while cursor:
            next = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = next
            
        return prev