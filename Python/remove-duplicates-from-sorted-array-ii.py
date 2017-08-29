# Time:  O(n)
# Space: O(1)
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# 
# Your function should return length = 5, and A is now [1,1,2,2,3].
#

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1
            
        return last + 1

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 1, 2, 2, 3])

"""
1. Can I think for a second?
2. Think loud

소팅되어 있는데, 중복된 것이 있으면 하나만 남기고 다 지우라는 문제이군요

다른 어레이나 딕셔너리를 두고, 그 안에 있는 지 조사해서 없으면 넣는 방식이 있습니다.
이 방식은 소팅되어 있지 않아도 가능한 방식이면서 엑스트라 공간을 사용하는 방식인데
더 효율적인 솔루션을 구하라고 한다면, 소팅이 되어 있는 특징을 이용해야 할 것 같아요

인덱스 제로에서 시작하는 포인터 엘과, 인덱스 원에서 시작하는 포인터 알을 두고,
알은 마지막까지 트래버스해가면서 값들이 같지 않으면 엘을 증가하고 알의 값을 복사해가면
될 것 같다.

3. I can think a few more examples
[1,1,2,3,3,4,5,6,6,7,8,9], 1

4. Does it seem like a good strategy?

----

추가로 두개까지 허용하게 한다면 어떻게 할래 하는 문제로 쩜프할 수가 있는데, 
Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3].

그렇다면 같은 값을 만났을 때, 내가 지금 두번째 만나는 것인가? 하는 변수가 있어서
바꿔쓰기 전에 체크할 수 있으면 해결할 수 있을 것 같다.

"""
