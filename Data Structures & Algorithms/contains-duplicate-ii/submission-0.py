class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_table = dict()
        len_nums = len(nums)
        pointer = 0

        if len_nums == 1:
            return False

        def is_valid(i: int, j: int) -> bool:
            return nums[i] == nums[j] and abs(i - j) <= k

        while pointer < len_nums:
            current_val = nums[pointer]
            if current_val not in nums_table:
                nums_table[current_val] = [pointer]
            else:
                current_list = nums_table[current_val]
                for current_index in current_list:
                    result = is_valid(current_index, pointer)
                    if result:
                        return True

                nums_table[current_val].append(pointer)

            pointer += 1

        return False
                        

            