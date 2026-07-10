class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-num for num in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = []

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt<0:
                    q.append((time + n,cnt))

            if q and q[0][0] == time:
                heapq.heappush(maxHeap,q.pop(0)[1])
        return time