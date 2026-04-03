class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [len(nums)-1]
        hashmap = {}
        hashmap[len(nums)-1] = len(nums)-2
        while len(stack)!=0:
            goal = stack[-1]
            i = hashmap[goal]
            while i >=0:
                if (i+nums[i])>=goal:
                    hashmap[goal] = i-1
                    stack.append(i)
                    hashmap[i] = i-1
                    break
                i-=1
            if i==-1:
                stack.pop()
                
            if 0 in hashmap:
                return True
        return False
                