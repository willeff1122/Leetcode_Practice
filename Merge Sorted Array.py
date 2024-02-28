class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        idx = 0
        for i in range(len(nums1)):
            if idx >= n:
                break
            if nums1[i] == 0:
                nums1[i]=nums2[idx]
                idx += 1

        for j in range(len(nums1)):
            for k in range(len(nums1)):
                if nums1[j] < nums1[k]:
                    nums1[j], nums1[k] = nums1[k], nums1[j]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            elif nums1[m - 1] <= nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
