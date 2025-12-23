class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
            
        word1 = {}
        word2 = {}
        for letter in s:
            if letter in word1.keys():
                word1[letter] += 1
            else:
                word1[letter] = 1
        
        for characters in t:
            if characters in word2.keys():
                word2[characters] += 1
            else:
                word2[letter] = 1
        
        for letter in word1.keys():
            if word1[letter] != word2[letter]:
                return False
            else:
                return True