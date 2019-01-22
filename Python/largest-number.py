# Time:  O(nlogn)
# Space: O(1)
#
# Given a list of non negative integers, arrange them such that they form the largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead of an integer.
#

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y + x, x + y))
        largest = ''.join(num)
        return largest.lstrip('0') or '0'

if __name__ == "__main__":
    num = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(num)

"""

주어진 숫자들을 사용해서 만들 수 있는 가장 큰 수를 만들어라는 문제인데

Can I think for a second?

알파베틱 오더로 큰 수를 앞에 놓는 방식으로 소트해서 문자열을 다 더하면 될 것 같은데

Does it look like a good strategy?

소트는 시스템에서 제공하는 소트를 써도 되나? 어차피 구현해도 타임 컴플렉서티는 바뀌지 않는데
안된다면 소트함수를 만들어야 한다.

"""
