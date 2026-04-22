class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0

        left_pointer = 0
        right_pointer = len(nums) - 1

        

        while left_pointer <= right_pointer:
            middle_pointer = round((left_pointer + right_pointer) / 2)

            if nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            elif nums[middle_pointer] > target:
                right_pointer = middle_pointer - 1
            else:
                return middle_pointer


        return -1