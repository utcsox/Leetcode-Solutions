class Solution:
  def remove_all_adjacent_duplicates_variant_1047_python(self, s):
      stack = []
      for i in range(len(s)):
        if stack and stack[-1][0] == s[i]:
            stack[-1][1] += 1
        else:
            stack.append([s[i],1])
        if i == len(s)-1 or s[i] != s[i+1]:
            if stack[-1][1] >= 2:
              stack.pop()

      res = ''
      for elem in stack:
          res += elem[0] * elem[1]
      return res


def test_remove_all_adjacent_duplicates_variant(): 
  solution = Solution()
  
  s = "azxxxzy"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == "ay"

  s = "abbaxx"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == ""

  s = "aabbccdd"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == ""

  s = "aaabbaad"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == "d"

  s = "abcdefg"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == "abcdefg"

  s = "abbcddeff"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == "ace"

  s = "abcdeffedcba"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == ""

  s = "aabccddeeffbbbbbbbbbf"
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == "f"

  s = "abbbacca"; # Cannot pick and choose duplicates in the middle to delete first
  assert solution.remove_all_adjacent_duplicates_variant_1047_python(s) == "a"

test_remove_all_adjacent_duplicates_variant()
