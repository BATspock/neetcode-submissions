class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def helper(i):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res+=1
                l-=1
                r+=1

            l, r = i , i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res+=1
                l-=1
                r+=1

        for i in range(len(s)):
            helper(i)

        return self.res