# Time:  O(logn)
# Space: O(1)

# Given a positive integer num, write a function
# which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid >= num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == num / left and num % left == 0

"""
퍼펙스 스퀘어는 그냥 제곱수이다. 어떤 수의 제곱수인지를 조사하는 문제이다.

값을 찾아가는 방법은
1. 1부터 넘까지 1씩 증가해가면서 찾아 가는방법
2. 1부터는 아니고 적당한 수 부터 1씩 증가해가면서 찾아가는 방법
    여기서는 제곱값이 넘보다 작을 때까지 넘을 둘로 나눠가면서 찾는다.
3. 바이너리 서치로 찾는 방법이 있고

    퍼펙트스퀘어(넘)
        엘, 알 = 1, 넘
        엘 <= 알 루프
            미드 = 엘 + (알 - 엘) // 2
            템프 = 미드 곱하기 미드
            만약 템프 == 넘 이면
                리턴 트루
            만약 미드 곱하기 미드 > 넘
                알 = 미드 - 1 
            아니면
                엘 = 미드 + 1

        리턴 폴스


4. 수학적으로 찾는 방법이 있다.
1 = 1
4 = 1 + 3
9 = 1 + 3 + 5
16 = 1 + 3 + 5 + 7
25 = 1 + 3 + 5 + 7 + 9
36 = 1 + 3 + 5 + 7 + 9 + 11
....
1+3+...+(2n-1) = (2n-1 + 1)n/2 = n*n

넘에서 1빼고, 3빼고, 5빼고, ... (2개씩 더한 값)빼고 해서 0이 되면 퍼펙트 스퀘어이다.
덧셈은 O(sqrt(n))번 일어난다.

    퍼펙트스퀘어(넘)
        아이는 1
        넘이 0보다 크면 루프
            넘은 넘에서 아이를 뺀것
            아이는 아이 더하기 2

        넘이 0 이면 트루


5. 2번의 방법을 변형해서, 적당한 시작점부터 적당한 변형(일 증가가 아니라)으로 찾아가는 방법인데
    오의 로그엔으로 푸는 방법이 있다.

    퍼펙트스퀘어(넘)
        엑스는 넘
        엑스 곱하기 엑스가 넘보다 크면
            엑스는 (엑스 더하기 넘 나누기 엑스) // 2
            # x = (x + num // x) // 2
            # 넘이 100이면 처음에는 (101) //2 = 50
            # 두번째는 (50 + 2) // 2 = 26
            # 세번째는 (26 + 3) // 2 = 14
            # 네번째는 (14 + 7) // 2 = 10

        엑스 곱하기 엑스가 넘 이면 트루

6. 오원으로 푸는 방법도 있다. 
https://en.wikipedia.org/wiki/Fast_inverse_square_root
1999년 퀘이크 쓰리에서 빛과 반사를 계산했을 때 사용했다라고 한다.

"""
