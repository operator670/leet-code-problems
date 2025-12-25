class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_number_times = ceil(len(nums)/2)
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
                if seen[num] == majority_number_times :
                    return num
            else:
                seen[num] = 1
        return num