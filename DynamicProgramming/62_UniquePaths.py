# 아이디어 : (1,2)에 도달하기 위한 방법은 (1,1)에 도달할 수 있는 방법 + (0,2)에 도달할 수 있는 방법
# 이걸 도식화 해보면, reach(i,j) = reach(i,j-1) + reach(i-1,j)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m=3 row(행) /  n=7 col(열)
        matrix = [[1 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):# row 기준 / 가장 위쪽인 row 0빼고
            for j in range(1, n): # col 기준 / 가장 왼쪽인 col 0 빼고
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] #(1,1)부터 시작해서, 위쪽 노드 더하기 왼쪽 노드 더하기
            
        return matrix[-1][-1]
                