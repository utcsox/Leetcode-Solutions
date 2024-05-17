def find_max_duplicate(text:str):
    if not text:
        return []

    if len(text) == 1:
        return [text]
        
    lookup = defaultdict(int)
    
    curr_char, curr_count = text[0], 1
    
    for char in text[1:]:
        if char == curr_char:
            curr_count += 1
        else:
            if lookup[curr_char] < curr_count:
                lookup[curr_char] = curr_count
    
            curr_char = char
            curr_count = 1

    # add last char and count to the lookup dictionary
    lookup[curr_char] = curr_count

    output = [k for k, v in lookup.items() if v == max(lookup.values())]
    
    return output

# test_cases = [
#   ("aaaabbbbccc", ['a', 'b']),
#   ("abcd", ['a', 'b', 'c', 'd']),
#   ("aa", ['a', 'a']),
#   ("", []),
# ]
