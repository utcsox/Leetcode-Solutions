class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        abs_diff, output= float('inf'), []
        
        for index in range(1, len(arr)):
            abs_diff = min(abs_diff, abs(arr[index]-arr[index-1]))
            
            
        for index in range(1, len(arr)):
            if (arr[index]-arr[index-1]) == abs_diff:
                output.append([arr[index-1], arr[index]])
        return output
