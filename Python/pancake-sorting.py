class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        output = []
        # 1.  If the list is sorted, return epty list        
        if A == sorted(A):
            return output
        
        def flip(end):
            start = 0
            while (start < end):
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1

        # 2. Find the largest element and swap with the first element then reverse
        
        N = len(A)
        for i in range(N-1, -1, -1):
            A = A[:i + 1]
            index = A.index(max(A))
            if index != i:
                flip(index)
                flip(i)
                output.append(index+1)
                output.append(i+1)
            
        return output
