"""
WITHOUT EXPLICIT SUBARRAY CREATION
"""

class Solution:
    def search(self, nums, target: int) -> int:
        """
        Hints: all items are unique. asc order
        logn -> binary search. need to half the input at every stage.
        BIGGEST HINT: After rotation, atleast ONE of the subarray (left or right) is going to be sorted. We find which one is sorted, see if the elem
        is in that subarray by checking subarray[start]<=target<=subarray[end]. If its there, we do bin search on that half.
        If NOT, we do search ONLY on the right subarray. So we are halving our input at each step i.e. O(logn)
        
        GOTCHAS: The indexing i.e. mid+1, mid-1 and nums[low] <= nums[mid] instead of nums[low] < nums[mid]
        """
        
        return self.modifiedBinarySearch(nums, target, 0, len(nums)-1)
    
    def modifiedBinarySearch(self, nums, target, low, high):
        mid = (low + high)//2
        
        if low > high:
            return -1
        
        if nums[mid] == target:
            return mid
        
        # check if left subarray is sorted or not
        if nums[low] <= nums[mid]:
            # check if elem is in this subarray:
            if target >= nums[low] and target <= nums[mid]:
                return self.modifiedBinarySearch(nums, target, low, mid - 1) # mid -1 because we actually checked if nums[mid] == target on line 22
            
            # target is not on left subarray, so only search on right subarray
            return self.modifiedBinarySearch(nums, target, mid+1, high)
        
        else:
            # check if elem is in right subarray
            if target >= nums[mid] and target <= nums[high]:
                return self.modifiedBinarySearch(nums, target, mid+1, high)
            
            # target is on left subarray
            return self.modifiedBinarySearch(nums, target, low, mid-1)