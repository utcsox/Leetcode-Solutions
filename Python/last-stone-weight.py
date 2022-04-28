class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first < second:
                heapq.heappush(stones, first-second)
                
        return abs(stones[0]) if stones else 0

class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones = sorted(stones)
            first = stones.pop()
            second = stones.pop()
            if first > second:
                stones.append(first-second)
                
        return stones[0] if stones else 0
