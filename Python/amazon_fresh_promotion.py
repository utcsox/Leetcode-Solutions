class Solution1:
    def isCustomerWinner(self, codeList: List[List[str]], shoppingCart: List[str]) -> int:
        
        lookup = [y for x in codeList for y in x]
                
        for i in range(len(shoppingCart)-len(lookup) + 1):
            first_item = shoppingCart[i]
            output = []
            if first_item != lookup[0]:
                continue
            
            output.append(first_item)
            
            for j in range(1, len(lookup)):
                
                if lookup[j] == 'anything':
                    output.append(shoppingCart[j+i])
                    continue
                elif shoppingCart[i+j] == lookup[j]:
                    output.append(shoppingCart[j+i])
                else:
                    break
            
            if len(output) == len(lookup):
                return 1
        
        return 0
    
class Solution2:
    def isCustomerWinner(self, codeList: List[List[str]], shoppingCart: List[str]) -> int:
        
        lookup = [y for x in codeList for y in x]
        
        if len(shoppingCart) <  len(lookup):
            return 0
        
        # two pointer solution
        
        fast, right = 0, len(shoppingCart)-len(lookup)
          
        while fast <= right:
            
            if shoppingCart[fast] != lookup[0]:
                fast += 1
                continue
            output = []
            output.append(shoppingCart[fast])
                
            for index in range(1, len(lookup)):
                if lookup[index] == 'anything':
                    output.append(shoppingCart[index + fast])
                    continue
                elif lookup[index] == shoppingCart[fast+index]:
                    output.append(shoppingCart[fast+index])

                else:
                    fast = fast + index
                    break
            
            if len(output) == len(lookup):
                return 1

            fast += 1
           
        return 0
