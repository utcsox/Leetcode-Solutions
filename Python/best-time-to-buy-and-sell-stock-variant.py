class Solution:
  def find_cheapest_tickets(self, departures, returns):
    min_price = float(math.inf)
    min_depart = departures[0]

    for i in range(1, len(departures)):
      min_price = min(min_price, min_depart + returns[i])
      min_depart = min(min_depart, departures[i])

    return min_price

def test_find_cheapest_tickets():
    solution = Solution()
    departures = [8, 3, 6, 10]
    returns = [10, 9, 5, 8]
    assert solution.find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns = [4, 20, 6, 7, 10]
    assert solution.find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns = [1, 20, 6, 7, 10]
    assert solution.find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert solution.find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert solution.find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert solution.find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert solution.find_cheapest_tickets(departures, returns) == 5

test_find_cheapest_tickets()
