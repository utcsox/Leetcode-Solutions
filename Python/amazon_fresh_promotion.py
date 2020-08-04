class Solution:
    def isCustomerWinner(self, codeList: List[List[str]], shoppingCart: List[str]) -> int:
        
        lookup = [y for x in codeList for y in x]
        
        if len(shoppingCart) <  len(lookup):
            return 0
        
        
        for i in range(len(shoppingCart)-len(lookup) + 1):
            first_item = shoppingCart[i]
            output = []
            
            if first_item != lookup[0]:
                continue
            
            output.append(first_item)
            
            for j in range(1, len(lookup)):
                
                if lookup[j] == 'anything':
                    output.append(shoppingCart[j])
                    continue
                else:
                    print(i, j, shoppingCart[i+j], lookup[j])
                    if shoppingCart[i+j] != lookup[j]:
                        break
                    else:
                        output.append(shoppingCart[j])
            
            print(i, j, output)
            if len(output) == len(lookup):
                return 1
        
        return 0
