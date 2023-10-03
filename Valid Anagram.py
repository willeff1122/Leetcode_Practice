class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = Counter(s), Counter(t)
        if a == b:
            return True
        return False