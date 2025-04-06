class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import defaultdict
        mapping = defaultdict(lambda: 0)
        output = ""
        for st in s:
            mapping[st] += 1

        for o in order:
            if o in mapping:
                output += o * mapping[o]
                del mapping[o]

        for k, v in mapping.items():
            output += k * v

        return output

class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        freqs = [0] * 26
        for ch in s:
            freqs[ord(ch) - ord('a')] += 1

        result = ""
        for ch in order:
            result += ch * freqs[ord(ch) - ord('a')]
            freqs[ord(ch) - ord('a')] = 0

        for i in range(26):
            result += chr(i + ord('a')) * freqs[i]

        return result
