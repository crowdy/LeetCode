# Time:  O(n)
# Space: O(1)
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
#

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in xrange(len(num) - 1):
            if num[i] < num[i + 1]:
                k = i
                
        if k == -1:
            num.reverse()
            return
        
        for i in xrange(k + 1, len(num)):
            if num[i] > num[k]:
                l = i
                
        num[k], num[l] = num[l], num[k]
        num[k + 1:] = num[:k:-1]

if __name__ == "__main__":
    num = [1, 4, 3, 2]
    Solution().nextPermutation(num)
    print num
    Solution().nextPermutation(num)
    print num
    Solution().nextPermutation(num)
    print num

    
"""
1. Can I think for a second?
2. Think loud

예제: 687432

먼저 오른쪽에서 왼쪽으로 오름차순을 위반하는 첫번째 숫자를 찾는다.
    이 경우는 6. 왜냐하면 나머지는 전부 오름차순이기 때문에.
    이걸 파티션넘버라고 부르자
다시 오른쪽에서 왼쪽으로 파티션넘버보다 큰 수를 찾는다. 
    예제의 경우는 7. 이걸 체인지넘버라고 부르자
파티션넘버와 체인지넘버를 바꾼다.
    그러면 786432
파티션넘버의 오른쪽 부터 끝까지를 전부 뒤집는다.
    그러면 723468

3번 길이만큼 트래버스했으므로 3엔 = 오엔타임

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    # 1.6.3.3.3 -> 
    def nextPermutation(self, nums):
        n = len(nums)
        
        if n <= 1:
            return
        
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        
        if i > 0:
            m = n - 1
            while m >= i:
                if nums[m] > nums[i - 1]:
                    nums[m], nums[i - 1] = nums[i - 1], nums[m]
                    break
                m -= 1
                
        k = n - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1

"""
