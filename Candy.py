class Solution:
    def candy(self, ratings: list[int]) -> list[int]:
        length = len(ratings)
        candies = [1] * length
        for i in range(0, length - 1):
            if ratings[i] < ratings[i + 1]:
                candies[i + 1] = candies[i] + 1
        for i in range(length - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                candies[i - 1] = max(candies[i - 1], candies[i]+1)
        return candies

l = [1, 3, 4, 5, 2]
a = Solution()
print(a.candy(l))

#1,2,3,4,1