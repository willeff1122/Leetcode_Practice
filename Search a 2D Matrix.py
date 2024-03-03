class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][COL-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        if not top <= bot:
            return False
        l, r = 0, COL - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[mid][m]:
                return True
            if target > matrix[mid][m]:
                l = m + 1
            else:
                r = m - 1
        return False

matrix = [[1, 3]]

a = Solution()
a.searchMatrix(matrix,3)