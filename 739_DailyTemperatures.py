#문제 
# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
# If there is no future day for which this is possible, put 0 instead.
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

#아이디어
# T = [73,  74,  75,  71,  69,  72,  76,  73]
#     day0 day1 day2 day3 day4 day5 day6 day7
# 위와 같이 인덱스를 날짜라고 간주한다.
# 1. 검색 포인터가 되는 i를 7부터 시작하여 day 7부터 역순으로 비교를 시작한다. 
# 2. T[i]는 오늘 기온이라 간주하고, 오늘 기온이 stack에 들어간 마지막 날짜의 기온과 비교를 한다. 항상 오늘 날짜 < 스택의 마지막 날짜임
# 3. 오늘 기온이 stack에 들어간 마지막 날짜의 기온보다 따뜻하다면, 그 날짜는 고려대상이 아니기에 stack에서 날려버린다.
# 4. 오늘 기온이 미래의 기온(stack에 들어간 날짜들의 기온)보다 춥다면(낮다면), 미래의 날짜(인덱스) - 현재의 날짜(인덱스)를 계산한 값을 result에 넣어준다.
# 5. 그리고 현재 날짜와 현재 날짜의 온도를 stack에 넣어준다.(인덱스, 온도)
# 위 아이디어를 코드로 구현하면 된다.

class Solution:
    def dailyTemperatures(self, T):
        # T = [73, 74, 75, 71, 69, 72, 76, 73]
        
        result = [0] * len(T)
        stack = []
        
        #stack은 [ [index, value], [index, value] ....] 이렇게 구성시킬 예정
        # index는 현재 날짜를 의미한다고 생각하면 되고, value는 그 날짜의 온도를 의미
        
        for i in range(len(T)-1, -1, -1): # 역방향으로 살펴본다.
            #스택에 값이 있고, 스택의 마지막 값의 value(온도)가 현재 시점(i)의 온도보다 낮다면
            while stack and stack[-1][1] <= T[i]:
                stack.pop() # 마지막 값의 온도는 고려대상이 아니니 빼버린다. 우리는 따뜻한 것만 찾으면 돼
                
            if stack and stack[-1][1] > T[i]: # 스택의 마지막 값 온도가 i 시점의 온도보다 높다면
                result[i] = stack[-1][0] - i #그 따뜻한 온도의 인덱스에 현재 시점의 온도를 빼서 넣어준다
                
            stack.append([i, T[i]]) #그리고 현재 날짜와 온도를 스택 마지막 값에 넣어준다.
            
        print(result)
    
test = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
test.dailyTemperatures(T)