class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target==0:
            return [[]]

        list_with_x = []
        for j in range(len(nums)):
            x = nums[j]
            if target >= x:
                with_x = self.combinationSum(nums, target-x)
            else:
                with_x = []
            
            for i in with_x:
                list_with_x.append(i + [x])
        return self.remove_duplicates(list_with_x) 
    
    def l2s(self,lst):
        # print(lst)
        return ' '.join(map(str, lst))
    
    def s2l(self, s):
        lst = s.split(' ')
        return [int(i) for i in lst]

    def remove_duplicates(self, lst):
        newlst = []
        for l in lst:
            l.sort()
            newlst.append(self.l2s(l))
        newlst = list(set(newlst))
        ans = []
        for l in newlst:
            ans.append(self.s2l(l))
        return ans


    def combinationSum_chose_number_once(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)==0:
            return []

        
        x = nums.pop()
        remaining = self.combinationSum(nums, target)
        if target >= x:
            with_x = self.combinationSum(nums, target-x)
        else:
            with_x = []
        list_with_x = []
        for i in with_x:
            list_with_x.append(i + [x])
        return list_with_x + remaining