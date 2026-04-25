# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        guess_result = left
        while left <= right:
            middle = (left + right) // 2
            guess_result = guess(middle)
            if guess_result == -1:
                right = middle - 1
            elif guess_result == 1:
                left = middle + 1
            else:
                return middle
            
        return left