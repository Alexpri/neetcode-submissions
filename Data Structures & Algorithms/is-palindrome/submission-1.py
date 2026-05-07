class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        trimed_s = s.replace(" ", "")
        end = len(trimed_s) - 1

        while start <= end:
            trimmed_start = trimed_s[start].lower()
            trimmed_end = trimed_s[end].lower()
            if not trimmed_start.isalnum():
                start += 1
                continue

            if not trimmed_end.isalnum():
                end -= 1
                continue

            if trimmed_start != trimmed_end:
                return False

            start += 1
            end -= 1

        return True