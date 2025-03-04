class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = [1,1]
        left = 0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target and left <= right:
            num = numbers[left] + numbers[right]
            if num == target:
                break
            if num < target:
                left += 1
            else:
                right -= 1
        result[0] += left
        result[1] += right
        return result