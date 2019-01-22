# Time:  O(k), where k is the steps to be happy number
# Space: O(k)
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum 
# of the squares of its digits, and repeat the process until 
# the number equals 1 (where it will stay), or it loops endlessly 
# in a cycle which does not include 1. Those numbers for which 
# this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1
    
    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new += int(char)**2
        return new

"""

해피넘버는 각 자리수를 제곱한 수를 더해는 연산을 반복해서
결과같이 1이 나오거나 끝없이 반복하면 해피넘버이다.

1. Can I think for a second?
2. Think loud

넥스트넘버 함수를 따로 정의하지 않더라도 될 것 같은데.
해피넘버의 조건을 그대로 코드로 쓰면

먼저 스탑조건이 되는 값들을 정해놓고

엔이 값에 포함되지 않는다면 계속 루프
    엔 = 문자열로 바꿔서 각 자리를 숫자로 바꿔서 제곱한 썸
루프를 끝냈을 때 엔 == 1 이면 트루

4. Does it seem like a good strategy?

"""
