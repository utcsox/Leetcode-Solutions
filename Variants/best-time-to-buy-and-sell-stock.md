You are given two arrays `departures` and `returns` where `departures[i]` and `returns[i]` are ticket prices for departing and returning flights on the ith day, respectively.

You want to minimize your cost by choosing a single day to buy a departure flight and choosing a **different day in the future** to buy returning flight.

Return the minimum cost you can achieve from a single round-trip flight.

Example 1:
  Input: departures = [1, 2, 3, 4], returns = [4, 3, 2, 1]
  Output: 2

  Explanation:  Buy a departure flight on day 0 (price = 1) and buy a return ticket on day 3 (price = 1), cost 1 + 1 = 2
