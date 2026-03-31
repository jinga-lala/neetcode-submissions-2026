class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        
        x = nums.pop()
        remaining = self.subsets(nums)
        with_x = []
        for i in remaining:
            with_x.append(i + [x])
        return remaining + with_x
    

        