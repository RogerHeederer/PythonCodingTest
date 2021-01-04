class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair = []
        result = 0

        for i in range(len(nums)):
            pair.append(nums[i]) 
            # 이렇게 써도 됨 pair += [nums[i]]
            # 대신 pair += nums[i] 에러. nums[i] 값은 int. pair 값은 리스트 그래서 += 연산 불가
            if len(pair)==2:
                result += min(pair)
                pair = []
        
        return result