class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word  = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while (j < min(len(first_word), len(strs[i]))):
                if strs[i][j] == first_word[j]:
                    j += 1
                else:
                    break
            first_word = first_word[:j]
        return first_word
            