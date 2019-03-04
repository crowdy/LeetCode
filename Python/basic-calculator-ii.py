# Time:  O(n)
# Space: O(n)
#
# Implement a basic calculator to evaluate a simple expression string.
# 식을 계산하는 간단한 계산기를 구현하라.
#
# The expression string contains only non-negative integers, +, -, *, / 
# operators and empty spaces . The integer division should truncate toward zero.
# 식은 양의 정수와 +, -, *, / 공백으로 이루어져 있다. 정수의 나눗셈은 소수부분을 버린다.
#
# You may assume that the given expression is always valid.
# 식은 항상 유효하다고 가정해도 좋다.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 // 2 " = 5
# Note: Do not use the eval built-in library function.
#

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0  or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()
                
        while operators:
            self.compute(operands, operators)
            
        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)
