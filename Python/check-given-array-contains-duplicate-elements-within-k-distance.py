class Solution:
    def checkDuplicatesWithinK(self, arr: List, k:int)->bool:
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if j>i+k:
                    break
                elif arr[i] == arr[j]:
                    return True
                
        return False
