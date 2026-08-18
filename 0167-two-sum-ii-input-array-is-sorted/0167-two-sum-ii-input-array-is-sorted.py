'''
투 포인터로 각각 0(왼쪽)과 n-1(오른쪽, 리스트 길이)로 시작합니다
만약 두 포인터에 해당하는 값이 타겟보다 작으면, 왼쪽 포인터를 1 증가시킵니다.
크다면, 오른쪽 포인터를 1 증가 시킵니다
시간복잡도는 O(N), 공간복잡도는 O(1) 입니다.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left<right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                break
            elif cur < target:
                left += 1
            else:
                right -= 1
        return [left+1, right+1]