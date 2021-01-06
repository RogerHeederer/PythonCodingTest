# 문제 
# 수열이 주어짐
# [6,6,3,3,4,4,4,2,3,3,3,6,6,6]
# 연속해서 나오는 숫자의 횟수를 카운트해서 다시 리스트로 만듬
# [2,2,3,2,1,3,3]
# 연속해서 나오는 숫자의 횟수를 카운트해서 다시 리스트
# [2,1,1,1,2] ... 쭉쭉 반복해서 [1]이 나올때까지 만듬
# [1]로 완성되기까지의 위 과정을 수행한 횟수를 리천하라

# 풀이 B 승리#

# 풀이 A #
def solution(arr):
    call_count = 0

    def trim_count(arr):
        nonlocal call_count
        call_count += 1
        count = 1
        trim = []
        for i in range(len(arr)-1): # i = 0 ~ 5
            if arr[i] == arr[i+1]:
                count += 1
            else:
                trim.append(count)
                count = 1
        
        trim.append(count)

        if len(trim) >= 1:
            if len(trim) == 1 and trim[-1] == 1:
                return
            else:
                trim_count(trim)
        
    trim_count(arr)
    print(call_count)

#풀이 B#
def solution2(arr):
    def merge(arr):
        answer = []
        amount = 0
        for i in range(len(arr)):
          if i > 0:
            if arr[i] == arr[i-1]:
              amount += 1
            else:
              amount += 1
              answer.append(amount)
              amount = 0    
        answer.append(amount+1)
        return answer

    n = 0
    while arr != [1]:
        arr = merge(arr)
        n += 1
    return n