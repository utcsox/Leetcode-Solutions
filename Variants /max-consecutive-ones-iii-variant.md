Given an array of character days of 'W' and 'H' where 'W' represents a work day and 'H' represents a holiday, return the 
longest possible vacation of consecutive days you can take if you are allowed at most PTO days off.

Example 1:
  Input: days = [W, H, H, W, W, H, W], PTO = 2
  Output: 5
  Explanation: [W, H, H, H, H, H, W]
  Bolded characters were flipped from W to H.  The longest subarray is underlined.  

Example 2:
  Input: days = [W, W, W, H, H, W[, PTO = 0
  Output: 2
  Explanation: [W, W, W, H, H, W]
  Bolded characters were flipped from W to H.  The longest subarray is underlined.
