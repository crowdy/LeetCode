# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longestConsecutiveHelper(root):
            if not root:
                return 0, 0
            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)
            cur_inc_len, cur_dec_len = 1, 1
            if root.left:
                if root.left.val == root.val + 1:
                    cur_inc_len = max(cur_inc_len, left_len[0] + 1)
                elif root.left.val == root.val - 1:
                    cur_dec_len = max(cur_dec_len, left_len[1] + 1)
            if root.right:
                if root.right.val == root.val + 1:
                    cur_inc_len = max(cur_inc_len, right_len[0] + 1)
                elif root.right.val == root.val - 1:
                    cur_dec_len = max(cur_dec_len, right_len[1] + 1)
            self.max_len = max(self.max_len, cur_dec_len + cur_inc_len - 1)
            return cur_inc_len, cur_dec_len

        self.max_len = 0
        longestConsecutiveHelper(root)
        return self.max_len
 
"""
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. 
For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but 
the path [1,2,4,3] is not valid. On the other hand, the path can be 
in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].



연속시퀀스면 오름차순일 수도 있고, 내림차순일 수도 있다. 양쪽의 경우를 모두 볼 것

바이너리트리 가장 긴 연속시퀀스 구하기 투 오엔으로 구하기
    재귀함수(루트)
        루트가 없으면
            리턴 영, 영 # 증가, 감소의 수이다.
        왼쪽길이에 재귀함수(왼쪽아이) 대입
        오른쪽길이에 재귀함수(오른쪽아이) 대입
        현재증가길이, 현재감소길이 = 일, 일

        왼쪽아이가 있으면
            왼쪽아이의 값이 내 값 + 일 이면
                현재증가길이 = 맥스(현재증가길이, 왼쪽길이[0] 더하기 일)
            또는 왼쪽아이의 값이 내 값 - 일 이면
                현재감소길이 = 맥스(현재감소길이, 왼쪽길이[1] 더하기 일)

        오른쪽아이가 있으면
            오른쪽아이의 값이 내 값 + 일 이면
                현재증가길이 = 맥스(현재증가길이, 왼쪽길이[0] 더하기 일)
            또는 오른쪽아이의 값이 내 값 - 일 이면
                현재감소길이 = 맥스(현재감소길이, 오른쪽쪽길이[1] 더하기 일)

        최대길이는 맥스(최대길이, 증가길이 더하기 감소길이 빼기 일)
        리턴 증가길이, 감소길이

    최대길이 = 0
    재귀함수(루트)
    리턴 최대길이


좀 더 최적화 한다면, 
    재귀함수(루트, 부모)
        루트가 없으면
            리턴 영, 영
        왼쪽값은 재귀함수(루트의 왼쪽아이, 루트)
        오른쪽값은 재귀함수(루트의 오른쪽아이, 루트)
        결과 = 맥스(결과, 왼쪽값의 증가길이 + 오른쪽의 감소길이 + 1)
        결과 = 맥스(결과, 왼쪽값의 감소길이 + 오른쪽의 증가길이 + 1)
        증가길이, 감소길이 = 영, 영
        루트값이 부모값 더하기 일이면
            증가길이는 맥스(왼쪽아이의 증가길이, 오른쪽아이의 증가길이) 더하기 일
        또는 루트값 더하기 일이 부모값이면
            감소길이이는 맥스(왼쪽아이의 감소길이, 오른쪽아이의 감소길이) 더하기 일

        리턴 증가길이, 감소길이

    재귀함수(루트, 루트)

좀 더 최적화 한다면
    재귀함수(루트, 차이값)
        루트가 없으면 영을 리턴
        증가길이, 감소길이 = 영, 영
        왼쪽아이가 있고, 루트값 빼기 왼쪽아이의 값이 차이값이면
            증가길이 = 일 더하기 재귀함수(왼쪽아이, 차이값)
        오른쪽아이가 있고, 루트값 빼기 오른쪽아이의 값이 차이값이면
            감소길이 = 일 더하기 재귀함수(오른쪽아이, 차이값)
        리턴 맥스(증가값, 감소값)

    루트가 앖으면 영을 리턴
    결과값은 재귀함수(루트, 1) 더하기 재귀함수(루트, -1) + 일
    리턴 맥스(결과값, 맥스(전체함수(왼쪽아이), 전체함수(오른쪽아이)))

"""
