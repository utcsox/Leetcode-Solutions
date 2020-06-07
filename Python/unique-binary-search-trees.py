class Solution:
    def numTrees(self, n: int) -> int:
        counts = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(1, i+1):
                count += counts[j-1] * counts[i-j]
            counts.append(count)
        return counts[-1]
