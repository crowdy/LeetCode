# Time:  O(n^2)
# Space: O(n)

# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.

import math


# Cantor ordering solution
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in range(1, n + 1)]
        for i in reversed(range(n)):
            curr = perm[k // fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact //= i
        return seq


if __name__ == "__main__":
    print(Solution().getPermutation(3, 2))

    """
    
    1. Can I think for a second?
    2. Think loud
    
    엔개의 점을 잇는 방법은 엔팩토리얼이죠. 이건 트래블링 세일즈먼 프러블럼 (약자로 TSP)의 
    나이브한 해결방법인데, 이건 디피로 (엔제곱 곱하기 2의엔승)으로 해결하는 방법이 있다고 한다.
    
    헬프함수의 파라메터를 (넘스, 시퀀스 n, k번째) 라고 한다면
    
    첫번째 문자는 i 번째
    i = (k -1) // (n -1)!
    
    두번째 문자는 헬스함수는 재귀하는데
    첫 번째 파라메터 넘스는 i 번재 문자가 빠지니까 넘스[:i] + 넘스[i+1:]
    두 번째 파라메터 시퀀스가 하나 줄으니까 n -1
    세 번째 파라메터 나머지니까 (k -1) % (n -1)! + 1
    (넘스[:i] + 넘스[i+1:], n -1, (k -1) % (n -1)! + 1 )
    
    class Solution:
        # @param {integer} n
        # @param {integer} k
        # @return {string}
        def getPermutation(self, n, k):
            return self.helper([x + 1 for x in range(n)], n, k)
        
        def helper(self, nums, n, k):
            if n == 1:
                return str(nums[0])
                
            i = (k - 1) / math.factorial(n - 1)
            return str(nums[i]) + self.helper(nums[:i] + nums[i + 1:], n - 1, (k - 1) % math.factorial(n - 1) + 1)
    
    이게 리커젼, 백트래킹으로 푸는 방법이고, 팩토리얼이 오엔인데, 재귀하니까
    오엔제곱 타임, 오원 스페이스
    
    ----
    
    근데 재귀를 디피를 사용하면 오엔으로 구할 수 있으니까(대신에 오엔 스페이스를 사용하지만)
    이터레이션으로 푸는 방법으로 한다면
    
    class Solution(object):
        def getPermutation(self, n, k):
            """
    # :type n: int
    # :type k: int
    # :rtype: str
    """
    fac = [1] * (n + 1)
   
    for i in range(1, n + 1):
       fac[i] = fac[i - 1] * i
     
    nums = [str(x+1) for x in range(n)] 
    ans = ''
    
    for i in range(n):
        j = (k - 1) / fac[n - i - 1]
        ans += nums[j]
        nums.remove(nums[j])
        k = (k - 1) % fac[n - i - 1] + 1
    
    return ans 
"""
