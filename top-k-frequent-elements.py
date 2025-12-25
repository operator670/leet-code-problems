class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       seen = {}
       for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
        
       sorted_seen = sorted(seen.items(), key=lambda item: item[1], reverse=True)
       top_k_keys = [sorted_seen[0] for sorted_seen in sorted_seen[:k]]
       return top_k_keys 

              