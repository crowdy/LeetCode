# Time:  O(logm + logn)
# Space: O(1)
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
#

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid / n][mid % n] >= target:
                right = mid
            else:
                left = mid + 1

        return left < m * n and matrix[left / n][left % n] == target


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print(Solution().searchMatrix(matrix, 3))

"""
    서치매트릭스(매트릭스, 타겟)
        매트릭스가 없으면
            리턴 폴스
        
        엠, 엔 = 매트릭스 열 길이, 매트릭스 행 길이
        엘, 알 = 0, 엠 곱하기 엔 - 1
        엘과 알이 같거나 엘이 작은동안 루프
            미드 = 엘 + (알 - 엘) // 2
            넘 = 매트릭스[미드 // 엔][미드 % 엔]

            만약 넘 이 타겟이면
                리턴 트루
            아니고 혹시 넘이 타겟보다 작으면
                엘은 미드 더하기 일
            아니면
                알은 미드 빼기 일

        리턴 폴스
"""
