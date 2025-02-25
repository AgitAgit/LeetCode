def quicksort(nums):
        if len(nums) < 2:
            return nums

        pivot_idx = (len(nums) - 1)//2
        pivot = nums[pivot_idx]
        left = []
        right = []
        pivot_arr = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
            else:
                pivot_arr.append(nums[i])

        return quicksort(left) + pivot_arr + quicksort(right)

arr1 = [0, 7, 1, 2, 4, 3]
sorted = quicksort(arr1)
print(sorted)