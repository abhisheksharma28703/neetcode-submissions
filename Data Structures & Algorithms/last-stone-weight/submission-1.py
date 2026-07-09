class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        while len(stones) > 1:
            stones.sort()
            curr = stones.pop() - stones.pop()
            if curr:
                stones.append(curr)
            
        return stones[0] if stones else 0
        