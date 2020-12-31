#백트레킹 문제 = recursion + termination check를 하면 된다.
#아이디어 : 재귀 파트 구현과, 끝내야 되는 부분을 분리해서 구현해보자
class Solution(object):

    def generateParenthesis(self, n):

        def process(n, numOpen, numClosed, str, result):

            # recurse part
            if numOpen < n: # 주어진 숫자보다 여는 괄호가 부족하다면
                process(n, numOpen+1, numClosed, str+"(", result) #여는 괄호 1개 더해주기

            if numOpen > numClosed: # 현재 여는 괄호가 닫는 괄호보다 많다면
                process(n, numOpen, numClosed+1, str+")", result) #닫는 괄호 1개 더해주기

            # termination check
            if numOpen == n and numClosed == n: #완성 조건을 만족할 때
                result.append(str) #result 객체는 res 주소값을 가지고 있으니, res에 값을 append하는 결과가 됨.
                return
        

        res = [] #generateParenthesis에서 사용할 리스트 변수를 하나 선언해주고
        process(3, 0, 0, '', res)
        print(res)
        return res