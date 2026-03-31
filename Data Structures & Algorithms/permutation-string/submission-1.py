class Solution:
    dp = {}
    def getpermutations(self, s1):
        if len(s1)==0:
            return ['']
        if s1 in self.dp:
            return self.dp[s1]
        ans = []
        for i in range(len(s1)):
            x = s1[i]
            rest = s1[:max(i,0)] + s1[i+1:]
            # print(x,rest)
            y = self.getpermutations(rest)
            self.dp[rest] = y
            # print(y, x)
            z = []
            for str1 in y:
                z.append(str(x) + str(str1))
            ans.extend(z)
        return ans 

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 in s2:
            return True
        x = self.getpermutations(s1)
        # print(s1, x)
        for i in x:
            if i in s2:
                return True
        return False