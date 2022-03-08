"""
Sliding Window technique.

Instead of a set, we can use a hashmap to keep track of chars and their counter.
"""

def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    window_start = 0
    max_length = float('-inf')
    unique_chars = set()
    
    for window_end in range(len(s)):
        unique_chars = set(s[window_start: window_end+1])
        
        while len(unique_chars) > k: #eceba
            window_start += 1
            unique_chars = set(s[window_start: window_end+1])
            
        max_length = max(max_length, window_end - window_start + 1)
            
        
    return max_length