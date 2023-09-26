class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        a = set()
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left += 1
            a.add(s[right])
            count = max(count, right - left+1)
            print("left:", left)
            print("right:", right)
            print("a = ", a)
            print("count =", count)
        return count

a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))