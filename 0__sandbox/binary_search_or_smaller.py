class Solution:        
    def binary_search_or_larger(self, val, nums):
            if len(nums) == 0:
                return -1
            left = 0
            right = len(nums)//2
            mid = None
            while(left <= right):
                mid = (left + right) // 2
                if(nums[mid] == val):
                    return mid
                if(nums[mid] > val):
                    left = mid + 1
                else:
                    right = mid - 1
            if mid <= 0:
                return 0
            if nums[mid] > val:
                return mid
            return self.binary_search_or_larger(val + 1, nums) 

obj = Solution()

arr = [9,7,6,4,3]
target = 5
print("target: ",target)
print("list: ", arr)
print("index: ", obj.binary_search_or_smaller(target, arr))