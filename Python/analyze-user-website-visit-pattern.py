class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        UTW = sorted(zip(username, timestamp, website), key =lambda x: (x[0], x[1]))
        users = defaultdict(list)
        for user, time, site in UTW:
            users[user].append(site)
            
            
        patterns = Counter()
        
        for user, sites in users.items():
            unique_sequence_combo = set(combinations(sites, 3))
            unique_sequence_combo = Counter(unique_sequence_combo)
            patterns.update(unique_sequence_combo)
            
            
            
        return max(sorted(patterns), key = patterns.get)
