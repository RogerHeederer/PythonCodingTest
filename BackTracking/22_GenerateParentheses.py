#백트레킹 문제 = recursion + termination check
#아이디어 _ 열고 닫는 기호에 대해 생각해보자. 닫는 기호가 여는 기호보다 많을 때는 이미 unvalid한 상태 ()) 이미 잘못된 상태
# 하지만 여는 기호는 언제나 자유롭다. 열어 둔 만큼 닫아주기만 하면 되기 때문에. (((()()())))
# 그렇다면, 여는 기호를 기준으로 로직을 세워보자
# 1. 여는 기호가 주어진 n보다 작을 때는, n에 도달할 때 까지 계속 열어주면 된다. n = 3  이 행위
# 2. 닫는 기호가 여는 기호보다 적을 때는, 여는 기호의 갯수가 될 때까지만 닫아주면 된다. 이 행위 
# 3. 위 두 조건을 지켜가며 진행했을 때, 여는 기호와 닫는 기호가 n 값이 되면, 가능한 경우의 수는 다 나왔다.
# 1,2,3 을 로직으로 구현해보자. recursion을 적용해서
class Solution(object):

    def generateParenthesis(self, n):

        def process(n, numOpen, numClosed, str, result):

            # recurse part
            # 여기서 주의할 점은 아래의 if 조건은 다 별개의 조건이다. if, elif가 아니라는 말
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