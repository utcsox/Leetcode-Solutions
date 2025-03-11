class Solution:

    def __init__(self, nums: List[int]):
        self.lookup = defaultdict(list)
        for i, num in enumerate(nums):
            self.lookup[num].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.lookup[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
