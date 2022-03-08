def solution(N):
    # write your code in Python 3.6
    """        
    1. Convert number to binary. 
    2. Start 2 pointers at position 0. 
        a. Move pointer 1 to the first 1 which has a 0 next
           Move pointer 2 to pointer 1
           00110010001 -> 00110010001
           |                 |
            |                 |

           00110010001 -> 00110010001
           |                    |
           |                    |
         b. Keep moving pointer_2 if the elems are 0s. 
         c. it will either reach the end, wihtout encountering a 1, at this point we will return 0 (no trailing 1)
            or it will reach a 1. Then we count how many 0s in between.
            move pointer 1 to this position.
            Now, we need to repeat 2.a
    3. Keep track of max gap
    """
    
    bin_rep = str(bin(N))
    bin_rep = bin_rep[2:]
    pointer_1 = 0
    pointer_2 = 1

    str_len = len(bin_rep)
    max_gap_length = 0

    while pointer_1 < str_len and pointer_2 < str_len:
        while bin_rep[pointer_1] != "1" and bin_rep[pointer_2] != "0" and not isOutOfBounds(pointer_1, str_len) and not isOutOfBounds(pointer_2, str_len):
            pointer_1 += 1
            pointer_2 += 1
            
        # at this point, pointer 1 == 1 and pointer 2 == 0 OR we never found leading 1. so we will exit the first while loop
        _max_gap = 0
        while not isOutOfBounds(pointer_2, str_len) and bin_rep[pointer_2] == "0":
            pointer_2 += 1
            _max_gap += 1
            
        # this means that we have not found our trailing
        if pointer_2 >= str_len:
            return max_gap_length
        
        # update max
        if _max_gap > max_gap_length:
            max_gap_length = _max_gap
        
        # found trailing 1. restart search.
        pointer_1 = pointer_2
        pointer_2 += 1
    
    return max_gap_length

def isOutOfBounds(idx, length):
    return idx >= length