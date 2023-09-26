from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        a, b = Counter(ransomNote), Counter(magazine)
        if a <= b:
            return True
        return False

a = Solution()
ransomNote = "aabb"
magazine = "aab"
print(a.canConstruct(ransomNote, magazine))