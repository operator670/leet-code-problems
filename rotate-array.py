class Solution:

    def swapper(self, nums: List[int], left: int, right: int) -> None:

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.swapper(nums, 0, n-1)
        self.swapper(nums, 0, k-1)
        self.swapper(nums, k, n-1)
        

        