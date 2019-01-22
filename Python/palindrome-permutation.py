# Time:  O(n)
# Space: O(1)
import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) < 2


"""

Write an efficient function that checks whether any permutation 
of an input string is a palindrome.
You can assume the input string only contains lowercase letters.

Examples:

"civic" should return true
"ivicc" should return true
"civil" should return false
"livci" should return false


1. Can I think for a second?
2. Think loud

각 알파벳을 세어서, 전부 짝수개로 되어 있거나, 하나만 홀수개 이면 되는 거죠


"""
