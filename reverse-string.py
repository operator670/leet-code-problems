class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j=len(s)-1
        mid = (i+j)//2
        for i in range(mid+1):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
