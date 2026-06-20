class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = []
        temp = 0
        ans = 0

        for char in s:
            if char not in elements:
                temp+=1
                elements.append(char)
 
            else:
                while elements[0]!=char:
                    elements.pop(0)
                elements.pop(0)
                elements.append(char)
                temp = len(elements)
            if temp>ans:
                    ans = temp
            print(elements)
            print(temp)
            print(ans)
        return ans
        