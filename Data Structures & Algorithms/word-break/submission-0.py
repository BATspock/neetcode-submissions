class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        OPT = [False] * (len(s) + 1)
        OPT[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i : i + len(w)] == w:
                    OPT[i] = OPT[i + len(w)]
                if OPT[i]:
                    break
        return OPT[0]