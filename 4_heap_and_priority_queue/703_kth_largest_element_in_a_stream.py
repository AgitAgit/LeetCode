class KthLargest:

    def trim_heap(self):
        while len(self.num_heap) > self.k:
            heapq.heappop(self.num_heap)        

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.num_heap = nums 
        self.trim_heap()
        # while len(self.num_heap) > self.k:
            # heapq.heappop(self.num_heap)        

    def add(self, val: int) -> int:
        heapq.heappush(self.num_heap, val)
        self.trim_heap()
        # if len(self.num_heap) > self.k:
            # heapq.heappop(self.num_heap)
        return self.num_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)