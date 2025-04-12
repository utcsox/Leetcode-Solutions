class Solution:
    def isPalindrome(self, s: str, include: list[str]) -> bool:
      include = set(include)
      l, r = 0, len(s) - 1

      while l < r:
        while l < r and not s[l] in include:
          l += 1
        while l < r and not s[r] in include:
          r -= 1

        if s[l] != s[r]:
          return False

        l += 1
        r -= 1

      return True

def test_isPalindrome():
    solution = Solution()
    assert not solution.isPalindrome("racecarX", ["r", "X"])
    assert solution.isPalindrome("Yo, banana boY!", ["Y", "o", "b", "a", "n"])
    assert solution.isPalindrome("yo banana boy!", ["y", "o", "b", "a", "n"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", " ", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "e"])
    assert not solution.isPalindrome("Wow", ["W", "o", "w"])
    assert solution.isPalindrome("WwoWWWWWWWWWWWWWow", ["o", "w"])
    assert solution.isPalindrome("__________________", ["1", "2"])
    assert not solution.isPalindrome("________133__________", ["1", "3"])
    assert not solution.isPalindrome("____1____133_______________", ["1", "3", "_"])
    assert solution.isPalindrome("", ["1", "3", "_"])
    assert solution.isPalindrome("", [])
    assert solution.isPalindrome("MadaM", [])
    assert solution.isPalindrome("MadaM", ["z", "M", "d"])
    assert not solution.isPalindrome("MadaMM", ["z", "M", "d"])
    assert not solution.isPalindrome("racecarX", ["r", "X"])
test_isPalindrome()
