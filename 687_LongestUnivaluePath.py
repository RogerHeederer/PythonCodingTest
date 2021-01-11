# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#아이디어 : DFS로 순회를 시작하여, 현재 시점의 루트 노드와 자식 노드가 연결된다면 1로 처리. 안되면 0으로 처리
# 왼쪽 연결 결과물과 오른쪽 연결 결과물을 더한 결과를 longest[0]에 계속해서 저장해둔다.
#       4
#     4   4   이런 노드 형태면, 왼쪽 오른쪽 다 이어지기 때문에 1+1 = 2이며, 이 길이 값을 저장해둔다.

# 정리하자면, 로직 플로우는 -> 자식 노드들을 끝까지 타고 내려 간 다음, 각 level에서 left값 right값을 구한다.
# 그리고 left+right을 더해서 so_far_longest 값에 담아둔다.
# 그 후, left와 right 중에 큰 값을 부모 노드에게 던져준다. 
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        #인풋 데이터 형태 확인
        print(root)
            

        so_far_longest = [0]
        
        def traverse(node):
            if not node:
                return 0
            #맨 처음 root 5를 시작으로 왼쪽, 오른쪽을 순회시킨다.
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            
            #left와 right은 값이 0이 아니라는 거는 일단 자식 노드와 이어진다는 것. 
            #왼쪽 오른쪽 자식과 둘다 이어지면 길이는 1+1= 2이다. 
            #즉 매 루트 노드마다 좌,우를 더하여 가장 높은 값을 저장해둔다. 지금까지 가장 길게 이어진 길이값을 쟁여둔다.
            so_far_longest[0] = max(longest[0], left+right)
            
            #현재 노드 기준으로, left와 right 길이중에 긴 것을 리턴해준다. 어차피 range는 0,1임. 이어지냐 안이어지냐를 판별해주느것
            return max(left, right)
        
        
        traverse(root)
        return so_far_longest[0] # 가장 길게 연결된 애를 리턴해준다.