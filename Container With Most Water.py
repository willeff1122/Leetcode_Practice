class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        i = 1
        j = len(height)
        while i != j:
            area = max(area, (j - i) * (min(height[i-1],height[j-1])))
            if height[i-1] < height[j-1]:
                i += 1
            else:
                j -= 1
        return area

