class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered_sentence = ""
        for i in s:
            if i.isalnum():
                filtered_sentence += i.lower()
        left = 0
        right = len(filtered_sentence)-1
        while (left < right):
            if(filtered_sentence[left]!=filtered_sentence[right]):
                return False
            else:
                left = left + 1
                right = right - 1
        return True