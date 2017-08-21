# Time:  O(n * 4^n / n^(3/2)) ~= n * Catalan numbers = n * (C(2n, n) - C(2n, n - 1)), 
#                                due to the size of the results is Catalan numbers,
#                                and every way of evaluation is the length of the string,
#                                so the time complexity is at most n * Catalan numbers.
# Space: O(n * 4^n / n^(3/2)), the cache size of lookup is at most n * Catalan numbers.
#
# Given a string of numbers and operators, return all possible
# results from computing all the different possible ways to
# group numbers and operators. The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]
#

class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        lookup = [[None for _ in xrange(len(nums))] for _ in xrange(len(nums))]
        
        def diffWaysToComputeRecu(left, right):
            if left == right:
                return [nums[left]]
            if lookup[left][right]:
                return lookup[left][right]
            lookup[left][right] = [ops[i](x, y)
                                   for i in xrange(left, right)
                                   for x in diffWaysToComputeRecu(left, i)
                                   for y in diffWaysToComputeRecu(i + 1, right)]
            return lookup[left][right]
            
        return diffWaysToComputeRecu(0, len(nums) - 1)

class Solution2:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        lookup = [[None for _ in xrange(len(input) + 1)] for _ in xrange(len(input) + 1)]
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}

        def diffWaysToComputeRecu(left, right):
            if lookup[left][right]:
                return lookup[left][right]
            result = []
            for i in xrange(left, right):
                if input[i] in ops:
                    for x in diffWaysToComputeRecu(left, i):
                        for y in diffWaysToComputeRecu(i + 1, right):
                            result.append(ops[input[i]](x, y))
            
            if not result:
                result = [int(input[left:right])]
            lookup[left][right] = result     
            return lookup[left][right]
            
        return diffWaysToComputeRecu(0, len(input))

    """

이건 캐털랜 타임이라고 한다. 스페인의 북동부에 있는 지역이름이라고 한다.
(2엔)팩토리얼 / ( (엔+1)팩토리얼 엔 * 엔 팩토리얼)
1, 1, 2, 5, 14, 42, 132, 429 ...

2-1-1 이면 오퍼레이터가 2개이니까 2개,
2+3+-4*5 이면 오퍼레이터가 3개이니까 5개

엔 곱하기 엔 격자가 있다면, 모서리에서 대각선 모서리로 가는 방법의 수와 같다.


재귀함수(문자열) -> 숫자배열
    앤스 = 빈 배열
    전체 문자별로 
        문자가 '+-*' 중의 하나이면
        에이 = 재귀함수(문자열의 왼쪽부분)
        비 = 재귀함수(문자열의 오른쪽부분)
        리스트 에이의 멤버 엠으로 루프
            리스트 비의 멤버 엔으로 루프
                문자가 + 면
                    앤스에 (엠 + 엔) 추가
                문자가 - 면
                    앤스에 (엠 - 엔) 추가
                문자가 * 면
                    앤스에 (엠 * 엔) 추가
    앤스가 비어있다면(연산자가 없었으므로)
        엔스에 문자열을 숫자화해서 추가

    앤스를 리턴

----

재귀함수를 따로 정의해서 하는 방법

솔루션(인풋)
    토큰즈는 인풋을 디지털로 스플릿 한 것
    넘스는 토큰을 숫자화한 배열
    룩껍은 숫자만큼 2차원화 한 것 # 이것이 캐털랜 사각형을 나타낸다.

    재귀함수(왼쪽 인덱스, 오른쪽 인덱스)
        왼쪽과 오른쪽이 같으면
            넘스의 왼쪽번째 값을 리턴
        룩껍의 왼쪽번째 로우, 오른쪽번째 컬럼에 뭔가 있으면
            그놈을 리턴
        룩껍의 왼쪽번째 로우, 오른쪽번째 컬럼은 [ 옵스(엑스, 와이)
                            옵스는 덧셈¥뺄셈¥곱셈 퍼뮤테이션
                            아이는 왼쪽에서 오른쪽까지
                            엑스는 재귀함수(왼쪽번째 로우 번, 아이번)
                            와이는 재귀함수(아이 + 1 번, 오른쪽번)]
        채워넣은 놈 리턴

    재귀함수(왼쪽은 0, 오른족은 마지막번째 인덱스)

----

재귀함수만, 리스트의 필터를 사용하지 않고, 그냥 for문으로 하는 방법도 있다.

        아이는 레프트에서 라이트까지 루프
            아이가 오퍼레이터중의 하나이면
                엑스는 재귀함수(왼쪽번째 로우번, 아이번) 루프
                    와이는 재귀함수(아이 + 1 번, 오른쪽번) 루프
                        리절트에 (엑스 오퍼레이터 와이)를 추가
        리절트가 비어있으면
            리절트는 정수화(인풋의 왼쪽에서 오른쪽까지의 서브문자화
        룩껍[레프트, 라이트]

"""
