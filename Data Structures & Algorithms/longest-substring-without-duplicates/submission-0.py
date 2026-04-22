class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest_set = set()
        longest_len = 0
        # powwkew

        if len(s) == 0:
            return 0

        for right in range(len(s)):
            
            while s[right] in longest_set:
                longest_set.remove(s[left])
                left += 1

            longest_set.add(s[right])

            longest_len = max(longest_len, right - left + 1)
            
            

        return longest_len
            


        