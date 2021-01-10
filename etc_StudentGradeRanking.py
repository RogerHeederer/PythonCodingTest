# [2,3,1,2] -> [2,1,4,2]
def solution(grade):
    result = []
    for i in range(0, len(grade)): # A 포인트를 랭크 1로 잡고 시작
        rank = 1
        for j in range(0, len(grade)): # B 포인트가 순회하며 
            if grade[i] < grade[j]:
                rank += 1
        result.append(rank)

    return result

solution([2,2,1])
solution([3,2,1,2])