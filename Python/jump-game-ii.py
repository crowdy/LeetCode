# Time:  O(n)
# Space: O(1)
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# For example:
# Given array A = [2,3,1,1,4]
# 
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#

# not pass on leetcode because of time limit
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        jump_count = 0
        reachable = 0
        curr_reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                return -1
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1
            reachable = max(reachable, i + length)
        return jump_count


# Time:  O(n^2)
# Space: O(1)     
class Solution2:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        result, prev_reachable, reachable = 0, -1, 0
        while reachable > prev_reachable:
            if reachable >= len(A) - 1:
                return result
            result += 1
            prev_reachable = reachable
            for i, length in enumerate(A[:reachable + 1]):
                reachable = max(reachable, i + length)
        return -1


# when you on an index of nums, move to next index which can move farthest in range of this index reachable
# Time: O(log(n))
# Space: O(1)
class Solution3(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[-1] = 2 ** 31
        nums2, l = [i + j for i, j in enumerate(nums)], len(nums) - 1

        def find_max_index(index):
            tmp = nums2[index:index + nums[index] + 1]
            return index + tmp.index(max(tmp))

        index, steps = 0, 0
        while True:
            index = find_max_index(index)
            if index:
                steps += 1
            if index == l:
                break
        return steps


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([3, 2, 1, 0, 4]))

"""
1. Can I think for a second?
2. Think loud

[2,3,1,1,4]
갈 수 있는 맥스 값이 갱신되는 순간에 점프가 일어나면 되겠네요
0의 자리에서 2만큼 갈 수 있으니까 점프가 한 번 발생하고 맥스는 2
1의 자리는 맥스 2 보다 작고 업데이트 할 수 있으니까 점프가 또 발생하고 맥스는 1+3 = 4
2의 자리는 맥스 4보다 작고 업데이트해도 맥스보다 작으니까 점프 없음 맥스는 4
3의 자리는 맥스 4보다 작고 업데이트해도 맥스보다 작으니까 점프 없음 맥스는 4
4의 자리는 맥스 4와 같으므로 끝

3. I can have a few more examples
[4, 3, 2, 1]
[1, 1, 1, 1]

4. Does it seem like a good strategy?

함수 CanJump(A)
    도달할 수 있는 맥스 인덱스값 <- 0,
    한 번씩 루프를 돌면서 
        내 인덱스가 갱신이 일어날 위치보다 크다면
            다음번 비교해야 할 자리는 뛸 수 있는 최대값
            카운트 증가

        뛸 수 있는 최대값은 맥스(최대값, 내 위치 + 내 위치의 값)

    카운트를 리턴

----
현재 위치를 보지 않고 루프를 돈다면

함수 CanJump(A)
    맥스인덱스가 이전맥스보다 크다면 루프
        맥스인덱스가 마지막 인덱스보다 크다면
            카운트를 리턴
        카운트++
        이전맥스 = 맥스
        [:맥스+1]까지 루프
            맥스 = 맥스(맥스값, 내 위치 + 내 위치의 값)
    리턴 -1

이거 오엔스퀘어로 보이지만, 실제로는 오엔만큼만 돌 것 같은데

----
오로그엔으로 구하는 것은 잘 이해를 못하겠다.
"""
