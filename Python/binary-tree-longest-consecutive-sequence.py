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
        self.max_len = 0

        def longestConsecutiveHelper(root):
            if not root:
                return 0
    
            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)
    
            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1);
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len, left_len, right_len)

            return cur_len

        longestConsecutiveHelper(root)
        return self.max_len

"""
가장 긴 연속된 요소의 수를 구하는 문제, 소팅되어 있지 않다.
오엔으로 구하라는 문제다. 오엔으로 할 수 없는데 오엔으로 하라는 것은 해쉬테이블을 쓰라는 것이야.
그러면 스페이스는 오엔이지
루프는 한 번만 도니까 오엔

일단 해쉬 셋으로 바꾼다. 룩껍을 오원으로 하기 위해서

하나의 수에 대해서 엘, 알 투포인터를 두고, 엔 - 1 이 있으면 

솔루션(넘스)
    넘스셋 = 셋(넘스)
    앤스 = 0

    넘스셋이 있는 동안 루프 (왜냐하면 넘스셋의 요소를 지워가니까)
        엘 = 알 = 넘스셋에서 팝 한 놈
        엘 - 1이 넘스셋에 있으면 루프
            엘--
            넘스셋에서 엘 삭제
        알 + 1이 넘스셋에 있으면 루프
            알++
            넘스셋에서 알 삭제

        앤스는 앤스와 알-엘+1 중 큰 놈

    앤스를 리턴
"""
