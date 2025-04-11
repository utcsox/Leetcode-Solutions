class Solution:
  def remove_all_adjacent_duplicates_variant_1047_python(self, s):
      res = []

      for char in s:
        if not res:
          res.append({"k": char, "v": 1})
        elif res[-1]["k"] == char:
          res[-1]["v"] += 1
        else:
          if res[-1]["k"] != char and res[-1]["v"] > 1:
            res.pop()
  
          if res and res[-1]["k"] == char:
            res[-1]["v"] += 1

          else:
            res.append({"k": char, "v": 1})

      if res and res[-1]["v"] > 1:
        res.pop()

      return "".join([item["k"] for item in res])

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
