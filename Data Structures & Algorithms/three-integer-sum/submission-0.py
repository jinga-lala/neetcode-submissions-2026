class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        import bisect
        ans = []
        maps = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = -(nums[i] + nums[j])
                idx = bisect.bisect_left(nums[j+1:], target)  
                if idx >= len(nums) - j - 1: 
                    continue
                if nums[j+1+idx] == target:
                    # ans.append([nums[i],nums[j],nums[idx+j+1]])
                    maps[(nums[i],nums[j],nums[idx+j+1])] = 1
        
        return list(maps.keys())