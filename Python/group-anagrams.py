class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #.  if the sorted strings are the same, they are anagrams.
        anagrams_map, result = collections.defaultdict(list), []
        
        #1.  store same anagrams in the defaultdict
        for s in strs:
            sorted_string = ''.join(sorted(s))
            anagrams_map[sorted_string].append(s)
        
        #. sort the list of strings of same anagram
        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)
        
        return result
