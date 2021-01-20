class Solution1:
    def checkDuplicatesWithinK(self, arr: List, k:int)->bool:
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if j>i+k:
                    break
                elif arr[i] == arr[j]:
                    return True
                
        return False

    
class Solution2:
    def checkDuplicatesWithinK(self, arr: List, k:int)->bool:
        tmp = []
        for i in range(0, len(arr)):
            if arr[i] in tmp:
                return True
            
            tmp.append(arr[i])
            if i >=k:
                tmp.remove(arr[i-k])
                
        return False
