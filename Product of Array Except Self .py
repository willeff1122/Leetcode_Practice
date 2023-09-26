class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        product = [1] * length
        right = nums[length - 1]
        for i in range(1, length):
            product[i] = nums[i - 1] * product[i - 1]

        for i in range(length - 2, -1, -1):
            product[i] = product[i] * right
            right = right * nums[i]
        return product

nums = [3,2,1,0,4]
nums = [1,2,3,4]
a = Solution()
print(a.productExceptSelf(nums))