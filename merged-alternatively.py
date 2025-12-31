class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        start1 = 0
        start2 = 0
        merged_str = ""
        while start1 < len(word1) and start2 < len(word2):
            merged_str += word1[start1]
            merged_str += word2[start2]
            start1 += 1
            start2 += 1
        
        while start1 < len(word1):
            merged_str += word1[start1]
            start1 += 1
        while start2 < len(word2):
            merged_str += word2[start2]
            start2 += 1
        return merged_str