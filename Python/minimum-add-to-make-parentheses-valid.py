class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance, res = 0, 0

        for st in s:
            if st == "(":
                balance += 1

            else:
                balance -= 1

            if balance < 0:
                res += 1
                balance += 1

        return res + balance
