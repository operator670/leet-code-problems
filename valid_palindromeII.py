class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left]!=s[right]:
                left_string = s[left:right]
                right_string = s[left+1:right+1]
                return left_string == left_string[::-1] or right_string == right_string[::-1]
            left +=1
            right -= 1
        return True