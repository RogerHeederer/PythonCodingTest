# 비슷한 개념 Knapsack problem
# https://www.youtube.com/watch?v=mGfK-j9gAQA&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=4&t=11s

# 아이디어
# 3가지 경우의 수
# 1. 현재 버튼이 커맨드에 속할 경우에 해당 버튼을 사용할 경우 (Include)
# 2. 현재 버튼이 커맨드에 속할 경우에 해당 버튼을 배제할 경우 (Exclude)
# 3. 현재 버튼이 커맨드에 속하지 않을 경우, 해당 버튼을 배제하는 경우 (Exclude)

#[ABC, CXY, YZ] 
# 왼쪽 엣지는 해당 인덱스의 단어들을 쓰는 경우, 오른쪽 엣지는 해당 인덱스의 단어를 pass 하는 경우
# 해당 인덱스의 단어가 cmd에 속하지 않는 경우까지 구현해주어야 *로 표시된 단계에서 추가 엣지로 진행될 수 있다
#                                                   ABCXYZ
#         (i=0)ABC                    ()XYZ                                 ABCXYZ
#
#         (i=1)CXY                    *()XYZ                        *AB()Z               ABCXYZ
#
#         (i=2)YZ                   ()X()  ()XYZ                     AB()Z           ABCX()      ABCXYZ

def solution(cmd, btn, profit):
    
    #우선, btn 점수가 캐릭터 갯수 점수보다 작으면, 스킬 쓸 이유가 없음
    #해당 스킬 점수를 캐릭터 점수로 대체
    if len(btn) == 1:
        if profit[0] < len(btn[0]):
            print(len(cmd))
            return
    else:
        for i in range(1, len(profit)):
            if profit[i-1] < len(btn[i-1]):
                profit[i-1] = len(btn[i-1])
                
    
    def traverse(i, cmd, btn, profit):

        if i == len(btn):
            return len(cmd)

        n1, n2 = 0, 0

        if btn[i] in cmd: # 버튼이 커맨드에 있는 경우
            # 버튼이 커맨드에 있지만 AND 그 버튼을 스킬로 사용하지 않는 경우
            n1 = traverse(i+1, cmd, btn, profit)
            # 버튼이 커맨드에 있고 AND 그 버튼을 스킬로 사용하는 경우
            cmd = cmd.replace(btn[i], '')
            #print(cmd)
            n2 = profit[i] + traverse(i+1, cmd, btn, profit)
            
            return max(n1, n2)

        else: # 버튼이 커맨드에 없는 경우
            # 다음 
            n3 = traverse(i+1, cmd, btn, profit)
            return n3


    a = traverse(0, cmd, btn, profit)
    print(a)

#<vCZ
solution('ABCX', ['AB','CX'], [5,6]) # 정답 11
solution('ABCX', ['AB','BC'], [5,6]) # 정답 8
solution('<v>AB^CYv^XAZ',['v>AB^CYv^XA','<v>A', '^XAZ', 'Yv^XA', '>AB^'], [50, 18, 20, 30, 25]) #정답 59
solution('<v>AB^CYv^XAZ',['<v>A', '^XAZ', 'Yv^XA', '>AB^'], [18, 20, 30, 25]) #정답 59 fail
solution('ABCXYZ', ['CXYZ','AB'], [2,3]) #정답 7
solution('ABCXYZ', ['BCXY'], [2]) #정답 6
solution('ABCXYZ', ['BC','AB','CX'], [5,4,4]) #정답 10
solution('ABCXYZ', ['BCXY','AB'], [2,7]) # 정답 11
solution('ABCXYZ', ['ABC','CXY','YZ'], [4,5,4]) # 정답 9
solution('ABCXYZ', ['AB','BC','YZ'], [5,6,4]) # 정답 12
solution('ABCXYZ', ['AB','CX','YZ'], [4,4,4]) # 정답 12