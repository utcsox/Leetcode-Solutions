class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res, combinations = [], []

        def backtrack(start):

            if len(combinations) == k:
                res.append(combinations[:])
                return

            for i in range(start, n + 1):
                combinations.append(i)
                backtrack(i + 1)
                combinations.pop()

        backtrack(1)
        return res
