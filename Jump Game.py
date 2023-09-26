class Solution:
    def canJump(self, nums: list[int]) -> bool:
        steps = nums[0]
        for i in range(1, len(nums)):
            if steps == 0:
                return False

            steps = max(steps - 1, nums[i])
        return True