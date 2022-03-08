def fairIndexes(A, B) -> int:
    """
    get the sum first and see if its even. if not, return 0
    if its even, get the half of sum. this is our target sum
    from left, keep adding terms until we hit target sum. 
    """
    
    sum_A = sum(A)
    sum_B = sum(B)
    
    if (sum_A + sum_B)%2 != 0: return 0
    
    half_A = sum(A)/2
    half_B = sum(B)/2
    
    # both sum has to equal
    if half_A != half_B: return 0
    
    count = 0
    # [2,-2,-3,3]
    for idx in range(1, len(A)):
        total = sum(A[:idx])
        if total == half_A:
            count += 1
    return count
    
if __name__ == '__main__':
      A = [int(x) for x in input().split()]
      B = [int(y) for y in input().split()]
      print(fairIndexes(A, B))