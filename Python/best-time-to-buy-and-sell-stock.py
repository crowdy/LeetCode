# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element 
# is the price of a given stock on day i.
# i번째 요소가 i 번째 날의 주가인 배열을 가지고 있다고 하자.
# 
# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), 
# design an algorithm to find the maximum profit.
#
# 만약 딱 한번만 거래를 할 수 있다고 한다면 (즉, 한 번만 사고, 한 번만 팔 수 있다),
# 최대의 이익을 구하는 알고리즘을 디자인하라


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print(result)

    """
    1. Can I think for a second?
    2. Think loud
    [2, 1, 5, 9, 6, 8] 이 있다면,
    최소값을 유지해가면서 맥스프라핏값을 업데이트하면 될까?
    
    [2, 1, 1, 1, 1, 1] <- 최소값
    [0, 0, 3, 8, 8, 8] <- 맥스프라핏값
    
    4. Does it seem like a good strategy?
    
    함수 맥스프라핏(가격배열)
        최소값 = 가격배열[0]
        최대이익 = 0
        1 부터 가격배열 길이만큼 반복
            가격이 최소값보다 작다면
                최소값 <- 가격
                continue # 최대이익을 업데이트할 필요가 없으므로
            
            최대이익 = max(가격 - 최소가격, 최대이익)
    
        리턴 최대 이익
    
    """
