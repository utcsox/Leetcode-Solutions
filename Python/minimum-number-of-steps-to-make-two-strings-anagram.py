class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_counter, t_counter, count = Counter(s), Counter(t), 0
        
        for i in s_counter:
            si = s_counter.get(i, 0) - t_counter.get(i, 0)
            if si > 0:
                count += si    
                
        return count
