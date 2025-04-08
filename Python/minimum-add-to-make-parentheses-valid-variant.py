class Solution:
    def minimumAddToMakeValid(self, s: str) -> str:
        res = []
        balance = 0
        for c in s:
            if c == '(':
                balance += 1

            if c == ")":
              balance -= 1

            if balance < 0:
              res.append("(")
              balance += 1
            res.append(c)
                
        res += [')'] * balance
        return "".join(res)

def test_minimumAddToMakeValid():
  solution = Solution()
  assert solution.minimumAddToMakeValid("(())((") == "(())(())"
  assert solution.minimumAddToMakeValid("))(") == "()()()"
  assert solution.minimumAddToMakeValid(")))") == "()()()"
  assert solution.minimumAddToMakeValid("(((") == "((()))"
  assert solution.minimumAddToMakeValid("") == ""
  assert solution.minimumAddToMakeValid("(())") == "(())"
  assert solution.minimumAddToMakeValid(")))(((") == "()()()((()))"
  assert solution.minimumAddToMakeValid("abcxyz") == "abcxyz"
  assert solution.minimumAddToMakeValid("(()()))((") == "(()())()(())"
  assert solution.minimumAddToMakeValid("((a)()))((xyz") == "((a)())()((xyz))"

test_minimumAddToMakeValid()
