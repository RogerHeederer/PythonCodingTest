# nums = [1]
# output = [ [], [1] ]

# nums = [1,2]
# output = [ [], [1], [2], [1,2] ]

# nums = [1,2,3]
# output = [ [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]

#아이디어 _ 새로운 넘버가 생길때는, 그 전 스텝의 결과는 그대로 이어 붙히고, 그 전 스텝에 새로운 넘버만 각각 넣어주면 된다.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        for i in nums:
            output += [lst for lst in output] #제일 바깥 리스트 안에 [] 형태로 들어감
        print(output)
        print('\n')
        
        
        print("해당 문제 솔루션")
        output = [[]]
        for i in nums:
            output += [[i] + lst for lst in output]
            print(output, '\n')
        
        return output