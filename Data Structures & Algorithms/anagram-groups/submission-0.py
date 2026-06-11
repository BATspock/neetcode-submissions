class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
        for s in strs:
            freq = [0]*26
            for i in range(len(s)):
                freq[ord(s[i])-ord('a')]+=1
            #print(freq)
            anagrams[tuple(freq)].append(s)
        return list(anagrams.values())