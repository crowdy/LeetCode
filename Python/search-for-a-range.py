# Time:  O(logn)
# Space: O(1)
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the first index where target <= nums[idx]
        left = self.binarySearch(lambda x, y: x >= y, nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        # Find the first index where target < nums[idx]
        right = self.binarySearch(lambda x, y: x > y, nums, target)
        return [left, right - 1]

    def binarySearch(self, compare, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid + 1
        return left

    def binarySearch2(self, compare, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if compare(nums[mid], target):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binarySearch3(self, compare, nums, target):
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid
        return right


if __name__ == "__main__":
    print(Solution().searchRange([2, 2], 3))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

    """
    compare 함수를 파라메터로 넘기지 않는다면?
        찾기상위경계인덱스 함수라던지
        찾기하위경계인덱스 함수를 각각 구현해야 한다.
    
        하위인덱스를 찾으려면 크거나 **같으면** 오른쪽의 절반씩 가보고, 반대면 왼쪽을 하나씩 늘려본다.
        상위인덱스를 찾으려면 작거나 **같으면** 왼쪽의 절반씩 가보고, 반대면 오른쪽을 하나씩 줄여본다.
    """
