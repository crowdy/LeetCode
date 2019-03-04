# Time:  O(n^2)
# Space: O(n)
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
# 문자열 s 와 t가 주어졌을 때, S안에서 T의 subsequence의 수를 구하여라
# 
# A subsequence of a string is a new string which is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# 문자열의 subsequence은 오리지널 문자열에서 repositioning없이 어떤 문자들을 빼서 얻을 수 있는 문자열이다.
# 예를 들면 ABC는 ABCDE의 subsequence이지만, ACE는 아니다.
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
# 
# Return 3.
#

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in range(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j, T_char in reversed(list(enumerate(T))):
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]


if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    result = Solution().numDistinct(S, T)
    print(result)
