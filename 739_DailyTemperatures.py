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
        result = [0]*len(T)
        stack = []

        for i in range(len(T)-1, -1, -1):
            while stack and stack[-1][1] <= T[i]: #현재 날씨가 미래 날씨보다 따뜻하다면
                stack.pop()                       #그 날씨는 고려대상이 아니기에 빼버린다.
            if stack and stack[-1][1] > T[i]:     #현재 날씨가 미래 날씨보다 춥다면
                result[i] = stack[-1][0] - i      #결과 리스트에 해당 미래날씨 일자 - 현재 일자를 해서 넣어준다.
            stack.append([i, T[i]])               #그리고 현재 날씨를 stack에 넣어준다.

        print(result)


arr = [73,74,75,71,69,72,76,73]

test = Solution()
test.dailyTemperatures(arr)