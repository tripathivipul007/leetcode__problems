class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        ar = s.split()
        ar = ar[:k]
        return ' '.join(ar)
        