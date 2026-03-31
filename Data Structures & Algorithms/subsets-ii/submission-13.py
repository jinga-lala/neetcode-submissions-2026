class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset(l,):
            if len(l) == 0:
                return [[]]  # list containing the empty subset
            
            x = l.pop(0)
            ans = subset(l)
            
            appended_ans = []
            for i in ans:
                tmp = [x] + i
                tmp.sort()
                appended_ans.append(tmp)
                  # creates a new list instead of mutating
            
            return appended_ans + ans  # flat concatenation instead of nesting

        # covered_elements = set()

        def convert_to_str(lst):
            x = ''
            for l in lst:
                x += str(l) + ' '
            return x
        
        def str_to_int(st):
            st = st.split(" ")
            ans = []
            for s in st:
                if s=='': continue
                ans.append(int(s))
            return ans
        ans = subset(nums, )
        str_ans = []
        print(ans)
        for i in range(len(ans)):
            str_ans.append(convert_to_str(ans[i]))
        str_ans = list(set(str_ans))
        print(str_ans)
        final_ans = []
        for i in range(len(str_ans)):
            final_ans.append(str_to_int(str_ans[i]))
        return final_ans
