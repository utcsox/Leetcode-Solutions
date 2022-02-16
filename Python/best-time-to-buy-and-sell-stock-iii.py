class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        fb, fs, sb, ss = float('-inf'), 0, float('-inf'), 0
        
        for price in prices:
            fb = max(fb, -price)
            fs = max(fs, price + fb)
            sb = max(sb, fs-price)
            ss = max(ss, sb + price)
            
        return ss
