class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, permutation = [], []

        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for num in counter:
                if counter[num] > 0:
                    permutation.append(num)
                    counter[num] -= 1
                    backtrack()
                    permutation.pop()
                    counter[num] += 1
                
        counter = collections.Counter(nums)
        backtrack()

        return res
