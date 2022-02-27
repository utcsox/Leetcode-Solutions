class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        tmp = [amount + 1] * (amount + 1)
        tmp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    tmp[a] = min(tmp[a], 1 + tmp[a-c])
                    
                    
        if tmp[amount] != (amount + 1):
            return tmp[amount]
        
        else:
            return - 1
