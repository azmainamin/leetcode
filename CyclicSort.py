def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1 #because 0 index based
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums