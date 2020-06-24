class Solution:
    def minWindow(self, s: str, t: str) -> str:
               # Set up a dictionary object that stores the numbers of time an alphabet appears in a the string t
        lookup = dict(collections.Counter(t))
        
        # setup a slow pointer and a fast pointer
        # setup a counter to track the numbers of alaphbet in lookup table equals to 0 
        # setup the minimum string length and minimum_string
        
        slow = 0 
        counter = 0
        minimum_string_length = float('inf')
        minimum_string = ''
        
        
        # if the alphabet is not appear in the lookup table, continue
        # else if it is in the lookup table, decrement lookup count
        for fast in range(len(s)):
            char = s[fast]
            if char not in lookup:
                continue
            lookup[char] -= 1
            
        # Increment the counter if the alphabet in the lookup table equals to 0
            if lookup[char] == 0:
                counter += 1

            # if the counter equals to the length of lookup, we can move the slow
            # pointer from the left
            # first, update the minimum length and minimum string accordingly

            while (counter == len(lookup) and slow <= fast):
                curr_len = fast - slow +1
                if curr_len < minimum_string_length:
                    minimum_string_length = curr_len
                    minimum_string = s[slow:fast+1]
                    
                # start moving the slow pointer from the left
                # if the characters point by the slow pointer is in lookup for t string,
                # need to a) increment the count for that alphabet by one
                # b)  if the lookup table for that alphabet equals to one, need to decrease 
                # the counter by one

                left_char = s[slow]
                slow += 1
                if left_char not in lookup:
                    continue

                lookup[left_char] += 1

                if lookup[left_char] == 1:
                    counter -= 1
                
        return minimum_string if minimum_string is not None else ""
        
        

        
