#아이디어 : 나아가는 방향은 어차피 오른쪽 방향, 아래쪽 방향. 두가지 방향밖에 없다.
#         첫 행과 첫 열을 기준으로 삼아 누적값을 만든다.
#         1  4  5
#         2
#         6     ?

# 우리가 구하고자 하는 값은 ?이니까, 빈 공간들을 채워 넣으면서 ?로 도달하면 된다.
# 즉, 왼쪽과 위쪽 방향에 위치한 두 원소들 중에서 작은 값을 더하는 식으로 계산을 반복하면, ?까지 도달하기 위한 최소값을 구할 수 있다.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        
        row, col = len(grid), len(grid[0])
        
        for i in range(1, col): # i= 1, 2, 3, 4 ... n / # row를 고정
            grid[0][i] += grid[0][i-1] # grid[0][1] += grid[0][0]
                                       # grid[0][2] += grid[0][1]

        for i in range(1, row): # i = 1, 2, 3, 4 ... m / # col를 고정
            grid[i][0] += grid[i-1][0] # grid[1][0] += grid[0][0]
                                       # grid[2][0] += grid[1][0]
  

        # 위 작업으로, [0,0]에서 시작하여 가로 한줄, 세로 한줄의 누적값은 다 구했다.
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])#위쪽과 왼쪽 값 중에 최소값을 더하는 형태로 계산
        
        return grid[-1][-1]