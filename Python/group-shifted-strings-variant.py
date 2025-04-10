class Solution:
    def rotationalCipher(self, string: str, rotation_factor: int) -> str:
        if rotation_factor == 0:
            return string

        result, shift_char = "", ""
        for char in string:
            if char.isalpha():
                start = ord("a") if char.islower() else ord("A")
                shift_char = chr((ord(char) - start + rotation_factor) % 26 + start)
                
            elif char.isdigit():
              shift_char = str((ord(char) - ord("0") + rotation_factor) % 10)

            else:
              shift_char = char

            result += shift_char

        return result

def test_rotationalCipher():
  solution = Solution()
  assert solution.rotationalCipher("minMerz-894", 5) == "rnsRjwe-349"
  assert solution.rotationalCipher("XYZ_abo_112288", 39) == "KLM_nob_001177"


test_rotationalCipher()
