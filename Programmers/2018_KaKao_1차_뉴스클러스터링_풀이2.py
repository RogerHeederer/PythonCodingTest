#우리밋 유투버 자료 참고
def solution(str1, str2):
    strings = []
    #-----Preprocessing start-----#
    for string in [str1, str2]: # for in에서 두 개의 인자를 받아서 리스트 묶음으로도 처리 가능
            charset = string.upper()
            strset = {}
            for i in range(1, len(charset)):
                word = charset[i-1] + charset[i]
                if word.isalpha():
                    strset[word] = strset.get(word, 0) + 1 # 단어 등장 횟수를 딕셔너리로 구성/ .get 활용해서 value가 없으면 0으로 세팅
            strings.append(convs) #str1에 대해서 워드 딕셔너리 만들어서 strings에 넣고. str2에 대해서도 반복
    #-----Preprocessing End-----#

    str1, str2 = strings # 언패킹 : strings에 포함된 str1 워드 딕셔너리, str2 워드 딕셔너리를 str1,str2에 각각 분배해줌
                         # 여러 개의 객체를 포함하고 있는 하나의 객체를 풀어주는 것

    # 교집합 생성
    intersection = []
    for s1 in str1:
        if s1 in str2:
            intersection += [s1 for _ in range(min(str1[s1], str2[s1]))]
    
    # 합집합 생성
    union = []
    jaccard_keys = set(list(str1.keys()) + list(str2.keys())) #일단 키들 중복제거해서 셋을 만들어주고
    for j in jaccard_keys:
        union += [j for _ in range(max(str1.get(j, 0), str2.get(j, 0)))]

    if union and intersection:
        answer = int(float(len(intersection)) / float(len(union)) * 65536)
        return answer
    else:
        return 65563