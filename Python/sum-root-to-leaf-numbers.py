# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersRecu(root, 0)
    
    def sumNumbersRecu(self, root, num):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return num * 10 + root.val
        
        return self.sumNumbersRecu(root.left, num * 10 + root.val) + self.sumNumbersRecu(root.right, num * 10 + root.val)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumNumbers(root)    
    

"""
DFS이고 리커시브인데 어떻게 오에이치 스페이스야. 오로그엔 스페이스이지
10단위씩 곱한 수를 리커시브 함수에 패스하는 방식

재귀함수(노드, 썸)
    내가 없으면 0을 리턴

    밸류 = 10 * 썸 + 나의 밸류
    단말 노드이면(왼쪽아이, 오른쪽아이가 모두 없으면)
        넘겨받은 썸에 나의 밸류 더해서 리턴

    리턴 재귀함수에 왼쪽아이에 넣고 계산한 값 + 재귀함수에 오른쪽아이 넣고 계산한 값
"""
