class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        output = []
        
        for i, value in enumerate(prices):
            boo = 0
            for j in range(i + 1, len(prices)):
                
                if prices[j] <= value:
                    output.append(value-prices[j])
                    boo = 1
                    break
            if boo == 0:       
                output.append(value)
            
        return output
