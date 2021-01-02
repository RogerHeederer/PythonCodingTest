#아이디어
#왼쪽 벽 기준으로 담을 수 있는 물의 가능 높이 구하기
        #         ---
        #  ___    |  |
        #  |  |   |  |
        #  |  |   |  |
        #   3   0   5
        # 왼쪽 건물 기준으로 물이 쌓일 수 있는 높이는 3 3 5
        # 오른쪽 건물 기준으로 물이 쌓일 수 있는 높이 5 5 5
        # 둘 중에 min값을 구한다            min:3 3 5
        # 여기서 건물의 높이는 뺀다         mins:3 0 5
        # 최종 물의 가능 높이는(Potential water:0 3 0
        
        
        #왼쪽->오른쪽
        #왼쪽 기준 가능 물 높이 = [1,1,2,2,2,2,3,3,3,3,3] #건물이 x축 1부터 있으니 input값의 인덱스는 1부터 시작
        #오른쪽->왼쪽
        #오른쪽 기준 가능 물높이 =[3,3,3,3,3,3,3,2,2,2,1]
        #둘 중의 Min값       = [1,1,2,2,2,2,3,2,2,2,1]
        #건물 높이           = [1,0,2,1,0,1,3,2,1,2,1]
        #최종 물의 가능 높이   = [0,1,0,1,2,1,0,0,1,0,0]
class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,1,0,2,1,0,1,3,2,1,2,1] len:12
        
        left, right = [], []
        both = []
        result = []
        soFarMax = 0
        
        #왼쪽 벽 기준으로 담을 수 있는 물 높이
        for i in range(1, len(height)):
            soFarMax = max(soFarMax, height[i])
            left.append(soFarMax)
        print("left 기준 가능 물높이:", left)  
        
        
        #오른쪽 벽 기준으로 담을 수 있는 물 높이
        soFarMax = 0
        for i in range(len(height)-1, 0, -1):
            soFarMax = max(soFarMax, height[i])
            right.append(soFarMax)
        right.sort(reverse=True)
        print("right 기준 가능 물눞이:", right)

        #양쪽 벽을 고려했을 때 담을 수 있는 실제 높이
        for i in range(len(left)):
            both.append(min(left[i], right[i]))
        print("양쪽 건물 고려 가능 물 높이:", both)
        
        
        for i in range(0, len(both)):
            result.append(both[i] - height[i+1])
        print("최종 물 높이:", result)
        
        return sum(result)