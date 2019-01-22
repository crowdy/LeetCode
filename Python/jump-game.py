# Time:  O(n)
# Space: O(1)
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# A = [3,2,1,0,4], return false.

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(A) - 1
    
if __name__ == "__main__":
    print(Solution().canJump([2,3,1,1,4])
    print(Solution().canJump([3,2,1,0,4])

"""
1. Can I think for a second?
2. Think loud

한 칸만 있다고 해보죠
첫 번째 인덱스의 값이 0이어도 마지막 값에 도달한 것이겠네요

두 칸이 있다고 해보죠
첫 번째 인덱스의 값이 1보다 같거나 크면 도달한 것이겠네요

3 칸이 있다고 해보죠
첫 번째 칸에서 갈 수 있는 최대 맥스 인덱스가 있고, 
그 다음 인덱스에서 그 최대 인덱스를 업데이트 해가고, 
이걸 반복해 갈 때 갈 수 있는 최대값이 마지막 인덱스보다 크면 도달할 수 있겠네요

3. Does it seem like a good strategy?

함수 CanJump(A)
    도달할 수 있는 맥스 인덱스값 <- 0,
    한 번씩 루프를 돌면서 
        나의 인덱스가 맥스인덱스보다 크다면 그냥 리넡 폴스
        그렇지 않다면 맥스 인덱스 값을 갱신해 나가면,

    # 루프를 다 돌았을 때 맥스값이 마지막 인덱스 값보다 같거나 크다면 트루
    그냥 루프를 다 돌았으면 트루이다.
"""
