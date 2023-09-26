# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         nums.sort()
#         a = 0
#         length = 0
#         total = sum(nums)
#         if total < target:
#             return length
#         elif total == target:
#             return len(nums)
#         else:
#             for i in range(len(nums)-1, -1, -1):
#                 if a < target:
#                     length += 1
#                     a += nums[i]
#                     print(a)
#                 else:
#                     return length
#
#


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # initialize pointers and sum
        left, right, total = 0, 0, 0
        min_len = len(nums)
        if sum(nums) < target:
            return 0
        else:
            while right < len(nums):
                total += nums[right]
                right += 1
                while total >= target:
                    min_len = min(min_len, right - left)
                    total -= nums[left]
                    left += 1
        return min_len


target = 15
nums = [5,1,3,5,10,7,4,9,2,8]
a = Solution()
print(a.minSubArrayLen(target,nums) )