class Solution:
    def calculate_variant(self, s: str) -> int:
        if not s:
            return 0

        i, res, prev, num, op = 0, 0, 0, 0, "+"

        while i < len(s):
            c = s[i]
            if c.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                i -= 1

                if op == "+":
                    res += num
                    prev = num

                else:
                    res -= prev
                    res += prev * num
                    prev = prev * num

                num = 0

            elif c.isspace():
                pass

            else:
                op = c

            i += 1
        return res

def test_calculate_variant():
    solution = Solution()
    assert solution.calculate_variant("42") == 42
    assert solution.calculate_variant("3+2*2") == 7
    assert solution.calculate_variant(" 11+4+2+7 ") == 24
    assert solution.calculate_variant(" 3*5 * 2 ") == 30


test_calculate_variant()
