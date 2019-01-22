# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max_size = [1]

        def largestBSTSubtreeHelper(root):
            if root.left is None and root.right is None:
                return 1, root.val, root.val

            left_size, left_min, left_max = 0, root.val, root.val
            if root.left is not None:
                left_size, left_min, left_max = largestBSTSubtreeHelper(root.left)

            right_size, right_min, right_max = 0, root.val, root.val
            if root.right is not None:
                right_size, right_min, right_max = largestBSTSubtreeHelper(root.right)

            size = 0
            if (root.left is None or left_size > 0) and \
                    (root.right is None or right_size > 0) and \
                                    left_max <= root.val <= right_min:
                size = 1 + left_size + right_size
                max_size[0] = max(max_size[0], size)

            return size, left_min, right_max

        largestBSTSubtreeHelper(root)
        return max_size[0]


"""
        max_size = [1] # 이걸 배열로 할 필요는 없는 것 같은데

        재귀함수(루트)
            단말노드이면
                1, 루트.밸, 루트.밸 을 리턴 (1은 사이즈)
            
            왼쪽아이가 있으면
                왼쪽사이즈, 왼쪽최소, 왼쪽최대 는 재귀함수(왼쪽아이)

            오른쪽아이가 있으면
                오른쪽사이즈, 오른쪽최소, 오른쪽최대 는 재귀함수(오른쪽아이)

            왼쪽아이가 있거나 왼쪽사이즈가 0보다 크고, 오른쪽아이가 있거나 오른쪽사이즈가 0보다 크고, 왼쪽최대 < 내 밸류 < 오른쪽 최소이면 (BST이면)
                사이즈에 왼쪽사이즈 + 오른쪽사이즈 + 1 을 대입
                최대크기는 max(최대크기, 사이즈)

            리턴 사이즈, 왼쪽최소, 오른쪽최대

        재귀함수(루트)
        리턴 최대크기
"""
