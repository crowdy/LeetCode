# Time:  O(n)
# Space: O(1)
#
# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1


if __name__ == "__main__":
    print(Solution().removeElement([1, 2, 3, 4, 5, 2, 2], 2))

"""
1. Can I think for a second?
2. Think loud

새로운 길이를 리턴해야하고 인플레이스라면, 라스트 포인터가 있어서 지워질 때마다 움직여야겠군요
전체를 한 번 루프를 돌면서 같은 값을 만나면 지워야 하는데, 순서는 바뀌어도 괜찮나요?
지울 때 라스트 포인터의 값과 swap하면서 라스트 인덱스를 줄여가면 오엔으로 풀 수 있을 것 같은데요.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
라니까 괜찮겠네요.

3. I can think a few more examples
[9,1,1,1,8,1,1,1, 9], 1

4. Does it seem like a good strategy?

"""
