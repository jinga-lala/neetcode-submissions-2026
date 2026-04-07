class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = hmap.get(nums[i], 0) + 1
        hmap = dict(sorted(hmap.items(), key=lambda x: x[1], reverse=True))
        # hmap.sort()
        return list(hmap.keys())[:k]