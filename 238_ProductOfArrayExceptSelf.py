#아이디어
#1. i를 기준으로 i 위치를 제외한 왼쪽 요소만 곱한 리스트를 만든다 (left)
#2. 만들어진 Left 리스트에 i 위치를 제외한 오른쪽 요소를 덧붙여 곱한다.
# nums = p=1  [  1,        2,         3,            4     ]
# left =      [  p ,      p*1,     p*1*2,       p*1*2*3   ]   p=1
#output=      [p*2*3*4,  p*1*3*4,  p*1*2*4,     p*1*2*3*p ]

# deque의 특징을 활용해서 왼쪽으로 append시킴
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        left = []
        p = 1
        output = collections.deque()

        #왼쪽 요소 곱 리스트 만들기
        for i in range(len(nums)):
            left.append(p)
            p = p * nums[i]
        print(left)
        
        #오른쪽 요소 곱 리스트 만들기
        p = 1
        for i in range(len(nums)-1, -1, -1):
            output.appendleft(left[i]*p)
            p = p * nums[i]
        
        return output