class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(0,len(haystack)):
                if needle==haystack[i:i+len(needle)]:
                    return i
                    break
        else:
            return -1

        