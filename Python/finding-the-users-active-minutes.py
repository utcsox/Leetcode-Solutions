class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        UAM = defaultdict(set)
        output = [0] *k
        
        for user, minute in logs:
            UAM[user].add(minute)
        
        for key, values in UAM.items():
            output[len(values)-1] += 1
            
        return output
