class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = max(piles)
        import numpy as np
        # x = np.arange(1, max_num+1)
        import bisect
        import math

        def get_finishing_time(piles, k):
            ans = 0
            for i in range(len(piles)):
                ans += math.ceil(piles[i]/k)
            return ans
        ans = 0
        left = 0 
        right = max_num+1
        while right-left > 1:
            mid = (left+right)//2
            time = get_finishing_time(piles, mid)
            # print(len(x), mid, time)
            if time > h:
                # x = x[len(x)//2:]
                left = mid
            else:
                ans = mid
                # x = x[:len(x)//2]
                right = mid
            # break
        
        return int(ans)
