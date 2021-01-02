class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 리스트 활용법 소개
        
        # 유형 1 : 1차원 리스트 []
        # +=과 append의 미묘한 차이점
        print("-------유형 1 시작------")
        output = []
        for i in nums:
            output += [i] # == output.append(i)
        print(output) #[1, 2, 3]
        print('\n')
        
        output = []
        for i in nums:
            #output += i # 리스트 안에 int 못들어감
            output.append(i) # 대신 append로 넣으면 가능
        print(output) #[1, 2, 3]
        print('\n')
        
        output = []
        for i in nums:
            output += str(i)
        print(output) #['1', '2', '3']
        print('\n')
        
        output = []
        for i in nums:
            output.append(str(i)) #['1', '2', '3']
        print(output)
        print('\n')
        print('------유형 1 끝--------')
        print('------유형 2 시작--------')
        #유형 2: 2차원 리스트 [[]]
        # 여기서부터 +=과 append의 미묘한 차이가 나타난다.
        output = [[]]
        for i in nums:
            output.append(i)
        print(output) #[[], 1, 2, 3]
        print('\n')
        
        output = [[]]
        for i in nums:
            #output += i # int는 iterable에 넣을 수 없음
            output += str(i)
        print(output) #[[],'1','2','3']
        print('\n')
        
        print("아래 예시 주목")
        # 위에 예시까지는 append와 += 연산 역할이 크게 달라보이지 않는다.
        # 하지만 아래 예시에서는 차이가 나타남
        
        output = [[]]
        for i in nums:
            output.append([i])
        print(output) #[[],[1],[2],[3]] # row 4 / co1 1
        print('\n')
        
        output = [[]]
        for i in nums:
            output += [i]
        print(output) #[[],1,2,3] # 이건 1차원 리스트임
        print('\n')
        
        print("다른 유형")
        output = [[]]
        for i in nums:
            output.append([[i]])
        print(output) #[[],[[1]],[[2]],[[3]]]
        print("\n")

        output = [[]]
        for i in nums:
            output += [[i]]
        print(output) #[[], [1],[2],[3]]
        print("\n")
        
        print("리스트 연산 유형")
        print([] + [2]) #파이썬은 리스트 끼리의 연산이 가능함
        print([2] + [1]) #[2,1]
        #print([2] - [1]) #에러
        print([2]*10)
        print('\n')