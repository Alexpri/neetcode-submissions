class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr_pointer = len(nums1) - 1
        n1 = m - 1
        n2 = n - 1


        while n2 >= 0 and n1 >= 0:
            if nums1[n1] > nums2[n2]:
                nums1[curr_pointer] = nums1[n1]
                n1 -= 1
            else:
                nums1[curr_pointer] = nums2[n2]
                n2 -= 1

            curr_pointer -= 1

        while n2 >= 0:
            nums1[curr_pointer] = nums2[n2]
            n2 -= 1
            curr_pointer -= 1





        # while n != 0:
        #     if n1 >= m:
        #         n -= 1

        #     if nums1[n1] > nums2[n2] or nums1[n1] == 0:
        #         nums1[n1], nums2[n2] = nums2[n2], nums1[n1]
        #         n1 += 1
        #         if n1 < len(nums1) and nums1[n1] == nums2[n2]:
        #             n2 += 1
        #         if n2 == len_nums2:
        #             n2 = 0
        #     elif nums1[n1] <= nums2[n2]:
        #         n1 += 1


