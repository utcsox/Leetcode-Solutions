class Solution:
    def removeDuplicates(self, s: str) -> str:

        res = []

        for c in s:
            if res and c in res[-1]:
                res.pop()

            else:
                res.append(c)

        return "".join(res)
   
