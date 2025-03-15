You are conducting an A/B test and need to randomly pick a person from a user base spread across multiple cities.  Each city has a known population, and you need to ensure that the probability of choosing a user from each city is proportional to the city's population.  

You are given a 0-indexed array of pairs city_population, where each pair consists of a string representation the name of the ith city, and an integer representating the population of the ith city (in millions, but treat these values as if in ones for computing purposes)

You need to implement the function pickIndex(), which randomly picks a person in and returns the name of the city the person is in.  

Example 1:  

  Input
  ["Solution", "pickIndex", "pickIndex"[
  [[["Seattle", 500], ["New York", 900], ["Los Angeles", 400]], [], []]
  Output
  [null, "New York", "Los Angeles"]
