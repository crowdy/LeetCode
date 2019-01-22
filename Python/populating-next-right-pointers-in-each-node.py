# Time:  O(n)
# Space: O(1)
#
# Given a binary tree
# 
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur and cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left


# Time:  O(n)
# Space: O(logn)
# recusion
class Solution2:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)


if __name__ == "__main__":
    root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left.left, root.left.right, root.right.left, root.right.right = TreeNode(4), TreeNode(5), TreeNode(
        6), TreeNode(7)
    Solution().connect(root)
    print(root)
    print(root.left)
    print(root.left.left)

"""
오엔 타임
오원 스페이스

이건 헤드가 있다면 반복
    내가 존재하고, 나의 왼쪽아이도 있다면 반복
        왼쪽 아이의 넥스트를 오른쪽으로 설정
        나의 넥스트가 있다면, 
            나의 오른쪽 아이의 넥스트를 넥스트의 왼쪽아이로 설정
        나의 넥스트를 나로 설정
    나의 왼쪽 아이를 헤드로



오엔 타임
오로그엔 스페이스 : 리커시브니까

함수
    내가 없으면 넌 리턴
    나의 왼쪽 아이가 있으면
        왼쪽아이의 넥스트는 오른쪽아이로 설정
    나의 오른쪽 아이와 나의 넥스트가 있으면
        오른쪽아이의 넥스트는 나의 넥스트의 왼쪽아이

    나의 왼쪽아이로 함수 반복
    나의 오른쪽아이로 함수 반복
"""
