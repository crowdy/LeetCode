# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# 
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)
        global_max, local_max = float("-inf"), 0
        for x in nums:
            local_max = max(0, local_max + x)
            global_max = max(global_max, local_max)
        return global_max


if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
"""

맥시멈 서브어레이

1. Can I think for a second?

2. Think out loud
[−2,1,−3,4,−1,2,1,−5,4]

어레이의 요소가 적은 경우부터 생각해 봅시다.
0번째 자리의 맥시멈서브어레이섬은 -2
1번째 자리의 맥시멈서브어레이섬은 이전 자리의 매시멈서브어레이섬을 이어간 경우와 버린경우가 있는데
    버리는 쪽이 더 크므로 버려버리면 맥시멈서브어레이섬은 1
2번째 자리에서는 이어가는 경우 1 -3 = -2, 나를 버려버리면 1

결국 각 자리에서의 맥시멈서브어레이섬은 

이전의 값을 이어간것에 내 자리를 더한 것과, 지금 자리의 나의 값중에 큰 것
에프(아이) = 맥스(에프(아이 빼기 1) 더하기 넘아이, 넘아이)
다이나믹 프로그래밍이네

이 데이타를 구해놓고 이 중에서 가장 큰 값을 찾는다.

[−2,1,−3,4,−1,2,1,−5,4] dp = [-2, 1, -2, 4, 3, 5, 6, 1, 5]

3. Okay this is a of course a given example 
but I can think of a few more examples

[-1, -2, -3, -4],  dp = [-1, -1, -1, -1]
[0, -1, 1, 2, -2], dp = [0, 0, 1, 3, 3]

4. Does it look like a good strategy?

--------

디바이드앤 컹커




"""
