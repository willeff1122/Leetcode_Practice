# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hashmap = {}
#         n = len(nums)
#         for i in range(n):
#             hashmap[nums[i]] = i

#         for i in range(n):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i :
#                 return [i,hashmap[complement]]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i


a = Solution()            
nums = [0,0,3,3,45,4,8]
target = 7
b = a.twoSum(nums,target)
print (b)