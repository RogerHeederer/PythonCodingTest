class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) # row
        n = len(word2) # col
        
        #https://www.youtube.com/watch?v=ZkgBinDx9Kg 이 강의 참조
        #   '' r o s
        #''
        # h
        # o
        # r
        # s
        # e        ??
        
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0: # 행이 공백일 때, insert만 해주면 되니까
                    dp[i][j] = j # j값을 그대로 넣어주기
                elif j == 0: #열이 공백일 때, isert만 수행해주면 되니까
                    dp[i][j] = i # i값을 그대로 넣어주기
                    #여기까지 수행했을 때의 결과
                    #   '' r o s
                    #''  0 1 2 3
                    # h  1
                    # o  2
                    # r  3
                    # s  4
                    # e  5     ??
                    
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1])
        
        print(dp)
        return dp[m][n]
        
