class Solution:
    def match(self, compare_str: str) -> bool:
        compare_map = {}
        for char in compare_str:
            compare_map[char] = 1 + compare_map.get(char, 0)
        
        for c in self.base:
            if c not in compare_map:
                return False
            elif compare_map[c] == 0:
                return False
            else:
                compare_map[c]-=1

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        self.base = s1

        l, r = 0, len(s1)-1

        while r < len(s2): 
            if self.match(s2[l:r+1]):
                return True
            l+=1
            r+=1

        return False