# 아이디어 : (1,2)에 도달하기 위한 방법은 (1,1)에 도달할 수 있는 방법 + (0,2)에 도달할 수 있는 방법
# 이걸 도식화 해보면, reach(i,j) = reach(i,j-1) + reach(i-1,j)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #로봇이 갈 수 있는 방향은 오른쪽 or 아래 밖에 없음
        # m(row) = 3  /  n(col) = 7
        result = [] # [[1,1,1,1,1,1,1,],[],[]]
        for i in range(m):
            #다른 문법 표현에 따른, 다른 결과를 인지할 수 있어야 한다.
            #result.append([i]) #[[0],[1],[2]]
            #result.append(i) #[0,1,2]
            #result+=[i] #[0,1,2]
            result+=[[i]] #[[0],[1],[2]]
        print(result)
        
        print("문제 풀이 시작")
        # 3row X 7col 원소에 전부 1로 채워넣는 로직
        # 제일 안쪽 []에 1을 먼저 7개 채워넣고, [1,1,1,1,1,1,1] 이 덩어리를 3번 수행함
        matrix = [[1 for j in range(n)] for i in range(m)]

        for i in range(1,m): # row 1부터 시작
            for j in range(1, n) #col 1부터 시작
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
            
            return matrix[-1][-1] #가장 마지막 매트릭스 값 = 제일 오른쪽 아래