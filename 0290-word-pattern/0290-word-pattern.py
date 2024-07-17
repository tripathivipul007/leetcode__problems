class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        if len(pattern) != len(word_list):
            return False
        match={}
        
        for i in range(0, len(pattern)):
            if pattern[i] not in match:
                if word_list[i] not in match.values():
                    match[pattern[i]] = word_list[i]
                else:
                    return False
            else:
                if match[pattern[i]] != word_list[i]:
                    return False
        return True