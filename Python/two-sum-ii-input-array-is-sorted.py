# Time:  O(n)
# Space: O(1)
#
# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#

class Solution:
    def twoSum(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start != end:
            sum = nums[start] + nums[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9)


"""

1. Can I think for a second?
2. Think loud

소팅이 안되어 있다면, 아이와 제이로 두번 루프를 돌아서 합이 타겟이 되면 되겠네요
그러면 오엔스퀘어 타임이고 오원스페이스

해쉬를 쓴다면 한 번만 돌아도 되겠구요
그러면 오엔타임, 오엔스페이스

소팅을 한다면 일단 오엔로그엔 타임이고
투포인터로 리니어서치를 하는 방법
투포인터로 퀵서치를 하는 방법

등등이 있습니다.

----

미리 소팅이 되어 있다면 투 포인터로 양쪽 끝에서부터 다가오는 방법.

"""
