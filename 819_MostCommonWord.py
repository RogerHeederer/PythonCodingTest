class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #우선 paragraph를 정규식 활용해서 전처리. ^\w : 단어가 아닌 것은 전부 ' ' 공백 처리 후 소문자화 + 공백 단위 구분 시키기
        paragraph = re.sub('[^\w]', ' ', paragraph).lower().split()
        #print(paragraph) # str 형태였던 paragraph가 위 기준으로 전처리 된 후 리스트 형태로 뿌려진다.
        
        #paragraph에 있는 word중에 if 조건을 만족하는 word 만 가져와라
        #if 조건은 word가 banned에 없는 것. 
        #즉 paragraph에 word를 가져오는데, banned 리스트를 참고해서 banned에 없는 것을 가져와
        
        #필터링 시작
        words = [word for word in paragraph if word not in banned]
        
        print(words)
        
        #Counter 모듈 사용 : (value)의 횟수를 세어 리스트 형태로 리턴해준다.
        counts = collections.Counter(words)
        print(counts.most_common(1)) # [('ball', 2)]
        print(counts.most_common(1)[0]) #('ball', 2)
        print(counts.most_common(1)[0][0]) # ball
        
        return counts.most_common(1)[0][0]