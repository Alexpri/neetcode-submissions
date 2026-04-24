class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_sum = len(nums)
        left = 0
        right = len_sum - 1
        result = -1

        while left <= right:
            cur_index = (right + left) // 2
            if nums[cur_index] > target:
                right = cur_index - 1

            elif nums[cur_index] < target:
               left = cur_index + 1
            else:
                return cur_index

        return left