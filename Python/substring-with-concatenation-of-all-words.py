# Time:  O((m + n) * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)

# You are given a string, s, and a list of words, words,
# that are all of the same length. Find all starting indices of substring(s)
# in s that is a concatenation of each word in words exactly once and
# without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).

# Sliding window solution
import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return result

        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                # Space: O(n * k)

        for i in range(k):               # Time:  O(k)
            left, count = i, 0
            tmp = collections.defaultdict(int)
            for j in range(i, m-k+1, k): # Time:  O(m / k)
                s1 = s[j:j+k];            # Time:  O(k)
                if s1 in lookup:
                    tmp[s1] += 1
                    if tmp[s1] <= lookup[s1]: 
                        count += 1
                    else:
                        while tmp[s1] > lookup[s1]:
                            s2 = s[left:left+k]
                            tmp[s2] -= 1
                            if tmp[s2] < lookup[s2]:
                                count -= 1
                            left += k
                    if count == n:
                        result.append(left)
                        tmp[s[left:left+k]] -= 1
                        count -= 1
                        left += k
                else:
                    tmp = collections.defaultdict(int)
                    count = 0
                    left = j+k
        return result


# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)
class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result, m, n, k = [], len(s), len(words), len(words[0])
        if m < n*k:
            return result
 
        lookup = collections.defaultdict(int)
        for i in words:
            lookup[i] += 1                            # Space: O(n * k)

        for i in range(m+1-k*n): # Time: O(m)
            pass


class Solution3:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        result, word_num, word_len = [], len(L), len(L[0])

        n = len(L)
        k = len(S[0])
        words = collections.defaultdict(int)
        for i in L:
            words[i] += 1

        lookup = collections.defaultdict(int)
        for i in range(len(S) + 1 - word_len * word_num):
            cur, j = collections.defaultdict(int), 0
            while j < n:                              # Time: O(n)
                word = S[i+j*k:i+j*k+k]               # Time: O(k)
                if word not in lookup: 
                    break
                cur[word] += 1
                if cur[word] > lookup[word]:
                    break
                j += 1
            if j == n:
                result.append(i)
                
        return result


if __name__ == "__main__":
    print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
