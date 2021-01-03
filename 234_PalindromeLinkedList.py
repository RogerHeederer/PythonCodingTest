# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#아이디어 _ collections 모듈의 deque 특성을 활용해보자
# deque는 오른쪽 끝과 왼쪽 끝의 위치에서 원소를 넣었다 뺐다 할 수 있다.
# appendleft, append / popleft, pop
# deque에 모든 원소들을 넣은 다음에, 양쪽 끝을 동시에 빼서 같은지 비교해보면 된다.
from collections import deque

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        q = collections.deque()
        
#         print(ListNode)
#         print(head)
        
        #Termination condition check
        if not head: # 아무것도 없는 공백이라면 팰린드롬 만족
            return True
        
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
        print(q)
        
        while len(q) > 1: # 길이가 1이면 원소가 하나라 팰린드롬 만족
            if q.popleft() != q.pop():
                return False
        
        return True
        