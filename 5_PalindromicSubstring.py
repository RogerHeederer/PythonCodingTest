#아이디어 _ i=0 부터 시작하여 left, right 포인터를 좌 우로 확장시켜나간다
#         1개의 자리수만 고려하여 홀수 확장 후 팰린드롬을 만족하는지 확인하는 방법(1->3->5 ...)
#         2개의 자리수를 고려하여 짝수 확장 후 팰린드롬을 만족하는지 확인하는 방법(2->4->6 ...)을 병행한다
#         현재의 result 값과, 위 두 방법을 통해 얻어낸 스트링값의 결과를. len 길이를 적용하여 max값을 선택한다. 그게 곧 가장 긴 팰린드롬

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left, right): # 좌,우 포인터를 활용하여 확장시키는 함수 정의
            while left >=0 and right < len(s) and s[left] == s[right]: # s길이 범주에 들어오고, 왼쪽과 오른쪽이 같다면
                left -= 1 #확장 시도
                right += 1 #확장 시도
            return s[left+1:right] # 확장된 부분 결과 리턴
                                   # left+1 : 확장 시도가 실패해서 while에 못 들어갔으니, 확징 시도 전 값
                                   # right : [:right] 슬라이싱에서는 right값은 제외되니까 left처럼 +1 안해줘도 됨

        # 여기서부터 확장 시작하는 로직
        # 우선 예외 케이스 처리부터.
        if len(s) < 2 or s == s[::-1]: #글자가 1,0글자거나, 전체 글자와 전체 글자의 역순과 같다면
            return s
        
        # s = "bababd"
        result = ''
        for i in range(len(s) - 1): #오른쪽으로 확장하는 right 인덱스를 고려하여 -1
            result = max(result,
                         expand(i,i), # 1개의 자리수만 고려하여 확장하는 방식 (홀수 확장)
                         expand(i, i+1), # 이어진 2개의 자리수를 고려하여 확장하는 방식 (짝수 확장)
                         key = len) #기준은 길이값. 리턴 받은 문자열에 len함수 적용을 자동으로 시킨다.
            
            #result = max('', expand(0,0), expand(0,1)) = max('', s[0:1], s[1:1]) = s[0:2] #문자열이 긴게 값이 더 큼
            #result = max('ba', expand(1,1), expand(1,2)) = max('b', s[0:3], s[2:2])
            #result = max('bab', expand(2,2), expand(2,3)) = max('bab', s[0:5], s[3:3])
            #result = max('babab', expand(3,3), expand(3,4)) = max('babab', s[2:5], s[4:4])