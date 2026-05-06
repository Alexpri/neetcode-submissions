class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_nums = len(nums)
        counter = 0
        result = nums[0]

        for el in nums:
            if el == result:
                counter += 1
            elif el != result:
                if counter == 0:
                    counter += 1
                    result = el
                else:
                    counter -= 1

        return result
            

        