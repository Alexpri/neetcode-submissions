class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = 0

        while left <= right:
            middle = (right + left) // 2
            sqr = middle * middle
            if sqr > x:
                right = middle - 1
            elif sqr < x:
                left = middle + 1
                result = middle
            else:
                return middle

        return result 
