class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split()
        last = s[-1]
        return len(last)