from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        
        freq = Counter(hand)
        while freq:
            min_hand = min(freq)
            for i in range(groupSize):
                if min_hand + i not in freq:
                    return False
                freq[min_hand + i]-=1
                if freq[min_hand + i] == 0:
                    del freq[min_hand + i]
        return True
