class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_length = 1
        
        for sentence in sentences:
            temp_length = 1
            for i in range(len(sentence)):
                if sentence[i] == ' ':
                    temp_length +=1
                    if temp_length > max_length:
                        max_length = temp_length
                        
        return max_length
                        
                    
        