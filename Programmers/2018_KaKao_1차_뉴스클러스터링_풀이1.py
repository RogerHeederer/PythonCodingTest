# 카운터 라이브러리를 사용한 간결한 풀이
# 카운터 객체는 교집합, 합집합, +,-,substract 연산이 가능하다. elements() 메서드로 요소 리스트 리턴도 가능
# https://dongdongfather.tistory.com/70 카운터 객체 연산 참조

from collections import Counter
def solution(str1, str2):

    #-----Preprocessing Start-----#
    s1, s2 = [], []
    for i in range(1, len(str1)):    
        if str1[i-1:i+1].isalpha():
            s1.append(str1[i-1:i+1].lower()) # +=으로 사용하면 캐릭터by캐릭터로 들어감
    
    for i in range(1, len(str2)):
        if str2[i-1:i+1].isalpha():
            s2.append(str2[i-1:i+1].lower())

    c1 = Counter(s1)
    c2 = Counter(s2)
    print(c1)
    print(c2)
    print(c1&c2)
    #-----Preprocessing End-----#
    
    intersection = sum((c1&c2).values())
    union = sum((c1|c2).values())


    if c1 and c2: # c1, c2 둘다 존재하는 경우
        answer = int(float(intersection)/float(union) * 65536)
        return answer
    else:
        return 65536

    solution('FRACNE', 'french')
    solution('handshake', 'shake hands')
    solution('aa1+aa2', 'AAAA12')

    