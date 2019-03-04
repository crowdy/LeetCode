# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element is 
# the price of a given stock on day i.
# i번째 요소가 i 번째 날의 주가인 배열을 가지고 있다고 하자.
#
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). 
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxProfit2(self, prices):
        return sum(map(lambda x: max(prices[x + 1] - prices[x], 0), range(len(prices[:-1]))))


if __name__ == "__main__":
    result = Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print(result)

"""
1. Can I think for a second?
2. Think loud
[1, 2, 1, 5, 9, 6, 8] 이 있다면,
2-1 + 5-1 + 9-5 + 8-6 = 3 + 4 + 4 + 2 = 13

그냥 내 전의 값보다 크다면 그 차이를 더하면 될 것 같다.

3. I can have a few more examples
[4, 3, 2, 1] 
[1, 1, 1, 1]

4. Does it seem like a good strategy?

함수 맥스프라핏(가격배열)
    결과 = 0
    1 부터 가격배열 길이만큼 반복
        나의 가격이 하나 전의가격 보다 크다면
            결과 += 나의 가격 - 하나 전의 가격
    리턴 결과

---

나와 하나 전의 가격을 보면 되므로 맵함수를 사용하면 될 것 같다.

"""
