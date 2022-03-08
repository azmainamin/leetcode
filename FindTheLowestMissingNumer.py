def find_missing_number(nums):
    i, length = 0, len(nums)

    while i < length:
        item_at_i = nums[i]
        if item_at_i < length and nums[item_at_i] != item_at_i:
            nums[i], nums[item_at_i] = nums[item_at_i], nums[i]
        else:
            i += 1
    
    for i in range(length):
        if nums[i] != i:
            return i
    
    return length