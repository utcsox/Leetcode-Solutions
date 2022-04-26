class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right, result = 1, max(piles), max(piles)
        
        while left <= right:
            rate =  left + (right-left)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)
                    
            if hours <= h:
                result = min(result, rate)
                right = rate - 1
              
            else:
                left = rate + 1

                
        return result
