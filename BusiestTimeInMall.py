from collections import OrderedDict

def find_busiest_period(data):
  """
  We have to keep a RUNNING tab of people currently in mall.
  
  Gotchas:
  - not how many net people ENTERED but a running TOTAL of people in mall
  - since its a running sum, the ORDER matters. Use an OrderedDict
  - O(n) spacetime - :(
  
  Runtime: O(2n) = O(n)
  Spacetime: O(n)
  """
  visitor_log = OrderedDict()
  
  for item in data:
    timestamp, num, entrance_flag = item
    if timestamp in visitor_log:
      visitor_log[timestamp] = update_log(visitor_log[timestamp], num, entrance_flag)
    else:
      visitor_log[timestamp] = update_log(0, num, entrance_flag)
      
  max_total = float('-inf')
  running_sum = 0
  max_timestamp = 0
  
  for key, val in visitor_log.items():
    running_sum += val
    if running_sum > max_total:
      max_total = running_sum
      max_timestamp = key
    
  print(visitor_log)
  return max_timestamp
    
    
def update_log(current, num, entrance_flag):
  if entrance_flag == 1:
    return current + num
  else:
    return current - num
    
      
      
    