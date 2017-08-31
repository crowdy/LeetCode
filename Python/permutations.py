# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers, return all possible permutations.
# 
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRecu(result, used, [], num)
        return result
    
    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur + [])
            return
        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False

if __name__ == "__main__":
    print Solution().permute([1, 2, 3])

"""

1. Can I think for a second?
2. Think loud

리커시브로 풀려고 했나본데, 좀 어렵게 썼네
하나를 잡아놓고 나머지는 계속 리커시브돌리는 방법이 깔끔하다.
이것도 DFS라고 부를 수 있는 지, 백트래킹이라고 불러야 하는지.

def permute(self, num):
    if len(nums) <= 1:
        return [nums]
    res = []
    for i, x in enuerate(nums):
        for elem in self.permute(nums[:i] + nums[i+1:]):
            res.append([x] + eleme)
    return res
    
타임 컴플렉시티가 왜 그렇게 되는 거지?
이거 아닌가?

---------------
T(n) = nT(n-1)+c
T(n-1) = (n-1)T(n-2)+c
...
T(2) = 2T(1)+c

=> T(n) = n!T(1)+n(n+1)c/2 = O(n!) time
----------------

이 문제는 중복을 포함하는 숫자가 있다면 어떻게 되는가 하는 문제로 발전할 수 있다.
"""
