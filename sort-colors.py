class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_object = len(nums)
        count0 = 0
        count1 = 0
        count2 = 0
        for i in nums:
            if i==0:
                count0 +=1
            elif i==1:
                count1 +=1
            else:
                count2+=1
        for j in range(n_object):
            if (count0 > 0):
                nums[j] = 0
                count0 -=1
            elif (count0 == 0 and count1 > 0):
                nums[j] = 1
                count1 -=1
            else:
                nums[j] = 2
                count2 -=1
        return nums