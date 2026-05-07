class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        trimed_s = s.replace(" ", "")
        end = len(trimed_s) - 1

        while start <= end:
            trimmed_start = trimed_s[start].lower()
            trimmed_end = trimed_s[end].lower()
            if not trimmed_start.isalpha() and not trimmed_start.isnumeric():
                start += 1
                continue

            if not trimmed_end.isalpha() and not trimmed_end.isnumeric():
                end -= 1
                continue

            if trimed_s[start].lower() != trimed_s[end].lower():
                return False

            start += 1
            end -= 1

        return True