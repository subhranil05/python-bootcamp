class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""

        for i in range (len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return out
            out += strs[0][i]
            
            
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        minlen = len(strs[0])
        for i in range(1,len(strs)):
            minlen = min(minlen, len(strs[i]))
        
        add = ""

        for i in range(minlen):
            si = strs[0][i]
            for j in range(1,len(strs)):
                if si != strs[j][i]:
                    return add
            add += si
        return add