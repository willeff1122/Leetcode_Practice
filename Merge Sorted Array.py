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
