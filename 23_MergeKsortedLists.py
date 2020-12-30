#문제
# Leet Code 23번
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #아이디어 : heapque 자료구조(루트 노트가 가장 작은 값으로 위치시킴)의 성질을 이용해서, 최소값 우선을 꺼내는 성질을 사용해서 풀어보자
        dummy = ListNode(0)
        current = dummy
        data = []
        
        # 리스트에 담겨있는 [1,4,5], [1,3,4], [2,6] 덩어리들을 하나씩 가져온다. 이 덩어리들은 연결 리스트 구조임
        for node in lists:
             while node: #여기 노드에 들어가는 순서는 1,4,5,1,3,4,2,6 순서로 들어간다
                    #여기서 heapq가 동작하는 원리 설명이 필요하다.
                    #data 리스트에 위 노드 순으로 입력을 넣어주는데, 넣은 후 힙 조건을 만족하게 바로 바로 , 그때 그때 정렬해준다고 생각하면 된다.
                    #즉, 가장 작은 값이 완전 이진 트리의 노드로 오도록 정렬을 계속 해주는 방식이다.
                    # 1 넣고 힙조건에 맞게 정렬. 4 넣고 힙 조건에 맞게 정렬. 5 넣고 힙 조건에 맞게 정렬, 1넣고 힙 조건에 맞게 정렬
                    # [1] / [1,4] / [1,4,5] / [1,1,5,4] / [1,1,5,4,3] 이런 식으로 힙 특성에 맞는 정렬이 계속 이루어진다.
                    heapq.heappush(data, node.val)
                    node = node.next
        
        while data:#그렇게 정렬된 데이터를 기반으로
            val = heapq.heappop(data)#이진트리의 루트부터 꺼낸다 -> 최소값 우선으로 꺼낸다는 말 -> 루트가 뽑힌 후 다시 힙 성질에 맞게 정렬작업을 해 놓는다.
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next #애초에 dummy 객체는 ListNode(0)을 가르키고 있었고, dummy.next가 data의 시작점 주소를 지니고 있다.

        #코딩테스트 훈련 공간 리트코드 문제풀이 위주로 학습하며, 초보자들도 수월하게 이해할 수 있도록. 최대한 자세하게 주석을 달아 해석하고자 합니다.