class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        index_counter = {}
        for i in range(len(s)):
            index_counter[s[i]] = i
            
        print(index_counter)
             
            
        ans = 0
        for j in range(len(t)):
            ans += abs(j-index_counter[t[j]])
            
        return ans
            
            
        