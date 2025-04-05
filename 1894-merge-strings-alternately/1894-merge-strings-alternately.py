class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        len1, len2 = len(word1), len(word2)
        i=0
        while i< len1 and i<len2:
            merged+= word1[i]+word2[i]
            i+=1
            if i==len1:
                merged+=word2[i:]
            elif i==len2:
                merged+=word1[i:]

        return merged
        