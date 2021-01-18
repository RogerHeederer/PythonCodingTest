#우리밋 유투버 자료 참고
import re
import itertools

def solution(expression):
    operators = list(itertools.permutations(['-', '+', '*'], 3))

    expression = re.split('([-+*])', expression)
    #expression = re.split('[-+*]', expression) 이 조건으로 넣으면 부호들이 다 빠진다.
    print("expression is : ", expression)

    results = []
    for operator in operators:
        exp = expression[:] # 위에 expression으로 가져와 복사 및 초기화 / 각 부호 우선순위별 최종 값을 구해야하니까
        for op in operator: #[-, +, *], [+, -, *] ... 조합들을 다 돌림
            while op in exp: # -가 단수/복수개를 전부 훑고 -> + -> *
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1])) #eval이 반환하는 값은 정수. 
                del exp[idx:idx+2]
        
        results.append(abs(int(exp[0])))
    
    print(max(results))

solution("100-200*300-500+20")
solution("50*6-3*2")