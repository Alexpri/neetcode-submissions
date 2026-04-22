class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_numbers = len(numbers)
        left_pointer = 0
        right_pointer = len_numbers - 1
        result = []

        while left_pointer < right_pointer:
            summary = numbers[left_pointer] + numbers[right_pointer]
            if summary > target:
                right_pointer -= 1
            elif summary < target:
                left_pointer += 1
            else:
                return [left_pointer + 1, right_pointer + 1]
            