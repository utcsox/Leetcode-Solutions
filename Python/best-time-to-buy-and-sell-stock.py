import math
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        max_profit, min_price = 0, math.inf
        for num in nums:
            min_price = min(min_price, num)
            max_profit = max(max_profit, num-min_price)
        return max_profit
