class Solution:
    def NMaxElementMatrix(self, list1: List, N: int) -> List:
        list1.sort(reverse=True)
        return list1[:N]
