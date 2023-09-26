class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         count = 0
#         candidate = 0
#         for i in nums:
#             if count == 0:
#                 candidate = i
#             if i == candidate:
#                 count += 1
#             if i != candidate:
#                 count -= 1
#
#         return candidate

nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 6, 6]
a = Solution()

print(a.majorityElement(nums))