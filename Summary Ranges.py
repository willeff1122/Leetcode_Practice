class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start, end = 0, 0
        while start < len(nums) and end < len(nums):
            if (end + 1) < len(nums) and nums[end] + 1 == nums[end+1]:
                end += 1
            else:
                if start == end:
                    result.append(str(nums[start]))
                    start += 1
                    end = start
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                    end += 1
                    start = end
        return result
