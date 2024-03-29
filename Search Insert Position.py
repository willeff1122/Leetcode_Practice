#linear solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in nums:
            if i >= target:
                return ans
            else:
                ans += 1
        return ans
    
#binary search solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l=