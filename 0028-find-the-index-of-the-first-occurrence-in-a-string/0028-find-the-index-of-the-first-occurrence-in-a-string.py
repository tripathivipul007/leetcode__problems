class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nedlen = len(needle)
        for i in range(len(haystack)-nedlen+1):
            if haystack[i:i+nedlen] == needle:
                return i
            
        return -1