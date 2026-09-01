from collections import deque
class RecentCounter:

    def __init__(self):
        self.requests = deque([])
        self.range = range(0,0)

    def ping(self, t: int) -> int:
        self.requests.append(t)
        count = 0
        while self.requests:
            request = self.requests.popleft()
            if request >= t-3000:
                self.requests.appendleft(request)
                break
        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)