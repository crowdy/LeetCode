# Time:  O(k * log(min(n, m, k))), with n x m matrix
# Space: O(min(n, m, k))

# Given a n x n matrix where each of the rows and
# columns are sorted in ascending order,
# find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order,
# not the kth distinct element.
#
# Example:
#
# matrix = [
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note: 
# You may assume k is always valid, 1 <= k <= n^2.

from heapq import heappush, heappop

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        kth_smallest = 0
        min_heap = []

        def push(i, j):
            if len(matrix) > len(matrix[0]):
                if i < len(matrix[0]) and j < len(matrix):
                    heappush(min_heap, [matrix[j][i], i, j])
            else:
                if i < len(matrix) and j < len(matrix[0]):
                    heappush(min_heap, [matrix[i][j], i, j])

        push(0, 0)
        while min_heap and k > 0:
            kth_smallest, i, j = heappop(min_heap)
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
            k -= 1

        return kth_smallest

"""
jikai tang은 수평검색과 수직검색으로 나눠서 코드를 작성했는데 이 코드가 더 퍼포먼스가 좋다.

먼저 생각해 보자.
먼저 전체를 민힙에 다 넣고, ｋ번만큼 꺼내면 될 것 같애.
그러면 로그(엔 곱하기 엔)이겠지.
이건 소트가 안되어 있는 것에서도 유효해.

그런데 소트가 되어있다니까 작은 것 부터 넣으면 전부를 다 넣을 필요가 없을 것 같애.
제일 작은 수는 왼쪽 탑에 있는 수야. 1이지. 
그런데 그 다음 수를 오른쪽을 넣을 지, 아래쪽을 넣을 지 선택해야 하네
어느 쪽이 더 작은 지 알 수 없잖아.

그래서 민힙에 넣을 때, 값만 넣는 것이 아니라 좌표도 같이 넣고,
팝을 한 다음 그다음 좌표값을 넣어야겠다. 민힙이기 때문에 다음번 팝은
오른쪽이든 아래쪽이든 작은 것이 팝되겠지

팝을 하면 한 만큼, 케이값을 줄 일 수 있기 때문에
케이가 0이 되면 그다음번 팝이 케이번째 작은 값일 것이다.
"""
