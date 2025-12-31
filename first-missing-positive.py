class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] < 0 or nums[i] > n:
                i += 1
                continue
            index = nums[i] - 1
            if index >= 0 and nums[index] != nums[i]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1
        
        for j in range(n):
            if nums[j] != j+1:
                return j+1
        return n+1
