# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element 
# is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. 
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).
#

# Time:  O(n)
# Space: O(1)
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2    = max(hold2,    release1 - i)
            release1 = max(release1, hold1 + i)
            hold1    = max(hold1,    -i);
        return release2
    
# Time:  O(k * n)
# Space: O(k)
class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return self.maxAtMostKPairsProfit(prices, 2)
        
    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i/2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])

        return max_sell[k]

# Time:  O(n)
# Space: O(n)     
class Solution3:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit_from_left, max_profits_from_left = float("inf"), 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit_from_left = max(max_profit_from_left, price - min_price)
            max_profits_from_left.append(max_profit_from_left)
            
        max_price, max_profit_from_right, max_profits_from_right = 0, 0, []
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_from_right = max(max_profit_from_right, max_price - prices[i])
            max_profits_from_right.insert(0, max_profit_from_right)
            
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profits_from_left[i] + max_profits_from_right[i])
        
        return max_profit
        
if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print result


"""
1. Can I think for a second?
2. Think loud

최대 이익을 구하는데 최소 두번 거래를 해야 한다고.
일단 최대값을 구하는데, 매 자리에서 최대값을 저장해 두면

[2, 1, 5, 9, 6, 8] 이 있다고 했을 때
[2, 1, 1, 1, 1, 1] <- 최소값
[0, 0, 3, 8, 8, 8] <- 맥스프라핏값

일단 최대 이익값은 제일 뒤의 값이고,
n-2 번 째부터 거꾸로 루프
    가격이 피크보다 작으면
        거기가 사는 트랜잭션이 일어나는 곳이잖아.

4. Does it seem like a good strategy?

함수 맥스프라핏(가격배열)
    배열길이가 2보다 작으면 0 리턴
    DP = 같은 크기의 배열

    최소값 = 가격배열[0]
    1 부터 가격배열 길이만큼 반복
        최소값 = min(최소값, 현재 가격)
        DP[i] = max(가격 - 최소가격, DP[i-1])
    피크 = 마지막 값

    # 하나를 더 구해본다면
    n-2번째부터 -1까지 -1씩 루프
        현재 가격이 피크보다 작다면
            DP[i] += 피크 - 현재 가격
    리턴 피크

오엔 타임
오엔 스페이스
"""
