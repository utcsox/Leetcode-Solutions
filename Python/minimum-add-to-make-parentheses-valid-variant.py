class Solution:
    def minimumAddToMakeValid(self, s: str) -> str:
        res, extra_open = [], 0
        for c in s:
            
            if c == "(":
              extra_open += 1
                
            else:
                if c == ")":
                  if extra_open > 0:
                    extra_open -= 1

                  else:
                    if c == ")":
                      res.append("(")
                      extra_open = 0

            res.append(c)

        return "".join(res) + ")" * extra_open

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
