# Time:  O(26 * n) = O(n)
# Space: O(26) = O(1)

# Find the length of the longest substring T of a given string
# (consists of lowercase letters only) such that every character in T
# appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# Recursive solution.
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def longestSubstringHelper(s, k, start, end):
            count = [0] * 26
            for i in range(start, end):
                count[ord(s[i]) - ord('a')] += 1
            max_len = 0
            i = start
            while i < end:
                while i < end and count[ord(s[i]) - ord('a')] < k:
                    i += 1
                j = i
                while j < end and count[ord(s[j]) - ord('a')] >= k:
                    j += 1

                if i == start and j == end:
                    return end - start

                max_len = max(max_len, longestSubstringHelper(s, k, i, j))
                i = j
            return max_len

        return longestSubstringHelper(s, k, 0, len(s))

"""
최소 케이 번 반복하는 가장 긴 반복문자, 오엔으로 구하기


오엔으로 구하려면 뭔가를 저장해야 하는데 뭘 저장할 지 전략을 잘 세우는 것이 중요


    재귀함수(문자열, 케이, 시작인덱스, 끝인덱스)

        해쉬테이블 26사이즈 카운터 준비
        아이는 시작인텍스부터 끝인덱스까지
            각 카운터의 위치값을 하나씩 증가

        아이는 시작인덱스
        아이가 끝인덱스보다 작으면 루프
            아이인덱스 문자의 갯수가 케이보다 작으면
                아이를 하나 증가
            제이에 아이를 대입 # 여기부터가 케이번 이상 등장하는 문자
            제이인덱스 문자의 갯수가 케이보다 작으면
                케이를 하나 증가

            아이인덱스가 시작인덱스이고, 제이인덱스가 끝인덱스이면 # 전체가 하나의 문자
                리턴 엔드인덱스 - 시작인덱스

            최대길이는 최대(최대길이, 케이, 아이인덱스, 제이인덱스) # 위의 리턴으로 값을 구하기 위해서
            아이에 제이를 대입 # 그 다음 부분을 진행하기 위해서
        리턴 최대길이

    리턴 재귀함수(문자열, 케이, 영, 문자길이)
"""
