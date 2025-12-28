class Solution:
    def compress(self, chars: List[str]) -> int:

        i, index = 0, 0

        while i < len(chars):

            curr_char, curr_length = chars[i], 1

            while (curr_length + i < len(chars)):
                if chars[curr_length + i] == curr_char:
                    curr_length += 1

                else:
                    break

            chars[index] = curr_char
            index += 1
