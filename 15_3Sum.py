# 아이디어 _ i를 피벗으로 박아두고, left와 right 포인터를 조절하면서 해당 조건에 만족하는 값들을 찾아낸다
# left는 i의 왼쪽이 아닌, i+1 부터 시작한다. 그리고 right는 제일 끝에서 위치하여, 점점 좁혀들어온다.
# i값과 i-1값이 같은 경우는, 동일한 조건을 2번 비교할 필요 없으니, 건너 뛰어야 한다. 이 부분이 로직 반영에 필요함


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                # sum이 0보다 작으면, 0에 도달하기 위해서는 값을 더 키워야 한다.# 현재 while 문에서 조정하는 요소는 left, right 둘 뿐이다. 그리고 리스트는 정렬된 상태다
                if sum < 0: 
                    left += 1 # 여기서 값을 키우려면 left 포인터가 오른쪽으로 이동하는 방법이 유일함
                elif sum > 0: # 반대 케이스
                    right -= 1 # 여기서 값을 줄이려면 right 포인터가 왼쪽으로 이동하는 방법이 유일
                else: # 정답 케이스를 찾은 경우
                    results.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]: # left 포인터에서 같은 번호가 이어지면 한칸 더 옮겨준다
                        left += 1 #옮겼는데 같으면, 달라질 게 없잖아. 그러니 한칸 더 ㄱㄱ
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    #여기서 옮기는 작업을 한번 더 하는 이유는, 정답을 찾았고, 그 조합 이외에 다른 조합이 있는지 확인하는 단계
                    #[-4, -3, -2, -1, 0, 1, 2, 3, 4] 여기서 나올 수 있는 케이스는 첫번째로 [-4(i), 0(left), 4(right)]이 있다
                    # -4는 여전히 고정한 채, -4, 1(left), 3(right)도 나올 수 있다. 이처럼 현재 찾은 조합 이외에 다른 조합이 더 있을 수 있기에
                    # 주어진 i값에서, left right를 계속 옮겨본다. left나 right 중 하나만 옮기면 안되나? 이런 생각을 할 수 있는데
                    # 0 = -4 + 0 + ?  : ?에 들어갈 수 있는 해는 1개가 유일하다. 그래서 ?를 2개 만들어서 둘다 옮겨봐야 함
        return results

                    