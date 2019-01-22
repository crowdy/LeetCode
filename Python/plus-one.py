# Time:  O(n)
# Space: O(1)

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# in-place solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)


class Solution:
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    def plusOne(self, digits):
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits = [1] + digits
        return digits


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = digits[::-1]
        carry = 1
        for i in range(len(result)):
            result[i] += carry
            carry, result[i] = divmod(result[i], 10)
        if carry:
            result.append(carry)
        return result[::-1]


if __name__ == "__main__":
    print(Solution().plusOne([9, 9, 9, 9]))
