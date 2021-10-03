class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        
        flowerbed.extend([0, 0])
        
        for index in range(len(flowerbed)-2):
            if flowerbed[index-1] == flowerbed[index] == flowerbed[index+1] == 0:
                count += 1
                flowerbed[index] = 1
                
                
        return count >= n
        
