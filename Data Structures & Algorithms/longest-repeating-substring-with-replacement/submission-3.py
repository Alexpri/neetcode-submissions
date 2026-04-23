class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest_s = 0
        left_p = 0
        max_freq = 0
        for right_p in range(len(s)):
            count[s[right_p]] = 1 + count.get(s[right_p], 0)
            max_freq = max(max_freq, count[s[right_p]])

            while (right_p - left_p + 1) - max_freq > k:
                count[s[left_p]] -= 1
                left_p += 1
            longest_s = max(longest_s, right_p - left_p + 1)

        return longest_s

            


