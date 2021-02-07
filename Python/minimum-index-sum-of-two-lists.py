class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        lookup = {}
        least_index_sum = 100000
        restaraunt_name = []
        
        for index, value in enumerate(list1):
            lookup[value] = index
            
        for index, value in enumerate(list2):
            if value in lookup:
                if lookup[value] + index == least_index_sum:
                    restaraunt_name.append(value)
                elif lookup[value] + index < least_index_sum:
                    restaraunt_name.clear()
                    least_index_sum = lookup[value] + index
                    restaraunt_name.append(value)
                    
        return restaraunt_name
                
