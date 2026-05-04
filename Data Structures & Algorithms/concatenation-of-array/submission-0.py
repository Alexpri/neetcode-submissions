class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        ans = [0] * (2 * len_nums)

        for i, el in enumerate(nums):
            ans[i] = ans[i + len_nums] = el

        return ans
        