# Time:  O(logn)
# Space: O(1)

# Implement int sqrt(int x).
# 
# Compute and return the square root of x.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    print Solution().sqrt(10)
            
"""

오른쪽의 초기값을 절반으로 하는 것은 좋은 전략이다.

비교문을 복잡하게 하지 말고

    템프 = 미드 * 미드
    템프 > 엑스 이면
        알 = 미드 - 일
    아니면
        엘 = 미드

로 하는 것이 좋다.
"""
