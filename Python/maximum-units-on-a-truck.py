class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: -x[1])
        
        capacity = 0
        for box, unit in boxTypes:
            
            count = min(box, truckSize)
            
            capacity += unit * count
            truckSize -= count
            
            if truckSize < 0:
                break
                
        return capacity
