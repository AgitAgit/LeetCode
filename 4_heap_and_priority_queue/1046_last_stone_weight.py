class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        # self.negative_heap = stones
        # print(stones)
        while len(stones) > 1:
            remaining = None
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            # print("stone1", stone1, "stone2", stone2)
            if stone1 > stone2:
                # stone1 = stone1 - stone2 
                # remaining = stone1
                # why doesn't this work as expected?
                remaining = stone1 - stone2
            if stone2 > stone1:
                remaining = stone2 - stone1
            if remaining is not None:
                # print(remaining)
                remaining = -remaining
                heapq.heappush(stones, remaining)
            # print(stones)
        if len(stones) > 0:
            return -stones[0]
        return 0

    