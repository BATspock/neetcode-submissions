class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def isPalindrome(str):
            return str == str[::-1]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]) and len(s[i:j+1]) >= len(res):
                    res = s[i:j+1]
        return res