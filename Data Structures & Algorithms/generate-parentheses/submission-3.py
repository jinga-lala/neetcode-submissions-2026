class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # f(n) = ()f(n-1)
        # f(n) = (f(n-1))
        # f(n) = f(n-1)()
        # is incorrect because you miss f(2)f(2) case
        # correct way is f(n) = (f(i))f(n-i-1)
        """    
        hashmap = {}
        def gp(n):
            if n==0:
                return [""]
            if n==1:
                return ["()"]
            if n in hashmap:
                return hashmap[n]
            x = []
            for i in range(n):
                tmp1 = gp(i)
                tmp2 = gp(n-i-1)
                tmp3 = []
                for j in tmp1:
                    for k in tmp2:
                        tmp3.append("("+j+")" + k)
                tmp3 = list(set(tmp3))
                x.extend(tmp3)
            x = list(set(x))
            hashmap[n] = x
            return x
        ans =list(set(gp(n)))
        print(len(ans))
        return ans
        """
        results = []
        def backtrack(s, open, closed):
            if len(s) == 2*n and open==closed:
                results.append(s)
                return
            if open <= n:
                backtrack(s + "(", open+1, closed)
            if open > closed and open <=n:
                backtrack(s + ")", open, closed+1)
            return
        backtrack("", 0,0)
        return results
