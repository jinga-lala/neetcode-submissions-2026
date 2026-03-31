class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hist = {}
        ans = 0
        tmp = 0
        cstr = ''
        for i in range(len(s)):
            if s[i] in cstr:
                ans = max(ans, tmp)
                cstr = s[hist[s[i]]+1:i+1]
                tmp = len(cstr)
                hist[s[i]] = i
            else:
                hist[s[i]] = i
                tmp +=1
                cstr = cstr + s[i]
        ans = max(ans, tmp)
        return ans