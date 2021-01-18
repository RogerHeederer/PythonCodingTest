import re
def solution(dartResult):
    
    #0. 문자 변환에 필요한 딕셔너리 구성/ '*' 이 문자는 요구사항이 추가적으로 반영되어야 하여 따로 구현
    charConv = {'S': '**1', 'D':'**2', 'T':'**3', '#': '*-1'}
    results = []
    #1. 입력 문자열을 분할시키기
    parser = re.sub('([SDT][*#]?)', '\g<0> ', dartResult).split()
    print(parser)

    #----- 필요 지식 첨언 ----------
    # print(re.sub('([SDT][*#]?)', '\g<0> ', dartResult)) 
    # #  \g<1> 비명명 그룹 사용, \g<name> 이름을 정하는 명명 그룹도 사용 가능 
    # [SDT][*#]? --> ? 앞의 문자[SDT][*#]가 없거나 하나 있음 = ({0,1})
    #[SDT] 중에 없거나 하나 있는지 체크하고 [*#] 중에 없거나 하나 있는지 체크해서 그룹화해주고, 한칸 띄워줌
    #----- 필요 지식 첨언 끝----------

    #2. 분할된 문자열을 문제 요구사항에 맞춰서 변환시키자
    for parse in parser:
        for char in parse:
            parse = parse.replace(char, charConv.get(char, char)) #.get을 통해 charConv에 key값이 있으면
            #그에 상응하는 value를 리턴해주고, 없으면 key로 던져준 char를 리턴한다.
        print("1차필터:",parse)
        if parse[-1] == '*':
            parse += '2'
            if results: # *은 앞의 결과에도 영향을 줘야하기 때문에, result가 있다는 것은 앞에 결과물이 있다는 얘기
                results[-1] = results[-1][:-1] + '*2+'
        
        parse += '+'
        print("2차필터",parse)

        results.append(parse)
    
    print(results)
    #3. 변환된 문자열을 연산하기
    answer = ''.join(results)
    answer = answer[:-1]
    print(eval(answer))
    
#solution('1S2D*3T')
solution('1D2S3T*')