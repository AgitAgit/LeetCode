class Solution:
    def binary_search(self, numbers, start, target):
        lo = start
        hi = len(numbers) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if numbers[mid] == target:
                return mid
            if numbers[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = [1, 1]
        for i in range(len(numbers)):
            num1 = numbers[i]
            new_target = target - num1
            new_target_idx = self.binary_search(numbers, i + 1, new_target)
            if new_target_idx != -1:
                result[0] += i
                result[1] += new_target_idx
                return result        