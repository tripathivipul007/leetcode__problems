class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            temp_wealth = 0
            for bank in customer:
                temp_wealth += bank
                if temp_wealth > max_wealth:
                    max_wealth = temp_wealth
        return max_wealth