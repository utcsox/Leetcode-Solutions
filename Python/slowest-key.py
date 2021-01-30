class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        max_key = keysPressed[0]
        max_release = releaseTimes[0]
        
        for r in range(1, len(releaseTimes)):
            if releaseTimes[r] - releaseTimes[r-1] > max_release:
                max_key = keysPressed[r]
                max_release =  releaseTimes[r] - releaseTimes[r-1]
                
            elif releaseTimes[r] - releaseTimes[r-1] == max_release:
                if keysPressed[r] > max_key:
                    max_key = keysPressed[r]
                
        return max_key
