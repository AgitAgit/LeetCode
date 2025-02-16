# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashT = {}
        for num in nums:
            if str(num) in hashT:
                return True
            hashT[str(num)] = num
        return False