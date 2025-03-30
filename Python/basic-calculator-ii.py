class Solution1:
    def calculate(self, s: str) -> int:

        if len(s) == 0:
            return 0

        num, output, op = 0, [], "+"

        for i, st in enumerate(s):
            if st.isdigit():
                num = 10 * num + int(st)

            if (not st.isspace() and not st.isdigit()) or i == len(s) - 1:

                if op == "+":
                    output.append(num)
                elif op == '-':
                    output.append(-num)
                elif op == "*":
                    output.append(output.pop() * num)

                else:
                    tmp = output.pop()
                    if (tmp // num) < 0 and (tmp % num) != 0:
                        output.append(tmp // num + 1)
                    else:
                        output.append(tmp // num)

                num = 0
                op = st

        return sum(output)

class Solution2:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        res, prev, curr, i = 0, 0, 0, 0
        sign = "+"

        while i < len(s):
            symbol = s[i]
            if symbol.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10  + int(s[i])
                    i += 1
                i -= 1

                if sign == "+":
                    res += curr
                    prev = curr

                elif sign == "-":
                    res -= curr
                    prev = -curr

                elif sign == "*":
                    res -= prev
                    res += prev * curr
                    prev = prev * curr

                else:
                    print(f"sign: {sign} symbol: {symbol}")
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev/ curr)

                curr = 0

            elif not symbol.isspace():
                sign = symbol

            i += 1

        return res

