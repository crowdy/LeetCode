# Time:  O(nlogn)
# Space: O(n)
#
# Given an unsorted array of integers, 
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#

# Binary search solution.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = left + (right - left) / 2;
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target);
            else:
                LIS[left] = target

        for num in nums:
            insert(num)

        return len(LIS)

# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in xrange(len(nums)):
            dp.append(1)
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

"""

0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15

a longest increasing subsequence is

0, 2, 6, 9, 11, 15.

The longest increasing subsequence in this example is not unique: for instance,

0, 4, 6, 9, 11, 15 or 0, 4, 6, 9, 13, 15

    이건 디피로 푸는 방법이고 시간은 오엔제곱이다.

    가장긴증가하는시퀀스(넘스)
        넘스가 없으면 
            영을 리턴
        디피를 넘스의 사이즈 만큼 준비, 디폴트는 일 # dp[i]: the length of LIS ends with nums[i]
        앤스는 영

        1부터 넘스만큼 아이로 반복
            아이만큼 제이로 반복
                아이가 제이보다 크거나 같다면
                    아이번째 디피값은 맥스(디피아이의 값, 디피제이의 값 + 1)
            앤스는 맥스(앤스, 디피아이)
        리턴 앤스

    마지막 두 라인은
        리턴 맥스(디피) 만약 디피 아니면 영
    으로 바꿔 쓸 수 있다.



    다음은 바이너리 서치로 하는 방법이다. 위키에 나와 있는 방법인데 어렵다.
    https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
    아래의 것은 jikai tang이 푼 문제인데 더 어렵다. 차라리 엘아이에스에 인서트하는 방법이 알기 쉽다.

    가장긴증가하는시퀀스(넘스)
        넘스가 없으면
            영을 리턴

        엔 = 넘스의 길이
        어레이 = [0] 곱하기 엔 # 이 어레이는 뭐하는 거지?
        어레이영은 넘스영
        케이는 일

        일부터 엔까지 아이로 반복
            넘스아이가 어레이영보다 작다면
                어레이영은 넘스아이
            또는 넘스아이가 넘스[케이-1]보다 크거나 같다면 
                어레이케이는 넘스아이
                케이는 일 증가
            아니면
                포즈는 어퍼바운드(어레이, 케이, 넘스아이)
                어레이포즈는 넘스아이
        리턴 케이

    함수 어퍼바운드(넘스, 알, 타겟)
        엘 = 0
        엘이 알보다 작은 동안
            미드는 엘 더하기 (알 - 엘) // 2

            만약 미드값이 타겟보다 크거나 같다면 # 여기, 같다면이 들어가면 상한값을 찾는 거야
                알 = 미드 # 위의 비교문에 '같다면'이 들어갔기 때문에 여기는 1을 안빼는 거야
            아니면
                엘 = 미드 + 1

        리턴 엘

"""
