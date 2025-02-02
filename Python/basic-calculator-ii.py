class Solution:
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
