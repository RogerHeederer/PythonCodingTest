# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 아이디어 _ l1.val과 l2.val을 비교하면서 더 작은 값을 새로운 node로 생성한다
# cursor가 움직이면서 새롭게 생성된 링크드 리스트를 이어준다.
# 핵심 로직 구현하기 전에, 예외 처리로 프로그램을 끝내야 하는 상황들을 우선 기술해준다.

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = cursor = ListNode(0)
        
        while True:
            # termination check 단계
            if l1 is None and l2 is None: # 둘 다 비었을 때
                break
            elif l1 is None:
                cursor.next = l2
                break
            elif l2 is None:
                cursor.next = l1
                break
            else:
                # 여기서부터 핵심 로직
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next #비교가 끝났으니 다음 값으로 넘어간다
                else:
                    smallerVal = l2.val
                    l2 = l2.next #비교가 끝났으니 다음 값으로 넘어간다
                    
                newNode = ListNode(smallerVal)
                cursor.next = newNode
                cursor = cursor.next
                
        return head.next