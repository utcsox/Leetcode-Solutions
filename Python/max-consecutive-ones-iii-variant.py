def longestVacationTimeFirstVariant(days, pto):
  max_vacation, slow = 0, 0

  for fast, day in enumerate(days):
    if day == "W":
      pto -= 1

    if pto < 0:
      if days[slow] == "W":
        pto += 1
      slow += 1

    max_vacation = max(max_vacation, fast - slow + 1)

  return max_vacation

def test_longestVacationTimeFirstVariant():
    days = ['W', 'H', 'H', 'W', 'W', 'H', 'W']
    pto = 2
    assert 5 == longestVacationTimeFirstVariant(days, pto)

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 0
    assert 2 == longestVacationTimeFirstVariant(days, pto)

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 5
    assert 7 == longestVacationTimeFirstVariant(days, pto)

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 10
    assert 7 == longestVacationTimeFirstVariant(days, pto)

    days = ['H', 'H', 'H', 'H', 'H', 'H', 'H']
    pto = 0
    assert 7 == longestVacationTimeFirstVariant(days, pto)

    days = ['W', 'H', 'W', 'W', 'W', 'H', 'W', 'H']
    pto = 1
    assert 3 == longestVacationTimeFirstVariant(days, pto)

test_longestVacationTimeFirstVariant()
