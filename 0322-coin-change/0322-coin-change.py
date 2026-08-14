class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        visit = {0: float('inf')}
        def func(cur, count, coins):
            if cur in visit:
                if visit[cur] <= count:
                    # print("HIT", cur, visit[cur], count)
                    return
            visit[cur] = count
            for coin in coins:
                nxt = cur - coin
                if nxt == 0:
                    visit[0] = min(visit[0], count+1)
                # else:
                #     if nxt in visit:
                #         visit[nxt] = min(visit[nxt], count)
                #         func(nxt, visit[nxt]+1, coins)
                elif nxt > 0:
                    func(nxt, count+1 ,coins)
        ret = func(amount, 0, coins)
        print(visit)
        if visit[0]:
            if visit[0] == float('inf'):
                return -1
            return visit[0]
        else:
            return -1
        return visit[0]

