class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
                break
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1