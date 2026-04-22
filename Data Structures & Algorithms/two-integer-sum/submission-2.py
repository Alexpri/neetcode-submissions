class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)

        # if len_nums == 2:
        #     return [0,1]

        # for i in range(len_nums):
        #     for j in range(i + 1, len_nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        # nums_dict = {
        #  3: 0 // index
        # }


        nums_dict = dict()
        for i in range(len_nums):
            looking_num = target - nums[i]
            if looking_num in nums_dict:
                return [nums_dict[looking_num], i]
            nums_dict[nums[i]] = i



        # for i in range(len_nums):
        #     if nums[i] not in nums_dict:
        #         nums_dict[nums[i]] = [i, target - nums[i]]
        #     else:
        #         nums_dict[nums[i]].append(nums[i])

        # for i in range(len_nums):
        #     if nums[i] in nums_dict and nums_dict[nums[i]][0] in nums_dict:
        #         target_el = nums_dict[nums[i]][0]
        #         return [i, nums_dict[target_el][1]]
