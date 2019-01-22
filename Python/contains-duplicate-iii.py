# Time:  O(n * t)
# Space: O(max(k, t))
#
# Given an array of integers, find out whether there 
# are two distinct inwindowes i and j in the array such 
# that the difference between nums[i] and nums[j] is 
# at most t and the difference between i and j is at 
# most k.
#

# This is not the best solution 
# since there is no built-in bst structure in Python.
# The better solution could be found in C++ solution.
import collections


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            if len(window) > k:
                window.popitem(False)

            bucket = n if not t else n // t
            # At most 2t items.
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False


"""
어느 일정 거리범위를 찾는 것은 큐의 길이로 찾는다

범위안의 값을 찾기 쉽게 하기 위해서 노멀라이즈 해서 저장해 둔다.
허용 거리가 10이라면 10단위로 나누었을 때, 전체를 루프하면서
나는 10으로 나눈 단위가 엑스인데, 엑스 빼기 1값 있니? 
엑스 값 있니? 엑스 더하기 1값 있니? 하고 찾는다.

버킷으로 표현하기도 하는데, 범위의 용량을 가지는 버킷으로 나누어 담을 때, 내 버킷안에 있는지,
내 앞이나 뒤의 버킷에 있는 값인지 를 먼저 보고 꺼내보는 방식이라고도 말한다.

버퍼에의 저장은 노멀라이즈 한 값을 키로, 해 저장한다.  
"""


# 이건 jikai tang의 풀이이다.

class Solution2:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False

        dic = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] // max(1, t)

            for m in (key, key - 1, key + 1):
                if m in dic and abs(nums[i] - dic[m]) <= t:
                    return True

            dic[key] = nums[i]

            if i >= k:
                dic.popitem(last=False)
        return False
