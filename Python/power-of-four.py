# Time:  O(1)
# Space: O(1)

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & (num - 1)) == 0 and \
               ((num & 0b01010101010101010101010101010101) == num)


# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num and not (num & 0b11):
            num >>= 2
        return (num == 1)


class Solution3(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = bin(num)
        return True if num[2:].startswith('1') and len(num[2:]) == num.count('0') and num.count(
            '0') % 2 and '-' not in num else False


"""
2의 제곱인가?

1. Can I think for a second?
2. Think loud

2의 제곱이라면, 2진수로 했을 때 1000000 과 같은 형태이기 때문에,
1을 뺀 값이거나 Not연산을 한 값이면 1111111과 같은 형태가 되죠.
그럼 그 값과 원래의 값을 AND 연산을 하면 0이다.
이건 오원으로 계산이 가능한데

만약에 2로 계속 나눠서 나머지가 0인 동안 계속 나눠서 남은 값이 1인가?
로 계산할 수도 있는데, 그러면 오로그엔 타임이다.

----

이 문재는 그러면 4의 제곱인지 조사하라고 하는 문제로 변형될 수 가 있다.
4의 제곱이면

100, 4
10000, 16

이렇게 되는데, 이 규칙을 이용하면,
1. 0b01010101010101010101010101010101 32자 와 AND연산을 하면 자기 자신이 나온다.

2. 4로 나눠가면서 0b11과 AND연산하면 0인 동안 계속 나눠가다가 더이상 나눠지지 않고 그 수가 1이다.

3. 파이썬에는 bin이라는 2진수 문자로 바꾸는 함수가 있다. 문자로 바꾸면 몇 가지 검사하기 편한 상황이 되는데
앞의 0b를 뺀 문자열이 1로 시작하고, 
앞의 0b를 뺀 문자열이 전부 0이고, (문자의 길이가 문자열안의 0의 수와 같고)
앞의 0b를 뺀 문자열이 2의 배수이고 (2, 4, 6, 8, ....)
마이너스 부호가 없으면 4의 배수
"""
