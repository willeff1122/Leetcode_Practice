class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split()
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = s[i]
            elif d[pattern[i]] != s[i]:
                return False
        return True

pattern = "abba"
s = "dog cat cat dog"
a = Solution()
print(a.wordPattern(pattern,s))
