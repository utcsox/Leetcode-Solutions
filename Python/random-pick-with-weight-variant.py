class Solution:

  def __init__(self, city_population):
    self.city_population = city_population
    self.prefix_sum = []
    total_population = 0
    for city, population in city_population:
      total_population += population
      self.prefix_sum.append((city, total_population))
    self.total_population = total_population

  def pickIndex(self):
    target = random.uniform(0, self.total_population)
    print(f"target: {target}")

    left, right = 0, len(self.prefix_sum) - 1
    while left <= right:
      mid = (right - left) // 2 + left
      if target < self.prefix_sum[mid][1]:
          right = mid - 1
      else:
          left = mid + 1
    return self.prefix_sum[left][0]

    # for city, population in self.prefix_sum:
    #   if population >= target:
    #     return city
