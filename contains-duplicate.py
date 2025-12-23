class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        threshold = 1
        counter = 1
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
                if seen[num] > threshold:
                    return True
            else:
                seen[num] =  counter
        return False