#아이디어 _ 기본적으로 가장 쌀 때 사서 가장 비쌀 때 파는 것이 이윤의 최대화
# 각 타임 스탭마다 가장 적은 값을 기록해둔다.

#[7, 1, 5, 3, 6, 4]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf') # min 값을 양의 무한대로 임의 설정
        
        for price in prices:
            # 현재 price - 지금까지의 최소값 =  현재의 이익
            # 현재의 이익과, 지금 가지고 있는 profit을 비교해서 max 값을 도출. 이 profit을 매번 기억해둠
            # 끝까지 다 돌고나면 최대의 이익이 나옴
            # 맨 처음은 무한대 값과 비교하기에 첫 시작 price가 현재 가장 작은 값이 됨
            min_price = min(price, min_price) 
            profit = max(profit, price - min_price)
            
            print("price:{}, min_price:{}, profit:{}".format(price, min_price, profit))
            # price : 7 -- min_price : 7 -- profit : 0
            # price : 1 -- min_price : 1 -- profit : 0
            # price : 5 -- min_price : 1 -- profit : 4
            # price : 3 -- min_price : 1 -- profit : 5
            # price : 6 -- min_price : 1 -- profit : 5