class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        free = 0
        i = 0
        l = len(flowerbed)
        if l == 1 and flowerbed[0] == 0:
            return n <= 1
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            free += 1
            i = 2
        else:
            i = 1
        while i < l-1:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                free += 1
                i += 2
            else:
                i += 1
        if i == l-1 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
            free += 1
        return n <= free

            
                