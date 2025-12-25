class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n not in seen and n != 1:
            total = 0
            seen.add(n)

            while n > 0:
                n, digit = n//10, n%10
                total += digit * digit

            n = total

        return n == 1
