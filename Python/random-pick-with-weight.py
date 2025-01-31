class Solution:

    def __init__(self, w: List[int]):
        cumu_sum, self.cumu_sum_array = 0, []

        for weight in w:
            cumu_sum += weight
            self.cumu_sum_array.append(cumu_sum)

        self.total_sum = cumu_sum

    def pickIndex(self) -> int:
        target = random.random() *  self.total_sum

        l, r = 0, len(self.cumu_sum_array)

        while l < r:
            mid = (l + r) // 2

            if self.cumu_sum_array[mid] < target:
                l = mid + 1

            else:
                r = mid

        return l
