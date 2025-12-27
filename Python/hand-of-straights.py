class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False

        count = Counter(hand) 
        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            curr_card = minheap[0]
            for i in range(curr_card, curr_card + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True
