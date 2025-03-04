def left_binary_search(val, nums):
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)//2
        mid

        while(left <= right):
            mid = (left + right) // 2
            if(nums[mid] == val):
                return mid
            if(nums[mid] < val):
                left = mid + 1
            else:
                right = mid - 1
        if mid <= 0:
            return 0
        if nums[mid] < val:
            return mid
        return left_binary_search(val - 1, nums)

arr1 = [-3000, -1, 0, 7, 100]
    