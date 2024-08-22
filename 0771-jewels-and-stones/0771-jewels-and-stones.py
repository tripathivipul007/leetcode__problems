class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter =0
        for character in stones:
            if character in jewels:
                counter+=1
        return counter