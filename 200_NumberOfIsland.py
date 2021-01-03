#아이디어 DFS를 사용해서 서치한다
#BFS는 Breadth-First Search의 약자로 Queue를 사용해서 방문 노드를 visited 처리를 한다
#DFS는 Depth-First Search의 약자로 stack 자료구조 혹은 재귀 함수를 이용하며, LIFO의 특징을 지닌다. 
#마지막에 들어간게 처음으로 out되는 개념이 깊이 탐색과 같은 개념이다. 그래서 DFS는 스택 자료구조로도 구현이 가능하다.
class Solution:

    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 인풋이 2차원인 경우 필요한 지식 정리
        print("Row 값 :",len(grid)) # row값으로 4 출력: 가장 바깥쪽 차원'[ ]'을 기준으로 내부 [] 덩어리 갯수 출력
        print("grid[0]:", grid[0])

        print("Col 값:", len(grid[0])) # col 값으로 5 출력 : 다음 안쪽 차원 '[]'을 기준으로 내부 길이 출력
        print("grid[0][4]:", grid[0][4])
        print(100 and 'hi') # 앞의 100은 트루로 인식
        print("----사전 지식 정리 끝----")

        row, col = len(grid), len(grid) and len(grid[0]) # row 및 col 할당 / 직관적 이해를 위해 row,col로 정의함
                                                     # len(grid) 행이 존재한다면 True and 열의 길이를 반환하는 코딩 방식
            
        count = 0
        for r in range(row): # 0 ~ 3
            for c in range(col): # 0 ~ 4
                if grid[r][c] == '1': #현재 위치에 값이 1이면(땅이면)
                    self.dfs(grid, r, c) # 현재 위치를 기점으로 dfs 시작
                    count += 1 #이 단계에 온거는, dfs로 상하좌우 이어진 탐색이 끝났다는 소리. 그럼 섬 사이즈 체크가 끝났으니 섬 갯수를 올려줌
            print(grid[r])
        return count
                    
    def dfs(self, grid, r, c):
        # Temination condition check
        #i,j가 음수이거나, 주어진 차원 길이를 넘어가거나, 현재 선택한 값이 1이 아닌 경우(땅이 아니고 물인 경우)
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != '1':
            return # DFS 수행 안함

        grid[r][c] = '#' # dfs 실행이 성공한 위치(1인 위치)에 # 표시로 캐릭터 대체. 그래야 위,아래,좌,우 움직이면서
                         # 이미 처리했던 곳은 반복해서 처리하지 않는다(무한루프에 빠지면 안된다)
        
        self.dfs(grid, r+1, c) # 상하 조절 row
        self.dfs(grid, r-1, c) # 상하 조절 row
        self.dfs(grid, r, c+1) # 좌우 조절 col
        self.dfs(grid, r, c-1) # 좌우 조절 col
