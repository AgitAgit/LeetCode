class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_numbers = {
            f"{nums[0]}":0
        }

        for i in range(1, len(nums)):
            temp = target - nums[i]
            if f"{temp}" in previous_numbers:
                return [previous_numbers[f"{temp}"], i]
            previous_numbers[f"{nums[i]}"] = i
        
        return False