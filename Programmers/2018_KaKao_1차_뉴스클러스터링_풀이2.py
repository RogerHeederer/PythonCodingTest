# def solution(str1, str2):
#     strings = []
#     for string in [str1, str2]:
#         conv = string.upper() #문자 전처리
#         convs = {}
#         for i in range(1, len(conv)):
#             word = conv[i-1] + conv[i] # 캐릭터 2개 단위로 끊어서 워드 만들기
#             if word.isalpha():
#                 # 단어 : 등장횟수로 딕셔너리 구성
#                 convs[word] = convs.get(word, 0) + 1 #get을 통해 value 가져오는데 없으면 0 넣어줌
#         strings.append(convs)
        
#     str1, str2 = strings #언패킹
    
#     #교집합 만들어주기
#     interaction = []
#     for s1 in str1:
#         if s1 in str2:
#             interaction += [s1 for _ in range(min(str1[s1], str2[s1]))]
    
#     #합집합 만들어주기
#     union = []
#     jaccard_keys = set(list(str1.keys()) + list(str2.keys()))
#     for j in jaccard_keys:
#         union += [j for _ in range(max(str1.get(j,0), str2.get(j,0)))] #get을 활용해 한쪽에는 없는 값들은 0으로 세팅해서 순회하는데 문제 없도록
    
#     n = len(interaction) / len(union) if len(union) != 0 else 1
#     return int(n * 65536)