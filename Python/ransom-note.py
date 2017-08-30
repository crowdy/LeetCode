# Time:  O(n)
# Space: O(1)

# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if
# the ransom  note can be constructed from the magazines ;
# otherwise, it will return false. 
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0] * 26
        letters = 0

        for c in ransomNote:
            if counts[ord(c) - ord('a')] == 0:
                letters += 1
            counts[ord(c) - ord('a')] += 1

        for c in magazine:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] == 0:
                letters -= 1
                if letters == 0:
                    break

        return letters == 0

# Time:  O(n)
# Space: O(1)
import collections

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)



"""
잡지에서 노트를 작성할 수 있는가?

1. Can I think for a second?
2. Think loud

노트에 있는 알파벳의 각 글자의 수가 잡지에 있는 알파벳의 글자의 수를 넘지 않는다면 노트를 작성할 수 있을 것 같다.
글자와 수를 저장하기에는 해쉬테이블을 사용하면 될 것 같은데
오엔 타임에 오원 스페이스로 해결할 수 있을 것 같다.

4. Does it seem like a good strategy?

"""
