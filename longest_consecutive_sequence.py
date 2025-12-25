class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        long_con = 0

        for num in set_num:
            if (num - 1) in set_num:
                continue

            current_num = num
            current_streak = 1

            while (current_num + 1) in set_num:
                current_num += 1
                current_streak += 1

            long_con = max(long_con, current_streak)

        return long_con           