class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        # Merge characters alternately
        for c1, c2 in zip(word1, word2):
            merged.append(c1)
            merged.append(c2)

        # Add the remaining part of the longer word
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])

        return ''.join(merged)
