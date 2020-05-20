class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map, result = collections.defaultdict(list), []
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_map[sorted_str].append(s)
        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)
        return result
