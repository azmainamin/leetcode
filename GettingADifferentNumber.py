def get_different_number(arr):

  """
  sorted_arr = sorted(arr) # O(nlogn)
  
  for i in range(len(sorted_arr)): # O(n)
    if i != sorted_arr[i]: return i + 1 #set(0, 1)
    
    if i + 1 < len(sorted_arr):
      curr = sorted_arr[i]
      next_item = sorted_arr[i+1]
      
      if next_item - curr > 1:
        return curr + 1
  
  #if sorted_arr[-1] == MAX_INT: return -1
  
  return sorted_arr[-1] + 1
  """

  idx = 0
  size = len(arr)
  
  while idx < len(arr):
    num = arr[idx]
    # num should be at arr[num]
    if num < size and num != arr[num]:
      # swap
      arr[idx], arr[num] = arr[num], arr[idx]
    else:
      idx += 1
      
      
  for i in range(size):
    if arr[i] != i:
      print(arr)
      return i
  
  
  return size
      

print(get_different_number([0,3,1,1]))