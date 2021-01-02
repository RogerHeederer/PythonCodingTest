#아이디어 : dict 사용

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = collections.defaultdict(list)
        
        #sort와 sorted의 차이점 먼저 짚고 가자
        #sorted의 경우 원본에 변화가 생기지 않는다.
        example = ["eat", "tea", "tan", "ate", "nat", "bat"]
        print(sorted(example))
        print(example)
        
        #sort()의 경우 원본에 변화가 생김
        example.sort()
        print(example)
        
        for s in strs:
            #data[ate].append('bat')
            # 정렬된 s값을 dict key에 두고 고정하고, 정렬되지 않는 값 s들을 value로 넣어준다.
            data[''.join(sorted(s))].append(s)
        

        print("최종 결과(key):", data.keys())
        print("최종 결과(value):", data.values())
        
        return data.values()