# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)

# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0
        
        node, level = root, 0
        while node.left is not None:
            node = node.left
            level += 1
        
        # Binary search.
        left, right = 2 ** level, 2 ** (level + 1)
        while left < right:
            mid = left + (right - left) // 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1
                
        return left - 1
    
    # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1
        k >>= 2
        
        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None

"""

일단 컴플리트트리가 뭔지 알아야 한다. 이것은 마지막 깊이의 것이 왼쪽으로 꽉꽉 채워져 있는 트리이다.

바이너리서치니, 엔번째 노드가 있는지 검사하는 것은 좀 이상하다

그냥 깊이를 구해서 컴플리트트리이니까 수학적으로 계산해 버리는 것이 깔끔하다.

    전체노드갯수(루트)
        왼쪽의 깊이가 오른쪽의 깊이와 같다면
            리턴 2의 (왼쪽깊이)승 -1
        아니면
            전체노드갯수(왼쪽아이) + 전체노드갯수(오른쪽아이) + 1 # 1 루트노드

    깊이(루트, 왼쪽방향인가)
        레벨은 0
        만일 루트가 있다면
            왼쪽방향이면
                루트는 왼쪽아이
            아니면
                루트는 오른쪽아이
            
            레벨은 1 증가

        레벨을 리턴
"""
