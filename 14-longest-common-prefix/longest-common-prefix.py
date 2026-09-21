class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        longest=""
        prefix = []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            prefix.append(first[i])
        
        for j in range(len(prefix)):
            longest=longest+prefix[j]

            
        return longest
        