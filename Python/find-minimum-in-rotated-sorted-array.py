# Time:  O(logn)
# Space: O(1)
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#

class Solution(object):
    def findMin(self, nums):
        """
        이 솔루션은 엘리먼트가 중복되지 않는다는 가정의 솔루션인 듯 한데
        좀 이상하다. 타겟값이 루프 바깥에서 고정이 되어 있으며
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        target = nums[-1]

        while left < right: # and nums[l] > nums[r] 조건도 빠져있다.
            mid = left + (right - left) / 2

            if nums[mid] <= target:
                right = mid
            else:
                left = mid + 1

        return nums[left]


class Solution2(object):
    def findMin(self, nums):
        """
        이 솔루션이 맞다 이 솔루션은 엘리먼트가 중복이 될 수 있다는 가정의 솔루션이다.
        미니멈값을 찾을 때는 타겟값이 없으므로 가운데값과 왼쪽값을 비교해서 찾는다.
        오른쪽값이 왼쪽값보다 커져버리면 왼쪽번째 값을 리턴한다.
        [1,1,1,1,2,3,4,1], 타겟=1
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:  # 중복을 허용하지 않는다면 같을 경우가 없다.
            mid = left + (right - left) / 2

            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == "__main__":
    print Solution().findMin([1])
    print Solution().findMin([1, 2])
    print Solution().findMin([2, 1])
    print Solution().findMin([3, 1, 2])
    print Solution().findMin([2, 3, 1])
