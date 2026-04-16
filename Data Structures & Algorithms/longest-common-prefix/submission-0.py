class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs = sorted(strs)
        print(strs)

        index = 0

        ans = ""

        def validate_and_assign(ind):

            if ind > len(strs[0]) - 1:
                return ans, True

            return strs[0][ind], False

        while(True):
            compare, _exit = validate_and_assign(index)
            if (_exit):
                return ans

            for i in range(len(strs)):
                if strs[i][index] == compare:
                    compare = strs[i][index]
                else:
                    return ans

            index+=1
            ans+=compare

        return ans
