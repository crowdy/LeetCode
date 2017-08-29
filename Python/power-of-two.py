# Time:  O(1)
# Space: O(1)
#
# Given an integer, write a function to determine if it is a power of two.


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0


class Solution2:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & ~-n) == 0


"""
1. Can I think for a second?
2. Think loud

2의 제곱이라면, 2진수로 했을 때 1000000 과 같은 형태이기 때문에,
1을 뺀 값이거나 Not연산을 한 값이면 1111111과 같은 형태가 되죠.
그럼 그 값과 원래의 값을 AND 연산을 하면 0이다.
이건 오원으로 계산이 가능한데

만약에 2로 계속 나눠서 나머지가 0인 동안 계속 나눠서 남은 값이 1인가?
로 계산할 수도 있는데, 그러면 오로그엔 타임이다.
"""
