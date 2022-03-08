def largest_k(nums) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    Brute force is O(n^2): for each elem, check other elem, keep track of highest
    
    I can create two sets: one positive and one negative. On the negative, I can flip the signs to make all positive.
    Then see if there are intersection between the two sets. Take highest intersection.
    
    Runtime: creating two sets: O(n). Iterating through positive/negative: O(n). 
    
    What happens to 0?
    """
    positive_set = set([num for num in nums if num >= 0])
    negative_set = set([num for num in nums if num < 0])
    
    flipped_negative = {abs(num) for num in negative_set}
    
    intersecting_elems = positive_set.intersection(flipped_negative)
    
    if len(intersecting_elems) > 0:
        return max(intersecting_elems)
    
    return 0