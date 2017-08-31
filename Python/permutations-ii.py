# Time:  O(n * n!)
# Space: O(n)
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# 
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
#

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(result, used, [], nums)
        return result
    
    def permuteUniqueRecu(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur + [])
            return
        for i in xrange(len(nums)):
            if used[i] or (i > 0 and nums[i-1] == nums[i] and not used[i-1]):
                continue
            used[i] = True
            cur.append(nums[i])
            self.permuteUniqueRecu(result, used, cur, nums)
            cur.pop()
            used[i] = False
                
class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        solutions = [[]]
        
        for num in nums:
            next = []
            for solution in solutions:
                for i in xrange(len(solution) + 1):
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
                
            solutions = next 
            
        return solutions

if __name__ == "__main__":
    print Solution().permuteUnique([1, 1, 2])
    print Solution().permuteUnique([1, -1, 1, 2, -1, 2, 2, -1])


"""

1. Can I think for a second?
2. Think loud

이 문제는 일반 퍼뮤테이션의 변형이다.

def permute(self, num):
    if len(nums) <= 1:
        return [nums]
    nums.sort()  # <- 여기하고
    res = []
    for i, x in enuerate(nums):
        if i == 0 or nums[i] != nums[i-1]:  # <- 여기, 이렇게 하면 같은 것은 안들어 가겠지
            for elem in self.permute(nums[:i] + nums[i+1:]):
                # res.append([x] + eleme)
                res.append(eleme + [x])  # <- 여기. 이렇게 하면 작은 수가 뒤로간다.
    return res

"""
