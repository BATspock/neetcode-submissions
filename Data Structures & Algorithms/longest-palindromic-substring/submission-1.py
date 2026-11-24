class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = ''
        # def isPalindrome(str):
        #     return str == str[::-1]

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if isPalindrome(s[i:j+1]) and len(s[i:j+1]) >= len(res):
        #             res = s[i:j+1]
        # return res

        self.res = ''

        def isPallindrome(str):
            return str == str[::-1]

        def helper(i):
            # odd
            l, r = i, i

            while l >= 0 and r < len(s):
                if isPallindrome(s[l:r+1]) and len(s[l:r+1]) >= len(self.res):
                    self.res = s[l:r+1]
                l-=1
                r+=1
            
            # even
            l, r = i, i+1

            while l >= 0 and r < len(s):
                if isPallindrome(s[l:r+1]) and len(s[l:r+1]) >= len(self.res):
                    self.res = s[l:r+1]
                l-=1
                r+=1

        for i in range(len(s)):
            helper(i)
            
        return self.res