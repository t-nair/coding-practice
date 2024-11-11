class Solution:
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            w = 0
            for num in customer:
                w += num
            
            if w >= max_wealth:
                max_wealth = w

        return max_wealth
        