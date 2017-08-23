# Time:  O(logn)
# Space: O(1)
#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# Write a function to determine if a given target is in the array.
#

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) / 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left]:
                left += 1
            elif (nums[mid] > nums[left] and nums[left] <= target < nums[mid]) or \
                 (nums[mid] < nums[left] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left = mid + 1

        return False
        

if __name__ == "__main__":
    print Solution().search([3, 5, 1], 3)
    print Solution().search([2, 2, 3, 3, 4, 1], 1)
    print Solution().search([4, 4, 5, 6, 7, 0, 1, 2], 5)

"""
만약 중복을 허용한다면 어떻게 되겠는가 그게 런타임 복잡도에 영향을 주는가?

[1,1,1,1,1,1,1,1,2] target=2 

이면, 모든 요소를 반복하게 된다. 그러면 오엔 타임

중복을 허용하지 않는 다면 오로그엔


    서치(넘스, 타겟)
        엘, 알 = 0, 전체길이 - 일
        엘이 알보다 작거나 같으면 루프
            미드는 엘 더하기 (알 - 엘) // 2
            만약 미드번째 값이 타겟이면
                리턴 트루
            아니고 만약 미드번째 값이 엘번째 값보다 크면 # 여기까진 오름차순 (1)
                만약 엘번째 값 <= 타겟 < 미드번째 값 이면 # 타겟이 미드의 왼쪽에 있다.
                    알 = 미드 - 1
                아니면
                    엘 = 미드 + 1
            아니고 만약 미드번째 값이 엘보다 작다면 # 뒤집어진 부분이라면 (2)
                만약 미드번째 값 < 타겟 <= 알번째 값 
                # [.... 1(미드), 2, 3, 4(알))] 찾는 값이 2 이면 
                    엘 = 미드 + 1
                아니면
                    알 = 미드 - 1
            아니면 # 즉 미드번째 값이 엘번째 값과 같다면, 
                # 이 부분은 중복을 허용하기 때문에 있다. 
                # 중복을 허용하지 않으면 (1)의 표현을 그냥 엘번째 값보다 크거나 같다면 으로 하면 된다.
                엘에 1 증가
        리턴 폴스


찾는 값이 중복을 허용하는 값이라면 첫번째 인덱스를 돌려야 하겠지
[4,5,5,6,7,8,0,0,0,1,2,2,3]  return 0

중복을 허용한다면 이런 경우가 있을 수 있다.

[1,1,1,1,2,3,4,1] 엘번째 값 == 미드번째 값 == 알번째 값 == 1

----

쉬프티드 소티드 어레이 문제에서는 최소값을 구하라는 문제가 나올 수도 있다.
이것도 중복을 허용하는 지, 안하는 지에 따라 조건문이 바뀐다.
"""
