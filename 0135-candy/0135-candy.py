class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        up = down = peak = 0
        total = 1  # First child gets 1 candy

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:  # Going uphill
                up += 1
                peak = up
                down = 0
                total += up + 1
            elif ratings[i] < ratings[i - 1]:  # Going downhill
                up = 0
                down += 1
                total += down
                if down > peak:
                    total += 1  # Fix peak point if downhill is longer
            else:
                up = down = peak = 0
                total += 1

        return total
