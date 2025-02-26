class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num, expt):
            if num == 0:
                return 0

            if expt == 0:
                return 1

            res = helper(num, expt // 2)
            res = res * res
            return num * res if expt % 2 else res

        output = helper(x, abs(n))
        return output if n >= 0 else 1/output
