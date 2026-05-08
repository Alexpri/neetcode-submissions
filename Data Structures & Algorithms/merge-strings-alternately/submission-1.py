class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_result = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        longest_w = word1 if len_word1 >= len_word2 else word2
        i_counter = 0

        while i_counter != min(len_word1, len_word2):
            final_result += word1[i_counter] + word2[i_counter]
            i_counter += 1

        if i_counter != len(longest_w):
            final_result += longest_w[i_counter:]
        
        return final_result
        