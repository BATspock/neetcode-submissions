class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_target, window = {}, {}

        for c in t:
            count_target[c] = 1 + count_target.get(c, 0)

        have, need = 0, len(count_target)
        res, res_len = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_target and window[c] == count_target[c]:
                have+=1

            while have == need:
                if ( r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -=1
                if s[l] in count_target and window[s[l]] < count_target[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l: r + 1] if res_len != float("infinity") else ""