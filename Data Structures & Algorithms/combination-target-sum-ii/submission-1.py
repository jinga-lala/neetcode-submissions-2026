class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def solution(candidates, target):
            if target==0 and len(candidates)==0:
                return [[]]
            if target!=0 and len(candidates)==0:
                return []
            
            
            y = candidates.copy() 
            x = candidates.pop()
            while len(candidates)> 0 and candidates[-1] == x:
                candidates.pop()
            without_x = solution(candidates, target)
            candidates = y
            candidates.pop()
            if target >= x:
                with_x = solution(candidates, target-x)
            else:
                with_x = []
            for i in range(len(with_x)):
                with_x[i] += [x]
            return with_x + without_x
        candidates.sort()
        return solution(candidates, target)
            
            
        