class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el_dict = dict()
        len_nums = len(nums)

        for el in nums:
            if el not in el_dict:
                el_dict[el] = 1
            else:
                el_dict[el] += 1

            if el_dict[el] > len_nums // 2:
                return el

        