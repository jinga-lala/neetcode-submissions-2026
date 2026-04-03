class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums)):
            if nums[i] <=0 and x==0:
                continue
            x = nums[i] + x
            if x < 0:
                # nums[i]=0
                x=0
            else:
                nums[i]=x
        return max(nums)
