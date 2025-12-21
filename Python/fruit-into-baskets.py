class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, res, basket = 0, 0, defaultdict(int)
      
        for r, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            res = max(res, r - l + 1)

        return res
