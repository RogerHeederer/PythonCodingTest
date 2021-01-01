# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#아이디어 _  1. 각 리스트에 포인터를 별개로 지정 후 순차적으로 탐색
#          2. 값 올림을 담을 수 있는 변수를 선언
#          3. 합계를 담을 수 있는 임시 노드를 선언(0)하고, 움직이면서 합을 담아낼 cursor 변수와, 맨 처음 자리를 지킬 head 변수를 선언
#          4. 각 리스트의 위치를 함께 순회하며, 값을 더하고, 더해진 값을 활용해 새로운 노드를 만든다. 그리고 그 새로운 노드에 cursor를 이어 줌

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # tmp = Node(0) l1 = [2,4,3] l2 = [5,6,4]
        # l1 reverse = [3,4,2] / l2 reverse = [4,6,5]
        
        #탐색을 위한 포인터 선언
        p1 = l1
        p2 = l2
        
        # 올림 수 값 선언
        currentCarry = 0
        
        #ListNode(0)을 선언하여 임시로 활용할 노드 선언
        head = cursor = ListNode(0) #cursor를 계속 조정하며 탐색할거고, head는 ListNode(0) 값에 고정하여 위치하고 있음
        
        # l1과 l2를 동시에 탐색 시작한다
        while p1 or p2 or currentCarry:
            print(p1.val, p2.val, currentCarry) # 현재 값 한번 확인해보고
            currentVal = currentCarry # 올림 값을 현재 값에 세팅해줌 (0 or 1)
            currentVal += 0 if p1 is None else p1.val #p1이 None 값이면 +=0을 연산하고, 그렇지 않으면 += p1.val을 연산
            currentVal += 0 if p2 is None else p2.val #p2가 None 값이면 +=0을 연산, 그렇지 않으면 +=p2.val을 연산
            
            if currentVal >= 10: # p1.val + p2.val이 10을 넘어가면, 자리수 올려주고, 지금 값은 10을 뺀다.
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0
            
            cursor.next = ListNode(currentVal) #p1.val과 p2.val을 합쳐서 나온 값을 새로운 리스트 노드로 생성하고, cur과 이어준다.
            cursor = cursor.next #그리고 cur의 위치를 currentVal로 옮겨준다. #이 과정을 반복하면, 각 자리의 합계 값들이 연결된다.
            
            # termination check
            if p1 is None and p2 is None: # p1과 p2가 더 이상 값이 없다면, 작업 끝. 종료.
                break
            elif p1 is None: # p1만 없다면, p2는 다음 원소로 넘어감
                p2 = p2.next
            elif p2 is None: # p2만 없다면, p1은 다음 원소로 넘어감
                p1 = p1.next
            else:
                p1 = p1.next # p1, p2 둘다 다음 원소로 넘김
                p2 = p2.next
                
        print('exit...')
        
        print(head)
        return head.next #head.next부터가 합계 값이 계산된 노드들이다.