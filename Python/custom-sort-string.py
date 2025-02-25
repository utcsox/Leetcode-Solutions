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
